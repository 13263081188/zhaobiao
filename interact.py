import streamlit as st
import numpy as np
# from bokeh.plotting import figure,show
# import matplotlib
# import matplotlib.pyplot as plt
import datetime
import time
import re
import requests
# matplotlib.rcParams['font.family'] = 'SimHei'  # 字体设置为黑体
# plt.rcParams['axes.unicode_minus']=False
import pandas as pd
x = np.array([i for i in range(10000)])
y = np.array(2*(x**4) + x**2 + 9*x + 2) #假设因变量y刚好符合该公式
#y = np.array([300,500,0,-10,0,20,200,300,1000,800,4000,5000,10000,9000,22000])
color_ = ['black','red','green','orange','yellow','blue']
sheaders={"Accept":"*/*",
"Accept-Encoding":"gzip, deflate, br",
"Cookie":"SINAGLOBAL=3135343932446.769.1569131735884; ULV=1569235400641:2:2:2:5816638612821.978.1569235400631:1569131735890; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5IBGXBvELiOe6cpQGizFv_5JpX5KzhUgL.Fo-ceo-XehzfeK.2dJLoIpHjIg2LxKqLBo-LB-2LxKnLB.qLBo.t; SUHB=0M2FtyTxiHeXaa; ALF=1600771552; wvr=6; SUB=_2A25wjNI0DeRhGeNI6VcV8CzJyjWIHXVT-ET8rDV8PUNbmtBeLRbkkW9NSJoA4XYiAxZAKyXLcYUpecXIHP09RvJR; login_sid_t=a04ceb7ade5efdc7dc78f30b154620e1; cross_origin_proto=SSL; _s_tentry=passport.weibo.com; UOR=,,www.baidu.com; Apache=5816638612821.978.1569235400631; SSOLoginState=1569235556; webim_unReadCount=%7B%22time%22%3A1569242365166%2C%22dm_pub_total%22%3A1%2C%22chat_group_client%22%3A0%2C%22allcountNum%22%3A7%2C%22msgbox%22%3A0%7D",
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0"
}#注意有时候的省略号表示属性太长

def get_data(datetime, key_words):
    for i in range(1, 1000):
        res = requests.get("https://www.jxsggzy.cn/web/jyxx/002001/002001001/" + str(i) + ".html", headers=sheaders)
        # print(res.text)
        str1 = res.text
        # key_words = "建设项目"
        date = datetime
        # print(str1)
        # pat = "< a href = "/web/jyxx/002001/002001001/20211203/6110045a-a095-46bb-8760-b4780a68be3f.html" target = "_blank"
        #
        #
        # class ="ewb-list-name" >[广信区]上饶市广信区金桥商住小区（含农贸市场）新建项目施工全过程跟踪审核和竣工结算审核（一审）服务 < font color='red' > < / font > < / a >
        # "
        # pat = "<li class=\"ewb-list-node clearfix\">\n<a href=\"/web/jyxx/002001/002001001/20211204/1fd3e19a-e076-4408-88d6-969a1a7a0c98\.html\" target=\"_blank\" class=\"ewb-list-name\">[樟树市]樟树市城市亮化工程—四特大道临街建筑立面亮化工程<font color=\'red\'></font></a>\n<span class=\"ewb-list-date\">2021-12-04</span>\n</li>"
        # pat = "<li class=\"ewb-list-node clearfix\">\n<a href=\"/web/jyxx/002001/002001001/.*html\" target=\"_blank\" class=\"ewb-list-name\">.*<font color=\'...\'></font></a>\n<span class=\"ewb-list-date\">.*</span>\n</li>"
        pat = "/web/jyxx/002001/002001001/.*html.*class=\"ewb-list-name\">.*" + key_words + ".*color.*"
        rst = re.compile(pat).findall(str1)
        # print(rst)
        if rst:
            # print(rst[0])
            str2 = rst[0]
            pat1 = "/web/jyxx/002001/002001001/" + date + ".*html"
            pat2 = ">.*"+key_words+".*<f"
            print(pat1)
            name = re.compile(pat2).findall(str2)
            dat = re.compile(pat1).findall(str2)
            if dat:
                html = "https://www.jxsggzy.cn/" + dat[0]
                print(html)
                # st.components.v1.html(html, width=None, height=None, scrolling=False)
                import streamlit.components.v1 as components
                # components.iframe(html,scrolling=True)
                # components.iframe(html, scrolling=True)
                print(name[0][1:-2])
                # print(str2)
