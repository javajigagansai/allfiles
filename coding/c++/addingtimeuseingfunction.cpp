#include<iostream>
using namespace std;
class Time
{
private:
int hrs,mins;
public:
void gettime(int h,int m)
{
hrs=h;
mins=m;
}
void timecal(Time t1,Time t2)
{
mins=t1.mins+t2.mins;
hrs=mins/60;
mins=mins%60;
hrs=hrs+t1.hrs+t2.hrs;
cout<<endl<<"Total time "<<hrs<<"hrs"<< mins<<"mins";
}
};
void main()
{
Time t1,t2,t3;
t1.gettime(6,50);
t2.gettime(5,20);
t3.timecal(t1,t2);
}