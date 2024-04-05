import requests
from bs4 import BeautifulSoup
import pandas as pd
import openpyxl



header = {
    'Referer': 'https://ssr1.scrape.center/',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
}
response = requests.get('https://p0.meituan.net/movie/ce4da3e03e655b5b88ed31b5cd7896cf62472.jpg@464w_644h_1e_1c', headers=header)
with open('test.jpg', 'wb') as f:
    f.write(response.content)

header = {
    'Referer': 'https://scrape.center/',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
}

movie_info = {'电影名字':[], '类型':[], '国家':[], '时长':[], '上映时间':[], '分数':[]}

for page in range(1, 11):

    response = requests.get('https://ssr1.scrape.center/page/%d' % page, headers=header)

    soup = BeautifulSoup(response.content, 'html.parser')
    result = soup.find_all('div', class_='p-h el-col el-col-24 el-col-xs-9 el-col-sm-13 el-col-md-16')
    for i in range(len(result)):
        movie_info['电影名字'].append(result[i].h2.string)
        movie_type = ''
        btn_list = result[i].find_all('button', class_='el-button category el-button--primary el-button--mini')
        for btn in btn_list:
            movie_type += btn.span.string + ', '
        movie_info['类型'].append(movie_type)
        info_list = result[i].find_all('div', class_='m-v-sm info')
        span_list = info_list[0].find_all('span')
        movie_info['国家'].append(span_list[0].string)
        movie_info['时长'].append(span_list[2].string)
        span_list = info_list[1].find_all('span')
        if len(span_list) > 0:
            movie_info['上映时间'].append(span_list[0].string)
        else:
            movie_info['上映时间'].append(None)
        score = soup.find_all('p', class_='score m-t-md m-b-n-sm')
        movie_info['分数'].append(score[i].string.strip())


data = pd.DataFrame(movie_info)
data.to_excel('./movieinfo.xlsx', index=False)