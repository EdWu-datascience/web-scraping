from bs4 import BeautifulSoup
from  urllib import request
import requests
from shortened_number import profile_number
import pandas as pd
import time
from fake_useragent import UserAgent
j = 0
data = {}
cookie=['your cookie here']
ua = UserAgent()

profile_number = profile_number[9499:9500]
#linqi 8750-9000
#9500从9499开始 9250-9500 差9499 index的value
#差5500-5750
for profile in profile_number:
    print(profile)
    j += 1
    print(j)
    headers = {
            'User-Agent':ua.chrome,
            'Cookie':cookie[0]
    }
    general_info = requests.get('https://my.pitchbook.com/web-api/profiles/'+profile+'/person/general-info', headers=headers).text#1
    contact_info = requests.get('https://my.pitchbook.com/web-api/profiles/'+profile+'/person/contact-info', headers=headers).text#2
    if '<!doctype html>' in general_info or '<!doctype html>' in contact_info:
        time.sleep(35)
        headers = {
            'User-Agent':ua.chrome,
            'Cookie':cookie[0]
        }
        general_info = requests.get('https://my.pitchbook.com/web-api/profiles/' + profile + '/person/general-info',headers=headers).text  # 1
        contact_info = requests.get('https://my.pitchbook.com/web-api/profiles/' + profile + '/person/contact-info',headers=headers).text  # 2
    print(general_info)
    print(contact_info)
    general_info = eval(general_info.replace('true', "'yes'", 100).replace('false', "'no'", 100))
    contact_info = eval(contact_info.replace('true', "'yes'", 100).replace('false', "'no'", 100).replace('\\','/',100))
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

