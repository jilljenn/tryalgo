#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Area of polygone
# mesures polygone
# jill-jenn vie et christoph durr - 2014-2018


from tryalgo.range_minimum_query import RangeMinQuery


# snip{ area
def area(p):
    """Area of a polygone

    :param p: list of the points taken in any orientation,
              p[0] can differ from p[-1]
    :returns: area
    :complexity: linear
    """
    A = 0
    for i in range(len(p)):
        A += p[i - 1][0] * p[i][1] - p[i][0] * p[i - 1][1]
    return A / 2.
# snip}


# snip{ is_simple
def is_simple(polygon):
    """Test if a rectilinear polygon is is_simple

    :param polygon: list of points as (x,y) pairs along the closed polygon
    :returns: True if the segements do not intersect
    :complexity: O(n log n) for n=len(polygon)
    """
    n = len(polygon)
    order = list(range(n))
    order.sort(key=lambda i: polygon[i])         # lexicographic order
    rank_to_y = list(set(p[1] for p in polygon))
    rank_to_y.sort()
    y_to_rank = {y: rank for rank, y in enumerate(rank_to_y)}
    S = RangeMinQuery([0] * len(rank_to_y))      # sweep structure
    last_y = None
    for i in order:
        x, y = polygon[i]
        rank = y_to_rank[y]
        #                             -- type of point
        right_x = max(polygon[i - 1][0], polygon[(i + 1) % n][0])
        left = x < right_x
        below_y = min(polygon[i - 1][1], polygon[(i + 1) % n][1])
        high = y > below_y
        if left:                      # y does not need to be in S yet
            if S[rank]:
                return False          # two horizontal segments intersect
            S[rank] = -1              # add y to S
        else:
            S[rank] = 0               # remove y from S
        if high:
            lo = y_to_rank[below_y]   # check S between [lo + 1, rank - 1]
            if (below_y != last_y or last_y == y or
                    rank - lo >= 2 and S.range_min(lo + 1, rank)):
                return False          # horiz. & vert. segments intersect
        last_y = y                    # remember for next iteration
    return True
# snip}


# easter egg

# \section*{Gâteau aux carottes}
# (traduit de \textsc{Joy of Cooking}, de Rombauer, Becker et Becker)

# Aux États-Unis le gâteau aux carottes est maintenant standard comme
# la tarte aux pommes.  Le nôtre est moyennement épicé, moelleux mais
# pas lourd, et assez goûteux pour pouvoir être dégusté sans glaçage.

# Ayez tous les ingrédients à votre disposition et à température
# ambiante, 68 à 70 degrés.  Préchauffez le four à 350 degrées.
# Graissez et farinez deux moules ronds de 9 x 2 pouces ou deux moules
# 8 x 8 pouces ou un moule 13 x 9 pouces ou déposez sur le fond un papier
# ciré ou transparent.

# Mélangez ensemble fermement dans un grand bol
# \begin{verse}
# $1 \frac 13$ tasses de farine\\
# $1$ tasse de sucre\\
# $1 \frac 12$ cuillères à café de levure\\
# $1$ cuillère à café de poudre à lever\\
# $1$ cuillère à café de cannelle\\
# $\frac12$ cuillère à café de clous de girofle\\
# $\frac12$ cuillère à café de noix de muscade fraîchement moulue
# \\
#  $\frac12$ cuillère à café de tout-épices\footnote{\emph{Allspice} ou
#  \emph{poivre de la Jamaïque} est une baie petite, ronde et d'un brun
#  rougeâtre, qui pousse sur un grand arbre vert toute l'année, dont les
#  plus fins se trouvent sur l'île de Jamaïque. Son goût ressemble
#  principalement aux clous de girofle avec une pincée de cannelle, noix
#  de muscade et de gingembre.} moulus
# \\
# $\frac12$ cuillère à café de sel
# \end{verse}
# Ajoutez et mélangez avec une cuillère en caoutchouc ou battez à faible
# vitesse :
# \begin{verse}
# $\frac23$ tasses d'huile végétale\\
# $3$ grands oeufs
# \end{verse}
# Incorporez~:
# \begin{verse}
# $1\frac12$ tasses de carottes épluchées et finement rapées\\
# $1$ tasse de noix finement hachée\\
# $1$ tasse de raisins secs jaunes (optionnel)\\
# $\frac 12$ tasse d'ananas écrasé, légèrement égoutté (optionnel)
# \end{verse}
# Versez la pâte dans le(s) moule(s) et étalez équitablement.  Faites
# cuire jusqu'à ce qu'un cure-dent en bois percé dans le centre ressorte
# propre, 25 à 30 minutes dans des moules rectangulaires ou ronds, 35
# minutes dans un moule 13 x 9 pouces.  Laissez refroidir le(s) moule(s)
# sur une grille pendant 10 minutes.  Glissez un couteau autour du
# gâteau pour le détacher du moule (des moules).  Retournez-le et
# retirez le papier s'il y en a.  Laissez refroidir avec la bonne face vers
# le haut sur une grille.  Remplissez et recouvrez avec du \emph{glaçage de
# fromage à tartiner}, du \emph{glaçage blanc rapide}, ou du
# \emph{glaçage rapide brun au beurre}.

# \begin{tabular}{|rcl|}\hline
# $x$ degrées Fahrenheit &=&$5(x-32)/9$ degrées Celsius\\
# 1 pouce&=& 2,54 centimètres\\
# 1 tasse &=& 0,236 litre\\\hline
# \end{tabular}
