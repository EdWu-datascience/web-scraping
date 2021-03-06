import requests
from profile_number import profile_number
import pandas as pd
import time
from fake_useragent import UserAgent
j = 0
position = {}
ua = UserAgent()
for profile in profile_number[0:100]:
    j += 1
    print(j)
    headers = {
            'User-Agent':ua.chrome,
            'Cookie':"your cookie"
    }
    cur_pos_info = requests.get('https://my.pitchbook.com/web-api/profiles/'+profile+
                                '/person/positions/current?page=1&pageSize=10', headers=headers).text#3
    print(cur_pos_info)
    if '<!doctype html>' in cur_pos_info:
        time.sleep(35)
        headers = {
            'User-Agent':ua.chrome,
            'Cookie': "your cookie"
        }
        cur_pos_info = requests.get('https://my.pitchbook.com/web-api/profiles/' + profile +
                                    '/person/positions/current?page=1&pageSize=10', headers=headers).text  # 3
        print(cur_pos_info)
    cur_pos_info = eval(cur_pos_info.replace('true', "'yes'", 100).replace('false', "'no'", 100))

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
    position_info = pd.DataFrame.from_dict(position)
    position_info.to_csv("cur_position_info.csv")
