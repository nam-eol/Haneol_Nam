## 북마케도니아 국기 ##
def draw_북마케도니아():
    import turtle as t
    t.reset()
    t.speed(10)
    t.colormode(255)

    R = 216, 33, 38
    Y = 248, 233, 46

    from shape import square as SQ
    from shape import circle as C
    from shape import black_line as B_L

    SQ(-140*3, -70*3,280*3,140*3,R)

    t.pu()
    t.goto(-140*3, 14*3)
    t.pd()
    t.begin_fill()
    t.color(Y)
    t.goto(140*3,-14*3)
    t.goto(140*3, 14*3)
    t.goto(-140*3, -14*3)
    t.end_fill()

    t.pu()
    t.goto(-140*3,-70*3)
    t.pd()
    t.begin_fill()
    t.color(Y)
    t.goto(140*3,70*3)
    t.goto(112*3,70*3)
    t.goto(-112*3,-70*3)
    t.end_fill()

    t.pu()
    t.goto(-14*3,-70*3)
    t.pd()
    t.begin_fill()
    t.color(Y)
    t.goto(14*3,70*3)
    t.goto(-14*3,70*3)
    t.goto(14*3,-70*3)
    t.end_fill()

    t.pu()
    t.goto(98*3,-70*3)
    t.pd()
    t.begin_fill()
    t.color(Y)
    t.goto(-98*3,70*3)
    t.goto(-140*3,70*3)
    t.goto(140*3,-70*3)
    t.end_fill()

    t.rt(90)
    C(-25*3,0,25*3,360,R)
    t.rt(90)
    C(-20*3,0,20*3,360,Y)

    B_L(-140*3,-70*3,280*3,140*3)

## 남아프리카 공화국 국기 ##
def draw_남아프리카공화국():
    import turtle as t
    t.reset()
    t.speed(10)
    t.colormode(255)

    BK= 0,0,0
    G=0,122,77
    R=222,56,49
    BL=0,35,149
    Y=255,182,18
    W=255,255,255

    from shape import square as SQ
    from shape import triangle as T
    from shape import black_line as B_L

    SQ(-45*10,-30*10,11.059*10,60*10,G)

    t.lt(30)
    t.pu()
    t.goto(-33.941*10,-30*10)
    t.pd()
    t.begin_fill()
    t.color(G)
    t.goto(1.907*10,-6*10)
    t.goto(1.907*10,6*10)
    t.goto(-33.941*10,30*10)
    t.seth(0)
    t.end_fill()

    SQ(1.907*10,-6*10,43.093*10,12*10,G)
    t.lt(30)
    T(-45*10,-22.775*10,45*10,Y)
    t.lt(30)
    T(-45*10,-18.178*10,36.356*10,BK)

    t.pu()
    t.goto(-26.695*10, 30*10)
    t.pd()
    t.begin_fill()
    t.color(R)
    t.goto(45*10,30*10)
    t.goto(45*10,10*10)
    t.goto(3.051*10,10*10)
    t.goto(-26.695*10, 30*10)
    t.end_fill()

    t.pu()
    t.goto(-26.695*10, -30*10)
    t.pd()
    t.begin_fill()
    t.color(BL)
    t.goto(45*10,-30*10)
    t.goto(45*10,-10*10)
    t.goto(3.051*10,-10*10)
    t.goto(-26.695*10, -30*10)
    t.end_fill()

    B_L(-45*10, -30*10,90*10,60*10)

## 튀니지 국기 ##
def draw_튀니지():
    import turtle as t
    t.reset()
    t.speed(10)
    
    R=231,0,19
    W=255,255,255

    t.colormode(255)

    from shape import square as SQ
    from shape import circle as C
    from shape import star as S
    from shape import black_line as B_L

    SQ(-60*5,-40*5,120*5,80*5,R)
    t.rt(90)
    C(-20*5,0,20*5,360,W)
    t.rt(90)
    C(-15*5,0,15*5,360,R)
    t.rt(90)
    C(-7.862*5,0,12*5,360,W)
    t.lt(18)
    S(-4.931*5,0,6.713*5,R)

    B_L(-60*5, -40*5,120*5,80*5)

