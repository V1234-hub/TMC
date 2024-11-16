
'''
path = "dcoument/tmc/session.py"

end_point ="session.py"

#url ==> universel resource locator => path to the page or Api 

#example 
url= "https://wwww.google.com/mail/acccount" 

'''


'''

import requests
import json

url= "https://datausa.io/api/data?drilldowns=Nation&measure=Population"

response= requests.get(url)

if response.status_code == 200:
    #print(json.dumps(response.json() , indent=2))
    json_response= response.json()
    data=json_response['data']
    #print(json.dumps(data, indent=2))
    year=input("enter a year:")
    for data_per_year in data:
        if data_per_year['Year'] == year:
            print(f"population is {data_per_year['Population']}")

else:
    print("not fetched")

'''



''''
import requests
import json

Url="https://api.coindesk.com/v1/bpi/currentprice.json"

response= requests.get(Url)

if response.status_code== 200:
    json_response= response.json()
    bpi= json_response['bpi']
    print(json.dumps(bpi,indent=2))
    clinet_currency= input('whats your currence ').upper()
    currency= bpi [clinet_currency]
    rate= currency['rate_float']
    print (rate)
    
    
else:
    print("NOt fetched")
'''


#algorithms

'''
#iteration 
def binary_search(min, max, number):
    while min <= max:
        mean= (min + max ) // 2

        if number == mean:
            return "found"
        elif number > mean:
            min = mean + 1 
        else:
            max = mean - 1 
    else:
        return "error"
print (binary_search(0,50,30)) 

'''


#recursoin
def binary_search(min, max, number):
    if min <= max:
        mean= (min + max ) // 2

        if number == mean:
            return "found"
        elif number > mean:
          return binary_search(mean+1,max, number)
        else:
            return binary_search (min , mean-1 , number)
        
    else:
        return "error"
print (binary_search(0,50,20)) 