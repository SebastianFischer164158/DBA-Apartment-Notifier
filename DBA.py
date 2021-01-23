import re

import requests


class DBA:

    # do stuff
    def __init__(self):
        self.reqx = None


    def __getter(self):
        URL = r'https://www.dba.dk/boliger/andelsbolig/reg-koebenhavn-og-omegn/?pris=(1500000-2499999)&pris=(1000000-1499999)&pris=(500000-999999)&pris=(-499999)&per=alle'
        headers = {
            'Host': 'www.dba.dk',
            'Accept' : '*/*',
            'User-Agent': ''
        }
        self.reqx = requests.get(url=URL,headers=headers)
        return self.reqx.content

    def get_number_of_postings(self):
        dba_content = self.__getter().decode('UTF-8')
        n = re.search('Alle annoncer <small> \((\d+)\)<\/small>', dba_content)
        return n.group(1)
