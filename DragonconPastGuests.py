#DragonconPastGuests.py - let user look at past guest data

import requests,os
from bs4 import BeautifulSoup

url = "http://www.dragoncon.org/?q=past_guests"
page = requests.get(url)
page.raise_for_status() #if == none, all is well
soup = BeautifulSoup(page.content,'html.parser')
names = soup.find(class_="content clearfix")

#TODO: ignore warning
# Some characters could not be decoded, and were replaced with REPLACEMENT CHARACTER.

print("Retreived from \"http://www.dragoncon.org/?q=past_guests\" ")
print("Website sorts past guest list by [first name,last name,last appearance]")

menu = int(input("Enter Number: \n1: Search by Guest\n2: Search by Year\n3 Enter guest with Last Name\n " ))

#retrieve from website, and put names into list
guestCount = 0
guest = list()
for b in soup.find_all('b'):
    name = b.text + str(b.next_sibling)
    guest.append(name)
    guestCount += 1

if(menu == 1):
    #look for a guest
    search = True
    while(search):
        guestName = input("Enter the guest you are looking for: ")
        for i in range(0,len(guest)-1):
            if guestName in guest[i]:
                print(guest[i])

        search = input("look for another guest? ('y','n')")
        if(search == 'n'):
            search = False
        
elif(menu == 2):
    #look for guests in a certain year
    guestCount = 0
    year = input("Enter the year you are looking for: ('n' to skip) ")
    if(year != 'n'):
        for i in range(0,len(guest)-1):
            if year in guest[i]:
                print(guest[i])
                guestCount += 1
                
        print("Total Guests: ", guestCount)

#TODO: ask user if they want only a certain letter (only A last names) 
##print(guest[3555].split()[1]+" "+guest[3555].split()[2])
##print(guest[3555])
##print(guest[3555].split()[1][0])
    
print("Total Guests: ", guestCount)

#TODO: search guest online
        
print("Done")
