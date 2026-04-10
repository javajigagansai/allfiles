#include<iostream>
using namespace std;
class abc;
class xyz
{
private:
int data;
public:
void setvalue(int value)
{
data=value;
}
friend void add(xyz,abc);
};
class abc
{
private:
int data;
public:
void setvalue(int value)
{
data=value;
}
friend void add(xyz,abc);
};
void add(xyz obj1,abc obj2)
{
cout<<"Sum of data value of xyz and abc class"<<obj1.data+obj2.data;
}
int main()
{
xyz x;
abc a;
x.setvalue(5);
a.setvalue(10);
add(x,a);
}