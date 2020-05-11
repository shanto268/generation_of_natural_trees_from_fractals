import turtle as tu 
import random
foo = tu.Turtle()
foo.speed(0) #fastest
foo.sety(-150)

def randomMove():
    rotate = random.randint(0,360)
    move = random.randint(-50,50)
    foo.seth(rotate)
    foo.forward(move)

def moveRandomly():
    time = random.randint(20,23)
    for i in range(time):
        randomMove()

def yTree(num):
    factor = random.uniform(0,1)
    angle = random.randint(30,32)
    if (num < 1):
        return 
    else:
        foo.fd(num)
        foo.left(angle)
        yTree(num*factor)
        foo.right(2*angle)
        yTree(num*factor)
        foo.left(angle)
        foo.bk(num)

foo.ht()
foo.left(90)
yTree(150)
#moveRandomly()
tu.mainloop()
