#include<iostream>
using namespace std;
class item
{
static int s;
int member;
public:
void getdata(int a)
{
member=a;
s++;
}
void getcount()
{
cout<<"the value of s is :"<<s<<endl;
}
};
int item::s;
int main()
{
item a,b,c;
a.getcount();
b.getcount();
c.getcount();
a.getdata(100);
b.getdata(200);
c.getdata(300);
cout<<"after read data"<<endl;
a.getcount();
b.getcount();
c.getcount();
}
