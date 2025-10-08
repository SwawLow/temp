definition des sous problèm:

tracer un rectangle (1)
tracer une étoile a 5 sommet (2)
tracer des étoiles dans un rond (3)
tracer le drapeau d'europe (4)
tracer le drapeau belgique (5)
tracer un drapeau avec des couleur et orientation des ligne au choix (6)

(1):
-fonction = rectangle()
-changer les dimension pour qu'elle correspond a 2(longeur*largeur) appartir de square()

(2):
-fonction = drawStar()
-sauvegarder les coordonner du debut
-trouver l'angle pour orienter la tortue
-faire une boucle for pour executer du 4 fois + un avancement
-remplir le pentagone dans l'étoile
-teleporter la tortue au coordonner sauvegarder

(3):
-fonction = shapeAlignement()
-sauvegarder les coordonner du debut
-appeler la fonction etoile autour des coordonner du debut
-teleporter la tortue au coordonner sauvegarder
-repeter appartir de "appeler la fonction etoile autour des coordonner du debut" 12 fois

(4):
-fonction = european_flag()
-appler la fonction rectangle() pour faire un rectangle blue
-positioner la tortue au-milieu du rectangle blue et appler la fonction shapeAlignement()

(5):
-fonction = belgian_flag()
-appler la fonction rectangle() 3 fois avec la longueur diviser en 3 pour faire les trois colognes:noir, jaune et rouge

(6):
-fonction = three_color_flag()
-ajouter une variable orientation pour soit faire des lines ou des colognes
-appler la fonction rectangle() 3 fois avec la longueur diviser en 3 pour faire les trois colognes avec des coleur aux choix
-appler la fonction rectangle() 3 fois avec la largeur diviser en 3 pour faire les trois lines avec des coleur aux choix
