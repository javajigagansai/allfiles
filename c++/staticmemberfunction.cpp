#include<iostream>
using namespace std;
class test
{
int code;
static int s;
public:
void setcode()
{ code=++s; }
void showcode()
{
cout<<" the object member function value is :"<<code<<endl;
}
static showcount()
{
cout<<" the value of s is:"<<s<<endl;
}
};
int test::s;
int main()
{
test t1,t2;
t1.setcode();
t2.setcode();
test::showcount();
test t3;
test::showcount();
t3.setcode();
t1.showcode();
t2.showcode();
t3.showcode();
}