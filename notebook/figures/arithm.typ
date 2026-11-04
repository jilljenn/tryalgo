/ Triangle de Pascal (Yang Hui):
  $
    binom(n, k) = binom(n - 1, k - 1) + binom(n - 1, k)
    quad "pour" 1 <= k < n.
  $
  $
    binom(n, 0) = binom(n, n) = 1
    quad "pour" n >= 0.
  $

/ Équation diophantienne linéaire:
  Soit $a x + b y = c$ une ED, et $d = op("gcd")(a, b)$.
  L'équation a au moins une solution ssi $d divides c$, et cette
  solution est $(x, y) = (x_0 + t b / d, y_0 + t a / d)$,
  où $t$ est entier. Pour trouver $x_0, y_0$, il suffit d'utiliser
  l'algorithme d'Euclide étendu, pour obtenir $a x_0 + b y_0 = d$
  et multiplier les deux valeurs obtenues par $c / d$.

/ Théorème des restes chinois:
  Le système $x equiv a_i quad (mod m_i)$ où
  $i in {1, dots, n}$ et les $m_i$ sont premiers entre eux
  a une seule solution modulo $M = m_1 m_2 dots m_n$.
  Si $b_i$ est l'inverse de $M / m_n quad (mod M)$,
  alors la solution est
  $x equiv a_1 b_1 M / m_1 + dots + a_n b_n M / m_n quad (mod M)$.

/ Somme et nombre de(s) diviseurs:
  Si $x = p_1^(alpha_1) dots p_k^(alpha_k)$, alors la somme
  des diviseurs est
  $S = (1 + p_1 + dots + p_1^(alpha_1)) dots.c
  (1 + p_k + dots + p_k^(alpha_k))$
  et le nombre de diviseurs est
  $C = (1 + alpha_1) dots (1 + alpha_k)$.

/ Fonction $phi$ de Euler:
  La fonction $phi(n)$ donne le nombre de nombres entiers
  plus petits que $n$ qui admettent des inverses multiplicatifs
  modulo $n$. Formule :
  $phi(p_1^(alpha_1) p_2^(alpha_2) dots p_k^(alpha_k)) =
  (p_1 - 1) p_1^(alpha_1 - 1)
  (p_2 - 1) p_2^(alpha_2 - 1) dots
  (p_k - 1) p_k^(alpha_k - 1)$.
  Elle a la propriété suivante : si $a, n$ sont premiers entre eux,
  $a^(phi(n)) equiv 1 quad (mod n)$.

/ Majoration des nombres premiers (PNT):
  $n / ln(n) < op("prim")(n) < 1.26 dot n / ln(n)$,
  où $op("prim")(n)$ est le nombre de nombres premiers
  plus petits que $n$.

/ Formule d'Euler (graphes dans le plan):
  $
    v - e + f_1 = 2;
    quad v - e + f_2 - k = 1
  $
  où :
  - $v = "nombre de sommets"$
  - $e = "nombre d'arêtes"$
  - $f_1 = "nombre de faces internes"$
  - $f_2 = 1 + f_1 quad ("faces internes + fond")$
  - $k = "nombre de composantes connexes"$
