
'''1. fizzbuzz variation
write a progarm that print the number from 1 to 100 but for multiples of 3 print "fizz"insted of the number and 
for the multiples of 5 print "buzz" for number which are multiplesof both 3 and 5 print "fizzbuzz"'''


for i in range (2,11):
    is_prime= True
    for j in range (2,i):
        if i % j == 0:
            is_prime= False
            break 
    if is_prime:
        print(i)







2. #prime numbers:
#write a progarm that prints all prime numbers between 1 to 100






'''3 #factorial calculation:
#wrirte a program thats calculates the factorial of giving number using a loop and recursion  
'''



'''4# sum of digits:
write a program that calculation 
write a function that calculate that factorial of a agiven number using a loop and recurstionn'''



'''.5 revers a string:
write a program that takes a string as input and reverses it using a loop 

'''

'''6.fibonacci sequence:
write a progarm to generate the first 20 number of the fibonacci sequence
'''