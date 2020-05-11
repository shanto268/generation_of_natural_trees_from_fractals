import turtle as tu 
import random
foo = tu.Turtle()
foo.speed(0) #fastest
foo.penup()
foo.setpos(0,-275)

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
    angle = random.randint(0,32)
    print("factor: ", factor)
    print("angle: ", angle)
    print("steps: ", num)
    print("y coordinate:", foo.ycor())
    print()
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


#still need to fix the y splitting
def notSoYtree(num):
    factor = random.uniform(0,1)
    angle = random.randint(0,32)
    prob = random.uniform(0, 1)
    xRand = random.uniform(0,1)
    print("factor: ", factor)
    print("angle: ", angle)
    print("steps: ", num)
    print("y coordinate:", foo.ycor())
    print()
    if (num < 1):
        return 
    else:
        leftBranch(num,angle)
        notSoYtree(num*factor)
        rightBranch(num, angle,factor)

def leftBranch(num,angle):
        foo.fd(num)
        foo.left(angle)

def rightBranch(num,angle,factor):
        foo.right(2*angle)
        notSoYtree(num*factor)
        foo.left(angle)
        foo.bk(num)

foo.ht()
foo.left(90)
foo.pendown()
notSoYtree(150)
tu.mainloop()
