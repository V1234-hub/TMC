
'''def hello(name):
    print(f"hello{name}")

name= input("whats is your name?")
hello(name)'''


'''def main():
    name=input("whats your name ")
    hello(name)

def hello(name="harry"):
    print(f"hello{name}")

main()'''


'''def main():
    number= int(input("enter number:"))
    print(double(number))

def double(y):
    return f"double of {y} is {y * 2}"

main()'''


'''def main():
    number= int(input("enter number:"))
    print(square (number))

def square (y):
    return f"square of {y} is {y * y}"

main()'''



'''def mian():
    number1= int(input("enter a number"))
    number2= int(input("enter another number"))
    divide(number1,number2)

def divide(x ,y):
    z= round(x/y,2)
    print(power(z))

def power(z):
    return z ** 2

mian()'''


def main(f):
    def secoundry(t):
        print("function is about to run..")
        f(t)
        print ("funtion is executed!")
        return secoundry
    
@main
def hello(name):
    print (f"hello {name}")

hello("harry")

