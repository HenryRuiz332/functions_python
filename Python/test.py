import urllib.request
import os


g = urllib.request.urlopen('https://www.google.com/search?q=precio+dolar+euro&oq=precio+dolar&aqs=chrome.1.69i57j69i59.4796j0j7&sourceid=chrome&ie=UTF-8').read().decode()
print(g)