import re
import requests
from pprint import pprint
from docopt import docopt
# from requests.packages.urllib3.exceptions import InsecureRequestWarning
# requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9050'
response = requests.get(url, )
stations = re.findall(u'([\u4e00-\u9fa5]+)\|([A-Z]+)',response.text)
pprint(dict(stations), )

# def cli():
#     """command-line interface"""
#     arguments = docopt(__doc__)
#     print(arguments)
    # from_station = stations.get(arguments['<from>'])
    # to_station = stations.get(arguments['<to>'])
    # date = arguments['<date>']
    # url = ('https://kyfw.12306.cn/otn/leftTicket/queryO?'
    #        'leftTicketDTO.train_date={}&'
    #        'leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT').\
    #     format(date,from_station,to_station)
    #
    # r=requests.get(url, verify=False)
    # print(r.json())