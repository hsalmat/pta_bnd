#o-*- coding: utf-8 -*-
#$Id: clase_zostera.py 12 2018-09-24 20:20:12Z hugo $

"""
 Clase de objeto Zostera. La clase es una representacion abstracta de
 de un rizoma de zostera marina. Un rizoma se representa como un
 conjunto de internodo, que se representam como un objeto de clase nodo(que esta
 en otro archivo:clase_nodo.py)

                   o
                  /
     o---o---o---o---o      <-Zostera marina
          \
           o
            \
             o              \(*w*)/

en este dibujito de un rizoma hay  3 ramas, con 5 2 y 1 nodo respectivamente
esto se representaria con 8 objeots de tipo nodo


"""
from clase_nodo import node
from clase_rama import branch
import random


#  constructor, necesita unalista de listas de objetos nodo, si es un solo
#  nodo igual debe ser una lista de lista, osea [[nodo()]]
class zostera:
    def __init__(self, branches):  # costructor, lo quiero para incializar
        self.branches = branches  # lista objetos rama
        self.num = branches[0].nodes[0].rhizome()  # numero de esta zostera

#  envejece en x unidad de tiempo a todos los nodos de la pradera, si ya son
#  muy viejos los mata
    def older_all(self, time):  # envejece todos los nodos en un tiempo
        for bran in self.branches:
            for nod in bran.nodes:
                nod.older(time)
                rand = random.random()
                if rand < (nod.age / 10.0):
                    del bran.nodes[bran.nodes.index(nod)]
                    nod.__del__()
#                    print("ruleta de la muerte nodo")
                    if len(bran.nodes) < 1:
                        del self.branches[self.branches.index(bran)]
                        bran.__del__()
#                        print("por ruleta de la muerte nodo, muerte de rama")

###aqui quite el metodo para aniadir nodo, lo movi a clase rama

    def add_branch(self, lengt, bran):  # bran es el index number de la rama
        last = self.branches[bran].nodes[-1]
        if self.branches[bran].angle is True:
            self.branches.append(branch([node(last.rhizome(),
            len(self.branches) + 1, last.nodenum(), 0, lengt, last.coord[1],
                        last.orient - 1.31)]))
        elif self.branches[bran].angle is False:
                self.branches.append(branch([node(last.rhizome(),
                                len(self.branches) + 1,
                        last.nodenum(), 0, lengt, last.coord[1],
                        last.orient + 1.31)]))
        self.branches[bran].angle_change()
"""
#rhizome, branch, prev_node, age, leng, firstcoord, orient

#####PRUEBAS ##############################################################
import math
una = [node(1, 1, 0, 3, 1,  [0, 0], math.radians(90)),
        node(1, 1, 1, 2, 0,  [0, 0], math.radians(90)),
        node(1, 1, 2, 1, 0,  [0, 0], math.radians(90)),
        node(1, 1, 3, 0, 0,  [0, 0], math.radians(90))]

dos = [node(1, 2, 0, 1, 0,  [0, 0], math.radians(90)),
        node(1, 2, 1, 0, 0,  [0, 0], math.radians(90))]


ramona = [branch(una), branch(dos)]

#rhizome, branch, prev_node, age, leng, coord,orient

a = zostera(ramona)

for b in a.branches:
    b.add_node(1)
a.add_branch(1,0)
for b in a.branches:
    print (b)
    for c in b.nodes:
        print (c)
        print (a.branches.index(b))



#    a.add_branch(1,b[-1].)

#lengt, bran)
"""