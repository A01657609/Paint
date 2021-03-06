from turtle import *
from freegames import vector

#Linea de un punto x a y
def line(start, end):
    "Draw line from start to end."
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

def square(start, end):
    "Draw square from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    #Dibujar 4 lineas con angulo de 90 para formar el cuadrado
    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

def circles(start, end):
    "Draw circle from start to end"
    begin_fill()
    up()
    goto(start.x, start.y)
    down()
    #Funcion circle para dibujar un circulo con un radio definido
    circle(end.x - start.x)
    end_fill()
    
  

def rectangle(start, end):
    "Draw rectangle from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    #ciclo para realizar un rectangulo de largo x, ancho y
    for count in range(2):
        forward(end.x - start.x)
        left(90)
        forward((end.x - start.x)/2)
        left(90)
    end_fill()
 

def triangle(start, end):
    "Draw triangle from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    #triangulo con un angulo de 60
    for count in range(3):
        forward(end.x - start.x)
        left(120)

    end_fill()

   
#definicion de los puntos x,y
def tap(x, y):
    "Store starting point or draw shape."
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

def store(key, value):
    "Store value in state at key."
    state[key] = value

#Llamar las funciones de las figuras
state = {'start': None, 'shape': line}
state = {'start': None, 'shape': circles}
state = {'start': None, 'shape': rectangle}
state = {'start': None, 'shape': square}
state = {'start': None, 'shape': triangle}

#Tamaño y ubicacion de la pantalla
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')

#Colores
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('orange'), 'O')
onkey(lambda: color('purple'), 'P')

#Inicializar la figura que se desea
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circles), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()

