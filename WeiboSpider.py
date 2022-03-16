import requests
import re
from DecryptLogin import login
from bs4 import BeautifulSoup
from time import sleep


"""模拟登录"""
lg = login.Login()
# user = input('输入微博账号：')
# pwd = input('输入微博密码：')
user = ''
pwd = ''
while True:
    try:
        session = lg.weibo(user, pwd, 'pc')
        break
    except RuntimeError:
        input('账号或者密码错误，请重试')


"""headers设置"""
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
headers['Accept']= 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
headers['Accept-Encoding']='gzip, deflate, br'
headers['Accept-Language']='zh-CN,zh;q=0.9'
headers['Connection']='keep-alive'
#headers['Cookie']='SINAGLOBAL=7126734822140.1589963710877; UM_distinctid=172364e993ca62-03c797a3198fd-d373666-144000-172364e993d3f; UOR=www.baidu.com,weibo.com,www.baidu.com; SCF=AqjP6A_d-ryWDOZq4fL8r2jUz9ZrqMSMaAMmQP5g2BgkgoHUym91QjOSTM-UFuTJQupVOyPCE3JAC0f5CBqYbvs.; SUHB=00x5tRrY_q6S94; ALF=1625587276; SUB=_2AkMoWeWnf8NxqwJRmfkSxGnqZIx-wwDEieKeBRR8JRMxHRl-yT9kqkA5tRB6A9nLSFRYidshnVWG1NiGzz1U9SQ1se-f; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9Whce-UkeChO8n-lKyqKeuPb; login_sid_t=ff181cd886d55c6fcf2eb463d537f42a; cross_origin_proto=SSL; _s_tentry=www.baidu.com; Apache=8991906009407.096.1594947144081; ULV=1594947144088:6:6:1:8991906009407.096.1594947144081:1594197087107; WBStorage=42212210b087ca50|undefined'
headers['Host']='s.weibo.com'
#headers['Referer']='https://s.weibo.com/weibo/%25E5%258C%2597%25E4%25BA%25AC%25E8%25BF%259E%25E7%25BB%25AD11%25E5%25A4%25A9%25E9%259B%25B6%25E6%2596%25B0%25E5%25A2%259E?topnav=1&wvr=6&Refer=top_button'
headers['Sec-Fetch-Dest']='document'
headers['Sec-Fetch-Mode']='navigate'
headers['Sec-Fetch-Site']='same-origin'
headers['Sec-Fetch-User']='?1'
headers['Upgrade-Insecure-Requests']='1'
#headers['X-Requested-With']='XMLHttpRequest'


"""获取个人主页"""
search_url = 'https://s.weibo.com/weibo'
para = {}
para['wvr']='6'
para['q']= input('输入微博用户名：')
para['Refere']='SWeibo_box'
response = requests.get(url=search_url,params=para,headers=headers)
reg = r'<a href="(.*?)" target="_blank" class="wb_url"'
reg = re.compile(reg)
personal = re.findall(reg,response.content.decode('utf8'))
if len(personal) == 0:
    uid = input('未查到该用户，请输入微博用户的uid：')
    personal_url = 'https://weibo.com/u/' + uid
else:
    personal_url = 'https:' + personal[0]
print(session)
Session1 = session[1]
print(personal_url)

"""第二个头设置"""
headers1 = {}
headers1['accept']='text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
headers1['accept-encoding']='gzip, deflate, br'
headers1['accept-language']='zh-CN,zh;q=0.9'
headers1['cache-control']='max-age=0'
headers1['cookie']='SINAGLOBAL=7126734822140.1589963710877; UM_distinctid=172364e993ca62-03c797a3198fd-d373666-144000-172364e993d3f; UOR=www.baidu.com,weibo.com,www.baidu.com; SCF=AqjP6A_d-ryWDOZq4fL8r2jUz9ZrqMSMaAMmQP5g2BgkgoHUym91QjOSTM-UFuTJQupVOyPCE3JAC0f5CBqYbvs.; SUHB=00x5tRrY_q6S94; ALF=1625587276; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9Whce-UkeChO8n-lKyqKeuPb; wb_view_log=1536*8641.25; SUB=_2AkMoTZRhf8NxqwJRmfkSxGnqZIx-wwDEieKeEWW6JRMxHRl-yj92qlcPtRB6A826jnmlqxuYYn_oqYUme4McyFVxgUEB; _s_tentry=-; Apache=961370729484.7896.1594972931804; ULV=1594972931817:7:7:2:961370729484.7896.1594972931804:1594947144088; YF-Page-G0=8438e5756d0e577d90f6ef4db5cfc490|1594972933|1594972931'
headers1['sec-fetch-dest']='document'
headers1['sec-fetch-mode']='navigate'
headers1['sec-fetch-site']='same-origin'
headers1['sec-fetch-user']='?1'
headers1['upgrade-insecure-requests']='1'
headers1['user-agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'


"""正式获取微博用户数据"""
i = 0
while True:
    i += 1
    print('\n\n\n\n--------正在获取第' + str(i) +'页微博---------\n\n\n\n')
    sleep(1)
    param1 = '?is_search=0&visible=0&is_all=1&is_tag=0&profile_ftype=1&page='+ str(i) + '#feedtop'
    personal_url = personal_url + param1
    response = Session1.get(url=personal_url,headers=headers1)
    html = response.content.decode('utf8',errors='ignore')


