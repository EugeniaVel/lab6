#include <iostream>
using namespace std;
void proiz(double *y,double *x,double xx,int n)
{
	double lp,pp,vp,cp;
	lp=(y[n]-y[n-1])/(x[n]-x[n-1]);
	cout<<"������������� �����������:"<<lp<<"\n";
	pp=(y[n+1]-y[n])/(x[n+1]-x[n]);
	cout<<"�������������� �����������:"<<pp<<"\n";
	vp=2*(pp-lp)/(x[n+1]-x[n-1]);
	cp=lp+(vp/2)*(2*xx-x[n-1]-x[n]);
	cout<<"����������� �����������:"<<cp<<"\n";
	cout<<"������ �����������:"<<vp;
}
int main()
{
	setlocale(LC_ALL, "Russian");
	int i;
	double *x,*y,xx;
	x=new double[5];
	y=new double[5];
	for (i=0;i<5;i++)
	{
		cout<<"������� x"<<i<<" � y"<<i<<" ����� ������:\n";
		cin>>x[i]>>y[i];
	}
	xx=1;
	proiz(y,x,xx,2);
	return 0;
}