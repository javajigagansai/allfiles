#include<iostream>
using namespace std;
int area(int a);
float area(float r);
int main()
{
int a=4,ar;
float b=5.4,br;
ar=area(a);
br=area(b);
cout<<"Area using function over load";
cout<<endl<< "Area of Square"<<ar;
cout<<endl<<"Area of circle"<<br;
}
int area(int a)
{
return(a*a);
}
float area(float r)
{
return(3.14*r*r);
}