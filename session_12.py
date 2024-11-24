

'''
name= input ("whats your name ")
file = open ("demo.txt", "a")
file.writelines (f"{name }\n ")
file.close()
'''

'''
file= open ("demo.txt", "r")
lines= file.readline()
for line in lines:
    print (line.rstrip())
file.close()
'''


'''
file= open("demo.txt", 'r')
lines= file.readlines()
for line in lines:
    print(line.rstrip())
file.close()
'''

''''
# to controal the secound word in the names 

with open("demo.txt") as file:
    lines= file.readlines()
    for line in sorted(lines, key= lambda line: line [1]):
         print(line.rstrip())
'''




'''
with open("demo.cvs", "a") as file:
    name= input ("whats your name? ")
    house= input("whats your house")
    file.writelines(name, house)
'''



'''
#csv comma seprated value 
with open("demo.cvs", "a") as file:
    file.writelines(["name",',',"house", "\n"])
    for _ in range(4):
     name= input ("whats your name? ")
     house= input("whats your house")
     file.writelines([name,',',house, "\n"])
'''



'''
with open("demo.cvs",'r') as file:
    lines= file.readlines()
    for line in lines:
     name,house= line.rstrip().split(',')
     if name == "name" and house == "house":
        continue
     print (f"{name} in {house}")
'''


'''
import csv

with open('demo.csv', "r") as file:
    rows= csv.reader(file)
    for row in rows:
        name= row[0]
        house= row[1]
        print(f"{name} from {house}")
'''

'''
with open("demo.csv", "a") as file:
    field_name= ["name","house"] 
    writer= csv.dictwriter(file, field_name)
    writer.writeheader()

    for _ in range(3):
        Name= input ("whats your name? ")
        house= input ("whats your house? ")
        writer.writerow({"name":name,"House":house})



with open("demo.csv", "r", newline="", encoding= "utf-8") as file:
    reader= csv.dictreader(file) 
    for line in reader:
        print(line)

'''


import csv
with open ("demo.csv", "a" , newline="") as file:
    field_names= ["id" , "firstname","lastname","country" , "age"]
    writer= csv.DictWriter(file, fieldnames=field_names)
    writer.writeheader()

    #for _ in range(5):
    id= input ("whats is ur ID")
    firstname= input ("whats is ur first name")
    lastname= input ("whats is last name")
    country= input (" what is ur country")
    age= input ("what is your age")
    writer.writerow({"id":id,"firstname": firstname , "lastname":lastname, "country": country,"age": age})

