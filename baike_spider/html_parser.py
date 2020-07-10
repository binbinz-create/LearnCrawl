from urllib.parse import urljoin

from bs4 import BeautifulSoup
import re
'''
解析一个页面，返回页面中的url以及对应的数据
'''
class HtmlParser(object):


    def _get_new_urls(self, page_url, soup):
        new_urls=set()
        links =  soup.find_all('a',href=re.compile(r"/item/.+"))
        for link in links:
            new_url = link["href"]
            new_full_url=urljoin(page_url,new_url)   #使用urljoin将爬取到的url根据page_url 合并成完整的url
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        res_data={}
        #url
        res_data['url'] = page_url

        title_node = soup.find('dd',class_="lemmaWgt-lemmaTitle-title").find("h1")
        res_data['title'] = title_node.get_text()

        summary_node = soup.find("div",class_="lemma-summary")
        res_data['summary'] = summary_node.get_text()

        return res_data


    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont,"html.parser",from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url,soup)
        new_data = self._get_new_data(page_url,soup)
        return new_urls , new_data
