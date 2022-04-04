import math
def l(xm,xx,nn):
    sl=0.
    y=[]
    for i in range(nn):
        yi=math.sin(xm[i])
        y.append(yi)
    for i in range(nn):
        nl=1
        pl=1
        for j in range(nn):
            if j!=i:
                nl=nl*(xm[i]-xm[j])
                pl=pl*(xx-xm[j])
        sl=sl+y[i]*pl/nl
    return sl
def ni(xm,x,n):
    def rr(xx,yy,i,j):
        if j-i==1:
            r=(yy[j]-yy[i])/(xx[j]-xx[i])
        else:
            r=(rr(xx,yy,i+1,j)-rr(xx,yy,i,j-1))/(xx[j]-xx[i])
        return r
    def pr(xm,x,k):
        p=1
        for i in range(k):
            p*=(x-xm[i])
        return p
    ym=[]
    for i in range(n):
        yi=math.sin(xm[i])
        ym.append(yi)
    sn=ym[0]
    for k in range(1,n):
        sn=sn+rr(xm,ym,0,k)*pr(xm,x,k)
    return sn
m=[math.pi*0.1,math.pi*0.2,math.pi*0.3,math.pi*0.4]
mm=[math.pi*0.1,math.pi/6,math.pi*0.3,math.pi*0.4]
x=math.pi/4
yl=l(m,x,4)
yll=l(mm,x,4)
yn=ni(m,x,4)
ynn=ni(mm,x,4)
pl=abs(abs(yl)-abs(math.sin(x)))
pll=abs(abs(yll)-abs(math.sin(x)))
pn=abs(abs(yn)-abs(math.sin(x)))
pnn=abs(abs(ynn)-abs(math.sin(x)))
print("Пункт а:")
print("Значение интерполяции Лагранжа: "+str(yl)+"\nПогрешность интерполяции Лагранжа "+str(pl))
print("\n    Значение интерполяции Ньютона: "+str(yn)+"\n    Погрешность интерполяции Ньютона: "+str(pn))
print("\nПункт б:")
print("Значение интерполяции Лагранжа: "+str(yll)+"\nПогрешность интерполяции Лагранжа "+str(pll))
print("\n    Значение интерполяции Ньютона: "+str(ynn)+"\n    Погрешность интерполяции Ньютона: "+str(pnn))