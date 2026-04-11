
package add;

public class Add {
    int res;
    public void addop(int a, int b) {
        res = a + b;
        System.out.println("Add: " + res);
    }
}


package sub;

public class Sub
{
int res;
public void subop(int a,int b)
{
res = a - b; 
System.out.println("Sub:"+	res);
}
}

package mul;

public class Mul
{
int res;
public void mulop(int a,int b)
{

res = a * b; 
System.out.println("Mul :"+res);
}
}
 
package div;

public class Div
{
int res;
public void divop(int a,int b)
{

res = a / b;
 System.out.println("Div :"+res);
}
}

import java.util.*; 
import add.*;
 import sub.*;
 import mul.*;
 import div.*;


public class ArithDemo
{
public static void main(String args[])
{

Add ad = new Add();
Sub su = new Sub();
Mul mu = new Mul(); 
Div di = new Div();

ad.addop(20,10);
su.subop(20,10);
mu.mulop(20,10);
di.divop(20,10);
}
}