## 우즈베키스탄 국기 ##
def draw_우즈베키스탄():
    import turtle as t
    t.reset()
    t.speed(0)
    
    B=0,153,181
    W=255,255,255
    G=30,181,58
    R=206,17,38

    t.colormode(255)

    from shape import square as SQ
    from shape import circle as C
    from shape import uzstar as S
    from shape import black_line as B_L

    SQ(-125*3, -62.49*3,250*3,40*3,G)
    SQ(-125*3,-22.49*3,250*3,2.5*3,R)
    SQ(-125*3,20*3,250*3,2.49*3,R)
    SQ(-125*3,22.49*3,250*3,40*3,B)

    t.rt(90)
    C(-105*3,42.5*3,15*3,360,W)
    t.rt(90)
    C(-100*3,42.5*3,15*3,360,B)


    t.pu()
    t.goto(-52*3,57.5*3)
    for i in range(3):
        t.rt(72)
        S(2.622*3,W)
        t.pu()
        t.fd(12*3)

    t.pu()
    t.goto(-64*3,45.5*3)
    for i in range(4):
        t.rt(72)
        S(2.622*3,W)
        t.pu()
        t.fd(12*3)

    t.pu()
    t.goto(-76*3,33.5*3)
    for i in range(5):
        t.rt(72)
        S(2.622*3,W)
        t.pu()
        t.fd(12*3)

    B_L(-125*3, -62.49*3,250*3,125*3)
    
## 앤티가 바부다 국기 ##
def draw_앤티가바부다():
    import turtle as t
    t.reset()
    t.speed(0)

    R=206,17,38
    BK=0,0,0
    Y=252,209,22
    BL=0,114,198
    W=255,255,255

    t.colormode(255)

    from shape import square as SQ
    from shape import circle as C
    from shape import black_line as B_L

    SQ(-34.5*10, -23*10,69*10,46*10,BK)

    t.right(90)
    C(-7.5*10,5*10,7.5*10,360,Y)

    SQ(-21.146*10,-5*10,42.292*10,10*10,BL)
    SQ(-13.597*10,-23*10,27.194*10,18*10,W)

    t.pu()
    t.goto(-34.5*10, 23*10)
    t.pd()
    t.begin_fill()
    t.color(R)
    t.goto(0,-23*10)
    t.goto(34.5*10, 23*10)
    t.goto(34.5*10, -23*10)
    t.goto(-34.5*10, -23*10)
    t.goto(-34.5*10, 23*10)
    t.end_fill()

    t.rt(180)
    t.pu()
    t.goto(-15*10,5*10)
    t.pd()
    t.right(168.496)
    t.begin_fill()
    t.color(Y)
    for i in range(8):
        t.fd(7.838*10)
        t.left(135.767)
        t.fd(7.838*10)
        t.right(158.392)
    t.end_fill()
    t.seth(0)

    B_L(-34.5*10, -23*10,69*10,46*10)

## 조선민주주의 인민공화국 국기 ##
def draw_조선민주주의인민공화국():
    import turtle as t
    t.reset()
    t.speed(10)
    
    B=2,79,162
    W=255,255,255
    R=237,28,39

    t.colormode(255)

    from shape import square as SQ
    from shape import circle as C
    from shape import star as S
    from shape import black_line as B_L

    SQ(-36*10, -18*10,72*10,36*10,B)
    SQ(-36*10, -12*10,72*10,24*10,W)
    SQ(-36*10, -11*10,72*10,22*10,R)
    
    t.right(90)
    C(-20*10, 0,8*10,360,W)
    t.rt(72)
    S(-12*10, 7.75*10,5.538*10,R)

    B_L(-36*10, -18*10,72*10,36*10)

## 이스라엘 국기 ##
def draw_이스라엘():
    import turtle as t
    t.reset()
    t.speed(10)
    

    W=255,255,255
    B=0,56,184

    t.colormode(255)

    from shape import square as SQ
    from shape import triangle as T
    from shape import black_line as B_L

    SQ(-55*5, 20*5,110*5,12*5,B)
    SQ(-55*5, -32*5,110*5,12*5,B)

    t.rt(120)
    T(0, 16.8*5,29.6*5,B)
    t.rt(120)
    T(0, 12*5,20.8*5,W)

    t.pu()
    t.goto(0, -16.8*5)
    t.pd()
    t.lt(60)
    t.begin_fill()
    t.color(B)
    for i in range(3) :
        t.fd(29.6*5)
        t.left(120)
    t.pu()
    t.goto(0, -12*5)
    for i in range(3) :
        t.fd(20.8*5)
        t.left(120)
    t.end_fill()

    t.seth(0)
    B_L(-55*5,-40*5,110*5,80*5)

