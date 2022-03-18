import pandas as pd
from bs4 import BeautifulSoup
from  urllib import request
import urllib
import requests
#from shortened_number import profile_number
import pandas as pd
import time
import json
from fake_useragent import UserAgent
from profile_info import key
ua = UserAgent()
data = {}
a = ['bGxsGDyvn']
cookie = ['your cookie here']
url = ['https://www.startupschool.org/graphql']
for index, value in enumerate(key[13000:]):
    print(value)
    payload_dict = {
        "operationName": "COFOUNDER_MATCHING_CANDIDATE",
        "variables": {
            "slug": value  # Change this
        },
        "your query here"
    }
    #print(payload_dict)
    headers = {
        'Origin': 'https://www.startupschool.org',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'User-Agent': ua.chrome,
        'content-type': 'application/json',
        'accept': '*/*',
        'Referer': 'https://www.startupschool.org/cofounder-matching/candidate/' + value,  # Change this
        'Cookie': cookie[0],
        'x-csrf-token': 
        # 'Connection': 'keep-alive',
        # 'x-original-url': 'https://www.startupschool.org'
    }
    response = requests.request("POST", url[0], headers=headers, data=json.dumps(payload_dict))
    str_info = response.content.decode()
    #print(str_info)
    if '<!DOCTYPE html>' in str_info:
        if 'education' not in data.keys():
            data['education'] = [None]
        else:
            data['education'].append(None)
        if 'employment' not in data.keys():
            data['employment'] = [None]
        else:
            data['employment'].append(None)
        continue
    dict_info = eval(str_info.replace('null', "'null'", 100).replace('false', "'no'", 100).replace('true', "'yes'", 100))
    #print(dict_info)
    if 'education' not in data.keys():
        if dict_info.get('data') is not None:
            if dict_info.get('data').get('cofounderMatching') is not None:
                if dict_info.get('data').get('cofounderMatching').get('candidate') is not None:
                    if dict_info.get('data').get('cofounderMatching').get('candidate').get('user') is not None:
                        data['education'] = [dict_info.get('data').get('cofounderMatching').get('candidate').get('user').get('education').replace('\n', '||', 100)]
                    else:
                        data['education'] = [None]
                else:
                    data['education'] = [None]
            else:
                data['education'] = [None]
        else:
            data['education'] = [None]
    else:
        if dict_info.get('data') is not None:
            if dict_info.get('data').get('cofounderMatching') is not None:
                if dict_info.get('data').get('cofounderMatching').get('candidate') is not None:
                    if dict_info.get('data').get('cofounderMatching').get('candidate').get('user') is not None:
                        data['education'].append(dict_info.get('data').get('cofounderMatching').get('candidate').get('user').get('education').replace('\n', '||', 100))
                    else:
                        data['education'].append(None)
                else:
                    data['education'].append(None)
            else:
                data['education'].append(None)
        else:
            data['education'].append(None)
    if 'employment' not in data.keys():
        if dict_info.get('data') is not None:
            if dict_info.get('data').get('cofounderMatching') is not None:
                if dict_info.get('data').get('cofounderMatching').get('candidate') is not None:
                    if dict_info.get('data').get('cofounderMatching').get('candidate').get('user') is not None:
                        data['employment'] = [dict_info.get('data').get('cofounderMatching').get('candidate').get('user').get('employment').replace('\n', '||', 100)]
                    else:
                        data['employment'] = [None]
                else:
                    data['employment'] = [None]
            else:
                data['employment'] = [None]
        else:
            data['employment'] = [None]
    else:
        if dict_info.get('data') is not None:
            if dict_info.get('data').get('cofounderMatching') is not None:
                if dict_info.get('data').get('cofounderMatching').get('candidate') is not None:
                    if dict_info.get('data').get('cofounderMatching').get('candidate').get('user') is not None:
                        data['employment'].append(dict_info.get('data').get('cofounderMatching').get('candidate').get('user').get('employment').replace('\n', '||', 100))
                    else:
                        data['employment'].append(None)
                else:
                    data['employment'].append(None)
            else:
                data['employment'].append(None)
        else:
            data['employment'].append(None)
#####
print(data)
data_info = pd.DataFrame.from_dict(data)
print(data_info)

data_info.to_excel("13000-_profiles.xlsx")
