import copy
import math
import matplotlib.pyplot as plt
def gauss(a,x,n):
    for k in range (n-1):
        am=math.fabs(a[k][k])
        im=k
        for i in range(k+1,n):
            if math.fabs(a[i][k])>am:
                am=math.fabs(a[i][k])
                im=i
        if k!=im:
            c=x[k]
            x[k]=x[im]
            x[im]=c
            for j in range (k,n):
                c=a[k][j]
                a[k][j]=a[im][j]
                a[im][j]=c
        for j in range(k+1,n):
            c=a[j][k]
            for i in range(k,n):
                a[j][i]=(a[j][i]*a[k][k]-a[k][i]*c)/c
            x[j]=(x[j]*a[k][k]-x[k]*c)/c
    x[n-1]=x[n-1]/a[n-1][n-1]
    i=n-2
    while i>=0:
        for j in range(i+1,n):
            x[i]=x[i]-x[j]*a[i][j]
        x[i]=x[i]/a[i][i]
        i=i-1
    return(x)
def mnk(x,y,n,N):
    a=[]
    ay=[]
    for k in range(n+1):
        am=[]
        for i in range(n+1):
            sx=0
            sy=0
            for j in range(N+1):
                sx=sx+(x[j])**(k+i)
            am.append(sx)
        for j in range(N+1):
            sy=sy+(y[j]*(x[j])**(k))
        a.append(am)
        ay.append(sy)
    ar=gauss(a,ay,n+1)
    return(ar)
x=[-1,0,1,2,3,4]
y=[-0.5,0,0.5,0.86603,1,0.86603]
n1=1
n2=2
N=5
a1=mnk(x,y,n1,N)
a2=mnk(x,y,n2,N)
f1=[]
f2=[]
for i in range(N+1):
    f=0
    ff=0
    for j in range(n1+1):
        f=f+a1[j]*(x[i])**j
    f1.append(f)
    for j in range(n2+1):
        ff=ff+a2[j]*(x[i])**j
    f2.append(ff)
ph1=0
ph2=0
for k in range(N+1):
    ph1=ph1+(f1[k]-y[k])**2
    ph2=ph2+(f2[k]-y[k])**2
print("Приближающий многочлен первой степени:")
print(str(round(a1[0],6))+"+"+str(round(a1[1],6))+"x")
print("Сумма квадратов ошибок Ф для первого многочлена:"+str(round(ph1,6)))
print("Приближающий многочлен второй степени:")
print(str(round(a2[0],6))+"+"+str(round(a2[1],6))+"x"+str(round(a2[2],6))+"x^2")
print("Сумма квадратов ошибок Ф для второго многочлена:"+str(round(ph2,6)))
plt.plot(x,y,"-r",x,f1,"-k",x,f2,"-y")
#красный цвет - график приближаемой функции, чёрный - многочлена первой степени, жёлтый - второй степени
plt.show()