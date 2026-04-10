#include<iostream>
using namespace std;
int count=0;
class test
{
public:
test()
{
count++;
cout<<"\nConstructor Msg object number "<<count<<"created";
}
~test()
{
cout<<"\nDestructor Msg: object number"<<count<<"destroyed";
count--;
}
};
int main()
{
clrscr();
cout<<"\nInside the main function";
test t1;
{
cout<<"\n Inside Block 1";
cout<<"\n Creating two more object t2 and t3";
test t2,t3;
cout<<"\n Leaving Block";
}
cout<<"\n Block Inside the main";
}
