from datetime import *

now = date.today()

#("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.") #Format types

#Example from formats date
new = now.strftime("%d %b %Y")#31 mar 2020
new = now.strftime("%m-%d-%y")# 03-31-20
new = now.strftime("is a %A on the %d day of %B year %Y")# is a Tuesday on the 31 day of March year 2020

print(new)