j = 0
position = {}
ua = UserAgent()
for profile in profile_number:
    j += 1
    print(j)
    headers = {
            'User-Agent':ua.chrome,
            'Cookie': cookie[0]
    }
    cur_pos_info = requests.get('https://my.pitchbook.com/web-api/profiles/'+profile+
                                '/person/positions/current?page=1&pageSize=10', headers=headers).text#3
    print(cur_pos_info)
    if '<!doctype html>' in cur_pos_info:
        time.sleep(35)
        headers = {
            'User-Agent':ua.chrome,
            'Cookie': cookie[0]
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

j = 0
position = {}
ua = UserAgent()
for profile in profile_number:
    j += 1
    print(j)
    headers = {
            'User-Agent':ua.chrome,
            'Cookie': cookie[0]
    }
    for_pos_info = requests.get('https://my.pitchbook.com/web-api/profiles/' + profile +
                                '/person/positions/former?page=1&pageSize=10', headers=headers).text  # 4
    print(for_pos_info)
    if '<!doctype html>' in for_pos_info:
        time.sleep(35)
        headers = {
            'User-Agent':ua.chrome,
            'Cookie':cookie[0]
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
            if 'former position' + str(i) + '-until' not in position:
                position['former position' + str(i) + '-until'] = [None]
            else:
                position['former position' + str(i) + '-until'].append(None)
            if 'former position' + str(i) + '-companylink' not in position:
                position['former position' + str(i) + '-companylink'] = [None]
            else:
                position['former position' + str(i) + '-companylink'].append(None)


        else:
            if 'former position' + str(i) + '-firm name' not in position:
                if i  <= for_pos_num:
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
                    position['former position' + str(i) + '-until'] = [
                        for_pos_info.get('content')[i - 1].get('endDate')]
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
                    position['former position' + str(i) + '-until'] = [None]
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
                    position['former position' + str(i) + '-until'].append(for_pos_info.get('content')[i - 1].get('endDate'))
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
                    position['former position' + str(i) + '-until'].append(None)
                    position['former position' + str(i) + '-companylink'].append(None)
for_position_info = pd.DataFrame.from_dict(position)
for_position_info.to_csv("for_position_info.csv")
#print(position)

j = 0
position = {}
ua = UserAgent()
for profile in profile_number:
    j += 1
    print(j)
    headers = {
            'User-Agent':ua.chrome,
            'Cookie':cookie[0]
    }
    cur_bor_info = requests.get('https://my.pitchbook.com/web-api/profiles/' + profile +
                                    '/person/board-seats/current?page=1&pageSize=10', headers=headers).text  # 5 结果是none
    print(cur_bor_info)
    if '<!doctype html>' in cur_bor_info:
        time.sleep(35)
        headers = {
            'User-Agent':ua.chrome,
            'Cookie':cookie[0]
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
                    if cur_bor_info.get('content')[i - 1].get('entity').get('pbId') is not None:
                        position['current board' + str(i) + '-companylink'] = ['https://my.pitchbook.com/profile/' +
                                                                              cur_bor_info.get('content')[i - 1].get(
                                                                                  'entity').get('pbId') +
                                                                              '/company/profile']
                    else:
                        position['current board' + str(i) + '-companylink'] =[None]
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
                    if cur_bor_info.get('content')[i - 1].get('entity').get('pbId') is not None:
                        position['current board' + str(i) + '-companylink'].append('https://my.pitchbook.com/profile/' +
                                                                                  cur_bor_info.get('content')[
                                                                                      i - 1].get('entity').get('pbId') +
                                                                                  '/company/profile')
                    else:
                        position['current board' + str(i) + '-companylink'].append(None)


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
#print(position)

j = 0
position = {}
ua = UserAgent()
for profile in profile_number:
    j += 1
    print(j)
    headers = {
            'User-Agent':ua.chrome,
            'Cookie': cookie[0]
    }
    for_bor_info = requests.get('https://my.pitchbook.com/web-api/profiles/'+profile+
                                '/person/board-seats/former?page=1&pageSize=10', headers=headers).text#6
    print(for_bor_info)
    if '<!doctype html>' in for_bor_info:
        time.sleep(35)
        headers = {
            'User-Agent':ua.chrome,
            'Cookie':cookie[0]
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
            if 'former board' + str(i) + '-until' not in position:
                position['former board' + str(i) + '-until'] = [None]
            else:
                position['former board' + str(i) + '-until'].append(None)
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
                    position['former board' + str(i) + '-until'] = [
                        for_bor_info.get('content')[i - 1].get('endDate')]
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
                    position['former board' + str(i) + '-until'] = [None]
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
                    position['former board' + str(i) + '-until'].append(for_bor_info.get('content')[i - 1].get('endDate'))
                    if for_bor_info.get('content')[i - 1].get('entity').get('pbId') is not None:
                        position['former board' + str(i) + '-companylink'].append('https://my.pitchbook.com/profile/' +
                                                                                  for_bor_info.get('content')[
                                                                                      i - 1].get('entity').get('pbId') +
                                                                                  '/company/profile')
                    else:
                        position['former board' + str(i) + '-companylink'].append(None)


                else:
                    position['former board' + str(i) + '-firm name'].append(None)
                    position['former board' + str(i) + '-firm type'].append(None)
                    position['former board' + str(i) + '-title'].append(None)
                    position['former board' + str(i) + '-location'].append(None)
                    position['former board' + str(i) + '-industry'].append(None)
                    position['former board' + str(i) + '-since'].append(None)
                    position['former board' + str(i) + '-until'].append(None)
                    position['former board' + str(i) + '-companylink'].append(None)
for_board_info = pd.DataFrame.from_dict(position)
for_board_info.to_csv("for_board_info.csv")

#print(position)
j = 0
position = {}
ua = UserAgent()
for profile in profile_number:
    j += 1
    print(j)
    headers = {
            'User-Agent':ua.chrome,
            'Cookie':cookie[0]
    }
    cur_adv_info = requests.get('https://my.pitchbook.com/web-api/profiles/'+profile+
                                '/person/advisory-roles/current?page=1&pageSize=10',headers=headers).text
    print(cur_adv_info)
    if '<!doctype html>' in cur_adv_info:
        time.sleep(35)
        headers = {
            'User-Agent':ua.chrome,
            'Cookie':cookie[0]
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
#print(position)

j = 0
position = {}
ua = UserAgent()
for profile in profile_number:
    j += 1
    print(j)
    headers = {
            'User-Agent':ua.chrome,
            'Cookie':cookie[0]
    }
    for_adv_info = requests.get('https://my.pitchbook.com/web-api/profiles/'+profile+
                                '/person/advisory-roles/former?page=1&pageSize=10', headers=headers).text

    print(for_adv_info)
    if '<!doctype html>' in for_adv_info:
        time.sleep(35)
        headers = {
            'User-Agent':ua.chrome,
            'Cookie': cookie[0]
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
            if 'former advisor' + str(i) + '-until' not in position:
                position['former advisor' + str(i) + '-until'] = [None]
            else:
                position['former advisor' + str(i) + '-until'].append(None)
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
                    position['former advisor' + str(i) + '-until'] = [
                        for_adv_info.get('content')[i - 1].get('endDate')]
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
                    position['former advisor' + str(i) + '-until'] = [None]
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
                    position['former advisor' + str(i) + '-until'].append(for_adv_info.get('content')[i - 1].get('endDate'))
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
                    position['former advisor' + str(i) + '-until'].append(None)
                    position['former advisor' + str(i) + '-companylink'].append(None)
for_advisor_info = pd.DataFrame.from_dict(position)
for_advisor_info.to_csv("for_advisor_info.csv")
total_data = pd.concat([data_info,position_info,for_position_info,board_info,for_board_info,advisor_info,for_advisor_info],axis=1)
total_data.to_csv('total_data.csv')

