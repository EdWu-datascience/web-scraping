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
    cur_bor_info = requests.get('https://my.pitchbook.com/web-api/profiles/' + profile +
                                    '/person/board-seats/current?page=1&pageSize=10', headers=headers).text  # 5 结果是none
    print(cur_bor_info)
    if '<!doctype html>' in cur_bor_info:
        time.sleep(35)
        headers = {
            'User-Agent':ua.chrome,
            'Cookie': "your cookie"
        }
        cur_bor_info = requests.get('https://my.pitchbook.com/web-api/profiles/' + profile +
                                    '/person/board-seats/current?page=1&pageSize=10', headers=headers).text  # 5 结果是none
        print(cur_bor_info)
    cur_bor_info = eval(cur_bor_info.replace('true', "'yes'", 100).replace('false', "'no'", 100))


    if cur_bor_info.get('content') is not None:  # 如果没有current board的话是不会有content这个key word的
        cur_bor_num = len(cur_bor_info.get('content'))
    else:
        cur_bor_num = 0
    for i in range(1, 11):
        if cur_bor_num == 0:
            if 'current board' + str(i) + '-firm name' not in position:
                position['current board' + str(i) + '-firm name'] = [None]
            else:
                position['current board' + str(i) + '-firm name'].append(None)
            if 'current board' + str(i) + '-firm type' not in position:
                position['current board' + str(i) + '-firm type'] = [None]
            else:
                position['current board' + str(i) + '-firm type'].append(None)
            if 'current board' + str(i) + '-title' not in position:
                position['current board' + str(i) + '-title'] = [None]
            else:
                position['current board' + str(i) + '-title'].append(None)
            if 'current board' + str(i) + '-location' not in position:
                position['current board' + str(i) + '-location'] = [None]
            else:
                position['current board' + str(i) + '-location'].append(None)
            if 'current board' + str(i) + '-industry' not in position:
                position['current board' + str(i) + '-industry'] = [None]
            else:
                position['current board' + str(i) + '-industry'].append(None)
            if 'current board' + str(i) + '-since' not in position:
                position['current board' + str(i) + '-since'] = [None]
            else:
                position['current board' + str(i) + '-since'].append(None)
            if 'current board' + str(i) + '-companylink' not in position:
                position['current board' + str(i) + '-companylink'] = [None]
            else:
                position['current board' + str(i) + '-companylink'].append(None)

        else:
            if 'current board' + str(i) + '-firm name' not in position:
                if i <= cur_bor_num:
                    position['current board' + str(i) + '-firm name'] = [
                        cur_bor_info.get('content')[i - 1].get('entity').get('name')]
                    position['current board' + str(i) + '-firm type'] = [
                        cur_bor_info.get('content')[i - 1].get('entity').get('type')]
                    position['current board' + str(i) + '-title'] = [cur_bor_info.get('content')[i - 1].get('title')]
                    position['current board' + str(i) + '-location'] = [
                        cur_bor_info.get('content')[i - 1].get('location')]
                    position['current board' + str(i) + '-industry'] = [
                        cur_bor_info.get('content')[i - 1].get('companyIndustry')]
                    position['current board' + str(i) + '-since'] = [
                        cur_bor_info.get('content')[i - 1].get('startDate')]
                    position['current board' + str(i) + '-companylink'] = ['https://my.pitchbook.com/profile/' +
                                                                              cur_bor_info.get('content')[i - 1].get(
                                                                                  'entity').get('pbId') +
                                                                              '/company/profile']
                else:
                    position['current board' + str(i) + '-firm name'] = [None]
                    position['current board' + str(i) + '-firm type'] = [None]
                    position['current board' + str(i) + '-title'] = [None]
                    position['current board' + str(i) + '-location'] = [None]
                    position['current board' + str(i) + '-industry'] = [None]
                    position['current board' + str(i) + '-since'] = [None]
                    position['current board' + str(i) + '-companylink'] = [None]
            else:
                if i <= cur_bor_num:
                    position['current board' + str(i) + '-firm name'].append(
                        cur_bor_info.get('content')[i - 1].get('entity').get('name'))
                    position['current board' + str(i) + '-firm type'].append(
                        cur_bor_info.get('content')[i - 1].get('entity').get('type'))
                    position['current board' + str(i) + '-title'].append(
                        cur_bor_info.get('content')[i - 1].get('title'))
                    position['current board' + str(i) + '-location'].append(
                        cur_bor_info.get('content')[i - 1].get('location'))
                    position['current board' + str(i) + '-industry'].append(
                        cur_bor_info.get('content')[i - 1].get('companyIndustry'))
                    position['current board' + str(i) + '-since'].append(cur_bor_info.get('content')[i - 1].get('startDate'))
                    position['current board' + str(i) + '-companylink'].append('https://my.pitchbook.com/profile/' +
                                                                                  cur_bor_info.get('content')[
                                                                                      i - 1].get('entity').get('pbId') +
                                                                                  '/company/profile')

                else:
                    position['current board' + str(i) + '-firm name'].append(None)
                    position['current board' + str(i) + '-firm type'].append(None)
                    position['current board' + str(i) + '-title'].append(None)
                    position['current board' + str(i) + '-location'].append(None)
                    position['current board' + str(i) + '-industry'].append(None)
                    position['current board' + str(i) + '-since'].append(None)
                    position['current board' + str(i) + '-companylink'].append(None)
    board_info = pd.DataFrame.from_dict(position)
    board_info.to_csv("cur_board_info.csv")
print(position)
