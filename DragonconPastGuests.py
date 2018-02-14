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

#retrieve from website, and put names into list
guest = list()
for b in soup.find_all('b'):
    name = b.text + str(b.next_sibling)
    guest.append(name)

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
    

#look for guests in a certain year
guestCount = 0
year = input("Enter the year you are looking for: ('n' to skip) ")
if(year != 'n'):
    for i in range(0,len(guest)-1):
        if year in guest[i]:
            print(guest[i])
            guestCount += 1
            
    print("Total Guests: ", guestCount)

#TODO
#print menu: certain year,range,or guest
#ask user if they want only a certain letter (only A last names)
#ask user to search for guests in a given series
    #(buffy,got,star wars,star trek,dr who,firefly,the 100,marvel,dc,disney)
#search guest online

print("Done")
