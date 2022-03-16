import requests
from time import sleep
from bs4 import BeautifulSoup
from random import choice

header = {}
header['user-agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
header1 = {}
header1['accept']='text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
#header1['accept-encoding']='gzip, deflate, br'
header1['accept-language']='zh-CN,zh;q=0.9'
header1['cache-control']='max-age=0'
#header1['cookie']='_xsrf=DoAN0WTOuQ7G2yas4YY4kDdgQwNUIZeu; _zap=879a350a-b309-40c5-8756-411e12d29131; d_c0="AGCelyUgShGPTiIrHNrp4mPPrrSNImRk4fw=|1589812259"; _ga=GA1.2.1353073019.1589812259; __utmz=51854390.1590151541.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/question/264793150; tst=r; __utma=51854390.1353073019.1589812259.1590151541.1591537573.2; __utmv=51854390.100--|2=registration_date=20160716=1^3=entry_date=20160716=1; q_c1=c569ee8f017e4370b98a77c0429146aa|1593571416000|1590151542000; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1596452640,1596453352,1597153135,1598534824; _gid=GA1.2.627266046.1598534824; capsion_ticket="2|1:0|10:1598535485|14:capsion_ticket|44:MGM3YzQ0NmM0YjI0NGUzNmFhMzU1Mjc5Y2RhNDRmMTA=|00b901ec8613e4ad8011d0b2c485250f4064d511128bd8bfb1f8716c1b91e61a"; SESSIONID=YsxzGMP9jWgV9qemC3Ou4W6KOiBtYH4iiCQtIVUg2fT; JOID=UVwQC00eAd7AXjMPTxUDySio9JZYQHOrtBx5XntxUbibaUdtIya6mpRcNQNMB2HJubuilcXau7Fklvb2sj-tieI=; osd=VFkTBkwbBN3NXzYKTBgCzC2r-ZddRXCmtRl8XXZwVL2YZEZoJiW3m5FZNg5NAmTKtLqnkMbXurRhlfv3tzquhOM=; z_c0="2|1:0|10:1598535504|4:z_c0|92:Mi4xc3ZkQUF3QUFBQUFBWUo2WEpTQktFU1lBQUFCZ0FsVk5VQVUxWUFCa2hjLXJOZWhZYnY0NjltRnRmbDBrWnVCb2ZR|9567c499b9d75743aaea0065d84e28ea9792b6dc8a73d4d638fb5beaf5339212"; unlock_ticket="AECAWDTVPAomAAAAYAJVTVi-R1-j8Mgyn4f5El-rbbglowp3LEw2lg=="; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1598535703; KLBRSID=d6f775bb0765885473b0cba3a5fa9c12|1598535835|1598534820'
header1['sec-fetch-dest']='document'
header1['sec-fetch-mode']='navigate'
header1['sec-fetch-site']='same-origin'
header1['sec-fetch-user']='?1'
header1['upgrade-insecure-requests']='1'
#header1['user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36

#随机选取ua
h1 = []
h1.append('Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60')
h1.append('Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0')
h1.append('Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36')
h1.append('Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER')
h1.append('Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0')
h1.append('Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5')
h1.append('Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5')
h1.append('Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+')
h1.append('Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 UBrowser/4.0.3214.0 Safari/537.36')
h1.append('Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11')
h1.append('Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)')
h1.append('Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5')
h1.append('Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0')

#处理位统一的网址
def url_transform(url):
    if 'answer' in url or 'ANSWER' in url or 'Answer' in url:
        i,j = 0,0
        for url1 in url:
            if url1 == 'a' or url1 =='n' or url1 =='s' or url1 =='w' or url1 =='e' or url1 =='r' or url1 =='A' or url1 =='N' or url1 =='S' or url1 == 'W' or url1=='E' or url1=='R' :
                i += 1
            else:
                if i >=5:
                    return url[0:j-1]
                if i == 0:
                    j += 1
                else:
                    j += i + 1
                i = 0
    return url


#直接得到知乎API接口
def url_add_api(url):
    a = url.split('/')
    j = 0
    url1 = ''
    length = len(a)
    i = 0
    for a1 in a:
        i += 1
        if 'zhihu' in a1 or 'question' in a1:
            j += 1
        if j == 0:
            if 'https' in a1:
                url1 = url1 + a1 + '/'
            else:
                if i != length:
                    url1 = url1 + a1 + '/'
                else:
                    url1 = url1 + a1
        elif j == 1:
            url1 = url1 + a1 + '/api/v4' + '/'
            j = 0
    url1 = url1.replace('question/', 'questions/').replace('/questions/api/v4/','/questions/')
    return url1 + '/answers'

#通过API爬取知乎
def zhihu_spider(url,path,header1,h1):
    para = {}
    para1 = {}
    para['include'] = 'data[*].is_normal,admin_closed_comment,reward_info,is_collapsed,annotation_action,annotation_detail,collapse_reason,is_sticky,collapsed_by,suggest_edit,comment_count,can_comment,content,editable_content,voteup_count,reshipment_settings,comment_permission,created_time,updated_time,review_info,relevant_info,question,excerpt,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp,is_labeled,is_recognized,paid_info,paid_info_content;data[*].mark_infos[*].url;data[*].author.follower_count,badge[*].topics'
    para1['include'] = para['include'].replace('[*]', '%5B%2A%5D')
    para['offset'] = '0'
    para['limit'] = '5'
    para['sort_by'] = 'default'
    para['platform'] = 'desktop'
    url1 = url + '?' + 'include=' + para1['include'] + '&' + 'offset=' + para['offset'] + '&' + 'limit' + para['limit'] + '&' + 'sort_by' + '=' + para['sort_by'] + '&' + 'platform' + '=' + para['platform']
    print(url1)
    header = {}
    header['user-agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
    header1['User-Agent'] = choice(h1)
    response = requests.get(url=url1,headers=header1).text
    response = response.replace('true','\'true\'').replace('false','\'false\'').replace('null','\'null\'')

    response = eval(response)
    totals = response['paging']['totals']
    title = response['data'][0]['question']['title']
    print(title)
    j = 0
    xx = 0
    if len(path) == 0:
        f = open(str(totals) + '个回答_' +title.replace('\\','').replace('?','').replace('？','') + '.txt','w',encoding='utf8',errors='ignore')
    else:
        f = open(path + '\\' + str(totals) + '个回答_' +title + '.txt','w',encoding='utf8',errors='ignore')

    for i in range(0,totals):
        if j % 5 == 0 and j != 0:
            para['offset'] = eval(para['offset'])
            para['offset'] += 5
            para['offset'] = str(para['offset'])
            url1 = ''
            url1 = url + '?' + 'include=' + para1['include'] + '&' + 'offset=' + para['offset'] + '&' + 'limit' + para['limit'] + '&' + 'sort_by' + '=' + para['sort_by'] + '&' + 'platform' + '=' + para['platform']
        sleep(0.3)
        try:
            header1['User-Agent'] = choice(h1)
            response = requests.get(url=url1, headers=header1,timeout=3).content.decode('utf8')
        except:
            print('\n-----获取超时，睡眠中，10秒后自动重启------')
            sleep(10)
            response = requests.get(url=url1, headers=header1,timeout=3).content.decode('utf8','ignores')
        response = response.replace('true', '\'true\'').replace('false', '\'false\'').replace('null', '\'null\'')
        response = eval(response)


        for jishu in response['data']:
            author = jishu['author']['name']
            vote = jishu['voteup_count']

            xx += 1
            content = jishu['content']
            soup = BeautifulSoup(content,'lxml')
            content1s = soup.find_all('p')
            content2 = ''
            for content1 in content1s:
                content1 = str(content1)
                if 'class=' in content1:
                    continue
                content2 = content2 + content1.replace('<p>','').replace('</p>','').replace('<b>','').replace('</b>','').replace('<i>','').replace('</i>','')
            print( '\n'+ str(xx) + '、' + '(作者:'+author + '，点赞数：' + str(vote) + '):' + content2)
            f.write(str(xx) + '、' + '(作者:'+author + '，点赞数：' + str(vote) + '):' + content2 + '\n')
        if xx == totals:
            break
        j = 5
    return totals
print('\n文件地址格式，如：“C:\新建文件夹\新建文件夹”(不要保存到磁盘根目录！！！)')
path = input('输入文件保存地址（若不输入，则默认保存到程序所在位置）：')
while True:
    url = input('输入网址:')
    url = url_transform(url)
    url = url_add_api(url)
#得到api url
    totals = zhihu_spider(url,path=path,header1=header1,h1=h1)
    print('\n-------' + str(totals) + '个回答已获取完毕-------\n')
    select = input('是否还要获取？（yes/no）:')
    if select == 'yes':
        continue
    else:
        break