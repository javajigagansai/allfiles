#include<iostream>
using namespace std;
class matrix
{
private:
int m1[3][3],i,j;
public:
void getdata();
void display();
friend matrix trans(matrix);
};
void matrix::getdata()
{
cout<<"Enter the 3X3 matrix value";
for(i=0;i<3;i++)
for(j=0;j<3;j++)
cin>>m1[i][j];
}
void matrix::display()
{
for(i=0;i<3;i++)
for(j=0;j<3;j++)
{
cout<<m1[i][j]<<"\t";
}
cout<<endl;
}
matrix trans(matrix m)
{
int i,j;
matrix m2;
for(i=0;i<3;i++)
for(j=0;j<3;j++)
m2.m1[i][j]=m.m1[j][i];
return m2;
}
int main()
{
matrix mat1,mat2;
mat1.getdata();
mat1.display();
mat2=trans(mat1);
cout<<"Transpose Matrix";
mat2.display();
}