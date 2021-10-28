# -*- coding: utf-8 -*-
"""
/***************************************************************************
Name                 : Mascaret
Description          : Pre and Postprocessing for Mascaret for QGIS
Date                 : June,2017
copyright            : (C) 2017 by Artelia
email                :
***************************************************************************/
/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 3 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/

"""
import math
import os
import dateutil
from shutil import copy2
from qgis.core import *
import numpy as np


def data_to_float(txt):
    try:
        float(txt)
        return float(txt)
    except ValueError:
        return None


def data_to_date(txt):
    try:
        dateutil.parser.parse(txt, dayfirst=True)
        return dateutil.parser.parse(txt, dayfirst=True)
    except ValueError:
        return None


def data_to_int(txt):
    try:
        int(txt)
        return int(txt)
    except ValueError:
        return None


def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def distance(a, b):
    return math.sqrt(math.pow(a.x() - b.x(), 2) + math.pow(a.y() - b.y(), 2))


def interpole(a, l1, l2):
    """ Interpolation
        l1: list 1
        l2: list 2
        a interpol value"""
    i, x = min(enumerate(l1), key=lambda xx: abs(xx[1] - a))

    if i < len(l1) - 1 and a >= x:
        return (l2[i + 1] - l2[i]) / (l1[i + 1] - x) * (a - x) + l2[i]
    elif i > 0 and a <= x:
        return (l2[i] - l2[i - 1]) / (x - l1[i - 1]) * (a - l1[i - 1]) + l2[
            i - 1]
    else:
        return None


def str2bool(s):
    """string to bool"""
    if "True" in s or "TRUE" in s:
        return True
    else:
        return False


def get_couche(nom, iface):
    for couche in iface.legendInterface().layers():
        if couche.name() == nom:
            return couche

    return None


def calcul_abscisses(liste_couches, riviere, iface, dossier):
    couche_riv = get_couche(riviere, iface)
    # fusion des branches
    nom_fich = os.path.join(dossier, "temp.shp")
    id = couche_riv.fieldNameIndex("branche")
    QgsGeometryAnalyzer().dissolve(couche_riv, nom_fich,
                                   onlySelectedFeatures=False,
                                   uniqueIdField=id, p=None)

    couche_dissoute = QgsVectorLayer(nom_fich, "temp", "ogr")

    long_branche = {}
    dico = {}
    for f in couche_dissoute.getFeatures():
        long_branche[f["branche"]] = f.geometry().length()
        dico[f["branche"]] = f

    longueur_zone = {}
    for f in couche_riv.getFeatures():
        if not f["branche"] in longueur_zone.keys():
            longueur_zone[f["branche"]] = []

        longueur_zone[f["branche"]].append(
            (f["numZone"], f.geometry().length()))

    for c in liste_couches:
        if c == riviere:
            continue

        couche = get_couche(c, iface)
        if couche.wkbType() == 5:
            couche_noeud = QgsVectorLayer("Point", "temporary_points", "memory")

            couche_noeud.dataProvider().addAttributes(
                [QgsField("nom", QVariant.String, 'string', 10, 0),
                 QgsField("numBranche", QVariant.Int, 'int', 2, 0),
                 QgsField("abscisse", QVariant.Double, 'double', 10, 1)])

            couche_noeud.startEditing()
            for f in couche.getFeatures():
                for r in couche_dissoute.getFeatures():
                    if f.geometry().intersects(r.geometry()):
                        feat = QgsFeature(couche_noeud.dataProvider().fields())
                        feat.setGeometry(f.geometry().intersection(
                            r.geometry()))
                        feat["nom"] = f["nom"]
                        feat["numBranche"] = r["branche"]
                        couche_noeud.dataProvider().addFeatures([feat])
            couche_noeud.commitChanges()

        else:
            couche_noeud = couche

        couche_noeud.startEditing()

        # parcours de la liste de coucheNoeuds
        for n in couche_noeud.getFeatures():

            num = n["numBranche"]
            branche = dico[num]

            # mini = 999999999
            # i = 0
            # recuperation des coordonnees du point
            coord = n.geometry().asPoint()

            # on cherche le segment le plus proche du point souhaité
            d, dist, v_b = branche.geometry().closestSegmentWithContext(coord)
            v_a = v_b - 1

            # calcul de la distance depuis le début de la ligne
            somme = 0
            for i in range(1, v_b):
                somme += distance(branche.geometry().vertexAt(i - 1),
                                  branche.geometry().vertexAt(i))

            somme += distance(branche.geometry().vertexAt(v_a), dist)

            # calcul de l'abcisse
            somme_b = sum(
                [long_branche[i] for i in long_branche.keys() if i < num])
            if somme < long_branche[num]:
                n["abscisse"] = somme + somme_b
            else:
                n["abscisse"] = None
            couche_noeud.updateFeature(n)

        couche_noeud.commitChanges()

        if couche.wkbType() == 5:
            couche.startEditing()

            for f in couche_noeud.getFeatures():
                for g in couche.getFeatures():
                    if f["nom"] == g["nom"]:
                        g["abscisse"] = f["abscisse"]
                        g["numBranche"] = f["numBranche"]
                        couche.updateFeature(g)

            couche.commitChanges()

    if riviere in liste_couches:
        absc_debut = {}
        absc_fin = {}

        couche_profil = get_couche("profils", iface)

        for p in couche_profil.getFeatures():

            if p["abscisse"] and p["actif"]:
                num = p["numBranche"]

                if num not in absc_debut.keys():
                    absc_debut[num] = 99999999
                if num not in absc_fin.keys():
                    absc_fin[num] = -99999999

                absc_debut[num] = min(absc_debut[num], p["abscisse"])
                absc_fin[num] = max(absc_fin[num], p["abscisse"])

        couche_riv.startEditing()

        for f in couche_riv.getFeatures():
            num = f["branche"]
            f["absc_debut"] = absc_debut[num]
            f["absc_fin"] = absc_fin[num]
            somme_b = sum(
                [long_branche[i] for i in long_branche.keys() if i < num])

            list_deb = [long for i, long in longueur_zone[num] if
                        i < f["numZone"]]
            f["absDebZone"] = max(sum(list_deb) + somme_b, absc_debut[num])

            list_fin = [long for i, long in longueur_zone[num] if
                        i <= f["numZone"]]
            f["absFinZone"] = min(sum(list_fin) + somme_b, absc_fin[num])
            couche_riv.updateFeature(f)

        couche_riv.commitChanges()
        # del(couche_dissoute)
        # liste = glob.glob(nom_fich[:-4]+".*")
        # for fich in liste :
        # os.remove(fich)


