is_adn regard si une chaine de caractere contient que A, C, G et T, 
si il contient que se dernier, il retourn vrai sinon faux.

positions retourn l'indexe d'ou commence un chaine de caractere specifier.
"AC" apparait 3 fois dans "ACGTACTCAC" dans cet ordre: indexe 0, indexe 4 et indexe 8.

distance_h retourn le nombre de difference entre deux chaine de caractere en regardant 
si chaque indexe est indentique. exemple: ACTG et ACGT => 2, T et G son inverser se qui done 2.

distance_matrice creer une matrice avec le fonction distance_h 
en comparant tout les chaine de characteres d'une list entre eux, 
si une chaine de charactere est l'input il va traiter chaque caractere individuellement 
et si il y a qu'eu un charactere il va retourner une list comme cela [0]