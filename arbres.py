# import numpy as np
# from igraph import *
# import cairo

class noeudArbre:
    def __init__(self,valeur,gauche,droite, niveau):
        self.val=valeur
        self.filsgauche=gauche
        self.filsdroit=droite
        self.niveau = niveau
    def __init__(self):
        self.val=0
        self.filsgauche=None
        self.filsdroit=None
        self.niveau = 0
    def __repr__(self):
        return "Noeud de valeur "+str(self.val)

def setupTree():
    tree = []
    setupNoeuds(tree)
    return tree

def setupNoeuds(tree, pos=0):
    pos+= 1
    noeud = noeudArbre()
    tree.append(noeud)
    noeud.niveau = pos
    print("valeur du noeud de niveau "+ str(pos) + " ?")
    noeud.val = input()
    print("fils gauche du noeud  ? (o/n)")
    dr = input()
    print("fils droit du noeud ? (o/n)")
    ga = input()
    if(dr == "o"):
        noeud.filsgauche = setupNoeuds(tree, pos)
    if(ga == "o"):
        noeud.filsdroit = setupNoeuds(tree, pos)
    return noeud

# file = []
#
# def enfiler(val):
#     file.append(val)
#
# def defiler():
#     if(len(file) < 1):
#         return "erreur file vide"
#     else:
#         elem = file[0]
#         file.pop(0)
#         return elem

def parcoursProfondeur(noeud, dejavisit=None):
    # if dejavisit is None :
    #     dejavisit = []
    # if noeud not in dejavisit :
    #     dejavisit.append(noeud.val)
    #
    # if (noeud.filsgauche is not None):
    #     parcoursProfondeurRec(noeud.filsgauche, dejavisit)
    # if (noeud.filsdroit is not None):
    #     parcoursProfondeurRec(noeud.filsdroit, dejavisit)
    # return dejavisit
    afficherArbre(arbre)


def parcoursLargeur(arbre):
    tableauLargeur = []
    niveaumax = cherherNivMax(arbre)
    for i in range(niveaumax):
        for j in range(len(arbre)):
            if(arbre[j].niveau == i+1):
                tableauLargeur.append(arbre[j])
    return tableauLargeur

def cherherNivMax(arbre):
    niveau = 1
    for i in range(len(arbre)):
        if (arbre[i].niveau > niveau):
            niveau = arbre[i].niveau
    return niveau

# def parcoursLargeurRec(curseur, tableauLargeur=None):
#     if(tableauLargeur is None):
#         tableauLargeur = []
#
#     tableauLargeur.append(curseur)
#     if(curseur.filsgauche is not None):
#         tableauLargeur.append(curseur.filsgauche)
#     if(curseur.filsdroit is not None):
#         tableauLargeur.append(curseur.filsdroit)

def afficherArbre(arbre):
    for i in range(len(arbre)):
        print(arbre[i].val)

arbre = setupTree()
afficherArbre(parcoursProfondeur(arbre))
afficherArbre(parcoursLargeur(arbre))
#print(parcoursProfondeurRec(premierNoeud))