def del_accent(ligne):
    """ supprime les accents du texte source """
    accents = {u'a': [u'à', u'ã', u'á', u'â'],
               u'e': [u'é', u'è', u'ê', u'ë'],
               u'i': [u'î', u'ï'],
               u'u': [u'ù', u'ü', u'û'],
               u'o': [u'ô', u'ö']}
    for (char, accented_chars) in accents.items():
        for accented_char in accented_chars:
            ligne = ligne.replace(accented_char, char)
    return ligne


def copy_dir_to_dir(src, target):
    """ Copi file in directory"""
    files = os.listdir(src)
    for i in range(0, len(files)):
        copy2(os.path.join(src, files[i]),
              os.path.join(target, files[i]))


def del_symbol(ligne):
    """ supprime les accents du texte source """
    accents = {u'_': [u'-', u'.']}
    for (char, accented_chars) in accents.items():
        for accented_char in accented_chars:
            ligne = ligne.replace(accented_char, char)
    return ligne


def replace_all(txt, dico):
    """
    Replace several items
    :param txt: text orginal
    :param dico: de remplacement des variable
    :return:
    """
    for i in dico:
        txt = txt.replace(i, dico[i])
    return txt


def read_version(masplug_path):
    """
    read version of plugin
    :return: (str) version
    """
    file = open(os.path.join(masplug_path, 'metadata.txt'), 'r')
    for ligne in file:
        if ligne.find("version=") > -1:
            ligne = ligne.split('=')
            val = ligne[1].strip()
            break
    file.close()
    return val


def tw_to_txt(tw, range_r, range_c, sep):
    clipboard = ''
    for c in range_c:
        if c != range_c[-1]:
            clipboard = '{}{}{}'.format(clipboard,
                                        tw.horizontalHeaderItem(c).text(), sep)
        else:
            clipboard = '{}{}\n'.format(clipboard,
                                        tw.horizontalHeaderItem(c).text())
    for r in range_r:
        for c in range_c:
            if c != range_c[-1]:
                clipboard = '{}{}{}'.format(clipboard, tw.item(r, c).data(0),
                                            sep)
            else:
                clipboard = '{}{}\n'.format(clipboard, tw.item(r, c).data(0))
    return clipboard

def ortho_line(inters_prec, inters_suiv, inters_courant, largeur_vallee):
    x1 = inters_prec.x()
    y1 = inters_prec.y()
    x2 = inters_suiv.x()
    y2 = inters_suiv.y()
    x3 = inters_courant.x()
    y3 = inters_courant.y()
    # y = coeff_A * x + coeff_B est l'équation de la droite perpendiculaire à X1-X2 passant par X3
    coeff_A = (x2 - x1) / (y1 - y2)
    coeff_B = y3 - x3 * ((x2 - x1) / (y1 - y2))
    # linestart et lineend sont les 2 extrémités de la polyligne perpendiculaire à X1-X2 passant par X3
    if coeff_A < -1:
        y_start = y3 + largeur_vallee
        x_start = (y_start - coeff_B) / coeff_A
        y_end = y3 - largeur_vallee
        x_end = (y_end - coeff_B) / coeff_A
    elif coeff_A <= 0 and coeff_A >= -1:
        x_start = x3 + largeur_vallee
        y_start = coeff_A *  x_start + coeff_B
        x_end = x3 - largeur_vallee
        y_end = coeff_A *  x_end + coeff_B
    elif coeff_A > 0 and coeff_A <= 1:
        x_start = x3 + largeur_vallee
        y_start = coeff_A *  x_start + coeff_B
        x_end = x3 - largeur_vallee
        y_end = coeff_A *  x_end + coeff_B
    elif coeff_A > 1:
        y_start = y3 + largeur_vallee
        x_start = (y_start - coeff_B) / coeff_A
        y_end = y3 - largeur_vallee
        x_end = (y_end - coeff_B) / coeff_A
    return x_start, y_start, x_end, y_end

