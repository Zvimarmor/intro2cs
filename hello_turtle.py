#####################
#login=zvi.marmor
#ID=206949539
#name= Zvi Marmor
#####################


import turtle

def draw_triangle():
    '''definding a function that draws a triangle'''
    #These next lines draws a triangle
    turtle.forward(45)
    turtle.right(120)
    turtle.forward(45)
    turtle.right(120)
    turtle.forward(45)
    turtle.right(120)
    

def draw_sail():
    '''definding a function that draws a sail'''
    #these next lines draw a sail
    turtle.left(90)
    turtle.forward(50)
    turtle.right(150)
    draw_triangle()
    turtle.right(30)
    turtle.up()
    turtle.forward(50)
    turtle.down()
    turtle.left(90)

def draw_ship():
    '''definding a function that draws a ship'''
    #these next lines uses previous function and draws ship
    turtle.forward(50)
    draw_sail()
    turtle.forward(50)
    draw_sail()
    turtle.forward(50)
    draw_sail()
    turtle.forward(50)
    turtle.right(120)
    turtle.forward(20)
    turtle.right(60)
    turtle.forward(180)
    turtle.right(60)
    turtle.forward(20)
    turtle.right(120)
    

def draw_fleet():
    '''definding a function that draws a triangle'''
    #these next lines uses previous function and draws fleet of ships
    draw_ship()
    turtle.up()
    turtle.right(180)
    turtle.forward(300)
    turtle.right(180)
    turtle.down()
    draw_ship()
    turtle.up()
    turtle.forward(300)
    turtle.done()

if __name__=='__main__':
    draw_fleet()
