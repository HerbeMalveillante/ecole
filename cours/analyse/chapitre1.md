# ANALYSE - CHAPITRE 1 : GÉNÉRALITÉS SUR $\mathbb{R}$

[ Mots clefs : intervalle, voisinage, majoré, minoré, borne, segments emboîtés, bolzano-weierstrass, densité ]

> Après quelques rappels, cette fiche introduit des propriétés fines de $\mathbb{R}$, non démontrables en **L1L2**, et qui seront utilisées parcimonieusement dans les premières fiches de l'ouvrage, et un peu plus ensuite.

----

## 1) Intervalles et voisinages

- $\mathbb{R}$ est constitué des entiers naturels, des entiers relatifs, des nombres rationnels (de la forme $p/q$ où $p\in \mathbb{Z}$ et $q \in \mathbb{N}^*$) et des autres, les irrationnels comme $\sqrt{2}$ ou $\pi$. Ce sont eux les "plus nombreux". On a les inclusions $\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R}$.
- Un intervalle d'extrémités $a$ et $b$ avec $a < b$, est l'ensemble des réels compris, au sens strict et/ou large entre $a$ et $b$. On a l'intervalle ouvert $]a,b[$, le **segment** $[a, b]$ et les intervalles semi-ouverts $[a,b[$ et $]a,b]$.
- Une demi-droite $]- \infty, A [$ est l'ensemble des réels strictement inférieurs à $A$, et $]A, \infty[$ l'ensemble des réels strictement plus grands que $A$. On définit de même $]- \infty, A]$, et $[A, + \infty[$.

> Un voisinage d'un réel $x_0$ est une partie de $\mathbb{R}$ contenant un intervalle ouvert $]x_0 - h, x_0 + h[$ de centre $x_0$.

> **Méthodologie**
>
>On se contentera de prendre pour voisinages de $x_0$ les intervalles ouverts $]x_0 - h, x_0 + h[$ de centre $x_0$. L'expression "au voisinage de $x_0$" signifie donc "dans un intervalle ouvert bien choisi de centre $x_0$". On ne précise pas, en général, le rayon $h$ de cet intervalle.

**Exemple 1** : Soit $a > 0$. Il existe un voisinage de $a$ ne contenant que des nombres strictements positifs. Par exemple $]a-a/2, a+a/2[=]a/2, 3a/2[$.

**Exemple 2** : Au voisinage de $x_0 = 2$, la quantité $x^2 -3$ est strictement positive. Il suffit de se placer dans $]1.9;2.1[$.

> Un voisinage de $-\infty$ est une demi-droite $]- \infty, A [$ et un voisinage de $+\infty$ est une demi-droite $]A, + \infty[$.

**Exemple 3** : Au voisinage de $+ \infty$, on a $x-45sin(x)>0$. Il suffit de se placer sur $]45, +\infty[$, puisque $-1 \leq sin(x) \leq 1$.

> **Méthodologie**
>
> En pratique, *"au voisinage de"* veut dire **tout près de**. *"Au voisinage de $x_0$* sous-entend que le rayon $h$ est "très petit". *"Au voisinage de $+\infty$"* signifie que $A$ est positif "très grand" et *"au voisinage de $-\infty$"* sous-entend que $A$ est négatif de "très grande valeur absolue".

----

## 2) Partie majorée, minorée, bornée

- Dans tout ce paragraphe, $E$ est une partie non vide de $\mathbb{R}$, différente de $\mathbb{R}$.

### 2.1 Partie majorée

> On dit que $E$ est majorée quand il existe un réel $M$ supérieur ou égal à tous les éléments de $E$ :
>
> $$ (\exists M \in \mathbb{R}) (\forall x \in E)(x \leq M) $$
> Un tel réel $M$ s'appelle majorant de $E$.

- Si $M$ est majorant de $E$, tout réel $M' >M$ est encore un majorant de $E$.

**Exemple 4** : Tout intervalle $E$ d'extrémités $a$ et $b$ est majoré, l'extrémité supérieure $b$ étant un majorant de $E$. L'ensemble des réels $x$ vérifiant $x^3-3x < 67$ est majoré par $10$, comme le montre une étude rapide de fonction. La partie $\mathbb{N}$ n'est pas majorée.

- Dire que le réel $\mu$ **n'est pas** un majorant de $E$ signifie qu'il existe au moins un élément $x$ de $E$ qui est **strictement** plus grand que $\mu$.

### 2.2 Partie minorée

> On dit que $E$ est minorée quand il existe un réel $m$ inférieur ou égal à tous les éléments de $E$ :
>
> $$ (\exists m \in \mathbb{R}) (\forall x \in E)(m \leq x) $$
> Un tel réel $m$ s'appelle minorant de $E$.

- Si $m$ est minorant de $E$, tout réel $m' <m$ est encore un minorant de $E$.

**Exemple 5** : Tout intervalle $E$ d'extrémités $a$ et $b$ est minoré, l'extrémité inférieure $a$ étant un minorant de $E$. L'ensemble des réels $x$ vérifiant $x^3-3x > 67$ est minoré par $2$, comme le montre une étude rapide de fonction. La partie $\mathbb{Z}$ n'est pas minorée, et la partie $\mathbb{N}$ est minorée.

### 2.3 Partie bornée

> On dit que $E$ est bornée quand elle est à la fois majorée et minorée :
>
> $$ (\exists m, M \in \mathbb{R})(\forall x \in E)(m \leq x \leq M) $$

- Une partie est bornée si et seulement si elle est incluse dans un segment $[m, M]$. D'ailleurs, ce mot "segment" est une abréviation de "intervalle fermé borné".

**Exemple 6** : Tout intervalle d'extrémités $a$ et $b$ est borné. L'ensemble des solutions de l'intéquation $-12 < x^3 - 34 cos(x) < 53$ est borné : il est inclus dans l'ensemble des solutions de $-12 - 34 < x^3 < 53+34$ qui est un intervalle borné.

> **Point d'interrogation**
>
> Sachant qu'une partie majorée admet **une infinité** de majorants, y en a-t-il un "plus intéressant" que les autres ? Sachant qu'une partie minorée admet une infinité de minorants, y en a-t-il un "plus intéressant" que les autres ?

- Cette question fondamentale a une réponse dans les deux paragraphes suivants.

## 3) Borne supérieure d'une partie non vide majorée

- Prenons une partie non vide $E$ majorée (par exemple) par $M=1$. Dire, ce qui est vrai, que $E$ est majorée par $2.567$ ne présente aucun intérêt car $2.567$ est "plus loin de $E$ que $1$" puisque $E$ est incluse par hypothèse dans $]-\infty, 1]$. Il est **bien plus intéressant** de regarder si des réels **plus petits** que $1$ sont encore des majorants de $E$, histoire de se "rapprocher de $E$".
- Parmi tous les majorants de $E$, celui qui serait le plus intéressant est celui qui est "le plus proche possible de $E$" : un nombre qui est plus grand que tous les éléments de $E$, mais qui en est "tout près" : ce doit être le plus petit majorant possible de $E$. Le théorème fondamental suivant assure son existence :