def vertex_add(geom, couche, feat_id, x, y, tol=0.01):
    p1, at, b1, after, d1 = geom.closestVertex(QgsPointXY(x, y))
    dist, p2, to, _ = geom.closestSegmentWithContext(QgsPointXY(x, y))
    if at == 0:
        if dist < tol:
            # insert into first segment
            couche.insertVertex(x, y, feat_id, after)
            geom.insertVertex(x, y, after)
        else:
            # insert before first vertex
            couche.insertVertex(x, y, feat_id, 0)
            geom.insertVertex(x, y, 0)
    elif after == -1:
        if dist < tol:
            # insert after last vertex
            couche.insertVertex(x, y, feat_id, at)
            geom.insertVertex(x, y, at)
        else:
            # insert into last segment
            couche.insertVertex(x, y, feat_id, at - 1)
            geom.insertVertex(x, y, at - 1)
    return geom

def tronque_profil(x_str, z_str, dist_rg, dist_rd):
    flag_rg = False
    flag_rd = False
    x_tronque = []
    z_tronque = []
    for i, xx in enumerate(x_str):
        x = float(xx)
        if x < dist_rg:
            pass
        elif x >= dist_rg and x <= dist_rd:
            if x == dist_rg or flag_rg:
                x_tronque.append(x)
                z_tronque.append(float(z_str[i]))
                flag_rg = True
            elif x == dist_rd:
                x_tronque.append(x)
                z_tronque.append(float(z_str[i]))
                flag_rd = True
            else:
                x_tronque.append(dist_rg)
                z_tronque.append((dist_rg - float(x_str[i - 1])) * (float(z_str[i]) - float(z_str[i - 1])) / (x - float(x_str[i - 1])) + float(z_str[i - 1]))
                flag_rg = True
        elif x > dist_rd and not flag_rd:
            x_tronque.append(dist_rd)
            z_tronque.append((dist_rd - float(x_str[i - 1])) * (float(z_str[i]) - float(z_str[i - 1])) / (x - float(x_str[i - 1])) + float(z_str[i - 1]))
            flag_rd = True
    return x_tronque, z_tronque

def calcul_planim_sh(ref_plani, x_z):
    # Il faut d'abord s'assurer que x_z est trié dans l'ordre croissant
    ref_sh = np.zeros(np.shape(ref_plani)[0])
    if len(ref_plani) > 1:
        pas_plani = ref_plani[1] - ref_plani[0]
        for i in range(len(x_z) - 1):
            d1 = x_z[i][0] # distance
            z1 = x_z[i][1] # cote
            d2 = x_z[i+1][0]
            z2 = x_z[i+1][1]
            en_eau = False
            for ip, p in enumerate(ref_plani):
                if en_eau:
                    sh_cur = math.fabs(d2 - d1) * pas_plani
                elif (p + pas_plani) <= z1 and (p + pas_plani) <= z2:
                    sh_cur = 0
                else:
                    sh_cur = (p + pas_plani - max(z1, z2)) * (d2 - d1) + (math.fabs(z2 - z1) * (d2 - d1) * 0.5)
                    en_eau = True
                ref_sh[ip] += sh_cur
    return ref_sh

def tri_pt_profils(x_z_t, ordre_croissant):
    left = []
    equal = []
    right = []
    if ordre_croissant:
        if len(x_z_t) > 1:
            pivot = x_z_t[0][0]
            for i, x in enumerate(x_z_t):
                if x[0] < pivot:
                    left.append([x_z_t[i][0], x_z_t[i][1]])
                elif x[0] == pivot:
                    equal.append([x_z_t[i][0], x_z_t[i][1]])
                elif x[0] > pivot:
                    right.append([x_z_t[i][0], x_z_t[i][1]])
            return tri_pt_profils(left, ordre_croissant) + equal + tri_pt_profils(right, ordre_croissant)
        else:
            return x_z_t
    else: # Ordre décroissant
        if len(x_z_t) > 1:
            pivot = x_z_t[0][0]
            for i, x in enumerate(x_z_t):
                if x[0] > pivot:
                    left.append([x_z_t[i][0], x_z_t[i][1]])
                elif x[0] == pivot:
                    equal.append([x_z_t[i][0], x_z_t[i][1]])
                elif x[0] < pivot:
                    right.append([x_z_t[i][0], x_z_t[i][1]])
            return tri_pt_profils(left, ordre_croissant) + equal + tri_pt_profils(right, ordre_croissant)
        else:
            return x_z_t