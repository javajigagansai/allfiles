#include<iostream>
using namespace std;
class student
{
private:
int feet;
int inch;
public:
student()
{
feet=0;
inch=0;
}
void getheight(int f,int i)
{
feet=f;
inch=i;
}
int operator > (student s3)
{
if (feet>s3.feet)
return 1;
else if(feet==s3.feet&&inch>s3.inch)
return 0;
else
return 0;
}
};
int main()
{
student s1,s2;
s1.getheight(5,10);
s2.getheight(6,1);
if(s1>s2)
cout<<"student s1 is taller";
else if(s2>s1)
cout<<"student s2 is taller";
else
cout<<"both are of equal height";
}