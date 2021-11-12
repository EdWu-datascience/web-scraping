#general information
#'https://my.pitchbook.com/web-api/profiles/'+profile+'/person/general-info'
#concact information
#'https://my.pitchbook.com/web-api/profiles/'+profile+'/person/contact-info'
# current position link
# 'https://my.pitchbook.com/web-api/profiles/'+profile+'/person/positions/current?page=1&pageSize=10'
# former position link
# 'https://my.pitchbook.com/web-api/profiles/'+profile+'/person/positions/former?page=1&pageSize=10'
# current board link
# 'https://my.pitchbook.com/web-api/profiles/'+profile+'/person/board-seats/current?page=1&pageSize=10'
# former board link
# 'https://my.pitchbook.com/web-api/profiles/'+profile+'/person/board-seats/former?page=1&pageSize=10'
#network consist of board member\portfolio member\fund member
#'https://my.pitchbook.com/web-api/profiles/'+profile+'/person/network/fund-team-members?page=1&pageSize=10'
#'https://my.pitchbook.com/web-api/profiles/'+profile+'/person/network/board-members?page=1&pageSize=10'
#'https://my.pitchbook.com/web-api/profiles/'+profile+'/person/network/portfolio-executives?page=1&pageSize=10'
#current advisor role
#'https://my.pitchbook.com/web-api/profiles/'+profile+'/person/advisory-roles/current?page=1&pageSize=10'
#former advisor role
#'https://my.pitchbook.com/web-api/profiles/'+profile+'/person/advisory-roles/former?page=1&pageSize=10'
'''
from test import general_info,contact_info,cur_pos_info,for_pos_info,cur_bor_info,for_bor_info,fund_info,board_info,port_info,cur_adv_info,for_adv_info
print(general_info)
print(contact_info)
print(cur_pos_info)
print(for_pos_info)
print(cur_bor_info)
print(for_bor_info)
print(fund_info)
print(board_info)
print(port_info)
print(cur_adv_info)
print(for_adv_info)
'''
data = {}
position = {}
general_info='{"primaryPosition":"Co-Founder & Head of Technology","primaryPositionActive":true,"primaryEntity":{"pbId":"101216-62","name":"Cursive Labs","type":"COMPANY"},"primaryEntityLinkedInId":"cursive-labs","educationList":[{"degree":"BS (Bachelor of Science)","majorConcentration":"Physics and Mathematics","institute":"University of Mississippi","year":1995}],"gender":"Male","lastUpdateDate":"2021-10-27","biography":"Mr. Josh Schlesser is a Co-Founder and serves as Head of Technology at Cursive Labs. He is also a Co-Founder and serves as Board Member at Spritzr. He serves as the Chief Technology Officer at Spoutable. He drives the creation of Cursives technology and infrastructure. Josh was SVP of Technology at Active Network for 12 years where he architected multiple high volume transaction processing platforms and data management systems, and scaled the R&D team from a handful of people to over 800. He has also been acting CTO and advisor to a variety of startups in the San Diego-area including Sirenas Marine Discovery, Spritzr and Luckybolt. Josh was a particle physicist at Fermi National Accelerator Laboratory and earned his BS in Physics from the University of Mississippi.","isMorningstarPerson":false}'
contact_info='{"firstName":"Josh","lastName":"Schlesser","email":"josh@cursivelabs.com","linkedInLink":"http://www.linkedin.com/in/joshschlesser","primaryOffice":{"name":"San Diego","email":"info@cursivelabs.com","address":["101 West Broadway","San Diego, CA 92101","United States"],"stateCode":"sCA","country":"United States"},"hasLinkedIn":false}'
cur_pos_info='{"content":[{"title":"Co-Founder & Head of Technology","entity":{"pbId":"101216-62","name":"Cursive Labs","type":"COMPANY"},"entityType":"Company","companyIndustry":"Consulting Services (B2B)","location":"San Diego, CA","startDate":"2014-01-01","positionId":1252057},{"title":"Chief Technology Officer","entity":{"pbId":"102485-62","name":"Spoutable","type":"COMPANY"},"entityType":"Company","companyIndustry":"Media and Information Services (B2B)","location":"San Diego, CA","positionId":1993546}],"total":2,"pagination":{"page":1,"pageSize":10},"totalPages":1,"hasNextPage":false,"lastPage":true}'
for_pos_info='{"content":[{"title":"Co-Founder & Board Member","entity":{"pbId":"161275-24","name":"Ponder","type":"COMPANY"},"entityType":"Company","companyIndustry":"Other Software","location":"Los Angeles, CA","startDate":"2013-05-01","positionId":1801538}],"total":1,"pagination":{"page":1,"pageSize":10},"totalPages":1,"hasNextPage":false,"lastPage":true}'
cur_bor_info='{"total":0,"pagination":{"page":1,"pageSize":10},"totalPages":0,"hasNextPage":false,"lastPage":true}'
for_bor_info='{"content":[{"entity":{"pbId":"161275-24","name":"Ponder","type":"COMPANY"},"companyIndustry":"Other Software","companyOwnershipStatus":"Out of Business","companyFinancingStatus":"Formerly VC-backed","location":"Los Angeles, CA","startDate":"2013-05-01","selfRepresenting":false,"positionId":1801538}],"total":1,"pagination":{"page":1,"pageSize":10},"totalPages":1,"hasNextPage":false,"lastPage":true}'
fund_info='{"total":0,"pagination":{"page":1,"pageSize":10},"totalPages":0,"hasNextPage":false,"lastPage":true}'
board_info='{"content":[{"person":{"pbId":"137930-05P","firstName":"Denise","lastName":"Gitsham","contactInfo":{"phone":"+1 (917) 690-7293","hasLinkedIn":false}},"positions":[{"companyInfo":{"pbId":"161275-24","name":"Ponder","type":"COMPANY"},"representedEntity":{"pbId":"161275-24","name":"Ponder","type":"COMPANY"},"companyLocation":"Los Angeles, CA","from":"2015-08-28","selfRepresenting":false}],"positionsCount":1}],"total":1,"pagination":{"page":1,"pageSize":10},"totalPages":1,"hasNextPage":false,"lastPage":true}'
port_info='{"total":0,"pagination":{"page":1,"pageSize":10},"totalPages":0,"hasNextPage":false,"lastPage":true}'
cur_adv_info='{"content":[{"title":"Technical Advisor","entity":{"pbId":"88164-91","name":"Sirenas (Biotechnology)","type":"COMPANY"},"entityType":"Company","companyIndustry":"Biotechnology","location":"San Diego, CA","startDate":"2013-01-01","positionId":1338898}],"total":1,"pagination":{"page":1,"pageSize":10},"totalPages":1,"hasNextPage":false,"lastPage":true}'
for_adv_info='{"total":0,"pagination":{"page":1,"pageSize":10},"totalPages":0,"hasNextPage":false,"lastPage":true}'
general_info = eval(general_info.replace('true','"yes"',10).replace('false','"no"',10))
contact_info = eval(contact_info.replace('true','"yes"',10).replace('false','"no"',10))
cur_pos_info = eval(cur_pos_info.replace('true','"yes"',10).replace('false','"no"',10))
for_pos_info = eval(for_pos_info.replace('true','"yes"',10).replace('false','"no"',10))
cur_bor_info = eval(cur_bor_info.replace('true','"yes"',10).replace('false','"no"',10))
for_bor_info = eval(for_bor_info.replace('true','"yes"',10).replace('false','"no"',10))
fund_info = eval(fund_info.replace('true','"yes"',10).replace('false','"no"',10))
board_info = eval(board_info.replace('true','"yes"',10).replace('false','"no"',10))
port_info = eval(port_info.replace('true','"yes"',10).replace('false','"no"',10))
cur_adv_info = eval(cur_adv_info.replace('true','"yes"',10).replace('false','"no"',10))
for_adv_info = eval(for_adv_info.replace('true','"yes"',10).replace('false','"no"',10))
#print(general_info)
#print(contact_info)
#get first name
if 'firstname' not in data.keys():
    data['firstname'] = [contact_info.get('firstName')]
