# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.files import FilesPipeline
import scrapy

class DouyinPipeline:
    def process_item(self, item, spider):
        return item

class videodownloadpipeline(FilesPipeline):
    
    def get_media_requests(self, item, info):
        yield scrapy.Request(url = item['videolink'], meta = {'name': item['name']})

    def file_path(self, request, response=None, info=None, *, item=None):
        filename = request.meta['name']
        return filename
    
