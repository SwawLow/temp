import turtle

totalsize = 400
length = (totalsize*1.9/3)//1
width = (totalsize*1/3)//1

t = turtle.Turtle()     # créer une nouvelle tortue
t.speed("fastest")      # tracé rapide

def square(size, color):
    """Trace un carré plein de taille `size` et de couleur `color`.

    pre: `size` spécifie une taile.
         `color` spécifie une couleur.
         La tortue `t` est initialisée.
         La tortue est placée à un sommet et orientée en direction d'un
         côté du carré.
    post: Le carré a été tracé sur la droite du premier côté.
          La tortue est à la même position et orientation qu'au départ.
    """
    t.color(color)
    t.pendown()
    t.begin_fill()
    for k in range(4):
        t.forward(size)
        t.right(90)    
    t.end_fill()
    t.penup()

def rectangle(length, width, color):
    """Trace un rectangle plein de taille `size` et de couleur `color`.

    pre: `length` spécifie une longueur.
         `width` spécifie une largeur.
         `color` spécifie une couleur.
         La tortue `t` est initialisée.
         La tortue est placée à un sommet et orientée en direction d'un
         côté du carré.
    post: Le carré a été tracé sur la droite du premier côté.
          La tortue est à la même position et orientation qu'au départ.
    """
    t.color(color)
    t.pendown()
    t.begin_fill()
    for k in range(2):
        t.forward(length)
        t.right(90)    
        t.forward(width)
        t.right(90)
    t.end_fill()
    t.penup()

def drawStar(color, size):

    """Trace une étoile 1.5/450 plein de la taille `size` et de couleur `color`.

    pre: `size` spécifie une taile.
         `color` spécifie une couleur.
         La tortue `t` est initialisée.
         La tortue est placée dans une position
    post: L'étoile a été tracé
          La tortue est à la même position et orientation qu'au départ.
    """

    starSize = size*1.5/450

    ogCenterPositionX = t.xcor()
    ogCenterPositionY = t.ycor()

    d = 10*starSize #mov dist
    g = 2.5*starSize #mov dist
    q = 6.3*starSize #mov dist

    r = 144 #angle
    h = 74 #angle

    t.setheading(0)
    t.color(color)
    t.pendown()
    t.begin_fill()

    for k in range(4):
        t.forward(d)
        t.right(r)
    t.forward(d)

    t.end_fill()
    t.penup()
    
    t.right(r+180)
    t.forward(-q)
    
    t.pendown()
    t.begin_fill()

    for k in range(4):
        t.forward(g)
        t.left(h)
    t.forward(g)

    t.end_fill()
    t.penup()
    t.teleport(ogCenterPositionX,ogCenterPositionY)

