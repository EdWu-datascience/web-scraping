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
    for_bor_info = requests.get('https://my.pitchbook.com/web-api/profiles/'+profile+
                                '/person/board-seats/former?page=1&pageSize=10', headers=headers).text#6
    print(for_bor_info)
    if '<!doctype html>' in for_bor_info:
        time.sleep(35)
        headers = {
            'User-Agent':ua.chrome,
            'Cookie': "your cookie"
        }
        for_bor_info = requests.get('https://my.pitchbook.com/web-api/profiles/' + profile +
                                    '/person/board-seats/former?page=1&pageSize=10', headers=headers).text  # 6
        print(for_bor_info)
    for_bor_info = eval(for_bor_info.replace('true', "'yes'", 100).replace('false', "'no'", 100))


    if for_bor_info.get('content') is not None:  # 如果没有former board的话是不会有content这个key word的
        for_bor_num = len(for_bor_info.get('content'))
    else:
        for_bor_num = 0
    for i in range(1, 11):
        if for_bor_num == 0:
            if 'former board' + str(i) + '-firm name' not in position:
                position['former board' + str(i) + '-firm name'] = [None]
            else:
                position['former board' + str(i) + '-firm name'].append(None)
            if 'former board' + str(i) + '-firm type' not in position:
                position['former board' + str(i) + '-firm type'] = [None]
            else:
                position['former board' + str(i) + '-firm type'].append(None)
            if 'former board' + str(i) + '-title' not in position:
                position['former board' + str(i) + '-title'] = [None]
            else:
                position['former board' + str(i) + '-title'].append(None)
            if 'former board' + str(i) + '-location' not in position:
                position['former board' + str(i) + '-location'] = [None]
            else:
                position['former board' + str(i) + '-location'].append(None)
            if 'former board' + str(i) + '-industry' not in position:
                position['former board' + str(i) + '-industry'] = [None]
            else:
                position['former board' + str(i) + '-industry'].append(None)
            if 'former board' + str(i) + '-since' not in position:
                position['former board' + str(i) + '-since'] = [None]
            else:
                position['former board' + str(i) + '-since'].append(None)
            if 'former board' + str(i) + '-companylink' not in position:
                position['former board' + str(i) + '-companylink'] = [None]
            else:
                position['former board' + str(i) + '-companylink'].append(None)

        else:
            if 'former board' + str(i) + '-firm name' not in position:
                if i <= for_bor_num:
                    position['former board' + str(i) + '-firm name'] = [
                        for_bor_info.get('content')[i - 1].get('entity').get('name')]
                    position['former board' + str(i) + '-firm type'] = [
                        for_bor_info.get('content')[i - 1].get('entity').get('type')]
                    position['former board' + str(i) + '-title'] = [for_bor_info.get('content')[i - 1].get('title')]
                    position['former board' + str(i) + '-location'] = [
                        for_bor_info.get('content')[i - 1].get('location')]
                    position['former board' + str(i) + '-industry'] = [
                        for_bor_info.get('content')[i - 1].get('companyIndustry')]
                    position['former board' + str(i) + '-since'] = [
                        for_bor_info.get('content')[i - 1].get('startDate')]
                    position['former board' + str(i) + '-companylink'] = ['https://my.pitchbook.com/profile/' +
                                                                              for_bor_info.get('content')[i - 1].get(
                                                                                  'entity').get('pbId') +
                                                                              '/company/profile']
                else:
                    position['former board' + str(i) + '-firm name'] = [None]
                    position['former board' + str(i) + '-firm type'] = [None]
                    position['former board' + str(i) + '-title'] = [None]
                    position['former board' + str(i) + '-location'] = [None]
                    position['former board' + str(i) + '-industry'] = [None]
                    position['former board' + str(i) + '-since'] = [None]
                    position['former board' + str(i) + '-companylink'] = [None]
            else:
                if i <= for_bor_num:
                    position['former board' + str(i) + '-firm name'].append(
                        for_bor_info.get('content')[i - 1].get('entity').get('name'))
                    position['former board' + str(i) + '-firm type'].append(
                        for_bor_info.get('content')[i - 1].get('entity').get('type'))
                    position['former board' + str(i) + '-title'].append(
                        for_bor_info.get('content')[i - 1].get('title'))
                    position['former board' + str(i) + '-location'].append(
                        for_bor_info.get('content')[i - 1].get('location'))
                    position['former board' + str(i) + '-industry'].append(
                        for_bor_info.get('content')[i - 1].get('companyIndustry'))
                    position['former board' + str(i) + '-since'].append(for_bor_info.get('content')[i - 1].get('startDate'))
                    position['former board' + str(i) + '-companylink'].append('https://my.pitchbook.com/profile/' +
                                                                                  for_bor_info.get('content')[
                                                                                      i - 1].get('entity').get('pbId') +
                                                                                  '/company/profile')

                else:
                    position['former board' + str(i) + '-firm name'].append(None)
                    position['former board' + str(i) + '-firm type'].append(None)
                    position['former board' + str(i) + '-title'].append(None)
                    position['former board' + str(i) + '-location'].append(None)
                    position['former board' + str(i) + '-industry'].append(None)
                    position['former board' + str(i) + '-since'].append(None)
                    position['former board' + str(i) + '-companylink'].append(None)
    board_info = pd.DataFrame.from_dict(position)
    board_info.to_csv("for_board_info.csv")
print(position)