> **Théorème de la borne supérieure**
>
> Toute partie non vide majorée de $\mathbb{R}$ admet un majorant **plus petit** que tous les autres majorants. On l'appelle borne supérieure de $E$, et on le note *sup $E$*. Attention, en général, sup $E$ n'appartient pas à $E$.

- Ce théorème est admis : on ne peut le démontrer qu'avec une construction complète de $\mathbb{R}$ à partir des rationnels.
- Écrire que $M =$ sup $E$ demande donc deux choses :
  - $M$ est un majorant de $E$ : $(\exists x \in E)(x \leq M)$
  - Un réel strictement inférieur à $M$, que l'on peut noter $M - \epsilon$, n'est pas un majorant de $E$ : il existe donc au moins un élément $x \in E$ supérieur ou égal à $M - \epsilon$.

On peut résumer ceci dans le point suivant :

> **Méthodologie**
>
> Le réel $M$ est la borne supérieure de $E$ si et seulement si:
>
> - $(\forall x \in E)(x \leq M)$.
> - Pour tout $\epsilon > 0$, le segment $[M - \epsilon, M]$ contient au moins un élément de $E$.

- La borne supérieure est dans $E$ si et seulement si $E$ admet un **plus grand élément**, et la borne supérieure est ce plus grand élément.

