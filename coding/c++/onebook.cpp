#include<iostream>
using namespace std;
class book
{
private:
int pages,price;
char name[50],author_name[50];
public:
int i,n;
void getdata()
{
cout<<"Enter name of book:-"<<endl;
cin>>name;
cout<<"Enter the author name:-"<<endl;
cin>>author_name;
cout<<"Enter the Number of pages :-"<<endl;
cin>>pages;
cout<<"Enter the price of book:-"<<endl;
cin>>price;
}
void display()
{
cout<<"Name:-"<<name<<endl;
cout<<"Author's Name:-"<<author_name<<endl;
cout<<"Price:-"<<price<<endl;
cout<<"No of pages:-"<<pages<<endl;
}
};
int main()
{
book b;
b.getdata();
b.display();
}