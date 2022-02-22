# pat="<div class=\"name\">.{1,100}出版社</div>"
# import urllib.request
# import re
# import string
# data=urllib.request.urlopen("https://www.jxsggzy.cn/web/jyxx/002001/002001001/jyxx.html").read()
# print(data.decode('GBK')

# https://www.xicidaili.com/带理网址


# import urllib.request as req
# def use_proxy(url,proxy_addr):
#     proxy=req.ProxyHandler({"http":proxy_addr})
#     opener=req.build_opener(proxy,req.HTTPHandler)
#     req.install_opener(opener)
#     data=req.urlopen(url).read()#.decode('utf-8','ignore')
#     return data
# proxy_addr="175.25.26.117:3128"
# url="https://www.jxsggzy.cn/web/jyxx/002001/002001001/jyxx.html"
# data=use_proxy(url,proxy_addr)
# print(data)


#
# import urllib.request as u_r
# url= "https://www.jxsggzy.cn/web/jyxx/002001/002001001/jyxx.html"
# headers=()
# opener=u_r.build_opener()
# opener.addheaders=[headers]
# u_r.install_opener(opener)
# data=opener.open(url).read()

import requests
import re

surl = "https://weibo.com/p/11005053793153047/follow?relate=fans&page="
surl2 = "#Pl_Official_HisRelation__49"
sheaders = {"Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Cookie": "SINAGLOBAL=3135343932446.769.1569131735884; ULV=1569235400641:2:2:2:5816638612821.978.1569235400631:1569131735890; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5IBGXBvELiOe6cpQGizFv_5JpX5KzhUgL.Fo-ceo-XehzfeK.2dJLoIpHjIg2LxKqLBo-LB-2LxKnLB.qLBo.t; SUHB=0M2FtyTxiHeXaa; ALF=1600771552; wvr=6; SUB=_2A25wjNI0DeRhGeNI6VcV8CzJyjWIHXVT-ET8rDV8PUNbmtBeLRbkkW9NSJoA4XYiAxZAKyXLcYUpecXIHP09RvJR; login_sid_t=a04ceb7ade5efdc7dc78f30b154620e1; cross_origin_proto=SSL; _s_tentry=passport.weibo.com; UOR=,,www.baidu.com; Apache=5816638612821.978.1569235400631; SSOLoginState=1569235556; webim_unReadCount=%7B%22time%22%3A1569242365166%2C%22dm_pub_total%22%3A1%2C%22chat_group_client%22%3A0%2C%22allcountNum%22%3A7%2C%22msgbox%22%3A0%7D",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0"
            }  # 注意有时候的省略号表示属性太长
for i in range(1, 25):
    res = requests.get("https://www.jxsggzy.cn/web/jyxx/002001/002001001/" + str(i) + ".html", headers=sheaders)
    # print(res.text)
    str1 = res.text
    key_words = "建设项目"
    date = "20211231"
    # print(str1)
    # pat = "< a href = "/web/jyxx/002001/002001001/20211203/6110045a-a095-46bb-8760-b4780a68be3f.html" target = "_blank"
    #
    #
    # class ="ewb-list-name" >[广信区]上饶市广信区金桥商住小区（含农贸市场）新建项目施工全过程跟踪审核和竣工结算审核（一审）服务 < font color='red' > < / font > < / a >
    # "
    # pat = "<li class=\"ewb-list-node clearfix\">\n<a href=\"/web/jyxx/002001/002001001/20211204/1fd3e19a-e076-4408-88d6-969a1a7a0c98\.html\" target=\"_blank\" class=\"ewb-list-name\">[樟树市]樟树市城市亮化工程—四特大道临街建筑立面亮化工程<font color=\'red\'></font></a>\n<span class=\"ewb-list-date\">2021-12-04</span>\n</li>"
    # pat = "<li class=\"ewb-list-node clearfix\">\n<a href=\"/web/jyxx/002001/002001001/.*html\" target=\"_blank\" class=\"ewb-list-name\">.*<font color=\'...\'></font></a>\n<span class=\"ewb-list-date\">.*</span>\n</li>"
    pat = "/web/jyxx/002001/002001001/.*html.*class=\"ewb-list-name\">.*" + key_words + ".*<font color.*"
    rst = re.compile(pat).findall(str1)
    if rst:
        # print(rst[0])
        str2 = rst[0]
        pat1 = "/web/jyxx/002001/002001001/" + date + ".*html"
        pat2 = ">.*建设项目.*<f"
        name = re.compile(pat2).findall(str2)
        dat = re.compile(pat1).findall(str2)
        if dat:
            html = "https://www.jxsggzy.cn/" + dat[0]
            print(html)
            print(name[0][1:-2])
            print(str2)
