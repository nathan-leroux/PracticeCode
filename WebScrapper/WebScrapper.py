from bs4 import BeautifulSoup
import requests
import logging
import re


class ScrapperAbstract:
    def __init__(self, scrapper_platform):
        self.scrapper_platform = scrapper_platform

    def scrape_one(self):
        logging.debug('printing dumb shit')
        self.scrapper_platform.skim_soup()

    def scrape_all(self):
        return None

class PlayerDatabaseStub:
    def __init__(self):
        self.recent_player = None

    def set_player(self,scraped_player):
        logging.debug(f'Saved : {scraped_player} to the player database ')
        self.recent_player = scraped_player

    def get_player(self,search_term):
        return self.recent_player

class WebsiteLogicStub:
    def __init__(self):
        self.recent_website = None

    def set_website(self, returned_website):
        logging.debug(f'Returned : {returned_website} to the scrapper')
        self.recent_website = returned_website

    def get_website(self):
        return self.recent_website

class ScrapperPlatform:
    def __init__(self):
        self.website = 'https://www.basketball-reference.com/boxscores/201910230CHO.html'
        self.soup = self._load_http()

    def _load_http(self):
        cunt = requests.get(self.website)
        cunt_soup = BeautifulSoup(cunt.content, 'html.parser')
        return cunt_soup

    def updateDatabase(self, stat, val):
        print(f'{stat} : {val}')


    def skim_soup(self):
        ref_points = []

        results = self.soup.find_all('table', id=re.compile(r'^box-\w{3}-game-basic'))
        for result in results:
            players = result.tbody.find_all('tr')
            for player in players:
                name = player.th.text
                if name != 'Reserves':
                    self.updateDatabase('name', name)
                    for stat in player.find_all('td'):
                        useful_stat = ['mp', 'fg', 'fga', 'fg3', 'fg3a', 'ft', 'fta', 'orb',
                                       'drb', 'ast', 'stl', 'blk', 'tov', 'pf']
                        if stat['data-stat'] in useful_stat:
                            self.updateDatabase(stat['data-stat'],stat.text)


        



if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG,
                        format='%(filename)s : %(funcName)s\t: %(msg)s')

    scrapper_platform = ScrapperPlatform()
    logging.debug('making platform...')
    scrapper_abstract = ScrapperAbstract(scrapper_platform)
    logging.debug('making abstract...')
    scrapper_abstract.scrape_one()
    logging.debug('scrapping once')

