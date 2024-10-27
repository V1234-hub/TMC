# > greater than
# < less than
# >= greater than or equal
# <= less than or equal 
# == is equal
# != not equal
# and, or, not


'''x= 2
y= 3'''

'''if x > y:
    print("x is greater than y")
if x < y:
    print("x is less than y")
if x == y:
    print("x is euqual to y")'''

'''if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
elif x == y:
    print("x is equal to y")'''


'''x= int(input("enter a number "))
y= int(input("enter another nuber"))
   
if x>y or x<y:
    print("x is equal to y ")
else:
    print("x is equal to y")'''


'''if x:
    print("x have value")

elif y:
    print("y has a value")


if x:
    print ("x have a value")

if y: 
    print ("y have a value")


if x and y:
    print(" there are values")

else:
    print ("no valuse provided")'''


'''x=input(" enter a value")
y=input("enter another value")

if not x:
    print("x dosnt have value")
if not y:
    print("y dosnt have value")
else:
    print("both have values")'''


'''name= input("write a name: ")

if name== "harry" or name== "ronald":
    print('gryfindor')
elif name== "luna" or name== "sybil":
    print('reaven')
elif name== "molfoy" or name== "snape":
    print('slytherin')
elif name== "cedric" or name== " helga":
     print('huflepff')

else:
    print('not a hogwart student')'''




'''name= input("write a name: ")

if name in ["harry" ," hermione" ," roanld" , "ginny"]
    print('gryfindor')
elif name in ["luna" ,"sybil" ,"cho"]:
    print('reaven')
elif name in ["molfoy", "snape" , "volder"]:
    print('slytherin')
elif name in ["cedric", "helga" , "tonks"]:
     print('huflepff')

else:
    print('not a hogwart student')'''




'''scour= int (input("score: "))

if 90 <= scour <=100:
    print("A+")

elif 80 <= scour <=90:
    print("A")

elif  70 <= scour <=80:
    print("B")

elif 60 <= scour <=70:
     print("C")

elif 50 <= scour <=60:
     print("D")

else:
    print("F")'''




'''def mian():
    number1= int(input("enter a number"))
    print (is_even(number1))

def is_even (x):
    if x % 2 == 0:
        return "is even"
    else:
        return "is even"

mian()'''


'''def even_required(f):
    def is_even(x):
        if x % 2 == 0:
            return f(x)
        else:
            return False
    return is_even

def main():
    number= int(input("enter a number "))
    print(square(number))

@even_required
def square(x):
    return x * x

main()'''



def meal_cost(f):
    def percentage (x):
        if x % 15 == 0:
            return f(x)
        else:
            return False
    return percentage

def main():
   meal_cost = int(input("how much is the meal"))
   print(square(number))

   percentage = int(input('whats is the perscentage of the meal '))
   print ()
   
@meal_cost
def percentage(x):
    return x % x

main()

