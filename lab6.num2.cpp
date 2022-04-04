#include <iostream>
#include <cmath>
using namespace std;
void gauss(float **a,float *x,int n)
{
	int i,j,k;
	float c;
	for(k=0;k<n-1;k++)
	{
		for(j=k+1;j<n;j++)
		{
			if (a[j][k]!=0)
			{
				c=a[j][k];
				for (i=k;i<n;i++)
				{
					a[j][i]=(a[j][i]*a[k][k]-a[k][i]*c)/c;
				}
				x[j]=(x[j]*a[k][k]-x[k]*c)/c;
			}
		}
	}
	x[n-1]=x[n-1]/a[n-1][n-1];
	i=n-2;
	while (i>=0)
	{
		for(j=i+1;j<n;j++)
		{
			x[i]=x[i]-x[j]*a[i][j];
		}
		x[i]=x[i]/a[i][i];
		i=i-1;
	}
}
float cubes(float *xx,float *y,float x)
{
	int i,j,k;
	float **am;
	float *cc,*c,*c1,*a,*b,*d,fx;
	cc = new float [3];
	am = new float*[3];
	c1=new float [3];
	a=new float [4];
	b=new float [4];
	c=new float [4];
	d=new float [4];
	for(i=0;i<4;i++)
	{
		am[i]=new float[3];
	}
	for(i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
		{
			if(i==j)
			{
				am[i][j]=4;
			}
			else if(fabs(i-j)>1)
			{
				am[i][j]=0;
			}
			else
			{
				am[i][j]=1;
			}
		}
		c1[i]=3*(y[i+2]-2*y[i+1]+y[i]);
	}
	gauss(am,c1,3);
	for(i=0;i<4;i++)
	{
		if(i==0)
		{
			c[i]=0;
		}
		else
		{
			c[i]=c1[i-1];
		}
		a[i]=y[i];
	}
	for(i=0;i<4;i++)
	{
		if(i==3)
		{
			b[i]=y[i+1]-y[i]-2*(c[i])/3;
			d[i]=-c[i]/3;
		}
		else
		{
			b[i]=y[i+1]-y[i]-(c[i+1]+2*c[i])/3;
			d[i]=(c[i+1]-c[i])/3;
		}
	}
	for(k=1;k<5;k++)
	{
		if(xx[k]<x)
		{
			i=k;
		}
	}
	cout<<"a[i]:"<<a[i]<<" b[i]:"<<b[i]<<" c[i]:"<<c[i]<<" d[i]:"<<d[i]<<"\n";
	fx=a[i]+b[i]*(x-xx[i])+c[i]*pow(x-xx[i],2)+d[i]*pow(x-xx[i],3);
	return fx;
}
int main()
{
	setlocale(LC_ALL, "Russian");
	float *xx,*y,x,fx;
	int i;
	xx=new float [4];
	y=new float [4];
	x=1.5;
	for(i=0;i<5;i++)
	{
		if (i==0)
		{
			xx[i]=0;
		}
		else
		{
			xx[i]=xx[i-1]+1;
		}
	}
	y[0]=0;
	y[1]=0.5;
	y[2]=0.86603;
	y[3]=1;
	y[4]=0.86603;
	fx=cubes(xx,y,x);
	cout<<"Значение функции при x=1.5: "<<fx;
}