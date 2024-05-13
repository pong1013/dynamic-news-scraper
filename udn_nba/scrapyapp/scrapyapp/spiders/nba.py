import scrapy

from scrapyapp.items import ScrapyappItem

class NbaSpider(scrapy.Spider):
    name = "nba"
    allowed_domains = ["tw-nba.udn.com"]
    start_urls = ["https://tw-nba.udn.com/nba/index"]

    def parse(self, response):
        articles = response.xpath('//ul[@class="splide__list"]/li')
        for article in articles:
            # 標題
            title = article.xpath('.//h1/text()').get()
            
            # 內頁連結
            link = article.xpath('.//@href').get()
            
            print("Title:", title)
            print("Link:", link)
            
            # relative url
            yield response.follow(url=link, callback=self.parse_content, meta={'title': title})
    
    def parse_content(self, response):
        title = response.request.meta['title']
        item = ScrapyappItem()
        if title:
            # 內文
            contents = response.xpath('//div[@id="story_body_content"]')
            item['title'] = title
            item['author'] = contents.xpath('.//div[@class="shareBar__info--author"]/text()').get()
            item['publish_time'] = contents.xpath('.//div[@class="shareBar__info--author"]/span/text()').get()
            paragraphs = []
            for content in contents:
                paragraph = content.xpath('.//span/p/text()').getall()
                paragraphs.extend(paragraph)
                item['content'] = paragraphs
        # print(item)
        yield item
