import feedparser
import pprint
import os

# 网站种子解析
rss_oschina = feedparser.parse('https://rsshub.app/qdaily/column/59')
# 抓取内容 ， depth 抓取深度

mylist = [entry['title'] for entry in rss_oschina['entries']]
pprint.pprint(mylist)


# 该代码运行于python3
# 功能:把内容保存为html格式文件
with open('file.html','w') as file: #以w的模式打开file.html文件，不存在就新建
    file.write('<html><body><table border=1><tr><th>a列表</th><th>b列表</th></tr><indent>输出结果:') #使用write写入字符串内容到file.html
    file.write('<tr><td>{}'.format(mylist)+'</td><td>{}') #使用write写入字符串内容到file.html
    file.write('</indent></table></body></html>') #使用write写入字符串内容到file.html
