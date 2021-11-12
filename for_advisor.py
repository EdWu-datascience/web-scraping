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
    for_adv_info = requests.get('https://my.pitchbook.com/web-api/profiles/'+profile+
                                '/person/advisory-roles/former?page=1&pageSize=10', headers=headers).text

    print(for_adv_info)
    if '<!doctype html>' in for_adv_info:
        time.sleep(35)
        headers = {
            'User-Agent':ua.chrome,
            'Cookie':"your cookie"
        }
        for_adv_info = requests.get('https://my.pitchbook.com/web-api/profiles/' + profile +
                                    '/person/advisory-roles/former?page=1&pageSize=10', headers=headers).text
        print(for_adv_info)
    for_adv_info = eval(for_adv_info.replace('true', "'yes'", 100).replace('false', "'no'", 100))


    if for_adv_info.get('content') is not None:  # 如果没有former advisor的话是不会有content这个key word的
        for_adv_num = len(for_adv_info.get('content'))
    else:
        for_adv_num = 0
    for i in range(1, 11):
        if for_adv_num == 0:
            if 'former advisor' + str(i) + '-firm name' not in position:
                position['former advisor' + str(i) + '-firm name'] = [None]
            else:
                position['former advisor' + str(i) + '-firm name'].append(None)
            if 'former advisor' + str(i) + '-firm type' not in position:
                position['former advisor' + str(i) + '-firm type'] = [None]
            else:
                position['former advisor' + str(i) + '-firm type'].append(None)
            if 'former advisor' + str(i) + '-title' not in position:
                position['former advisor' + str(i) + '-title'] = [None]
            else:
                position['former advisor' + str(i) + '-title'].append(None)
            if 'former advisor' + str(i) + '-location' not in position:
                position['former advisor' + str(i) + '-location'] = [None]
            else:
                position['former advisor' + str(i) + '-location'].append(None)
            if 'former advisor' + str(i) + '-industry' not in position:
                position['former advisor' + str(i) + '-industry'] = [None]
            else:
                position['former advisor' + str(i) + '-industry'].append(None)
            if 'former advisor' + str(i) + '-since' not in position:
                position['former advisor' + str(i) + '-since'] = [None]
            else:
                position['former advisor' + str(i) + '-since'].append(None)
            if 'former advisor' + str(i) + '-companylink' not in position:
                position['former advisor' + str(i) + '-companylink'] = [None]
            else:
                position['former advisor' + str(i) + '-companylink'].append(None)

        else:
            if 'former advisor' + str(i) + '-firm name' not in position:
                if i <= for_adv_num:
                    position['former advisor' + str(i) + '-firm name'] = [
                        for_adv_info.get('content')[i - 1].get('entity').get('name')]
                    position['former advisor' + str(i) + '-firm type'] = [
                        for_adv_info.get('content')[i - 1].get('entity').get('type')]
                    position['former advisor' + str(i) + '-title'] = [for_adv_info.get('content')[i - 1].get('title')]
                    position['former advisor' + str(i) + '-location'] = [
                        for_adv_info.get('content')[i - 1].get('location')]
                    position['former advisor' + str(i) + '-industry'] = [
                        for_adv_info.get('content')[i - 1].get('companyIndustry')]
                    position['former advisor' + str(i) + '-since'] = [
                        for_adv_info.get('content')[i - 1].get('startDate')]
                    position['former advisor' + str(i) + '-companylink'] = ['https://my.pitchbook.com/profile/' +
                                                                              for_adv_info.get('content')[i - 1].get(
                                                                                  'entity').get('pbId') +
                                                                              '/company/profile']
                else:
                    position['former advisor' + str(i) + '-firm name'] = [None]
                    position['former advisor' + str(i) + '-firm type'] = [None]
                    position['former advisor' + str(i) + '-title'] = [None]
                    position['former advisor' + str(i) + '-location'] = [None]
                    position['former advisor' + str(i) + '-industry'] = [None]
                    position['former advisor' + str(i) + '-since'] = [None]
                    position['former advisor' + str(i) + '-companylink'] = [None]
            else:
                if i <= for_adv_num:
                    position['former advisor' + str(i) + '-firm name'].append(
                        for_adv_info.get('content')[i - 1].get('entity').get('name'))
                    position['former advisor' + str(i) + '-firm type'].append(
                        for_adv_info.get('content')[i - 1].get('entity').get('type'))
                    position['former advisor' + str(i) + '-title'].append(
                        for_adv_info.get('content')[i - 1].get('title'))
                    position['former advisor' + str(i) + '-location'].append(
                        for_adv_info.get('content')[i - 1].get('location'))
                    position['former advisor' + str(i) + '-industry'].append(
                        for_adv_info.get('content')[i - 1].get('companyIndustry'))
                    position['former advisor' + str(i) + '-since'].append(for_adv_info.get('content')[i - 1].get('startDate'))
                    position['former advisor' + str(i) + '-companylink'].append('https://my.pitchbook.com/profile/' +
                                                                                  for_adv_info.get('content')[
                                                                                      i - 1].get('entity').get('pbId') +
                                                                                  '/company/profile')

                else:
                    position['former advisor' + str(i) + '-firm name'].append(None)
                    position['former advisor' + str(i) + '-firm type'].append(None)
                    position['former advisor' + str(i) + '-title'].append(None)
                    position['former advisor' + str(i) + '-location'].append(None)
                    position['former advisor' + str(i) + '-industry'].append(None)
                    position['former advisor' + str(i) + '-since'].append(None)
                    position['former advisor' + str(i) + '-companylink'].append(None)
    advisor_info = pd.DataFrame.from_dict(position)
    advisor_info.to_csv("for_advisor_info.csv")
print(position)