**Exemple 7.a** : C'est le cas de $E = ]0,1]$ ou de $E = \{1,1/2,1/3,1/4,...\}$, où sup $E = 1$ est dans $E$.

- Si $E$ est une partie finie de $\mathbb{R}$, elle admet évidemment un plus grand élément, qui en est donc la borne supérieure.
- Le seul cas vraiment intéressant de borne supérieure est lorsque $E$ est infini et ne possède pas de plus grand élément.

> **Méthodologie et Philosophie**
>
> La borne supérieure de $E$ est le réel qui "remplace" le plus grand élément de $E$ lorsque $E$ n'en a pas.

**Exemple 7.b** : Soit $E = \{1/2, 2/3, 3/4, 4/5, ...\}$ l'ensemble de tous les réels de la forme $1-1/n$ pour $n\geq 2$. $E$ est clairement majoré par $1$, et sup $E$ est donc inférieure ou égale à $1$. Tout segment $[1- \epsilon, 1]$ contient au moins un élément de $E$ : il suffit de prendre $n > 1/\epsilon$. On a donc sup $E = 1$, et elle n'appartient pas à $E$.

**Exemple 8** : La borne supérieure d'un intervalle d'extrémités $a$ et $b$ est égale à $b$. Elle appartient à l'intervalle dans les cas $]a,b[$ et $[a, b[$.

## 4) Borne inférieure d'une partie non vide minorée

- On a un résultat analogue pour les parties non vides et minorées de $\mathbb{R}$, où c'est le plus grand minorant de $E$ qui est intéressant.

> **Théorème de la borne inférieure**
>
> Toute partie non vide minorée de $\mathbb{R}$ admet un minorant **plus grand** que tous les autres minorants. On l'appelle borne inférieure de $E$, et on le note *inf $E$*. Attention, en général, inf $E$ n'appartient pas à $E$.

- Écrire que $m =$ inf $E$ demande donc deux choses :
  - $m$ est un minorant de $E$ : $(\exists x \in E)(x \leq m)$
  - Un réel strictement supérieur à $m$, que l'on peut noter $m + \epsilon$, n'est pas un minorant de $E$ : il existe donc au moins un élément $x \in E$ inférieur ou égal à $m + \epsilon$.

On peut résumer ceci dans le point suivant :

> **Méthodologie**
>
> Le réel $m$ est la borne inférieure de $E$ si et seulement si:
>
> - $(\forall x \in E)(m \leq x)$.
> - Pour tout $\epsilon > 0$, le segment $[m, m + \epsilon]$ contient au moins un élément de $E$.

