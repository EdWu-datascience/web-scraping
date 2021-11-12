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
            'Cookie': '_pxvid=f77eea90-3360-11ec-bf08-4f4265746a49; _dy_c_exps=; _dycnst=dg; _dyid=9178336480302660253; _biz_uid=56d920e73c4942569113231cffe64feb; _dy_c_att_exps=; _biz_flagsA={"Version":1,"ViewThrough":"1","XDomain":"1","Frm":"1"}; login-page-user=yaohuw1@uci.edu; place_id=1971da1a-3c5c-44de-9245-080359ae76f5; _gcl_au=1.1.1567555318.1634944567; fpid=421640cdef40c765d1ed7c65f81a677c; _mkto_trk=id:942-MYM-356&token:_mch-pitchbook.com-1634944567541-85538; _fbp=fb.1.1634944567787.200809850; _hjid=1f5cfb9e-2c36-4ff3-aefd-6aa76448b6f5; __adroll_fpc=4c0d4fd77e5894acf027f42dab39f0fd-1634944568372; drift_aid=e2de2001-cce2-400e-98d0-dfc653a18480; driftt_aid=e2de2001-cce2-400e-98d0-dfc653a18480; _dy_geo=US.NA.US_CA.US_CA_Irvine; _dy_df_geo=United States.California.Irvine; marketing_info=true; _uetvid=098dafe0338e11ec9470576b0495a4f0; __ar_v4=SOP5M4HBCJE37JJLCYZ2UJ:20211022:2|2HN5SB32U5B7RKLIF5GUQE:20211021:17|5S2POJ2OE5GPZNGPI6HCQ6:20211021:17|ABSQS3OE7JFQRP56UD4C6C:20211021:10|3LYSOYTQT5G77JYZ2SLG34:20211022:5; _ga_DS3177N6CK=GS1.1.1635022540.2.1.1635027978.44; _ga=GA1.2.182819584.1634925213; _dycst=dk.w.c.ws.; fs_uid=rs.fullstory.com#CMR2P#4984310359498752:4575762336423936#6b6f7dc3#/1666461451; _pxhd=bTvG-McuarzEoAanngQsP1C7x4osMppP0rzKhZSzItrrDe8HZUTxHRUhJijWI2-EuvHN9QRjinn-q1srMM77nw==:fw9M6zzPW7p1dNlLSDA8lHCEogVO9EqTxwWrt56SFlYYonOPUzh5a2BpX896V1TQlAoKlaSCzoBY4PJTM7OCMABbOK-qz-6Xwe-5VCmxrFc=; _gid=GA1.2.1488743850.1636220153; _dy_toffset=0; pxcts=f0132020-3ff7-11ec-b410-47deca8d0004; _dy_csc_ses=t; _dyjsession=dad59752e083cf57aa2b144e3cc6d28e; dy_fs_page=my.pitchbook.com/loginaction.do?action=login; _dy_ses_load_seq=31810:1636309507810; _dy_soct=417895.725550.1636309466*595811.1147350.1636309507*372970.622086.1636309507*589540.1135369.1636309507*589535.1135364.1636309507; _dy_lu_ses=dad59752e083cf57aa2b144e3cc6d28e:1636309508182; _biz_nA=125; _biz_pendingA=[]; SESSION=69929fab-7431-4cd8-ad92-b5894562c017; sourceType=DIRECT; sourceUrl=; _px3=445d0ce7dd6c3972ca7cc33215edb029294af63b9f0ee7d8fe243b6baa66eb9d:YjWbEAE9TQ94bWzMso8ZCSRl6iW3P5vb7R9WO7Y2zZtcZTP/04XQTsGZfE/MrIqYrOybAqMGsCVFm6ybCbP+fg==:1000:Whyfh6tTaZ+jaCkkNTMoVUbxKOXjF5XN8tu1rBDlWNQu0FUazHCAxeUSc64J3srhNPqT/F1kNRQjhPBSg1T7PVt20Kj8EiJnSDLPpWHyrP4w4u/xGb1h+suvRHjk1ix8d/WD3/Ya2gKviDMTCBaGQrVsEPqBZ4b1mK7E90Gk7FNC40199ty8DY2OstEsE11gcXe3bNlFGlFxddG9QgvV9A=='
        }
    for_bor_info = requests.get('https://my.pitchbook.com/web-api/profiles/'+profile+
                                '/person/board-seats/former?page=1&pageSize=10', headers=headers).text#6
    print(for_bor_info)
    if '<!doctype html>' in for_bor_info:
        time.sleep(35)
        headers = {
            'User-Agent':ua.chrome,
            'Cookie': '_pxvid=f77eea90-3360-11ec-bf08-4f4265746a49; _dy_c_exps=; _dycnst=dg; _dyid=9178336480302660253; _biz_uid=56d920e73c4942569113231cffe64feb; _dy_c_att_exps=; _biz_flagsA={"Version":1,"ViewThrough":"1","XDomain":"1","Frm":"1"}; login-page-user=yaohuw1@uci.edu; place_id=1971da1a-3c5c-44de-9245-080359ae76f5; _gcl_au=1.1.1567555318.1634944567; fpid=421640cdef40c765d1ed7c65f81a677c; _mkto_trk=id:942-MYM-356&token:_mch-pitchbook.com-1634944567541-85538; _fbp=fb.1.1634944567787.200809850; _hjid=1f5cfb9e-2c36-4ff3-aefd-6aa76448b6f5; __adroll_fpc=4c0d4fd77e5894acf027f42dab39f0fd-1634944568372; drift_aid=e2de2001-cce2-400e-98d0-dfc653a18480; driftt_aid=e2de2001-cce2-400e-98d0-dfc653a18480; _dy_geo=US.NA.US_CA.US_CA_Irvine; _dy_df_geo=United States.California.Irvine; marketing_info=true; _uetvid=098dafe0338e11ec9470576b0495a4f0; __ar_v4=SOP5M4HBCJE37JJLCYZ2UJ:20211022:2|2HN5SB32U5B7RKLIF5GUQE:20211021:17|5S2POJ2OE5GPZNGPI6HCQ6:20211021:17|ABSQS3OE7JFQRP56UD4C6C:20211021:10|3LYSOYTQT5G77JYZ2SLG34:20211022:5; _ga_DS3177N6CK=GS1.1.1635022540.2.1.1635027978.44; _ga=GA1.2.182819584.1634925213; _dycst=dk.w.c.ws.; fs_uid=rs.fullstory.com#CMR2P#4984310359498752:4575762336423936#6b6f7dc3#/1666461451; _pxhd=bTvG-McuarzEoAanngQsP1C7x4osMppP0rzKhZSzItrrDe8HZUTxHRUhJijWI2-EuvHN9QRjinn-q1srMM77nw==:fw9M6zzPW7p1dNlLSDA8lHCEogVO9EqTxwWrt56SFlYYonOPUzh5a2BpX896V1TQlAoKlaSCzoBY4PJTM7OCMABbOK-qz-6Xwe-5VCmxrFc=; _gid=GA1.2.1488743850.1636220153; _dy_toffset=0; pxcts=f0132020-3ff7-11ec-b410-47deca8d0004; _dy_csc_ses=t; _dyjsession=dad59752e083cf57aa2b144e3cc6d28e; dy_fs_page=my.pitchbook.com/loginaction.do?action=login; _dy_ses_load_seq=31810:1636309507810; _dy_soct=417895.725550.1636309466*595811.1147350.1636309507*372970.622086.1636309507*589540.1135369.1636309507*589535.1135364.1636309507; _dy_lu_ses=dad59752e083cf57aa2b144e3cc6d28e:1636309508182; _biz_nA=125; _biz_pendingA=[]; SESSION=69929fab-7431-4cd8-ad92-b5894562c017; sourceType=DIRECT; sourceUrl=; _px3=445d0ce7dd6c3972ca7cc33215edb029294af63b9f0ee7d8fe243b6baa66eb9d:YjWbEAE9TQ94bWzMso8ZCSRl6iW3P5vb7R9WO7Y2zZtcZTP/04XQTsGZfE/MrIqYrOybAqMGsCVFm6ybCbP+fg==:1000:Whyfh6tTaZ+jaCkkNTMoVUbxKOXjF5XN8tu1rBDlWNQu0FUazHCAxeUSc64J3srhNPqT/F1kNRQjhPBSg1T7PVt20Kj8EiJnSDLPpWHyrP4w4u/xGb1h+suvRHjk1ix8d/WD3/Ya2gKviDMTCBaGQrVsEPqBZ4b1mK7E90Gk7FNC40199ty8DY2OstEsE11gcXe3bNlFGlFxddG9QgvV9A=='
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