# -*- coding = utf-8 -*-

from bs4 import BeautifulSoup  # 网页解析，获取数据
import re  # 正则表达式，进行文字匹配
import urllib.request, urllib.error  # 指定URL，获取网页数据
import xlwt  # 进行excel操作
import time


def sleep(int):
    time.sleep(int)


def main():
    # 首先构建一个url
    baseurl = "http://cnews.chinadaily.com.cn/5bda64b0a3101a87ca904f12/"

    # 1.爬取网页
    datalist = getData(baseurl)
    savepath = "newsChinaDaily.xls"
    # 2.逐一解析数据
    # 3.保存数据
    saveData(datalist, savepath)
    askURL(baseurl)


findLink = re.compile(r'<h3><a href="(.*?)" shape="rect" target="_blank">')  # 创建正则表达式对象，表示字符串的模式，即规则
findTitle = re.compile(r'target="_blank">(.*?)</a></h3>')


# 爬取网页
def getData(baseurl):
    datalist = []
    for i in range(1, 301):
        print(i)
        followurl = "page_" + str(i) + ".html"
        url = baseurl + followurl  # str(i*25)
        html = askURL(url)  # 保存获取到的网页源码
        # 2.逐一解析数据
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all('div', class_="left-liebiao"):
            data1 = []
            data2 = []
            item = str(item)
            links = re.findall(findLink, item)
            for link in links:
                data1.append(link)
                print(link)
            titles = re.findall(findTitle, item)
            for title in titles:
                data2.append(title)
                print(title)
            datalist.append(data1)
            datalist.append(data2)
        sleep(3)

    return datalist


# 得到指定一个URL的网页内容
def askURL(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)"
                      " Chrome/78.0.3904.108 Safari/537.36"
    }
    request = urllib.request.Request(url=url, headers=headers)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8", "ignore")
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


def saveData(datalist, savepath):
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)  # 创建workbook对象(文件)
    sheet = book.add_sheet('新闻', cell_overwrite_ok=True)
    col = ('新闻详情链接', '新闻名', '新闻内容', '作者', '来源', '时间')
    for i in range(0, 6):
        sheet.write(0, i, col[i])
    for i in range(0, 300):
        data = datalist[i]
        for j in range(0 + i * (len(data)), +i * (len(data)) + len(data)):
            k = i % 2
            m = j - i * (len(data))
            n = (i // 2) * len(data) + j - i * len(data)
            sheet.write(n + 1, k, data[m])
            print(n, k, data[m])
            if k == 0:
                html = askURL("http:"+data[m])
                #print(html)
                reg1 = r'<meta name="Description" content="(.*?)"'
                reg2 = r'<meta name="author" content="(.*?)"'
                reg3 = r'<meta name="source" content="(.*?)"'
                reg4 = r'<meta name="publishdate" content="(.*?)"'

                findContent = re.compile(reg1)
                findAuthor = re.compile(reg2)
                findSource = re.compile(reg3)
                findDate = re.compile(reg4)
                content = re.findall(findContent, html)
                author = re.findall(findAuthor, html)
                source = re.findall(findSource, html)
                date = re.findall(findDate, html)
                sheet.write(n + 1, 2, content)
                sheet.write(n + 1, 3, author)
                sheet.write(n + 1, 4, source)
                sheet.write(n+1, 5, date)


    book.save(savepath)


# 保存数据
if __name__ == "__main__":
    main()