def shapeAlignement(numberOfShapes, color, length, width, pasteShape):

    """Trace des formes de taille `size` et de couleur `color`.

    pre: `length` spécifie une longueur.
         `width` spécifie une largeur.
         `color` spécifie une couleur.
         `number`spécifie un nombre.
         `object`spécifie une fonction pour tracer les formes.
         La tortue `t` est initialisée.
         La tortue est placée à une position.

    post: trace dans un rond autour de la tortue la form specifier, le nombre de fois qui a été specifier.
          La tortue est à la même position et orientation qu'au départ.
    """

    size = length+width


    t.forward(length//2)
    t.right(90)
    t.forward(width//2)
    ogCenterPositionX = t.xcor()
    ogCenterPositionY = t.ycor()

    for k in range(numberOfShapes):
        t.setheading(360//numberOfShapes*k)
        t.forward(size//8)
        pasteShape(color,size)
        t.teleport(ogCenterPositionX,ogCenterPositionY)

def european_flag(length,width,color1,color2,numberOfShapes,pasteShape):

    """Trace le drapeau d'europe plein de taille `size` et de couleur `color`.

    pre: `length` spécifie une longueur.
         `width` spécifie une largeur.
         `color1` spécifie une couleur.
         `color2` spécifie une couleur.
         `numberOfShapes`spécifie un nombre.
         `pasteShape`spécifie une fonction pour tracer les formes.
         La tortue `t` est initialisée.
         La tortue est placée à une position.

    post: trace le drapeau d'europe.
          La tortue est à la même position et orientation qu'au départ.
    """

    ogCenterPositionX = t.xcor()
    ogCenterPositionY = t.ycor()
    ogHeading = t.heading()

    rectangle(length, width, color1)
    shapeAlignement(numberOfShapes, color2, length, width, pasteShape)

    t.teleport(ogCenterPositionX,ogCenterPositionY)
    t.setheading(ogHeading)

def belgian_flag(length,width):
     
    """Trace le drapeau de belgique plein de taille `size` et de couleur `color`.

    pre: `length` spécifie une longueur.
         `width` spécifie une largeur.
         La tortue `t` est initialisée.
         La tortue est placée à une position.

    post: trace le drapeau d'europe.
          La tortue est à la même position et orientation qu'au départ.
    """

    ogCenterPositionX = t.xcor()
    ogCenterPositionY = t.ycor()
    ogHeading = t.heading()

    rectangle(length//3, width, 'black')
    t.forward(length//3)
    rectangle(length//3, width, 'yellow')
    t.forward(length//3)
    rectangle(length//3, width, 'red')
    
    t.teleport(ogCenterPositionX,ogCenterPositionY)
    t.setheading(ogHeading)

def three_color_flag(length,width,color1,color2,color3,orientation):
     
    """Trace un drapeau plein avec des couleur et les ligne aux choix de taille `size` et de couleur `color`.

    pre: `length` spécifie une longueur.
         `width` spécifie une largeur.
         `color1` spécifie une couleur.
         `color2` spécifie une couleur.
         `color3` spécifie une couleur.
         `orientation` spécifie une orientation(vertical, horizontal).
         La tortue `t` est initialisée.
         La tortue est placée à une position.

    post: trace le drapeau d'europe.
          La tortue est à la même position et orientation qu'au départ.
    """

    ogCenterPositionX = t.xcor()
    ogCenterPositionY = t.ycor()
    ogHeading = t.heading()

    if orientation == 'vertical':
        rectangle(length//3, width, color1)
        t.forward(length//3)
        rectangle(length//3, width, color2)
        t.forward(length//3)
        rectangle(length//3, width, color3)

    elif orientation == 'horizontal':
        rectangle(length, width//3, color1)
        t.right(90)
        t.forward(width//3)
        t.setheading(ogHeading)
        rectangle(length, width//3, color2)
        t.right(90)
        t.forward(width//3)
        t.setheading(ogHeading)
        rectangle(length, width//3, color3)
    
    t.teleport(ogCenterPositionX,ogCenterPositionY)
    t.setheading(ogHeading)

t.teleport(-100, 150)
t.ht()

european_flag(length, width,'blue','yellow',12,drawStar)
t.forward(length+20)
three_color_flag(length, width, 'black', 'yellow', 'red', 'vertical') #
t.forward(-length*2-40)
three_color_flag(length, width, 'blue', 'white', 'red', 'vertical')
t.right(90)
t.forward(width+20)
t.left(90)
three_color_flag(length, width, 'red', 'white', 'blue', 'horizontal')
t.forward(length+20)
three_color_flag(length, width, 'black', 'red', 'yellow', 'horizontal')
t.forward(length+20)
three_color_flag(length, width, 'red', 'white', 'cyan', 'horizontal')

turtle.done()

'''

#t.teleport(-100, 150)
#drawBonusFlag(length, width, 'red', 'black', 'red', 'black', 'yellow', 'red', 15, three_color_flag, 'horizontal', 'vertiacal')

def flagAlignement(numberOfShapes, color1, color2, color3, length, width, pasteShape, orientation):

    """Trace des formes plein de taille `size` et de couleur `color`.

    pre: `orientation` spécifie une longueur.
         `length` spécifie une longueur.
         `width` spécifie une largeur.
         `color` spécifie une couleur.
         `number`spécifie un nombre.
         `object`spécifie une fonction pour tracer les formes.
         La tortue `t` est initialisée.
         La tortue est placée à une position.

    post: trace dans un rond autour de la tortue la form specifier, le nombre de fois qui a été specifier.
          La tortue est à la même position et orientation qu'au départ.
    """

    size = length+width

    t.forward(length//2)
    t.right(90)
    t.forward(width//1.8)
    ogCenterPositionX = t.xcor()
    ogCenterPositionY = t.ycor()
    ogHeading = t.heading()

    t.setheading(0)
    for k in range(numberOfShapes):
        t.setheading(360//numberOfShapes*k)
        t.forward(size//8)
        t.setheading(ogHeading)
        pasteShape(length, width, color1, color2, color3, orientation)
        t.teleport(ogCenterPositionX,ogCenterPositionY)

def drawBonusFlag(length, width, color1, color2, color3, color4, color5, color6, numberOfShapes, pasteShape, orientation1, orientation2):

    """Trace le drapeau d'europe plein de taille `size` et de couleur `color`.

    pre: `length` spécifie une longueur.
         `width` spécifie une largeur.
         `color1` spécifie une couleur.
         `color2` spécifie une couleur.
         `numberOfShapes`spécifie un nombre.
         `pasteShape`spécifie une fonction pour tracer les formes.
         La tortue `t` est initialisée.
         La tortue est placée à une position.

    post: trace le drapeau d'europe.
          La tortue est à la même position et orientation qu'au départ.
    """

    ogCenterPositionX = t.xcor()
    ogCenterPositionY = t.ycor()
    ogHeading = t.heading()

    three_color_flag(length, width, color1, color2, color3, orientation1)
    flagAlignement(numberOfShapes, color4, color5, color6, length, width, pasteShape, orientation2)

    t.teleport(ogCenterPositionX,ogCenterPositionY)
    t.setheading(ogHeading)
'''
