
from bs4 import BeautifulSoup
from  urllib import request
import requests
from to_delete import profile_number
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
    'Cookie':'_pxvid=f77eea90-3360-11ec-bf08-4f4265746a49; _dy_c_exps=; _dycnst=dg; _dyid=9178336480302660253; _biz_uid=56d920e73c4942569113231cffe64feb; _dy_c_att_exps=; _biz_flagsA={"Version":1,"ViewThrough":"1","XDomain":"1","Frm":"1"}; login-page-user=yaohuw1@uci.edu; place_id=1971da1a-3c5c-44de-9245-080359ae76f5; _gcl_au=1.1.1567555318.1634944567; fpid=421640cdef40c765d1ed7c65f81a677c; _mkto_trk=id:942-MYM-356&token:_mch-pitchbook.com-1634944567541-85538; _fbp=fb.1.1634944567787.200809850; _hjid=1f5cfb9e-2c36-4ff3-aefd-6aa76448b6f5; __adroll_fpc=4c0d4fd77e5894acf027f42dab39f0fd-1634944568372; drift_aid=e2de2001-cce2-400e-98d0-dfc653a18480; driftt_aid=e2de2001-cce2-400e-98d0-dfc653a18480; _dy_geo=US.NA.US_CA.US_CA_Irvine; _dy_df_geo=United States.California.Irvine; marketing_info=true; _uetvid=098dafe0338e11ec9470576b0495a4f0; __ar_v4=SOP5M4HBCJE37JJLCYZ2UJ:20211022:2|2HN5SB32U5B7RKLIF5GUQE:20211021:17|5S2POJ2OE5GPZNGPI6HCQ6:20211021:17|ABSQS3OE7JFQRP56UD4C6C:20211021:10|3LYSOYTQT5G77JYZ2SLG34:20211022:5; _ga_DS3177N6CK=GS1.1.1635022540.2.1.1635027978.44; _ga=GA1.2.182819584.1634925213; _gid=GA1.2.2094934999.1635291609; _pxhd=DuWXfB0RqhsjYc/Vqgcf4Y72qCN9qtZhp13v0jCNWxwyBz64Ah7ZcafrQNk4HI5YIQQTyyI7PNucAOpoofFEWg==:SZ9PjoCUto8/MRS920BN3lpdrpQJupYg-Y587-XKlwXc25yY3fGtJDgy5ix1L2XDogWiARqGNEuleCd7ugyZWb9OtAK63pYL3Wr2dpF9hz0=; sourceType=REFERRAL; _dy_ses_load_seq=38322:1635372677063; _dy_csc_ses=t; _dy_soct=417895.725550.1635372677*595811.1147350.1635372677*372970.622086.1635372677*589540.1135369.1635372677*589535.1135364.1635372677; _biz_sid=8e56fc; _gat=1; _dyjsession=a25cd12188c948a105aeb512d924e7a7; dy_fs_page=my.pitchbook.com/loginaction.do?action=sso&defaultname=; _dy_lu_ses=a25cd12188c948a105aeb512d924e7a7:1635372678306; _dycst=dk.w.c.ss.; _dy_toffset=-1; pxcts=cf6adfd0-3772-11ec-acdb-19a1189d6ea2; _pxff_fp=1; _px3=7b3d27b9633d56bfad7df60e8c31313ae51ebe3589ea7491675e8f24437d7e2d:tuavVzyeK+kV52CQ1qAYa3zAIb/vULKqbbrhyc1DOqH7fu11Xlu2Ien2QBIaehPQpo75hasFRKhIg8nsOKnyog==:1000:sHrQBcUbj39hRMFPxTymi0y6dQ3TTNjrCzs0+1DsnxCupDRVevwjBrnGmAUwX930h6UoXQ7OZJg+g3/PgdNSLBpLgrMCrO2AxzRpenHZEjl73JY23OShiZuP9x49wvVMvu+nJ/H2XM6PuvVxpxi/4HzKvRnAWOdTdGq0hP9BKdh93uXujikoLvr2ImxHYWjRMfFDmS65XYGBFwp5VKLsLA==; _biz_nA=104; _biz_pendingA=[]; sourceUrl=https://shib.service.uci.edu/; SESSION=714c6add-bd58-4196-931f-7c55994d419d'
}
#quote_page = "https://my.pitchbook.com/profile/100009-36P/person/profile"
i = 0
for profile in profile_number[0:100]:
    if i == 1:
        break

    quote_page1 = 'https://my.pitchbook.com/web-api/profiles/'+profile+'/person/general-info'
    quote_page2 = 'https://my.pitchbook.com/web-api/profiles/'+profile+'/person/contact-info'
    general_information = requests.get(quote_page1, headers=headers).text
    contact_information = requests.get(quote_page2, headers=headers).text
    print(general_information)
    print(contact_information)
    i += 1
'''
#quote_page1 = 'https://my.pitchbook.com/web-api/profiles/100012-15P/person/general-info'
#quote_page2 = 'https://my.pitchbook.com/web-api/profiles/100012-15P/person/contact-info'
general_information = requests.get(quote_page1,headers=headers).text
contact_information = requests.get(quote_page2,headers=headers).text
print(general_information)
print(contact_information)

'''