## 영국 국기 ##
def draw_영국():
    import turtle as t
    t.reset()
    t.speed(0)
    
    B=0,36,125
    W=255,255,255
    R=207,20,43

    t.colormode(255)

    from shape import square as SQ
    from shape import black_line as B_L


    SQ(-30*10,-15*10,60*10,30*10,B)

    t.pu()
    t.goto(-30*10,11.667*10)
    t.pd()
    t.begin_fill()
    t.color(W)
    t.right(30)
    t.goto(-6.875*10,0)
    t.left(90)
    t.fd(6*10)
    t.left(90)
    t.goto(-22.292*10,15*10)
    t.goto(-30*10,15*10)
    t.end_fill()


    t.lt(180)
    t.pu()
    t.goto(-30*10,15*10)
    t.pd()
    t.begin_fill()
    t.color(R)
    t.goto(0,0)
    t.rt(90)
    t.fd(2*10)
    t.rt(90)
    t.goto(-30*10,12.709*10)
    t.end_fill()

    t.seth(0)

    t.pu()
    t.goto(30*10,-11.667*10)
    t.pd()
    t.rt(210)
    t.begin_fill()
    t.color(W)
    t.goto(6.875*10,0)
    t.lt(90)
    t.fd(6*10)
    t.lt(90)
    t.goto(22.292*10,-15*10)
    t.goto(30*10,-15*10)
    t.end_fill()


    t.lt(180)
    t.pu()
    t.goto(30*10,-15*10)
    t.pd()
    t.begin_fill()
    t.color(R)
    t.goto(0,0)
    t.rt(90)
    t.fd(2*10)
    t.rt(90)
    t.goto(30*10,-12.709*10)
    t.end_fill()

    t.seth(0)

    t.pu()
    t.goto(-30*10,-11.667*10)
    t.pd()
    t.lt(30)
    t.begin_fill()
    t.color(W)
    t.goto(-6.875*10,0)
    t.rt(90)
    t.fd(6*10)
    t.rt(90)
    t.goto(-22.292*10,-15*10)
    t.goto(-30*10,-15*10)
    t.end_fill()


    t.lt(180)
    t.pu()
    t.goto(-30*10,-15*10)
    t.pd()
    t.begin_fill()
    t.color(R)
    t.goto(0,0)
    t.rt(90)
    t.fd(2*10)
    t.rt(90)
    t.goto(-25.417*10,-15*10)
    t.end_fill()

    t.seth(0)

    t.pu()
    t.goto(30*10,11.667*10)
    t.pd()
    t.lt(30)
    t.begin_fill()
    t.color(W)
    t.goto(6.875*10,0)
    t.lt(90)
    t.fd(6*10)
    t.lt(90)
    t.goto(22.292*10,15*10)
    t.goto(30*10,15*10)
    t.end_fill()


    t.lt(180)
    t.pu()
    t.goto(30*10,15*10)
    t.pd()
    t.begin_fill()
    t.color(R)
    t.goto(0,0)
    t.lt(90)
    t.fd(2*10)
    t.lt(90)
    t.goto(25.417*10,15*10)
    t.end_fill()

    t.seth(0)

    SQ(-30*10,-5*10,60*10,10*10,W)
    SQ(-5*10,-15*10,10*10,30*10,W)
    SQ(-30*10,-3*10,60*10,6*10,R)
    SQ(-3*10,-15*10,6*10,30*10,R)

    B_L(-30*10,-15*10,60*10,30*10)

## 세인트빈센트 그레나딘 국기 ##
def draw_세인트빈센트그레나딘():
    import turtle as t
    t.reset()
    t.speed(0)

    B=0,38,116
    Y=252,208,34
    G=0,124,46

    t.colormode(255)

    from shape import square as SQ
    from shape import rhombus as RH
    from shape import black_line as B_L

    SQ(-70.5*5,-47*5,141*5,94*5,Y)
    SQ(-70.5*5,-47*5,35*5,94*5,B)
    SQ(35.5*5,-47*5,35*5,94*5,G)

    t.rt(60)
    RH(-19.5*5,0,18*5,G)
    t.rt(60)
    RH(1*5,0,18*5,G)
    t.rt(60)
    RH(-9.5*5,-20*5,18*5,G)

    B_L(-70.5*5,-47*5,141*5,94*5)

