from Joy import *
import math
bigr1=rectangle(w=200,h=200,x=0,y=0,fill='red',stroke='red')|repeat(18,rotate(10))
bigr2=rectangle(w=200,h=200,x=0,y=0,fill='green',stroke='green')|repeat(6,rotate(60))
bigr=bigr1+bigr2
bigc=circle(r=143,fill='maroon',stroke='maroon',stroke_width=2.5)
cir1=circle(x=115,y=0,r=15,fill='orange',stroke='orange')|repeat(36,rotate(10))
cir2=circle(x=115,y=0,r=15,fill='yellow ',stroke='maroon',stroke_width=5)|repeat(18,rotate(20))
colourcomb1=["maroon","#FF8C00", "#FFD700","#FFFF00","green"]
colourcomb2=["maroon","#FF8C00", "#FFD700","#FFFF00","#D9D9D9"]
shape=  ellipse(w=200,h=100,x=0,y=0,fill='#008B45')
extrac=circle(r=100,fill='#030303')
elwid=200
elhig=100
for i in colourcomb2:
    shape=shape+ellipse(w=elwid,h=elhig,x=0,y=0,fill=i,stroke=i)
    elwid=elwid-10
    elhig=elhig-10
shape=  shape | repeat(20,rotate(30))
def kathakali():
    c = circle(r=100,fill='white')
    t=100
    r=4
    for i in colourcomb1:
        c=c+circle(r=t,x=0,y=0,fill=colourcomb1[r],stroke=colourcomb1[r])
        t=t-7.5
        r=r-1
    ccextra=circle(x=96.5,y=0,r=2,fill='white',stroke='white')|Repeat(24, Rotate(angle=30))
    cb1=circle(r=62.5,fill='red',stroke='red')
    cb2=circle(r=58,fill='orange',stroke='orange')
    extras=circle(x=51,y=0,r=4,fill='maroon',stroke='maroon')|Repeat(12, Rotate(angle=30,anchor=Point(0,0)))
    cb3=circle(r=45,fill='#FF4500',stroke='#FF4500')
    extras1=circle(x=35,y=0,r=4,fill='yellow',stroke='yellow')|Repeat(12, Rotate(angle=30,anchor=Point(0,0)))
    cb4=circle(r=28,fill='brown',stroke='brown')
    trp=polygon([point(-20,-20),point(20,-20),point(60,-70),point(-60,-70)],fill='white',stroke='white')
    face=polygon([point(-30,-20),point(30,-20),point(30,-60),point(-30,-60)],fill='green',stroke='green')
    eyeslf1=polygon([point(-30,-20),point(-2,-40),point(-30,-40)],fill='black')
    eyesrf1=polygon([point(30,-20),point(2,-40),point(30,-40)],fill='black')
    eyeslf2=polygon([point(-25,-30),point(-2,-40),point(-25,-40)],fill='white')
    eyesrf2=polygon([point(25,-30),point(2,-40),point(25,-40)],fill='white')
    eyedowlf=polygon([point(-25,-40),point(-2,-40),point(-2,-42.5),point(-25,-42.5)],fill='black')
    eyedowrf=polygon([point(25,-40),point(2,-40),point(2,-42.5),point(25,-42.5)],fill='black')
    eyeblf1=circle(x=-15,y=-35,r=5,fill='black')
    eyebrf1=circle(x=15,y=-35,r=5,fill='black')
    eyerlf=circle(x=-15,y=-35,r=2,fill='red')
    eyerrf=circle(x=15,y=-35,r=2,fill='red')
    hd=polygon([point(-15,-20),point(15,-20),point(0,-35)],fill='yellow',stroke='yellow')
    hdr=polygon([point(-5,-20),point(5,-20),point(5,-27),point(-5,-27)],fill='red',stroke='red')
    hdb=polygon([point(-2.5,-20),point(2.5,-20),point(2.5,-23.5),point(-2.5,-23.5)],fill='black')
    earing1=circle(x=-40,y=-40,r=10,fill='yellow',stroke='red')
    design1=circle(x=-35,y=-40,r=2,fill='red',stroke='red')|Repeat(4, Rotate(angle=90,anchor=Point(-40,-40)))
    earing1=earing1+design1
    earing2=circle(x=40,y=-40,r=10,fill='yellow',stroke='red')
    design2=circle(x=35,y=-40,r=2,fill='red',stroke='red')|Repeat(4, Rotate(angle=90,anchor=Point(40,-40)))
    earing2=earing2+design2
    def semiconstructor(rad,xco,yco,colo):
        def part_of_circle(r,theta):
            return point(math.sin(theta)*r,math.cos(theta)*r)
        points = [point(0,0)]
        r = rad
        part = 0.5 
        step = 0.01  
        i = 0.00
        while i < 3.14*2*(part):
            points.append(part_of_circle(r,i))
            i = i+step 
        return polygon(points,fill=colo,stroke=colo)  | rotate(90) | translate ( x=xco, y= yco)
    keridm1=semiconstructor(30,0,-20,'#EEB422')
    keridm2=semiconstructor(22.5,0,5,"#FFD700")
    keridm3=semiconstructor(15,0,25,'yellow')
    def smallstrips(xco,yco):
        recs=rectangle(w=2,h=7,x=xco,y=yco,fill='maroon',stroke='maroon')
        
        return recs
    n=-6.5
    strp1=smallstrips(n,-10)
    while(n>=-20):
        n=n-4
        strp1=strp1+smallstrips(n,-10)
    n=6.5
    strp2=smallstrips(n,-10)
    while(n<=20):
        n=n+4
        strp2=strp2+smallstrips(n,-10)
    def smallcircs(xco,yco):
        sml=circle(x=xco,y=yco,r=1,fill='maroon',stroke='maroon')
        return sml
    l=-15
    smlcirc=smallcircs(l,10)
    while(l<=10):
        l=l+5
        smlcirc=smlcirc+smallcircs(l,10)
    l=-10
    smlcirc2=smallcircs(l,30)
    while(l<=5):
        l=l+5
        smlcirc2=smlcirc2+smallcircs(l,30)
    centrb=rectangle(w=7,h=7,x=0,y=-10,fill='yellow',stroke='yellow')|Rotate(angle=45,anchor=Point(0,-10))
    crown=rectangle(w=10,h=10,x=0,y=45,fill='yellow',stroke='yellow')|Rotate(angle=45,anchor=Point(0,45))
    mouth1=polygon([point(-10,-53),point(10,-53),point(10,-55),point(-10,-55)],fill='red',stroke='red')
    add=c+ccextra+cb1+cb2+extras+cb3+extras1+cb4+trp+face+eyeslf1+eyesrf1+eyeslf2+eyesrf2+eyeblf1+eyebrf1+eyerlf+eyerrf+eyedowlf+eyedowrf+hd+hdr+hdb+keridm1+keridm2+keridm3+crown+mouth1+earing1+earing2+strp1+strp2+centrb+smlcirc+smlcirc2
    return add
image=kathakali()|scale(0.75)
d=combine([bigc,bigr,extrac,shape,cir1,cir2,image])|scale(1.05)
show(d)