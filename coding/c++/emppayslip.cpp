#include<iostream>
using namespace std;
class employee
{
private:
int empid,basicpay;
char name[50],dept[30];
float da,hra,gpay,pf,lop,td,npay;
public:
void getempdetails();
void calculate();
void print();
};
int main()
{
employee e1;
e1.getempdetails();
e1.calculate();
e1.print();
}
void employee::getempdetails()
{
cout<<"Enter employee id:"<<endl;
cin>>empid;
cout<<"Enter Employee name:"<<endl;
cin>>name;
cout<<"Enter dept:"<<endl;
cin>>dept;
cout<<"Basic pay:"<<endl;
cin>>basicpay;
cout<<"Enter lop:"<<endl;
cin>>lop;
}
void employee::calculate()
{
da=(basicpay/100)*80;
hra=(basicpay/100)*20;
gpay=basicpay+da+hra;
pf=(basicpay/100)*12;
td=pf+lop;
npay=gpay-td;
}
void employee::print()
{
cout<<"employ id:"<<empid<<endl;
cout<<"Name: :"<<name<<endl;
cout<<"Department:"<<dept<<endl;
cout<<"----------";
cout<<"Basic pay:"<<basicpay<<endl;
cout<<"LOP:"<<lop<<endl;
cout<<"da:"<<da<<endl;
cout<<"Gpay:"<<gpay<<endl;
cout<<"Pf:"<<pf<<endl;
cout<<"Td:"<<td<<endl;
cout<<"Npay:"<<npay<<endl;
}