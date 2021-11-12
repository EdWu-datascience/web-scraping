from bs4 import BeautifulSoup
from  urllib import request
import requests
from profile_number import profile_number
import pandas as pd
import time
from fake_useragent import UserAgent
j = 0
data = {}
ua = UserAgent()
for profile in profile_number:
    j += 1
    print(j)
    headers = {
            'User-Agent':ua.chrome,
            'Cookie':"your cookie"
    }
    general_info = requests.get('https://my.pitchbook.com/web-api/profiles/'+profile+'/person/general-info', headers=headers).text#1
    contact_info = requests.get('https://my.pitchbook.com/web-api/profiles/'+profile+'/person/contact-info', headers=headers).text#2
    if '<!doctype html>' in general_info or '<!doctype html>' in contact_info:
        time.sleep(35)
        headers = {
            'User-Agent':ua.chrome,
            'Cookie':"your cookie"
        }
        general_info = requests.get('https://my.pitchbook.com/web-api/profiles/' + profile + '/person/general-info',headers=headers).text  # 1
        contact_info = requests.get('https://my.pitchbook.com/web-api/profiles/' + profile + '/person/contact-info',headers=headers).text  # 2
    print(general_info)
    print(contact_info)
    general_info = eval(general_info.replace('true', "'yes'", 100).replace('false', "'no'", 100))
    contact_info = eval(contact_info.replace('true', "'yes'", 100).replace('false', "'no'", 100))
    if 'firstname' not in data.keys():
        data['firstname'] = [contact_info.get('firstName')]
    else:
        data['firstname'].append(contact_info.get('firstName'))
    # get last name
    if 'lastname' not in data.keys():
        data['lastname'] = [contact_info.get('lastName')]
    else:
        data['lastname'].append(contact_info.get('lastName'))
    # get biography
    if 'biography' not in data.keys():
        data['biography'] = [general_info.get('biography')]
    else:
        data['biography'].append(general_info.get('biography'))
    # get primary position
    if 'primary_position' not in data.keys():
        data['primary_position'] = [general_info.get('primaryPosition')]
    else:
        data['primary_position'].append(general_info.get('primaryPosition'))
    # get gender
    if 'gender' not in data.keys():
        data['gender'] = [general_info.get('gender')]
    else:
        data['gender'].append(general_info.get('gender'))
    # get education
    if 'education' not in data.keys():
        data['education'] = [general_info.get('educationList')]
    else:
        data['education'].append(general_info.get('educationList'))
    # get email
    if 'email' not in data.keys():
        data['email'] = [contact_info.get('email')]
    else:
        data['email'].append(contact_info.get('email'))
    #get phone number
    if 'phone' not in data.keys():
        data['phone'] = [contact_info.get('phone')]
    else:
        data['phone'].append(contact_info.get('phone'))
    # get linkedin
    if 'linkedin' not in data.keys():
        data['linkedin'] = [contact_info.get('linkedInLink')]
    else:
        data['linkedin'].append(contact_info.get('linkedInLink'))
    # get address
    if 'address' not in data.keys():
        if contact_info.get('primaryOffice') is not None:
            data['address'] = [contact_info.get('primaryOffice').get('address')]
        else:
            data['address'] = [None]
    else:
        if contact_info.get('primaryOffice') is not None:
            data['address'].append(contact_info.get('primaryOffice').get('address'))
        else:
            data['address'].append(None)
    data_info = pd.DataFrame.from_dict(data)
    data_info.to_csv("general_info.csv")





