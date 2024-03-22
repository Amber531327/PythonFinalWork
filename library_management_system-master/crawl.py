import openpyxl
import urllib.request
from lxml import etree
def create_request(page):
    url = "https://book.douban.com/latest?subcat=%E5%85%A8%E9%83%A8&p="+str(page)
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
    }
    request=urllib.request.Request(url=url,headers=headers)
    return request
def get_content(request):
    response=urllib.request.urlopen(request)
    content=response.read().decode('utf-8')
    return content

def download(content,page):
    tree=etree.HTML(content)
    titles=tree.xpath('//*[@id="content"]/div/div[1]/ul/li/div/h2/a')
    otherinfo=tree.xpath('//*[@id="content"]/div/div[1]/ul/li/div[2]/p[1]')
    title_texts=[title.text.strip() for title in titles]
    author_texts = [author.text.split('/')[0].strip() for author in otherinfo]
    publish_texts = [publish.text.split('/')[2].strip() for publish in otherinfo]
    for id in range(0,20):
        sheet.append([20*(page-1)+id+1,title_texts[id], author_texts[id], publish_texts[id]])
    workbook.save("douban_books.xlsx")

if __name__ == "__main__":
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.append(["ID", "书名", "作者", "出版社"])
    for page in range(1,4):
        request = create_request(page)
        content = get_content(request)
        download(content,page)
