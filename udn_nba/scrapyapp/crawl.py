# from scrapy.crawler import CrawlerProcess
# from scrapy.utils.project import get_project_settings

# from scrapyapp.spiders.nba import NbaSpider

# def run_spider():
#     # get settings
#     process = CrawlerProcess(get_project_settings())
#     # add spider
#     process.crawl(NbaSpider)

#     process.start()

# if __name__ == "__main__":
#     run_spider()

from scrapy import cmdline

cmdline.execute('scrapy crawl nba'.split())