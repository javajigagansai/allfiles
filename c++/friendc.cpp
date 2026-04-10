#include <iostream>
#include <string>
using namespace std;
class Employee; 
class Student
{
private:
    string name;
    string address;
public:
    Student(string n, string addr) : name(n), address(addr) {}
    friend void getNameAndAddress(Student& student, Employee& employee);
};
class Employee
{
private:
    string name;
    string address;
public:
    Employee(string n, string addr) : name(n), address(addr) {}
    friend void getNameAndAddress(Student& student, Employee& employee);
};
void getNameAndAddress(Student& student, Employee& employee) 
{
    cout << "Student Name: " << student.name << ", Address: " << student.address << endl;
    cout << "Employee Name: " << employee.name << ", Address: " << employee.address << endl;
}

int main() 
{
    Student student("Alice", "123 College St");
    Employee employee("Bob", "456 Corporate Ave");
    getNameAndAddress(student, employee);
    return 0;
}