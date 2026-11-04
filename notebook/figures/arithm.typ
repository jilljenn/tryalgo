/ Pascal's triangle (Yang Hui):
  $
    binom(n, k) = binom(n - 1, k - 1) + binom(n - 1, k)
    quad "for" 1 <= k < n.
  $
  $
    binom(n, 0) = binom(n, n) = 1
    quad "for" n >= 0.
  $

/ Linear Diophantine equation:
  Let $a x + b y = c$ be a Diophantine equation, and let
  $d = op("gcd")(a, b)$.
  The equation has at least one solution if and only if
  $d divides c$, and its solutions are
  $(x, y) = (x_0 + t b / d, y_0 + t a / d)$,
  where $t$ is an integer. To find $x_0, y_0$, use the
  extended Euclidean algorithm to obtain $a x_0 + b y_0 = d$,
  then multiply both resulting values by $c / d$.

/ Chinese remainder theorem:
  The system $x equiv a_i quad (mod m_i)$, where
  $i in {1, dots, n}$ and the $m_i$ are pairwise coprime,
  has a unique solution modulo $M = m_1 m_2 dots m_n$.
  If $b_i$ is the multiplicative inverse of
  $M / m_n quad (mod M)$, then the solution is
  $x equiv a_1 b_1 M / m_1 + dots + a_n b_n M / m_n quad (mod M)$.

/ Sum and number of divisors:
  If $x = p_1^(alpha_1) dots p_k^(alpha_k)$, then the sum
  of its divisors is
  $S = (1 + p_1 + dots + p_1^(alpha_1)) dots.c
  (1 + p_k + dots + p_k^(alpha_k))$
  and the number of its divisors is
  $C = (1 + alpha_1) dots (1 + alpha_k)$.

/ Euler's totient function $phi$:
  The function $phi(n)$ counts the positive integers
  less than $n$ that have multiplicative inverses modulo $n$.
  Formula:
  $phi(p_1^(alpha_1) p_2^(alpha_2) dots p_k^(alpha_k)) =
  (p_1 - 1) p_1^(alpha_1 - 1)
  (p_2 - 1) p_2^(alpha_2 - 1) dots
  (p_k - 1) p_k^(alpha_k - 1)$.
  It has the following property: if $a, n$ are coprime,
  $a^(phi(n)) equiv 1 quad (mod n)$.

/ Bounds on the prime-counting function (PNT):
  $n / ln(n) < op("prim")(n) < 1.26 dot n / ln(n)$,
  where $op("prim")(n)$ is the number of primes less than $n$.

/ Euler's formula (plane graphs):
  $
    v - e + f_1 = 2;
    quad v - e + f_2 - k = 1
  $
  where:
  - $v = "number of vertices"$
  - $e = "number of edges"$
  - $f_1 = "number of internal faces"$
  - $f_2 = 1 + f_1 quad ("internal faces + outer face")$
  - $k = "number of connected components"$
