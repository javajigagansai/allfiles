#include<iostream>
using namespace std;
class space
{
int x,y,z;
public:
void getdata(int a,int b,int c);
void display ();
void operator-();
};
void space::getdata(int a,int b,int c)
{
x=a,y=b,z=c;
}
void space::display()
{
cout<<"x= "<<x<<endl<<"y= "<<y<<endl<<"z= "<<z<<endl;
}
void space::operator-()
{
x=-x;
y=-y;
z=-z;
}
int main()
{
space s;
s.getdata(40,-50,10);
cout<<"s"<<endl;
s.display();
-s;
cout<<"the value of s is :"<<endl;
s.display();
}