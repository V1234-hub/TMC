

'''#symtax error 
try:
    for _ in range(3):
        print ("hello world")

except SyntaxError:
    print ("please, check the syntax rules of python") 


#name error 
x= 3
print (y)

#type error 

try:
    x = input('enter a number')
    print (x+2)
except Exception as e:
    print (f"error: {e}")

#value error 

try:
    x =int( input("enter a number "))
    print (x+2)
except ValueError
    print("please check the value of input")'''

'''try:
    x=int(input("enter a number:"))
except Exception as e:
    print (f"error: {e}")
else:
    print (x+3)'''

'''#1

def main():
    text= input("text: ")
    print (upper_lower(text))

def upper_lower(t):
    if t.isupper():
        return "uppercase"
    elif not t.isupper() or not t.islower():
        return "neither upper nor lower" 
    else:
        return "lowercase"

main()
'''''''''

#2 

def is_gryffindor(name):
        if:
            return "is a gryffindor strudent"
        else:
            return "not a gryffindor student"
main()




#3 create a funation to prompt the user for file name and print the name of the file 
# jpg/.png => image file 
# pdf => PDF file 
# zip => compressed zip file 

def main():
    file= input ("write a file name ")
    print (file_format(file))

def file_format(file):
# spliet method us strings return  alist 

    name, format = file.split('.')
    if format in ['png , jpg']:
        return "image file "
    elif format == "pdf":
         return "PDF file" 
    elif format == "zip":
         return "zip compressed file "
    else:
        return "not recognised!"
main()

''''''''

#4 


def main():
     time= input ("whats the time now?")
     print (convert(time))


def convert(time):
     hour, minutes = time.split(':')
     decimal_minutes= int ( minutes)/60 
     if decimal_minutes < 0 or decimal_minutes > 1:
          return False 
     else:  
            final_time_format =int (hour) + decimal_minutes 
            print (meal(final_time_format))
            return True 

def meal(meal_time):
     if 7 <= meal_time <=8:
        return "breakfast"
     elif 12 <= meal_time <=13:
        return "lunch"
     elif 18<= meal_time <=19:
          return "dinner"
     
     else:
          return " not a meal time yet"

main()










'''text = input ("text:")
text1,text2,= text.split('')

print(text1)
print(text2)'''






''''''
