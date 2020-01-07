import numpy as np
from igraph import *
import cairo

g = Graph.Tree(10,2)
print(g.get_edgelist())

class noeudArbre:
    def __init__(self,valeur,gauche,droite):
        self.val=valeur
        self.filsgauche=gauche
        self.filsdroit=droite
    def __repr__(self):
        return "Noeud de valeur "+str(self.val)

file = []

def enfiler(val):
    file.append(val)

def defiler():
    if(len(file) < 1):
        return "erreur file vide"
    else:
        elem = file[0]
        file.pop(0)
        return elem

def parcoursprofondeur(graph, noeud):
    

def parcoursLargeur(graph):
    print(graph.get_edgelist())

plot(g)
