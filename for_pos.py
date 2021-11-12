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
            'Cookie': "your cookie"
    }
    for_pos_info = requests.get('https://my.pitchbook.com/web-api/profiles/' + profile +
                                '/person/positions/former?page=1&pageSize=10', headers=headers).text  # 4
    print(for_pos_info)
    if '<!doctype html>' in for_pos_info:
        time.sleep(35)
        headers = {
            'User-Agent':ua.chrome,
            'Cookie': "your cookie"
        }
        for_pos_info = requests.get('https://my.pitchbook.com/web-api/profiles/' + profile +
                                    '/person/positions/former?page=1&pageSize=10', headers=headers).text  # 4
        print(for_pos_info)
    for_pos_info = eval(for_pos_info.replace('true', "'yes'", 100).replace('false', "'no'", 100))
    if for_pos_info.get('content') is not None:  # 如果没有former position的话是不会有content这个key word的
        for_pos_num = len(for_pos_info.get('content'))
    else:
        for_pos_num = 0
    for i in range(1, 11):
        if for_pos_num == 0:
            if 'former position' + str(i) + '-firm name' not in position:
                position['former position' + str(i) + '-firm name'] = [None]
            else:
                position['former position' + str(i) + '-firm name'].append(None)
            if 'former position' + str(i) + '-firm type' not in position:
                position['former position' + str(i) + '-firm type'] = [None]
            else:
                position['former position' + str(i) + '-firm type'].append(None)
            if 'former position' + str(i) + '-title' not in position:
                position['former position' + str(i) + '-title'] = [None]
            else:
                position['former position' + str(i) + '-title'].append(None)
            if 'former position' + str(i) + '-location' not in position:
                position['former position' + str(i) + '-location'] = [None]
            else:
                position['former position' + str(i) + '-location'].append(None)
            if 'former position' + str(i) + '-industry' not in position:
                position['former position' + str(i) + '-industry'] = [None]
            else:
                position['former position' + str(i) + '-industry'].append(None)
            if 'former position' + str(i) + '-since' not in position:
                position['former position' + str(i) + '-since'] = [None]
            else:
                position['former position' + str(i) + '-since'].append(None)
            if 'former position' + str(i) + '-companylink' not in position:
                position['former position' + str(i) + '-companylink'] = [None]
            else:
                position['former position' + str(i) + '-companylink'].append(None)

        else:
            if 'former position' + str(i) + '-firm name' not in position:
                if i <= for_pos_num:
                    position['former position' + str(i) + '-firm name'] = [
                        for_pos_info.get('content')[i - 1].get('entity').get('name')]
                    position['former position' + str(i) + '-firm type'] = [
                        for_pos_info.get('content')[i - 1].get('entity').get('type')]
                    position['former position' + str(i) + '-title'] = [for_pos_info.get('content')[i - 1].get('title')]
                    position['former position' + str(i) + '-location'] = [
                        for_pos_info.get('content')[i - 1].get('location')]
                    position['former position' + str(i) + '-industry'] = [
                        for_pos_info.get('content')[i - 1].get('companyIndustry')]
                    position['former position' + str(i) + '-since'] = [
                        for_pos_info.get('content')[i - 1].get('startDate')]
                    position['former position' + str(i) + '-companylink'] = ['https://my.pitchbook.com/profile/' +
                                                                              for_pos_info.get('content')[i - 1].get(
                                                                                  'entity').get('pbId') +
                                                                              '/company/profile']
                else:
                    position['former position' + str(i) + '-firm name'] = [None]
                    position['former position' + str(i) + '-firm type'] = [None]
                    position['former position' + str(i) + '-title'] = [None]
                    position['former position' + str(i) + '-location'] = [None]
                    position['former position' + str(i) + '-industry'] = [None]
                    position['former position' + str(i) + '-since'] = [None]
                    position['former position' + str(i) + '-companylink'] = [None]
            else:
                if i <= for_pos_num:
                    position['former position' + str(i) + '-firm name'].append(
                        for_pos_info.get('content')[i - 1].get('entity').get('name'))
                    position['former position' + str(i) + '-firm type'].append(
                        for_pos_info.get('content')[i - 1].get('entity').get('type'))
                    position['former position' + str(i) + '-title'].append(
                        for_pos_info.get('content')[i - 1].get('title'))
                    position['former position' + str(i) + '-location'].append(
                        for_pos_info.get('content')[i - 1].get('location'))
                    position['former position' + str(i) + '-industry'].append(
                        for_pos_info.get('content')[i - 1].get('companyIndustry'))
                    position['former position' + str(i) + '-since'].append(for_pos_info.get('content')[i - 1].get('startDate'))
                    position['former position' + str(i) + '-companylink'].append('https://my.pitchbook.com/profile/' +
                                                                                  for_pos_info.get('content')[
                                                                                      i - 1].get('entity').get('pbId') +
                                                                                  '/company/profile')

                else:
                    position['former position' + str(i) + '-firm name'].append(None)
                    position['former position' + str(i) + '-firm type'].append(None)
                    position['former position' + str(i) + '-title'].append(None)
                    position['former position' + str(i) + '-location'].append(None)
                    position['former position' + str(i) + '-industry'].append(None)
                    position['former position' + str(i) + '-since'].append(None)
                    position['former position' + str(i) + '-companylink'].append(None)
    position_info = pd.DataFrame.from_dict(position)
    position_info.to_csv("for_position_info.csv")
print(position)
