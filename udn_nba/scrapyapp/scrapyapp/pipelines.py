# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter
from warehouse.models import UdnFocus
from asgiref.sync import sync_to_async

class ScrapyappPipeline:
    async def process_item(self, item, spider):
        try:
            # Check if exists
            news = UdnFocus.objects.get(title=item['title'])
            return item
        except:
            news = UdnFocus()
        news.title = item['title']
        news.author = item['author']
        news.publish_time = item['publish_time']
        news.content = item['content']
        await sync_to_async(news.save)()
        
        return item