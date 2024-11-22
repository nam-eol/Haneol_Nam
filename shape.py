x, y, r, a,la,lb =[0]*6

## 국기 윤곽선(검정) ##
def black_line(x,y,la,lb):
    import turtle as t
    t.pu()
    t.goto(x, y)
    t.pd()
    t.pencolor("black")
    for i in range(2) :
        t.fd(la)
        t.left(90)
        t.fd(lb)
        t.left(90)


## 원 ##
def circle(x, y, r, a, c):
    import turtle as t   
    t.pu()
    t.goto(x, y)
    t.pd()
    t.begin_fill()
    t.color(c)
    t.circle(r,a)
    t.end_fill()
    t.seth(0)

## 사각형 ##
def square(x,y,la,lb,c):
    import turtle as t   
    t.pu()
    t.goto(x, y)
    t.pd()
    t.begin_fill()
    t.color(c)
    for i in range(2):
        t.fd(la)
        t.lt(90)
        t.fd(lb)
        t.lt(90)
    t.end_fill()
    t.seth(0)

## 정삼각형 ##
def triangle(x,y,l,c):
    import turtle as t   
    t.pu()
    t.goto(x, y)
    t.pd()
    t.begin_fill()
    t.color(c)
    for i in range(3):
        t.fd(l)
        t.lt(120)
    t.end_fill()
    t.seth(0)

## 직각이등변 삼각형 ##
def my_triangle(x,y,l1,l2,c):
    import turtle as t   
    t.pu()
    t.goto(x, y)
    t.pd()
    t.begin_fill()
    t.color(c)
    t.fd(l1)
    t.lt(135)
    t.fd(l2)
    t.lt(135)
    t.fd(l1)
    t.end_fill()
    t.seth(0)
    
## 별 ##
def star(x,y,l,c):
    import turtle as t   
    t.pu()
    t.goto(x, y)
    t.pd()
    t.begin_fill()
    t.color(c)
    for i in range(5):
        t.fd(l)
        t.lt(72)
        t.fd(l)
        t.rt(144)
    t.end_fill()
    t.seth(0)

## 별(좌표X - 우즈베키스탄) ##
def uzstar(l,c):
    import turtle as t
    t.pd()
    t.begin_fill()
    t.color(c)
    for i in range(5):
        t.fd(l)
        t.lt(72)
        t.fd(l)
        t.rt(144)
    t.end_fill()
    t.seth(0)

## 마름모 ##
def rhombus(x,y,l,c):
    import turtle as t   
    t.pu()
    t.goto(x, y)
    t.pd()
    t.begin_fill()
    t.color(c)
    for i in range(2) :
        t.fd(l)
        t.left(120)
        t.fd(l)
        t.lt(60)
    t.end_fill()
    t.seth(0)
