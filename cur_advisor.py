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
    cur_adv_info = requests.get('https://my.pitchbook.com/web-api/profiles/'+profile+
                                '/person/advisory-roles/current?page=1&pageSize=10',headers=headers).text
    print(cur_adv_info)
    if '<!doctype html>' in cur_adv_info:
        time.sleep(35)
        headers = {
            'User-Agent':ua.chrome,
            'Cookie': "your cookie"
            }
        cur_adv_info = requests.get('https://my.pitchbook.com/web-api/profiles/' + profile +
                                    '/person/advisory-roles/current?page=1&pageSize=10', headers=headers).text
        print(cur_adv_info)
    cur_adv_info = eval(cur_adv_info.replace('true', "'yes'", 100).replace('false', "'no'", 100))


    if cur_adv_info.get('content') is not None:  # 如果没有current advisor的话是不会有content这个key word的
        cur_adv_num = len(cur_adv_info.get('content'))
    else:
        cur_adv_num = 0
    for i in range(1, 11):
        if cur_adv_num == 0:
            if 'current advisor' + str(i) + '-firm name' not in position:
                position['current advisor' + str(i) + '-firm name'] = [None]
            else:
                position['current advisor' + str(i) + '-firm name'].append(None)
            if 'current advisor' + str(i) + '-firm type' not in position:
                position['current advisor' + str(i) + '-firm type'] = [None]
            else:
                position['current advisor' + str(i) + '-firm type'].append(None)
            if 'current advisor' + str(i) + '-title' not in position:
                position['current advisor' + str(i) + '-title'] = [None]
            else:
                position['current advisor' + str(i) + '-title'].append(None)
            if 'current advisor' + str(i) + '-location' not in position:
                position['current advisor' + str(i) + '-location'] = [None]
            else:
                position['current advisor' + str(i) + '-location'].append(None)
            if 'current advisor' + str(i) + '-industry' not in position:
                position['current advisor' + str(i) + '-industry'] = [None]
            else:
                position['current advisor' + str(i) + '-industry'].append(None)
            if 'current advisor' + str(i) + '-since' not in position:
                position['current advisor' + str(i) + '-since'] = [None]
            else:
                position['current advisor' + str(i) + '-since'].append(None)
            if 'current advisor' + str(i) + '-companylink' not in position:
                position['current advisor' + str(i) + '-companylink'] = [None]
            else:
                position['current advisor' + str(i) + '-companylink'].append(None)

        else:
            if 'current advisor' + str(i) + '-firm name' not in position:
                if i <= cur_adv_num:
                    position['current advisor' + str(i) + '-firm name'] = [
                        cur_adv_info.get('content')[i - 1].get('entity').get('name')]
                    position['current advisor' + str(i) + '-firm type'] = [
                        cur_adv_info.get('content')[i - 1].get('entity').get('type')]
                    position['current advisor' + str(i) + '-title'] = [cur_adv_info.get('content')[i - 1].get('title')]
                    position['current advisor' + str(i) + '-location'] = [
                        cur_adv_info.get('content')[i - 1].get('location')]
                    position['current advisor' + str(i) + '-industry'] = [
                        cur_adv_info.get('content')[i - 1].get('companyIndustry')]
                    position['current advisor' + str(i) + '-since'] = [
                        cur_adv_info.get('content')[i - 1].get('startDate')]
                    position['current advisor' + str(i) + '-companylink'] = ['https://my.pitchbook.com/profile/' +
                                                                              cur_adv_info.get('content')[i - 1].get(
                                                                                  'entity').get('pbId') +
                                                                              '/company/profile']
                else:
                    position['current advisor' + str(i) + '-firm name'] = [None]
                    position['current advisor' + str(i) + '-firm type'] = [None]
                    position['current advisor' + str(i) + '-title'] = [None]
                    position['current advisor' + str(i) + '-location'] = [None]
                    position['current advisor' + str(i) + '-industry'] = [None]
                    position['current advisor' + str(i) + '-since'] = [None]
                    position['current advisor' + str(i) + '-companylink'] = [None]
            else:
                if i <= cur_adv_num:
                    position['current advisor' + str(i) + '-firm name'].append(
                        cur_adv_info.get('content')[i - 1].get('entity').get('name'))
                    position['current advisor' + str(i) + '-firm type'].append(
                        cur_adv_info.get('content')[i - 1].get('entity').get('type'))
                    position['current advisor' + str(i) + '-title'].append(
                        cur_adv_info.get('content')[i - 1].get('title'))
                    position['current advisor' + str(i) + '-location'].append(
                        cur_adv_info.get('content')[i - 1].get('location'))
                    position['current advisor' + str(i) + '-industry'].append(
                        cur_adv_info.get('content')[i - 1].get('companyIndustry'))
                    position['current advisor' + str(i) + '-since'].append(cur_adv_info.get('content')[i - 1].get('startDate'))
                    position['current advisor' + str(i) + '-companylink'].append('https://my.pitchbook.com/profile/' +
                                                                                  cur_adv_info.get('content')[
                                                                                      i - 1].get('entity').get('pbId') +
                                                                                  '/company/profile')

                else:
                    position['current advisor' + str(i) + '-firm name'].append(None)
                    position['current advisor' + str(i) + '-firm type'].append(None)
                    position['current advisor' + str(i) + '-title'].append(None)
                    position['current advisor' + str(i) + '-location'].append(None)
                    position['current advisor' + str(i) + '-industry'].append(None)
                    position['current advisor' + str(i) + '-since'].append(None)
                    position['current advisor' + str(i) + '-companylink'].append(None)
    advisor_info = pd.DataFrame.from_dict(position)
    advisor_info.to_csv("cur_advisor_info.csv")
print(position)