- La borne inférieure de $E$ n'a aucune raison d'appartenir à $E$. Elle en fait partie lorsque $E$ possède un plus petit élément : par exemple inf$[a,b[=a$. Le cas intéressant est celui où inf $E$ n'appartient pas à $E$. Voici un exemple de la vie sportive très parlant :

**Exemple 9.a** : Supposons que la vie sur terre soit éternelle, et appelons $E$ l'ensemble des performances, sur l'éternité, au 100m. C'est un ensemble non vide contenant une infinité d'éléments, la vie étant supposée durer indéfiniment sur terre. $E$ est clairement minoré par un nombre strictement positif : aucun homme ne courra le 100m en moins de (par exemple!) un centième de seconde. $E$ admet donc une borne inférieure $m$ supérieure ou égale à $0.01$, appartenant ou non à $E$.
Interprétons les conditions caractérisant la borne inférieure :

**Exemple 9.b** :

1. Personne ne mettra jamais, au grand jamais, moins de $m$ secondes pour courir 100m.
2. Dire que $m\in E$ signifie qu'il existera un jour un homme établissant le record du monde universel : il ne sera jamais battu.
3. Dire que $m \notin E$ signifie la chose suivante : personne ne mettra jamais $m$ seconeds pour courir 100m, mais pour tout $\epsilon > 0$, il y aura un homme qui mettra moins de $m+ \epsilon$ secondes : on s'approchera indéfiniment près de $m$. Tout record du monde sera temporaire, systématiquement battu plus tard.

**Exemple 9.c** : La valeur $m$ existe, les mathmétiques le disent, mais elle est inconnue. Les différents records du monde actuellement battus les uns après les autres s'approchent de $m$, vraisemblablement...

**Exemple 9.d** : On peut en dire autant pour la borne supérieure. L'ensemble $F$ contenant le nombre de victoires d'un coureur sain au tour de Franc eest un ensemble non vide dont on peut raisonnablement admettre qu'il est majoré par 100, même si l'espérance de vie augmente... Il possède donc une borne supérieure, qui est d'ailleurs son plsu grand élément, puisque l'on est dans les entiers. Actuellement, on sait que sup $F \geq 5$ ($5$ victoires pour Anquetil, Marcks, Hinault, Indurain). Mais ce nombre $5$ est-il la borne supérieure de $F$ ? Réponse dans une éternité !

## 5) Théorèmes sur les suites monotones

- Voici les grands théorèmes, qui seront démontrés grâce à la borne supérieure / inférieure, dans le chapitre sur les suites : 

> **Théorème 1** : Une suite croissante converge si et seulement si elle est majorée. Une suite décroissante converge si et seulement si elle est minorée.

- Ce théorème s'énonce géométriquement d'une façon très parlante. On dit qu'une suite $([a_n, b_n])$ de segments est emboîtée quand on a les inclusions suivantes :
$$ [a_1, b_1] \supset [a_2, b_2] \supset [a_3, b_3] \supset ... \supset [a_n, b_n] \supset [a_{n+1}, b_{n+1}] \supset ... $$

- L'énoncé géométrique est maintenant :

> **Théorème 2** : Soit $([a_n, b_n])$ une suite de segments emboîtés dont la longueur $b_n - a_n$ tend vers $0$. Alors il existe un et un seul réel appartenant à tous les segments.

Ce théorème sert par exemple à démontrer le théorème des valeurs intermédiaires pour une fonction continue.

- Une suite croissante non majorée tend vers $+\infty$ et une suite décroissante non minorée tend vers $-\infty$.

## 6) Point d'accumulation d'une partie infinie de $\mathbb{R}$

> On dit que $a$ est un point d'accumulation de la partie $E$ lorsque tout voisinage de $a$ contient **une infinité** de points de $E$.

**Exemple 10** : Le réel $1$ est un point d'accumulation de l'ensemble $E = \{1/2, 2/3, 3/4, 4/5, ...\}$ déjà rencontré. On voit assez facilement que c'est le seul. Cela vient du fait que $E$ est l'ensemble des termes d'une suite convergeant vers $1$.

**Exemple 11** : Tout réel de $[0,1]$ est point d'accumulation de $E = ]0,1[$.

**Exemple 12 [admis]** : Tout réel est point d'accumulation de l'ensemble $\mathbb{Q}$ des rationnels. Cela signifie que tout intervalle réel non réduit à un point contient **une infinité** de nombres rationnels. De même, tout réel est point d'accumulation de l'ensemble $\mathbb{R} \backslash \mathbb{Q}$ des irrationnels : tout intervalle réel non réduit à un point contient **une infinité** de nombres irrationnels.

## 7) Théorème de Bolzano-Weierstrass

- Ce théorème admet deux énoncés quivalents, mais très importants tous les deux :
  - > **Bolzano-Weierstrass 1** : Toute partie infinie et bornée de $\mathbb{R}$ admet au moins un point d'accumulation.

  - > **Bolzano-Weierstrass 2** : Toute suite bornée contient une sous-suite convergente.

- Cet énoncé signifie que si la suite $\{x_n\}$ est bornée, on peut trouver une infinité d'entiers $n_1 < n_2 < n_3 < ... < n_k ...$ tels que la suite $(x_{n_k})$ converge vers une limite finie.

**Exemple 13** : La suite de terme général $u_n = sin(n)$ ne converge pas. Mais, comme elle est bornée, elle contient au moins une sous-suite convergente.

- Ce théorème intervient dans des démonstrations théoriques. Par exemple celle disant que toute fonction continue sur un segment $y$ présente un minimum et un maximum.

## 8) Théorème de densité

> Une partie $E$ est dite dense dans $\mathbb{R}$ quand tout intervalle ouvert contient une infinité de points de $E$.

<!-- TODO : FINIR LE CHAPITRE 1 EN ANALYSE -- >