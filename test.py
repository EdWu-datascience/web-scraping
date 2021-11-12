
from bs4 import BeautifulSoup
from  urllib import request
import requests
from profile_number import profile_number
#from dict import info
import pandas as pd
import time
from fake_useragent import UserAgent
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
    'Cookie':"your cookie"
}
j = 0
position = {}
ua = UserAgent()
#for profile in ['100134-82P','100009-36P','100012-15P']:
for profile in profile_number[0:100]:
#for profile in ['100134-82P','100012-15P']:
#for profile in ['100009-36P','100012-15P']:
    #print(profile)
    j += 1
    print(j)
    position_info = pd.DataFrame.from_dict(position)
    position_info.to_csv("position_info.csv")
    # general information
    # 'https://my.pitchbook.com/web-api/profiles/'+profile+'/person/general-info'
    #general_info = requests.get('https://my.pitchbook.com/web-api/profiles/'
    #                            +profile+'/person/general-info', headers=headers).text#1
    # concact information
    # 'https://my.pitchbook.com/web-api/profiles/'+profile+'/person/contact-info'
    #contact_info = requests.get('https://my.pitchbook.com/web-api/profiles/'
    #                            +profile+'/person/contact-info', headers=headers).text#2
    # current position link
    # 'https://my.pitchbook.com/web-api/profiles/'+profile+'/person/positions/current?page=1&pageSize=10'
    headers = {
            'User-Agent':ua.chrome,
            'Cookie': "your cookie"
    }
    cur_pos_info = requests.get('https://my.pitchbook.com/web-api/profiles/'+profile+
                                '/person/positions/current?page=1&pageSize=10', headers=headers).text#3
    #print('s')
    print(cur_pos_info)
    if '<!doctype html>' in cur_pos_info:
        time.sleep(35)
        headers = {
            'User-Agent':ua.chrome,
            'Cookie': "your cookie"
        }
        cur_pos_info = requests.get('https://my.pitchbook.com/web-api/profiles/' + profile +
                                    '/person/positions/current?page=1&pageSize=10', headers=headers).text  # 3
    # former position link
    # 'https://my.pitchbook.com/web-api/profiles/'+profile+'/person/positions/former?page=1&pageSize=10'
    #for_pos_info = requests.get('https://my.pitchbook.com/web-api/profiles/'+profile+
    #                            '/person/positions/former?page=1&pageSize=10', headers=headers).text#4
    # current board link
    # 'https://my.pitchbook.com/web-api/profiles/'+profile+'/person/board-seats/current?page=1&pageSize=10'
    #cur_bor_info = requests.get('https://my.pitchbook.com/web-api/profiles/'+profile+
    #                            '/person/board-seats/current?page=1&pageSize=10', headers=headers).text#5 结果是none
    # former board link
    # 'https://my.pitchbook.com/web-api/profiles/'+profile+'/person/board-seats/former?page=1&pageSize=10'
    #for_bor_info = requests.get('https://my.pitchbook.com/web-api/profiles/'+profile+
    #                            '/person/board-seats/former?page=1&pageSize=10', headers=headers).text#6
    # network consist of board member\portfolio member\fund member
    # 'https://my.pitchbook.com/web-api/profiles/'+profile+'/person/network/fund-team-members?page=1&pageSize=10'
    # 'https://my.pitchbook.com/web-api/profiles/'+profile+'/person/network/board-members?page=1&pageSize=10'
    # 'https://my.pitchbook.com/web-api/profiles/'+profile+'/person/network/portfolio-executives?page=1&pageSize=10'

    #fund_info = requests.get('https://my.pitchbook.com/web-api/profiles/'+profile+'/person/network/fund-team-members?page=1&pageSize=10', headers=headers).text#
    #board_info = requests.get('https://my.pitchbook.com/web-api/profiles/'+profile+'/person/network/board-members?page=1&pageSize=10', headers=headers).text
    #port_info = requests.get('https://my.pitchbook.com/web-api/profiles/'+profile+'/person/network/portfolio-executives?page=1&pageSize=10', headers=headers).text

    # current advisor role
    # 'https://my.pitchbook.com/web-api/profiles/'+profile+'/person/advisory-roles/current?page=1&pageSize=10'
    #cur_adv_info = requests.get('https://my.pitchbook.com/web-api/profiles/'+profile+
    #                            '/person/advisory-roles/current?page=1&pageSize=10',headers=headers).text
    # former advisor role
    # 'https://my.pitchbook.com/web-api/profiles/'+profile+'/person/advisory-roles/former?page=1&pageSize=10'
    #for_adv_info = requests.get('https://my.pitchbook.com/web-api/profiles/'+profile+'/person/advisory-roles/former?page=1&pageSize=10', headers=headers).text

    #general_info = eval(general_info.replace('true', '"yes"', 100).replace('false', '"no"', 100))
    #contact_info = eval(contact_info.replace('true', '"yes"', 100).replace('false', '"no"', 100))
    cur_pos_info = eval(cur_pos_info.replace('true', '"yes"', 100).replace('false', '"no"', 100))
    #for_pos_info = eval(for_pos_info.replace('true', '"yes"', 100).replace('false', '"no"', 100))
    #cur_bor_info = eval(cur_bor_info.replace('true', '"yes"', 100).replace('false', '"no"', 100))
    #for_bor_info = eval(for_bor_info.replace('true', '"yes"', 100).replace('false', '"no"', 100))
    #fund_info = eval(fund_info.replace('true', '"yes"', 100).replace('false', '"no"', 100))
    #print(cur_pos_info)
    #board_info = eval(board_info.replace('true', '"yes"', 100).replace('false', '"no"', 100))
    #port_info = eval(port_info.replace('true', '"yes"', 100).replace('false', '"no"', 100))
    #cur_adv_info = eval(cur_adv_info.replace('true', '"yes"', 100).replace('false', '"no"', 100))
    #for_adv_info = eval(for_adv_info.replace('true', '"yes"', 100).replace('false', '"no"', 100))




    #print(cur_pos_info)
    if cur_pos_info.get('content') is not None:  # 如果没有current position的话是不会有content这个key word的
        cur_pos_num = len(cur_pos_info.get('content'))
    else:
        cur_pos_num = 0
    for i in range(1, 11):
        if cur_pos_num == 0:
            if 'current position' + str(i) + '-firm name' not in position:
                position['current position' + str(i) + '-firm name'] = [None]
            else:
                position['current position' + str(i) + '-firm name'].append(None)
            if 'current position' + str(i) + '-firm type' not in position:
                position['current position' + str(i) + '-firm type'] = [None]
            else:
                position['current position' + str(i) + '-firm type'].append(None)
            if 'current position' + str(i) + '-title' not in position:
                position['current position' + str(i) + '-title'] = [None]
            else:
                position['current position' + str(i) + '-title'].append(None)
            if 'current position' + str(i) + '-location' not in position:
                position['current position' + str(i) + '-location'] = [None]
            else:
                position['current position' + str(i) + '-location'].append(None)
            if 'current position' + str(i) + '-industry' not in position:
                position['current position' + str(i) + '-industry'] = [None]
            else:
                position['current position' + str(i) + '-industry'].append(None)
            if 'current position' + str(i) + '-since' not in position:
                position['current position' + str(i) + '-since'] = [None]
            else:
                position['current position' + str(i) + '-since'].append(None)
            if 'current position' + str(i) + '-companylink' not in position:
                position['current position' + str(i) + '-companylink'] = [None]
            else:
                position['current position' + str(i) + '-companylink'].append(None)

        else:
            if 'current position' + str(i) + '-firm name' not in position:
                if i <= cur_pos_num:
                    position['current position' + str(i) + '-firm name'] = [
                        cur_pos_info.get('content')[i - 1].get('entity').get('name')]
                    position['current position' + str(i) + '-firm type'] = [
                        cur_pos_info.get('content')[i - 1].get('entity').get('type')]
                    position['current position' + str(i) + '-title'] = [cur_pos_info.get('content')[i - 1].get('title')]
                    position['current position' + str(i) + '-location'] = [
                        cur_pos_info.get('content')[i - 1].get('location')]
                    position['current position' + str(i) + '-industry'] = [
                        cur_pos_info.get('content')[i - 1].get('companyIndustry')]
                    position['current position' + str(i) + '-since'] = [
                        cur_pos_info.get('content')[i - 1].get('startDate')]
                    position['current position' + str(i) + '-companylink'] = ['https://my.pitchbook.com/profile/' +
                                                                              cur_pos_info.get('content')[i - 1].get(
                                                                                  'entity').get('pbId') +
                                                                              '/company/profile']
                else:
                    position['current position' + str(i) + '-firm name'] = [None]
                    position['current position' + str(i) + '-firm type'] = [None]
                    position['current position' + str(i) + '-title'] = [None]
                    position['current position' + str(i) + '-location'] = [None]
                    position['current position' + str(i) + '-industry'] = [None]
                    position['current position' + str(i) + '-since'] = [None]
                    position['current position' + str(i) + '-companylink'] = [None]
            else:
                if i <= cur_pos_num:
                    position['current position' + str(i) + '-firm name'].append(
                        cur_pos_info.get('content')[i - 1].get('entity').get('name'))
                    position['current position' + str(i) + '-firm type'].append(
                        cur_pos_info.get('content')[i - 1].get('entity').get('type'))
                    position['current position' + str(i) + '-title'].append(
                        cur_pos_info.get('content')[i - 1].get('title'))
                    position['current position' + str(i) + '-location'].append(
                        cur_pos_info.get('content')[i - 1].get('location'))
                    position['current position' + str(i) + '-industry'].append(
                        cur_pos_info.get('content')[i - 1].get('companyIndustry'))
                    position['current position' + str(i) + '-since'].append(cur_pos_info.get('content')[i - 1].get('startDate'))
                    position['current position' + str(i) + '-companylink'].append('https://my.pitchbook.com/profile/' +
                                                                                  cur_pos_info.get('content')[
                                                                                      i - 1].get('entity').get('pbId') +
                                                                                  '/company/profile')

                else:
                    position['current position' + str(i) + '-firm name'].append(None)
                    position['current position' + str(i) + '-firm type'].append(None)
                    position['current position' + str(i) + '-title'].append(None)
                    position['current position' + str(i) + '-location'].append(None)
                    position['current position' + str(i) + '-industry'].append(None)
                    position['current position' + str(i) + '-since'].append(None)
                    position['current position' + str(i) + '-companylink'].append(None)
print(position)


