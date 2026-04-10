#include<iostream>
using namespace std;
class time
{
private:
int hour,min,sec;
public:
time()
{
hour=0;
min=0;
sec=0;
}
time(int h,int m,int s)
{
if(h>0 && h<23 &&m>0 &&m<=59 && s>0 && s<=59)
{
hour=h;
min=m;
sec=s;
}
else
cout<<"invalid time";
}
int operator==(time t3)
{
return(hour==t3.hour&&min==t3.min&&sec==t3.sec);
}
};
int main()
{
time t1(7,11,30);
time t2(3,30,41);
if(t1==t2)
cout<<" clock shows same time"<<endl;
else
cout<<"clock shows different time"<<endl;
}