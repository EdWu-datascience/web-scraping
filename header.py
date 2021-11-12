
from bs4 import BeautifulSoup
from  urllib import request
import requests
from to_delete import profile_number
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
    'Cookie': "your ccookie"
}
#quote_page = "https://my.pitchbook.com/profile/100009-36P/person/profile"
i = 0
for profile in profile_number[0:100]:
    if i == 1:
        break

    quote_page1 = 'https://my.pitchbook.com/web-api/profiles/'+profile+'/person/general-info'
    quote_page2 = 'https://my.pitchbook.com/web-api/profiles/'+profile+'/person/contact-info'
    general_information = requests.get(quote_page1, headers=headers).text
    contact_information = requests.get(quote_page2, headers=headers).text
    print(general_information)
    print(contact_information)
    i += 1
'''
#quote_page1 = 'https://my.pitchbook.com/web-api/profiles/100012-15P/person/general-info'
#quote_page2 = 'https://my.pitchbook.com/web-api/profiles/100012-15P/person/contact-info'
general_information = requests.get(quote_page1,headers=headers).text
contact_information = requests.get(quote_page2,headers=headers).text
print(general_information)
print(contact_information)

'''

