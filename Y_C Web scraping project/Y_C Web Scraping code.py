import pandas as pd
from bs4 import BeautifulSoup
from  urllib import request
import urllib
import requests
#from shortened_number import profile_number
import pandas as pd
import time
import json
from fake_useragent import UserAgent
from profile_info import key
ua = UserAgent()
data = {}
a = ['bGxsGDyvn']
cookie = ['_ga=GA1.2.1869520428.1644029943; _sso.key=Z_fuEQOQJM05-JzkGevlgRNlPRQ5h3Pu; _gid=GA1.2.173223410.1645666446; __insp_wid=328108914; __insp_slim=1645685158221; __insp_nv=true; __insp_targlpu=aHR0cHM6Ly93d3cuc3RhcnR1cHNjaG9vbC5vcmcvZGFzaGJvYXJk; __insp_targlpt=RGFzaGJvYXJkIHwgU3RhcnR1cCBTY2hvb2wgLSBUaGUgQmVzdCBSZXNvdXJjZSBmb3IgRm91bmRlcnM=; __insp_norec_sess=true; ph_phc_kqzJJG8aN5nevL0k1oW4Z8iAGswsxBnsWqIBcOuxjah_posthog={"distinct_id":"d69baa29-5a00-46b8-8b24-caeb73c16abf","$device_id":"17ec7d0671adf8-02eebb4c96d41-133f685c-16a7f0-17ec7d0671b1063","$initial_referrer":"https://www.startupschool.org/company/edit","$initial_referring_domain":"www.startupschool.org","$referrer":"https://www.startupschool.org/cofounder-matching","$referring_domain":"www.startupschool.org","$sesid":[1645724954303,"17f2cd9eebfae1-0521a7e1a8175e-37677a09-16a7f0-17f2cd9eec01533"],"$session_recording_enabled_server_side":false,"$user_id":"d69baa29-5a00-46b8-8b24-caeb73c16abf","$active_feature_flags":[],"$enabled_feature_flags":{}}; _sus_session=K1J1VU00R1FsZmJobzdXcXpSMFFpOHFZM0xBQXJYc3ZldzhvWC9LZEZ1SzlQOHNaMEFHNTBpRkp1WVVjVCtpQkx4SmpVWkVBck0zeWRCaGxwekhVQ1NJMklGcmthN01Vd2h0WGs2L0tDM2owc2xCZ2trTnBRbTRaN3hLMnE4YytCdWZPdGdhRC9ML2lTMC83cDRxN0dRPT0tLVBPZDVPT0h4ZGxydzZJck5ZU0daU1E9PQ==--8d3bc10e743b723b894727ffa612b88ed45e98d6']
url = ['https://www.startupschool.org/graphql']
for index, value in enumerate(key[13000:]):
    print(value)
    payload_dict = {
        "operationName": "COFOUNDER_MATCHING_CANDIDATE",
        "variables": {
            "slug": value  # Change this
        },
        "query": "query COFOUNDER_MATCHING_CANDIDATE($slug: ID) {\n  cofounderMatching {\n    invitesRemaining\n    profile {\n      ...CFMViewerProfileFragment\n      slug\n      active\n      email\n      user {\n        slug\n        isWoman\n        __typename\n      }\n      __typename\n    }\n    candidate(slug: $slug) {\n      ...CFMProfileFragment\n      request {\n        slug\n        status\n        message\n        sender {\n          slug\n          user {\n            slug\n            name\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment CFMProfileFragment on CofounderProfile {\n  ...BasicProfileFragment\n  canInviteTrial\n  conversationSlug\n  company {\n    ...BasicCompanyFragment\n    __typename\n  }\n  user {\n    ...BasicUserFragment\n    __typename\n  }\n  __typename\n}\n\nfragment BasicProfileFragment on CofounderProfile {\n  active\n  approvalStatus\n  commitment\n  email\n  emailSettings\n  hasIdea\n  interests\n  intro\n  lastSeenAt\n  other\n  reqFreeText\n  responsibilities\n  slug\n  videoLink\n  ...CofounderPreferenceFragment\n  __typename\n}\n\nfragment CofounderPreferenceFragment on CofounderProfile {\n  cfHasIdea\n  cfHasIdeaImportance\n  cfIsTechnical\n  cfIsTechnicalImportance\n  cfResponsibilities\n  cfResponsibilitiesImportance\n  cfLocation\n  cfLocationImportance\n  cfMinCommitment\n  cfMinCommitmentImportance\n  cfInterestsImportance\n  __typename\n}\n\nfragment BasicCompanyFragment on PublicCompany {\n  description\n  name\n  slug\n  url\n  __typename\n}\n\nfragment BasicUserFragment on User {\n  avatarUrl\n  impressiveThing\n  education\n  employment\n  isTechnical\n  isWoman\n  linkedin\n  location\n  name\n  slug\n  showYcFounder\n  __typename\n}\n\nfragment CFMViewerProfileFragment on CofounderProfile {\n  slug\n  email\n  intro\n  hasIdea\n  responsibilities\n  interests\n  ...CofounderPreferenceFragment\n  cfIsWomanImportance\n  cfIsYcAlumImportance\n  user {\n    slug\n    isTechnical\n    location\n    avatarUrl\n    name\n    __typename\n  }\n  __typename\n}\n"
    }
    #print(payload_dict)
    headers = {
        'Origin': 'https://www.startupschool.org',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'User-Agent': ua.chrome,
        'content-type': 'application/json',
        'accept': '*/*',
        'Referer': 'https://www.startupschool.org/cofounder-matching/candidate/' + value,  # Change this
        'Cookie': cookie[0],
        'x-csrf-token': '5JBVPiqown/+u9lRJld3H+RUmxuD+8/xDxsl05Yo0mYnsMhRQpUIeO+elts5RWhHY3nmIrVmBVH4ahsNtZU97w=='
        # 'Connection': 'keep-alive',
        # 'x-original-url': 'https://www.startupschool.org'
    }
    response = requests.request("POST", url[0], headers=headers, data=json.dumps(payload_dict))
    str_info = response.content.decode()
    #print(str_info)
    if '<!DOCTYPE html>' in str_info:
        if 'education' not in data.keys():
            data['education'] = [None]
        else:
            data['education'].append(None)
        if 'employment' not in data.keys():
            data['employment'] = [None]
        else:
            data['employment'].append(None)
        continue
    dict_info = eval(str_info.replace('null', "'null'", 100).replace('false', "'no'", 100).replace('true', "'yes'", 100))
    #print(dict_info)
    if 'education' not in data.keys():
        if dict_info.get('data') is not None:
            if dict_info.get('data').get('cofounderMatching') is not None:
                if dict_info.get('data').get('cofounderMatching').get('candidate') is not None:
                    if dict_info.get('data').get('cofounderMatching').get('candidate').get('user') is not None:
                        data['education'] = [dict_info.get('data').get('cofounderMatching').get('candidate').get('user').get('education').replace('\n', '||', 100)]
                    else:
                        data['education'] = [None]
                else:
                    data['education'] = [None]
            else:
                data['education'] = [None]
        else:
            data['education'] = [None]
    else:
        if dict_info.get('data') is not None:
            if dict_info.get('data').get('cofounderMatching') is not None:
                if dict_info.get('data').get('cofounderMatching').get('candidate') is not None:
                    if dict_info.get('data').get('cofounderMatching').get('candidate').get('user') is not None:
                        data['education'].append(dict_info.get('data').get('cofounderMatching').get('candidate').get('user').get('education').replace('\n', '||', 100))
                    else:
                        data['education'].append(None)
                else:
                    data['education'].append(None)
            else:
                data['education'].append(None)
        else:
            data['education'].append(None)
    if 'employment' not in data.keys():
        if dict_info.get('data') is not None:
            if dict_info.get('data').get('cofounderMatching') is not None:
                if dict_info.get('data').get('cofounderMatching').get('candidate') is not None:
                    if dict_info.get('data').get('cofounderMatching').get('candidate').get('user') is not None:
                        data['employment'] = [dict_info.get('data').get('cofounderMatching').get('candidate').get('user').get('employment').replace('\n', '||', 100)]
                    else:
                        data['employment'] = [None]
                else:
                    data['employment'] = [None]
            else:
                data['employment'] = [None]
        else:
            data['employment'] = [None]
    else:
        if dict_info.get('data') is not None:
            if dict_info.get('data').get('cofounderMatching') is not None:
                if dict_info.get('data').get('cofounderMatching').get('candidate') is not None:
                    if dict_info.get('data').get('cofounderMatching').get('candidate').get('user') is not None:
                        data['employment'].append(dict_info.get('data').get('cofounderMatching').get('candidate').get('user').get('employment').replace('\n', '||', 100))
                    else:
                        data['employment'].append(None)
                else:
                    data['employment'].append(None)
            else:
                data['employment'].append(None)
        else:
            data['employment'].append(None)
#####
print(data)
data_info = pd.DataFrame.from_dict(data)
print(data_info)

data_info.to_excel("13000-_profiles.xlsx")
