


'''
class hogwarts:
    def __init__(self,name):
        self.name= name 
    

    def check_student_house(Self):
        if self.name in ["harry", "hermione", "rounlad"]:
            return "gryffindor"
        
        elif Self.name in ["malfoy", "snape", "vodermort"]:
            return "slytherin"
        
        elif Self.name in ["luna", "cho", "sybil"]:
            return "slytherin"
        
        elif Self.name in ["cedirec", "helga", "tonks"]:
            return "slytherin"
        
        else:
            return "not a hogwarts student"
'''



#if not age
# riase valueerro('age is not provided)



arts:
def intit__(self,name,age):
if not name or not age:
    raise ValueError("invalid cerdentials name or age is missing")
if not ininstance(name,str):
    raise TypeError (" name is not a string")
if not ininstance(age,int):
    raise TypeError ("age isnt an integer")

self.name= name 
self.age = age 

def __str__(self):
    return f"the student name is {self.name}. the age is {self.age}"

#getter method for getting the name 
@property 
def name(self):
    return self._name

#setter method for setting the name 
@name.setter
def name (self,name):
    if not name:
        raise ValueError ("name is not defined")
    if not isinstance (name, str):
        raise TypeError ("name is not  string")
    self.name= name 

