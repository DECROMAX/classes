import requests
from bs4 import BeautifulSoup
import re

fighter = []
url = 'https://www.sherdog.com/fighter/Nate-Diaz-11451' #https://www.sherdog.com/fighter/Conor-McGregor-29688
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

firstname = soup.find('span', class_='fn').text.strip().split()[0]
lastname = soup.find('span', class_='fn').text.strip().split()[1]
try:
    nickname = soup.find('span', class_='nickname').text.strip()
except AttributeError:
    nickname = ''

dob = soup.find('span', attrs={'itemprop': 'birthDate'}).text.strip()
locality = soup.find('span', class_='locality').text.strip()
nationality = soup.find('strong', attrs={'itemprop': 'nationality'}).text.strip()
association = soup.find('span', attrs={'itemprop': 'name'}).text.strip()

height = soup.find('span', class_='item height').text.strip()[-9:-2]
weight = soup.find('span', class_='item weight').text.strip()[-9:-2].strip()
weight_class = soup.find('strong', class_='title').text.strip()

win_loss_loop = [i.text.strip() for i in soup.find_all('span', class_='counter')]
wins = win_loss_loop[0]
losses = win_loss_loop[1]

graph_tag_loop = [i.text.strip() for i in soup.find_all('span', class_='graph_tag')]

win_ko = graph_tag_loop[0][:2].strip()
win_submission = graph_tag_loop[1][:2].strip()
win_decisions = graph_tag_loop[2][:2].strip()

loss_ko = graph_tag_loop[3][0][:2].strip()
loss_submission = graph_tag_loop[4][:2].strip()
loss_decisions = graph_tag_loop[5][:2].strip()

fighter_meta = {
    'First_name': firstname,
    'Last_name': lastname,
    'Nickname': nickname,
    'Date_of_birth': dob,
    'Locality': locality,
    'Nationality': nationality,
    'Association': association,
    'Height': height,
    'Weight': weight,
    'Weight_class': weight_class,
    'Wins': wins,
    'Losses': losses,
    'Win_by_ko': win_ko,
    'Win_by_submission': win_submission,
    'Win_decision': win_decisions,
    'Loss_by_ko': loss_ko,
    'Loss_by_submission': loss_submission,
    'Loss_by_desision': loss_decisions
}
fighter.append(fighter_meta)
print(fighter)