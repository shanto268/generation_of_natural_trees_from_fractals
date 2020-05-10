import turtle as tu 
import random
foo = tu.Turtle()
foo.speed(0) #fastest
foo.sety(-70)

def randomMove():
    rotate = random.randint(0,360)
    move = random.randint(-50,50)
    foo.seth(rotate)
    foo.forward(move)

def moveRandomly():
    time = random.randint(20,23)
    for i in range(time):
        random()

def yTree(num):
    factor = random.uniform(0,1)
    if (num < 1):
        return 
    else:
        foo.fd(num)
        foo.left(30)
        yTree(num*factor)
        foo.right(60)
        yTree(num*factor)
        foo.left(30)
        foo.bk(num)

foo.ht()
foo.left(90)
yTree(120)
tu.mainloop()