else:
    data['firstname'].append(contact_info.get('firstName'))
#get last name
if 'lastname' not in data.keys():
    data['lastname'] = [contact_info.get('lastName')]
else:
    data['firstname'].append(contact_info.get('lastName'))
#get biography
if 'biography' not in data.keys():
    data['biography'] = [general_info.get('biography')]
else:
    data['biography'].append(general_info.get('biography'))
#get primary position
if 'primary_position' not in data.keys():
    data['primary_position'] = [general_info.get('primaryPosition')]
else:
    data['primary_position'].append(general_info.get('primaryPosition'))
#get gender
if 'gender' not in data.keys():
    data['gender'] = [general_info.get('gender')]
else:
    data['gender'].append(general_info.get('gender'))
#get education
if 'education' not in data.keys():
    data['education'] = [general_info.get('educationList')]
else:
    data['education'].append(general_info.get('educationList'))
#get email
if 'email' not in data.keys():
    data['email'] = [contact_info.get('email')]
else:
    data['email'].append(contact_info.get('email'))
#get linkedin
if 'linkedin' not in data.keys():
    data['linkedin'] = [contact_info.get('linkedInLink')]
else:
    data['linkedin'].append(contact_info.get('linkedInLink'))
#get address
if 'address' not in data.keys():
    data['address'] = [contact_info.get('primaryOffice').get('address')]
