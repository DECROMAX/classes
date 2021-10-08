import pandas as pd
import requests
from bs4 import BeautifulSoup

urls = []
fighter_data = []
test_url = 'https://www.sherdog.com/fighter/Nate-Diaz-11451'


def get_soup(url):
    """Creates soup"""
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
    }
    r = requests.get(url, headers=headers)
    return BeautifulSoup(r.content, 'html.parser')


def parse_dataframe():
    """Parses pro_mma_fighters.csv and returns fighter url list"""
    source_csv = 'pro_mma_fighters.csv'
    df = pd.read_csv(source_csv)
    for fighter in list(df['url']):
        urls.append(f'https://www.sherdog.com/{fighter}')



def get_fighter_meta(fighter_urls):
    """Scrapes meta from fighters page"""
    for counter, fighter_url in enumerate(fighter_urls, start=1):
        soup = get_soup(fighter_url)

        first_name = soup.find('span', class_='fn').text.strip().split()[0]
        last_name = soup.find('span', class_='fn').text.strip().split()[1]
        full_name = f'{first_name} {last_name}'
        try:
            nickname = soup.find('span', class_='nickname').text.strip()
        except (AttributeError, IndexError):
            nickname = ' '
        image_url = f"https://www.sherdog.com/{soup.find('img', class_='profile_image photo')['src']}"

        try:
            dob = soup.find('span', attrs={'itemprop': 'birthDate'}).text.strip()
        except (AttributeError, IndexError):
            dob = ' '

        try:
            location = soup.find('span', class_='locality').text.strip()
        except (AttributeError, IndexError):
            location = ''
        nationality = soup.find('strong', attrs={'itemprop': 'nationality'}).text.strip()

        try:
            association = soup.find('span', attrs={'itemprop': 'name'}).text.strip()
        except (AttributeError, IndexError):
            association = ' '

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
            'First_name': first_name,
            'Last_name': last_name,
            'Full name': full_name,
            'Nickname': nickname,
            'Image_url': image_url,
            'Date_of_birth': dob,
            'Location': location,
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
        fighter_data.append(fighter_meta)
        print(f'Saving: {full_name} {image_url}  - {counter} of {len(fighter_urls)}')


def main():
    parse_dataframe()
    get_fighter_meta(urls)

main()