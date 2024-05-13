from celery import shared_task
# from scrapy import cmdline
import os

@shared_task
def run_scrapy_spider():
    print("Start celery schedule!")
    # get current dir
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # go to scrapy project dir
    scrapy_project_dir = os.path.join(current_dir, '.')

    # switch to scrapy dir
    os.chdir(scrapy_project_dir)


    os.system('scrapy crawl nba')
    # cmdline.execute('scrapy crawl nba'.split())