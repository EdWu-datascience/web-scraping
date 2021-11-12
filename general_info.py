from bs4 import BeautifulSoup
from  urllib import request
import requests
from profile_number import profile_number
import pandas as pd
import time
from fake_useragent import UserAgent
j = 0
data = {}
ua = UserAgent()
for profile in profile_number:
    j += 1
    print(j)
    headers = {
            'User-Agent':ua.chrome,
            'Cookie': '_pxvid=f77eea90-3360-11ec-bf08-4f4265746a49; _dy_c_exps=; _dycnst=dg; _dyid=9178336480302660253; _biz_uid=56d920e73c4942569113231cffe64feb; _dy_c_att_exps=; _biz_flagsA={"Version":1,"ViewThrough":"1","XDomain":"1","Frm":"1"}; login-page-user=yaohuw1@uci.edu; place_id=1971da1a-3c5c-44de-9245-080359ae76f5; _gcl_au=1.1.1567555318.1634944567; fpid=421640cdef40c765d1ed7c65f81a677c; _mkto_trk=id:942-MYM-356&token:_mch-pitchbook.com-1634944567541-85538; _fbp=fb.1.1634944567787.200809850; _hjid=1f5cfb9e-2c36-4ff3-aefd-6aa76448b6f5; __adroll_fpc=4c0d4fd77e5894acf027f42dab39f0fd-1634944568372; drift_aid=e2de2001-cce2-400e-98d0-dfc653a18480; driftt_aid=e2de2001-cce2-400e-98d0-dfc653a18480; _dy_geo=US.NA.US_CA.US_CA_Irvine; _dy_df_geo=United States.California.Irvine; marketing_info=true; _uetvid=098dafe0338e11ec9470576b0495a4f0; __ar_v4=SOP5M4HBCJE37JJLCYZ2UJ:20211022:2|2HN5SB32U5B7RKLIF5GUQE:20211021:17|5S2POJ2OE5GPZNGPI6HCQ6:20211021:17|ABSQS3OE7JFQRP56UD4C6C:20211021:10|3LYSOYTQT5G77JYZ2SLG34:20211022:5; _ga_DS3177N6CK=GS1.1.1635022540.2.1.1635027978.44; _ga=GA1.2.182819584.1634925213; _dycst=dk.w.c.ws.; _pxhd=bTvG-McuarzEoAanngQsP1C7x4osMppP0rzKhZSzItrrDe8HZUTxHRUhJijWI2-EuvHN9QRjinn-q1srMM77nw==:fw9M6zzPW7p1dNlLSDA8lHCEogVO9EqTxwWrt56SFlYYonOPUzh5a2BpX896V1TQlAoKlaSCzoBY4PJTM7OCMABbOK-qz-6Xwe-5VCmxrFc=; pxcts=9d3efce0-43e7-11ec-b537-f142798b25dc; _dy_csc_ses=t; _biz_sid=6b8b15; _gid=GA1.2.438673417.1636742260; _gat=1; _dyjsession=b268782a9a74af15afd2b24427bd3eff; dy_fs_page=my.pitchbook.com/loginaction.do?action=login; _dy_toffset=0; _pxff_fp=1; _dy_ses_load_seq=52673:1636742264992; _dy_soct=417895.725550.1636742259*595811.1147350.1636742265*372970.622086.1636742265*589540.1135369.1636742265*589535.1135364.1636742265; _dy_lu_ses=b268782a9a74af15afd2b24427bd3eff:1636742265397; _biz_nA=131; _biz_pendingA=[]; sourceType=REFERRAL; sourceUrl=https://shib.service.uci.edu/; SESSION=74584fd1-6e03-4ecb-b06e-3938dbd0296c; _px3=9a36dd337319f581210252ecf36e773f11e9eb25cd23621bdef3392af4416dc0:QC5gdW6QPy8KXNVNMvOcASKzPIjtdFKWfI2LBXmiL4E00vVesdMbYhgEmlotfXfHrX6UA8fc+tzFgsTJMaUAtA==:1000:zxq2UZ9EpvfE4jVITtNFfKzz+RNWubhAdXt//faxraRvhJ601CKXZYrh4oTytxxuRCDEnlImL2H5l7I3dGYhSZfakm8wB7rl+egVOlPunpdWXA4rg6y518IBowmlpCwq/zTN7viz9lVTIVAaDXi7u4pJlaG40POP0vMZgJhmW6teJF8pi6swDB2003LWwF4P2YYTI7xD2JQOT6aZWg128A==; fs_uid=rs.fullstory.com#CMR2P#4984310359498752:5752591408930816#6b6f7dc3#/1666461451'
    }
    general_info = requests.get('https://my.pitchbook.com/web-api/profiles/'+profile+'/person/general-info', headers=headers).text#1
    contact_info = requests.get('https://my.pitchbook.com/web-api/profiles/'+profile+'/person/contact-info', headers=headers).text#2
    if '<!doctype html>' in general_info or '<!doctype html>' in contact_info:
        time.sleep(35)
        headers = {
            'User-Agent':ua.chrome,
            'Cookie':'_pxvid=f77eea90-3360-11ec-bf08-4f4265746a49; _dy_c_exps=; _dycnst=dg; _dyid=9178336480302660253; _biz_uid=56d920e73c4942569113231cffe64feb; _dy_c_att_exps=; _biz_flagsA={"Version":1,"ViewThrough":"1","XDomain":"1","Frm":"1"}; login-page-user=yaohuw1@uci.edu; place_id=1971da1a-3c5c-44de-9245-080359ae76f5; _gcl_au=1.1.1567555318.1634944567; fpid=421640cdef40c765d1ed7c65f81a677c; _mkto_trk=id:942-MYM-356&token:_mch-pitchbook.com-1634944567541-85538; _fbp=fb.1.1634944567787.200809850; _hjid=1f5cfb9e-2c36-4ff3-aefd-6aa76448b6f5; __adroll_fpc=4c0d4fd77e5894acf027f42dab39f0fd-1634944568372; drift_aid=e2de2001-cce2-400e-98d0-dfc653a18480; driftt_aid=e2de2001-cce2-400e-98d0-dfc653a18480; _dy_geo=US.NA.US_CA.US_CA_Irvine; _dy_df_geo=United States.California.Irvine; marketing_info=true; _uetvid=098dafe0338e11ec9470576b0495a4f0; __ar_v4=SOP5M4HBCJE37JJLCYZ2UJ:20211022:2|2HN5SB32U5B7RKLIF5GUQE:20211021:17|5S2POJ2OE5GPZNGPI6HCQ6:20211021:17|ABSQS3OE7JFQRP56UD4C6C:20211021:10|3LYSOYTQT5G77JYZ2SLG34:20211022:5; _ga_DS3177N6CK=GS1.1.1635022540.2.1.1635027978.44; _ga=GA1.2.182819584.1634925213; _dycst=dk.w.c.ws.; _pxhd=bTvG-McuarzEoAanngQsP1C7x4osMppP0rzKhZSzItrrDe8HZUTxHRUhJijWI2-EuvHN9QRjinn-q1srMM77nw==:fw9M6zzPW7p1dNlLSDA8lHCEogVO9EqTxwWrt56SFlYYonOPUzh5a2BpX896V1TQlAoKlaSCzoBY4PJTM7OCMABbOK-qz-6Xwe-5VCmxrFc=; pxcts=9d3efce0-43e7-11ec-b537-f142798b25dc; _dy_csc_ses=t; _biz_sid=6b8b15; _gid=GA1.2.438673417.1636742260; _gat=1; _dyjsession=b268782a9a74af15afd2b24427bd3eff; dy_fs_page=my.pitchbook.com/loginaction.do?action=login; _dy_toffset=0; _pxff_fp=1; _dy_ses_load_seq=52673:1636742264992; _dy_soct=417895.725550.1636742259*595811.1147350.1636742265*372970.622086.1636742265*589540.1135369.1636742265*589535.1135364.1636742265; _dy_lu_ses=b268782a9a74af15afd2b24427bd3eff:1636742265397; _biz_nA=131; _biz_pendingA=[]; sourceType=REFERRAL; sourceUrl=https://shib.service.uci.edu/; SESSION=74584fd1-6e03-4ecb-b06e-3938dbd0296c; _px3=9a36dd337319f581210252ecf36e773f11e9eb25cd23621bdef3392af4416dc0:QC5gdW6QPy8KXNVNMvOcASKzPIjtdFKWfI2LBXmiL4E00vVesdMbYhgEmlotfXfHrX6UA8fc+tzFgsTJMaUAtA==:1000:zxq2UZ9EpvfE4jVITtNFfKzz+RNWubhAdXt//faxraRvhJ601CKXZYrh4oTytxxuRCDEnlImL2H5l7I3dGYhSZfakm8wB7rl+egVOlPunpdWXA4rg6y518IBowmlpCwq/zTN7viz9lVTIVAaDXi7u4pJlaG40POP0vMZgJhmW6teJF8pi6swDB2003LWwF4P2YYTI7xD2JQOT6aZWg128A==; fs_uid=rs.fullstory.com#CMR2P#4984310359498752:5752591408930816#6b6f7dc3#/1666461451'
        }
        general_info = requests.get('https://my.pitchbook.com/web-api/profiles/' + profile + '/person/general-info',headers=headers).text  # 1
        contact_info = requests.get('https://my.pitchbook.com/web-api/profiles/' + profile + '/person/contact-info',headers=headers).text  # 2
    print(general_info)
    print(contact_info)
    general_info = eval(general_info.replace('true', "'yes'", 100).replace('false', "'no'", 100))
    contact_info = eval(contact_info.replace('true', "'yes'", 100).replace('false', "'no'", 100))
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





