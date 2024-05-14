# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter
from warehouse.models import UdnFocus
from asgiref.sync import sync_to_async
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction

class ScrapyappPipeline:
    async def process_item(self, item, spider):
        try:
            # Check if exists
            news = await sync_to_async(UdnFocus.objects.get)(title=item['title'])            
            return item
        except ObjectDoesNotExist:
            pass
        
            
        async with transaction.atomic():
            news = UdnFocus()
            news.title = item['title']
            news.author = item['author']
            news.publish_time = item['publish_time']
            news.content = item['content']
            await sync_to_async(news.save)()
            
            # Check if total records exceed 10
            if await sync_to_async(UdnFocus.objects.count)() > 10:
                # Delete the oldest record
                oldest_news = await sync_to_async(UdnFocus.objects.order_by('publish_time').first)()
                await sync_to_async(oldest_news.delete)()
        
            
        return item