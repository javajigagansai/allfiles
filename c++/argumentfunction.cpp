#include<iostream>
using namespace std;
void display(char c='*',int i=1);
int main()
{
cout<<"No argument passed \n";
display();
cout<<"\nFirst arugument passed:\n";
display('#');
cout<<"\nBoth argument passed:";
display('$',5);
}
void display(char c,int n)
{
int i,j;
for(i=1;i<=n;i++)
{
cout<<c;
}
cout<<endl;
}