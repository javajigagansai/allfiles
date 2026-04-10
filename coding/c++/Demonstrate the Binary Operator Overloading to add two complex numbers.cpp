#include<iostream>
using namespace std;
class complex
{
float x,y;
public:
complex()
{
}
complex(float real,float imaginary)
{
x=real;
y=imaginary;
}
complex operator+(complex);
void display ();
};
complex complex::operator+(complex c)
{
complex temp;
temp.x=x+c.x;
temp.y=y+c.y;
return temp;
}
void complex::display()
{
cout<<x<<"+"<<y<<"\n";
}
int main ()
{
complex c1,c2,c3;
c1=complex(2.5,3.5);
c2=complex(1.6,2.7);
c3=c1+c2;
cout<<"the value of c1 is :"<<endl;
c1.display();
cout<<"the value of c2 is :"<<endl;
c2.display();
cout<<"the value of c3 is :"<<endl;
c3.display();
}