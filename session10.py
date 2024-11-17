

'''
def main():
    hello("world")
    goodbye("world")

def hello(text):
    print(f"hello{text}")

def goodbye(text):
    print(f"goodbye{text}")

#main() no more use this becouse it allows all functions to be imported 

# this method allows only individual function to be imported 

if __name__== "__main__":

    main() 
'''

'''
def main():
    number= int (input("enter a number: "))
    print (square(number))

def square(x):
    return x + x

if __name__=="main":
    main()
'''


'''
def main():
    name= input ("what is your name? ")
    greet (name)

def greet(name):
   return f"hello {name}"

if __name__=="main":
    main()
'''


def main():
    text=input ("enter a text: ")
    print(ciphered(text))

def ciphered(text):
    aplhabet= "abcdefghijklmnopqrstuvwxyz"
    key= "ytnshkvefxrbauqzclwdmipgjo"

    deciphered_text= ""

    for t in text:
        if t in aplhabet:
            index= aplhabet.index(t)
            deciphered_text += key[index]
    return deciphered_text

if __name__ == "__main__":
    main()

