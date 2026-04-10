#include<iostream>
using namespace std;
class student
{
private:
char name[50],regno[15];
int m1,m2,m3,total;
float avg;
public:
void getdata()
{
cout<<"Enter student Regno:-"<<endl;
cin>>regno;
cout<<"Enter student name:-"<<endl;
cin>>name;
cout<<"Enter marks of student m1,m2,m3:-"<<endl;
cin>>m1>>m2>>m3;
total=m1+m2+m3;
avg=total/3;
}
void display()
{
cout<<"RegNo:-"<<regno<<endl;
cout<<"Name:-"<<name<<endl;
cout<<"Mark1:-"<<m1<<endl;
cout<<"Mark2:-"<<m2<<endl;
cout<<"Mark3:-"<<m3<<endl;
cout<<"Total:-"<<total<<endl;
cout<<"Average:-"<<avg<<endl;
}
};
int main()
{
student s[1000];
int n,i;
cout<<"Enter the number of students:-";
cin>>n;
for(i=0;i<n;i++)
s[i].getdata();
for(i=0;i<n;i++)
s[i].display();
}