## 대한민국 ##
def draw_대한민국():
    import turtle as t
    t.reset()
    t.speed(0)
    
    R=207,20,43
    BL=0,71,160
    BK=14,14,14
    W=255,255,255

    t.colormode(255)

    from shape import black_line as B_L

    B_L(-36*10,-24*10,72*10,48*10)

    t.pu()
    t.goto(0,0)
    t.lt(146.045)
    t.fd(12*10)
    t.pd()
    t.lt(90)
    t.begin_fill()
    t.color(BL)
    t.circle(12*10,180)
    t.end_fill()

    t.begin_fill()
    t.color(R)
    t.circle(12*10,180)
    t.end_fill()

    t.begin_fill()
    t.color(R)
    t.circle(6*10,180)
    t.end_fill()

    t.rt(180)
    t.begin_fill()
    t.color(BL)
    t.circle(6*10)
    t.end_fill()


    t.pu()
    t.goto(-115.79,150.31)
    t.pd()
    t.begin_fill()
    t.color(BK)
    for i in range(3):
        for j in range(2):
            t.fd(12*10)
            t.rt(90)
            t.fd(2*10)
            t.rt(90)
        t.pu()
        t.rt(90)
        t.fd(3*10)
        t.lt(90)
        t.pd()
    t.end_fill()

    t.seth(0)
    t.pu()
    t.goto(-182.82,-50.77)
    t.pd()
    t.rt(146.045)
    t.begin_fill()
    t.color(BK)
    for i in range(3):
        for j in range(2):
            t.fd(2*10)
            t.lt(90)
            t.fd(12*10)
            t.lt(90)
        t.pu()
        t.fd(3*10)
        t.pd()
    t.end_fill()

    t.pu()
    t.goto(-179.78,-109.00)
    t.begin_fill()
    t.color(W)
    for j in range(2):
        t.fd(2*10)
        t.lt(90)
        t.fd(1*10)
        t.lt(90)
    t.end_fill()

    t.seth(0)
    t.pu()
    t.goto(115.69,150.39)
    t.lt(33.995)
    t.pd()
    t.begin_fill()
    t.color(BK)
    for i in range(3):
        for j in range(2):
            t.fd(2*10)
            t.rt(90)
            t.fd(12*10)
            t.rt(90)
        t.pu()
        t.fd(3*10)
        t.pd()
    t.end_fill()

    t.pu()
    t.goto(146.44,104.79)
    t.pd()
    t.begin_fill()
    t.color(W)
    for i in range(2):
        for k in range(2):
            t.fd(2*10)
            t.rt(90)
            t.fd(1*10)
            t.rt(90)        
        t.pu()
        t.fd(6*10)
        t.pd()
    t.end_fill()

    t.seth(0)
    t.pu()
    t.goto(182.78,-50.90)
    t.rt(33.995)
    t.pd()
    t.begin_fill()
    t.color(BK)
    for i in range(3):
        for j in range(2):
            t.fd(2*10)
            t.rt(90)
            t.fd(12*10)
            t.rt(90)
        t.pu()
        t.fd(3*10)
        t.pd()
    t.end_fill()

    t.pu()
    t.goto(152.03,-96.50)
    t.pd()
    t.begin_fill()
    t.color(W)
    for i in range(3):
        for k in range(2):
            t.fd(2*10)
            t.rt(90)
            t.fd(1*10)
            t.rt(90)        
        t.pu()
        t.fd(3*10)
        t.pd()
    t.end_fill()

## 나만의 국기 ##
def draw_로고():
    import turtle as t
    t.reset()
    t.speed(0)

    LG=198,247,111
    LP=253,203,232
    LY=254,253,199
    G=78,227,3
    Y=245,254,130

    t.colormode(255)

    from shape import square as SQ
    from shape import circle as C
    from shape import my_triangle as M_T
    from shape import black_line as B_L


    SQ(-180,-180,360,360,LP)
    t.lt(135)
    SQ(90,0,(90**2+90**2)**0.5,(90**2+90**2)**0.5,LY)
    t.seth(0)

    t.lt(90)
    C(-30,0,60,360,LG)
    t.rt(180)
    C(0,-30,60,360,LG)
    t.rt(90)
    C(30,0,60,360,LG)
    C(0,30,60,360,LG)
    C(0,-40,40,360,G)

    t.pu()
    t.goto(-20,-20)
    t.pd()
    t.pencolor("yellow")
    t.pensize(5)
    t.lt(45)
    t.fd(60)
    t.pu()
    t.goto(-20,20)
    t.pd()
    t.rt(90)
    t.fd(60)

    t.seth(0)
    t.pu()
    t.goto(-120,0)
    t.pd()
    t.pencolor("yellow")
    t.pensize(5)
    t.fd(240)
    t.pu()
    t.goto(0,120)
    t.pd()
    t.rt(90)
    t.fd(240)

    t.seth(0)
    t.rt(90)
    M_T(-170,170,150,((150**2+150**2)**0.5),LY)
    M_T(-170,-170,150,((150**2+150**2)**0.5),LY)
    t.lt(90)
    M_T(170,-170,150,((150**2+150**2)**0.5),LY)
    t.lt(180)
    M_T(170,170,150,((150**2+150**2)**0.5),LY)

    t.pensize(1)
    B_L(-180,-180,360,360)
