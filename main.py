import urllib.request,urllib.error
import re
from bs4 import BeautifulSoup as BS
import time


# 运用爬虫技术，爬取luogu.com.cn前50道题目和题解
def get_problem_list():
    url = "https://www.luogu.com.cn/problem/P"
    

    problem_list = []
    for i in range(1000, 1050):
        problem_list.append(url + str(i))
    return problem_list




def get_data(url):
    headers={
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36" 
        }
    request = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(request)
    data= response.read().decode('utf-8')
    if str(data).find("Exception") == -1:
        return data
    else:
        return None
    
# 把上个函数获取的data转为Markdown文件
def get_md(data):
    bs = BS(data,"html.parser")
    core = bs.select("article")[0]
    md = str(core)
    md = re.sub("<h1>","# ",md)
    md = re.sub("<h2>","## ",md)
    md = re.sub("<h3>","#### ",md)
    md = re.sub("</?[a-zA-Z]+[^<>]*>","",md)
    return md

# 保存上个函数的Markdown文件

def save_md(md,cfilename):
    cfilename ="" + cfilename
    file = open(cfilename,"w",encoding="utf-8")
    for f in md:
        file.writelines(f)
    file.close()

if __name__ == '__main__':
    problem_list = get_problem_list() # 列出每题网址
    i=1000
    for url in problem_list:
        print("开始爬取P"+str(i))
        data = get_data(url)
        if(data==None):
            print("爬取数据失败")
        else:
            print("爬取数据成功")
            md = get_md(data)
            cfilename = "P"+str(i)+".md"
            save_md(md,cfilename)
            print("已保存P"+str(i))
        i=i+1
        # print(i)
        time.sleep(9)