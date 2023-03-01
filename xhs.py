import hashlib
import requests
import json
import urllib.parse
import csv


# 此处填入自己的微信Authorization
auth = ''
def xhs():
    user_input = input('输入需要搜索的关键词: \n')
    keyword = urllib.parse.quote(user_input)

    saveData = []
    for i in range(1,6):
        url = "https://www.xiaohongshu.com/fe_api/burdock/weixin/v2/search/notes?keyword={}&sortBy=hot_desc&page={}&pageSize=20&prependNoteIds=&needGifCover=true"
        # print(i)
        url = url.format(keyword, i)
        # print(url)
        xsign = "X{0}".format(
            hashlib.md5("{0}WSUDD".format(url.replace("https://www.xiaohongshu.com", "")).encode("utf-8")).hexdigest())
        # print(xsign)
        res = setxhs(url, xsign)
        notes = res['data']['notes']
        print(notes)
        for note in notes:
            saveData.append(note)
    print(saveData)
    csva(saveData,user_input)


def setxhs(url,xsign):
    headers = {
        # 'Accept-Encoding': 'gzip, deflate, br',
        # 'Accept-Language': 'zh-cn',
        'Connection': 'keep-alive',
        'Content-Type':'application/json',
        # 'Device-Fingerprint': 'WHJMrwNw1k/GlXqZzeuw8+tSQY4MXwq6dZ2nKzuBmvUOQrof1RlMW08Eos7yVvMgVhnYkWA10aq1rj6WzyrssBJh3Fx6nPiKJdCW1tldyDzmauSxIJm5Txg==1487582755342',
        # 'Cookie': 'smidV2=20220906172310c1f905ecd5e9146162e5d331df04408500bf3745eff353600; gid.ss=gSMQ9UOnDuZwH2oRGJG6BW6e4grs67TaYpnrW+8Wmd2VIB5Z2pKhUS3+SkAuyyEE; customerClientId=870744698665320; subsystem=ares; sso-type=customer; a1=184aed2d18bg4fo9oomfr4huwjtd4dp1qxdpmilu100000180114; webId=3b62753bb1c14a51e6eaab87fdee16a8; gid=yY40dfJfK0A4yY40dfJfyC31YDk4iljll6iFf7y4x7EV9U88f4fUy6888yY8yy48Y2fSqy2q; gid.sign=685UfbG/GgpMupLrf0P5Orh/lhw=; xhsTrackerId=46ea6e2f-91e7-4f14-948f-43dc63c0ba0a; xhsTrackerId.sig=1aK9QhJ4E9fP_vpEzjHkoxiKMqrCUIgTOZVKJuVJ4D8; x-user-id=63dd0af777bcdf0001cb898d; access-token=AT-3667b58efdf544deae96788358193893-98c5e01cf652458daba83f481297224a; galaxy.creator.beaker.session.id=1675952591505080499015; timestamp2=1675953578905bb47f14186238c7056432a31c549f85ef6bceebbc2363d9ddd; timestamp2.sig=rb36OMzgqMcLGwl4M68-yTYHr-JGdVuLgOKjtZjc4Fg; customerBeakerSessionId=3337022e21deee7b171fc0a143cfb04182f33b74gAJ9cQAoWBAAAABjdXN0b21lclVzZXJUeXBlcQFLAlgOAAAAX2NyZWF0aW9uX3RpbWVxAkdB2Pkty+otDlgJAAAAYXV0aFRva2VucQNYQQAAADYzODk2NjRkNGIyMjQxNjhiMmM2MmU4OTk3YmRkM2IwLWRlMWY0MzczNDlkNDQxNWU4MzdkMWQxMmFjOTE5ZDc4cQRYAwAAAF9pZHEFWCAAAABkNzY3ZjlkZWZkNDA0OTc0OTBiY2EzNmM0MDVlMmZhMXEGWA4AAABfYWNjZXNzZWRfdGltZXEHR0HY+WT9987ZWAYAAAB1c2VySWRxCFgYAAAANjNkZDBhZjc3N2JjZGYwMDAxY2I4OThkcQl1Lg==; access-token-redlive.xiaohongshu.com=customer.red_live.AT-687fc04b032e4c0f85eadf808f6e5bbd-11889e220b254889aef0cec6632f3421; web_session=0400698c5593bf1811f639d0d0314bd8ea8e9a; xhsTracker.sig=u1cFYHAwm89lKbFLL1Y8vp9JcskioXWTa56RKaAB2ys; websectiga=29098a4cf41f76ee3f8db19051aaa60c0fc7c5e305572fec762da32d457d76ae; extra_exp_ids=h5_1208_exp3,h5_1130_exp1,ios_wx_launch_open_app_exp,h5_video_ui_exp3,wx_launch_open_app_duration_origin,ques_exp1; extra_exp_ids.sig=5skoHGJgRD48znmDfG6Hn4CiTferl6T5KtzE4pAgw5c; webBuild=1.1.10; sec_poison_id=097839b5-f830-4b7a-a61f-21aea2435492; xhsTracker=url=explore&searchengine=baidu; xsecappid=creator-main',
        'Host': 'www.xiaohongshu.com',
        'Referer': 'https://servicewechat.com/wxb296433268a1c654/81/page-frame.html',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.10(0x18000a28) NetType/WIFI Language/zh_CN',
        'Host':'www.xiaohongshu.com',
        'Authorization': auth,
        'X-Sign': xsign,
    }

    response = requests.get(
        url=url,
        headers=headers,
    )
    content = response.content
    # 转换成字符串
    string = content.decode('utf-8')
    # 把字符串转成python数据类型
    results = json.loads(string)
    # print(results)
    return results

def csva(notes,keyword):
    # notes = results['data']['notes']
    # print(notes)

    file = open(keyword+'.csv', 'w', encoding='utf-8', newline='')
    # 先设置列名，并写入csv文件
    csv_writer = csv.DictWriter(file, fieldnames=['id', 'title', 'type', 'likes', 'isLiked', 'cover', 'time', 'comments', 'collects', 'user'])
    csv_writer.writeheader()
    for note in notes:
        csv_writer.writerow(note)

if __name__ == '__main__':
    xhs()