else:
    data['address'].append(contact_info.get('primaryOffice').get('address'))
#get network number#fund_info#board_info#port_info#因为要翻页不知道怎么做
#print(data)



print(cur_pos_info)
if cur_pos_info.get('content') is not None:#如果没有current position的话是不会有content这个key word的
    cur_pos_num = len(cur_pos_info.get('content'))
else:
    cur_pos_num = 0
for i in range(1,11):
    if cur_pos_num == 0:
        if 'current position'+str(i)+'-firm name' not in position:
            position['current position'+str(i)+'-firm name'] = [None]
        else:
            position['current position' + str(i) + '-firm name'].append(None)
        if 'current position'+str(i)+'-firm type' not in position:
            position['current position'+str(i)+'-firm type'] = [None]
        else:
            position['current position' + str(i) + '-firm type'].append(None)
        if 'current position'+str(i)+'-title' not in position:
            position['current position'+str(i)+'-title'] = [None]
        else:
            position['current position'+str(i)+'-title'].append(None)
        if 'current position'+str(i)+'-location' not in position:
            position['current position'+str(i)+'-location'] = [None]
        else:
            position['current position'+str(i)+'-location'].append(None)
        if 'current position'+str(i)+'-industry' not in position:
            position['current position'+str(i)+'-industry'] = [None]
        else:
            position['current position'+str(i)+'-industry'].append(None)
        if 'current position'+str(i)+'-since' not in position:
            position['current position'+str(i)+'since'] = [None]
        else:
            position['current position'+str(i)+'-since'].append(None)
        if 'current position'+str(i)+'-companylink' not in position:
            position['current position'+str(i)+'-companylink'] = [None]
        else:
            position['current position'+str(i)+'-companylink'].append(None)

    else:
        if 'current position'+str(i)+'-firm name' not in position:
            if i <= cur_pos_num:
                position['current position'+str(i)+'-firm name'] = [cur_pos_info.get('content')[i-1].get('entity').get('name')]
                position['current position' + str(i) + '-firm type'] = [cur_pos_info.get('content')[i-1].get('entity').get('type')]
                position['current position' + str(i) + '-title'] = [cur_pos_info.get('content')[i-1].get('title')]
                position['current position'+str(i)+'-location'] = [cur_pos_info.get('content')[i-1].get('location')]
                position['current position'+str(i)+'-industry'] = [cur_pos_info.get('content')[i-1].get('companyIndustry')]
                position['current position'+str(i)+'-since'] = [cur_pos_info.get('content')[i-1].get('startDate')]
                position['current position'+str(i)+'-companylink'] = ['https://my.pitchbook.com/profile/'+
                                                                      cur_pos_info.get('content')[i-1].get('entity').get('pbId')+
                                                                      '/company/profile']
            else:
                position['current position'+str(i)+'-firm name'] = [None]
                position['current position' + str(i) + '-firm type'] = [None]
                position['current position' + str(i) + '-title'] = [None]
                position['current position'+str(i)+'-location'] = [None]
                position['current position'+str(i)+'-industry'] = [None]
                position['current position'+str(i)+'-since'] = [None]
                position['current position'+str(i)+'-companylink'] = [None]
        else:
            if i <= cur_pos_num:
                position['current position'+str(i)+'-firm name'].append(cur_pos_info.get('content')[i-1].get('entity').get('name'))
                position['current position' + str(i) + '-firm type'].append(cur_pos_info.get('content')[i-1].get('entity').get('type'))
                position['current position' + str(i) + '-title'].append(cur_pos_info.get('content')[i-1].get('title'))
                position['current position'+str(i)+'-location'].append(cur_pos_info.get('content')[i-1].get('location'))
                position['current position'+str(i)+'-industry'].append(cur_pos_info.get('content')[i-1].get('companyIndustry'))
                position['current position'+str(i)+'-since'].append(cur_pos_info.get('content')[i-1].get('startDate'))
                position['current position'+str(i)+'-companylink'].append('https://my.pitchbook.com/profile/'+
                                                                      cur_pos_info.get('content')[i-1].get('entity').get('pbId')+
                                                                      '/company/profile')

            else:
                position['current position'+str(i)+'-firm name'].append(None)
                position['current position' + str(i) + '-firm type'].append(None)
                position['current position' + str(i) + '-title'].append(None)
                position['current position'+str(i)+'-location'].append(None)
                position['current position'+str(i)+'-industry'].append(None)
                position['current position'+str(i)+'-since'].append(None)
                position['current position'+str(i)+'-companylink'].append(None)
print(position)