def main():

    # Wide mode
    st.set_page_config(page_title="Investment automation")
    st.sidebar.title("请您设置相关参数")
    # key_words = "建设项目"
    # date = "20211231"
    x = st.form(key = "tiaoshi")
    if x.form_submit_button("调试"):
        st.write("begin")
        import twint
        c = twint.Config()
        c.Since = "2017-12-27"
        c.Username = "elonmusk"
        c.Links = "include"
        c.Limit = 100
        c.Store_csv = True
        c.Output = "none.csv"
        # c.Lang = "english"
        # c.Translate = True
        # c.TranslateDest = "italian"
        twint.run.Search(c)
        import pandas as pd
        st.dataframe(pd.read_csv("none.csv"))
        import os
        os.remove("none.csv")
        st.write("end")
    z = st.sidebar.form(key="input_")
    key_words = (z.text_input("key_words"))
    user_name = (z.text_input("user_name"))
    # import os
    # if "none.csv" in os.listdir():

    st.balloons()
    # date = (z.text_input("输入日期\n(2021年12月31日 输入 20211231)"))
    if z.form_submit_button("affirm"):
        import os

        if key_words and user_name:
            st.balloons()
            st.write("begin")
            import twint
            c = twint.Config()
            # c.Since = "2010-12-27"
            # c.Until = "2021-12-27"
            # c.Skip_certs = True

            c.Email = True
            c.Phone = True
            c.Verified = True

            c.Username = user_name
            c.Links = "include"
            c.Limit = 100000
            c.Store_csv = True
            st.balloons()

            c.Output = str(user_name+".csv"
            st.write(os.listdir())
            # c.Lang = "english"
            # c.Translate = True
            # c.TranslateDest = "italian"
            twint.run.Search(c)
            import pandas as pd
            data = pd.read_csv(user_name+".csv")
            st.write(data.shape)
            st.dataframe(data)
    # if key_words and user_name:
    #     os.remove(user_name+".csv")
        # for i in range(10):
            # st.text("年年西西...")
            # time.sleep(1)
    # if key_words and user_name:
    #     get_data(date,key_words)

        # embed streamlit docs in a streamlit app
        # components.iframe("https://docs.streamlit.io/en/latest")
        # col_form_input_x = [0 for _ in range(int(number))]
        # col_form_input_y = [0 for _ in range(int(number))]
        # col = st.columns(int(number))
        # col_form = [col[_].form(key=str(_)) for _ in range(int(number))]
        # col_form_c = [[] for _ in range(int(number))]
        # for i in range(int(number)):
        #     col_form_input_x[i] = col_form[i].text_input("浓度")
        #     col_form_input_y[i] = col_form[i].text_input("k/s值")
        #     if col_form[i].form_submit_button("确认"):
        #         # st.write(col_form_input_x)
        #         pass
        # st.write("输入对应浓度和选择的拟合多项式阶数")
        # z = st.form(key="input_")
        # c_ = (z.text_input("对应浓度"))
        # poly_ = (z.text_input("选择模拟多项式的阶数"))
        # if z.form_submit_button("确认"):
        #     st.write("请点击可视化分析显示结果》》》")
        # if st.button("可视化分析") and c_ and poly_:
        #     x = [float(j) for j in col_form_input_x]
        #     y = [float(j) for j in col_form_input_y]
        #
        #     fig, ax = plt.subplots()
        #     plt.xlabel('concentration')
        #     plt.ylabel('k/s')
        #     plt.title('k/s _ concentration')
        #     #origin
        #     ax.plot(x, y, label='origin_data', linewidth=1, color='black', marker='o',
        #             markerfacecolor='black', markersize=2)
        #     import  collections
        #     polyder = collections.defaultdict(np.poly1d)
        #     poly_fit = collections.defaultdict(np.poly1d)
        #     for i in range(1, 6):
        #         poly_fit['poly_fit'+str(i)] = np.poly1d(np.polyfit(x,y,i))
        #         ax.plot(x,poly_fit['poly_fit'+str(i)](x),label = 'coef'+str(i), color = color_[i],linewidth = 1)
        #     for i in range(1,6):
        #         # st.write("coef"+str(i),eval("coef"+str(i)))
        #         polyder["polyder"+str(i)] = np.polyder(poly_fit["poly_fit"+str(i)])
        #         # st.write(np.polyder(eval("poly_fit"+str(i)))(x))
        #     plt.legend()
        #     st.pyplot(fig)
        #     fig1, ax1 = plt.subplots()
        #     plt.xlabel('concentration',fontproperties='SimHei')
        #     plt.ylabel('k/s per concentration')
        #     plt.title('derivative_ concentration')
        #     for i in range(1,6):
        #         ax1.plot(x, polyder["polyder"+str(i)](x), label="Polynomial of order"+str(i)+"k/s", linewidth=1, color=color_[i])
        #         # st.write(i)
        #     plt.legend()
        #     st.pyplot(fig1)
        #     st.sidebar.write("单位浓度k/s结果：")
        #     st.sidebar.write(str(polyder["polyder"+str(poly_)](float(c_))))

if __name__ == '__main__':
    main()
