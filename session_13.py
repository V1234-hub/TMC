




#classes /oop => object oriented programming 


#name now is stored in self container under self.name

'''class Myclass:
    def __init__(self,name):
        self.name= name 
        self.age= age
        self.house= "gryffindor"

    def greet(self):
        return f"hello {self.name}. your age is {self.age}. your house is {self house}"



person= Myclass("Harry",10)

print(person.greet())
'''

'''
from session13  import hogwarts 

def main():
    name= input ("write your name ")
    student= hogwarts (name)
    print (student.check_student_house())

if__name__ == "__main__":
    main()
'''


from session13 import hogwarts


def main():
    try:
        name= input("write your name: ")
        age= input ("enter your age: ")
        student= hogwarts (name, age )
        if not isinstance (name, hogwarts):
            print ("name is not howgwart class")
        
        #student.name= "hermione"
        student.age= "13"
        student.name= 12 
        print(student)
    
    except Exception as e:
        print (f"error: {e}")

if __name__== "__main__":
    main()
