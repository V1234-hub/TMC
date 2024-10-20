'''list=["harry",1 ,3.14,'G',True]
students= ["harry","hermione","ronald"]
number=[1,4,7,9]
real_number=[3.14,5.15,6.00]
booleans=[True,False,True]
print(list)
print(students)
print(number)
print(real_number)
print(booleans)'''


'''gryffindor=["harry", "hermione","ronald"]
name=gryffindor[0]
print(gryffindor[0])
print(gryffindor[2])
print(name.upper())


print(f"the length of the list is:{len(gryffindor)}")'''


'''number=[1,7,3,9,2]
print(number)
print(sorted(number,reverse=False))
print(sorted(number,reverse=True))

names=["ahmed","rami","emar","harry"]
print(names)
print(sorted(names,reverse=False))
print(sorted(names,reverse=True))'''


#hogwarts=["harry","luna","malfoy"]
'''print(hogwarts)
hogwarts.append("cedric")
print(hogwarts)'''

'''name=input("writre a name: ").capitalize()
hogwarts.append(name)
print(hogwarts)'''


'''name1=input("enter name1: ")
hogwarts.append(name1)
name2=input("enter name2:")
hogwarts.append(name2)
name3=input("enter name3:")
hogwarts.append(name3)
print(hogwarts)'''

'''name1=input("enter name1: ")
name2=input("enter name2:")
name3=input("enter name3:")

hogwarts.append([name1,name2,name3])
print(hogwarts)'''


'''list=[]
name=input("write a name: ")
list.append(name)
print(list)'''

'''gryffindor=["harry","hermoin","ronald","malfoy"]
print(gryffindor)
gryffindor.pop(3)
print(gryffindor)'''


'''D= {
    "harry":"gryffindor",
    "hermoin":"gryffindor",
    "malfoy":"slytherin",
}

print(D)
print(D["harry"])
print(D["malfoy"])

print(D.keys())
print(D.values())


menu={
   "tea": 1,
   "coke": 1.4,
   "water": 1.1,
}

print(f"THe price is ${menu['coke']}")'''


'''hogwarts={
    "gryffindor":["harry","hermoin","ronald"],
    "raven":["luna","sybil","cho"],
    "slythiern":["cedric","tonks","helga"],
    "hufflepuff":["malfoy","snape","voldermort"],
}

print(hogwarts)
gryf=hogwarts['gryffindor']

print(gryf[1])'''


'''Hogwarts={
    "Gryffindor":{
        "Harry": "Auror",
        "hermion":"minster of magic",
    },
    "ravenclaw":{
        "luna":"zoolgist",
        "sybil":"diviantion techer",
    },
}

print(Hogwarts)
gryf=Hogwarts["Gryffindor"]

print(gryf['Harry'])'''


Gryffindor= {
        "Harry": "Auror",
        "Hermione": "Minsiter of Magic",
        "malfoy":"techer"
}

print(Gryffindor)
Gryffindor.pop("malfoy")
print(Gryffindor)