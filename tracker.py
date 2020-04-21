from bs4 import BeautifulSoup
import os 
import sys
import requests
import re
from colorama import init
from termcolor import *
import time

init()

url = 'https://www.worldometers.info/coronavirus/'
check = requests.get(url)
if check.status_code != 200:
    print('Somethings wrong. please check your connection.')
    sys.exit()
soup = BeautifulSoup(check.text, 'html.parser')
recover = soup.find('div', attrs={'style':'color:#8ACA2B '}).text
recover = re.sub('\n','',recover)
death = soup.find_all('div', attrs={'class':'maincounter-number'})
death = str(death)
d = death.split('>')
confirm_case = d[2].split(' ')[0]
death_case = death.split('<')[6].split('>')[1]
print(' ')
print(colored(' Worldwide data updating every 1 hour.', 'green'))
time.sleep(3)
print(' ')
print(colored(' Confirmed cases: {}'.format(confirm_case), 'yellow'))
print(colored(' Deceased: {}'.format(death_case), 'red'))
print(colored(' Recovered: {}'.format(recover), 'green'))
print(' ')