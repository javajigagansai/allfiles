def getdata():
    print("enter the number to check even or odd")
    global a
    a = int(input('enter the value of a:'))
def calculation():
    if (a%2==0):
        print("the a is even number")
    else:
        print("the a is odd number ")
getdata()
calculation()

