#include<iostream>
#include<string>
using namespace std;
const int sz=90;
class string
{
char str[sz];
public:
string()
{
strcpy(str," ");
}
string(char s[])
{
strcpy(str,s);
}
void display()
{
cout<<str<<"\n";
}
string operator+(string ss)
{
if(strlen(str)+strlen(ss.str)<sz)
{
string temp;
strcpy(temp.str,str);
strcat(temp.str,ss.str);
return temp;
}
else
cout<<"string overflow";
return 0;
}
};

int main()
{
string s1="hello";
string s2="world";
string s3;
s3=s1+s2;
s1.display();
s2.display();
s3.display();
}