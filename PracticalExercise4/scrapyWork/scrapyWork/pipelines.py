# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import subprocess
from itemadapter import ItemAdapter


class ScrapyworkPipeline:
    def process_item(self, item, spider):
        return item

class TxtExportPipeline: #Create a txt file in which the data is saved
    def __init__(self):
        self.file = open('UnivRanking.txt', 'w')

    def process_item(self, item, spider):
        cleaned_univname = item['univname'].replace('\n', ' ')
        cleaned_rank = item['rank'].replace('\n', ' ')
        cleaned_score = item['score'].replace('\n', ' ')

        line = f"University: {cleaned_univname}, Rank: {cleaned_rank}, Score: {cleaned_score}\n"
        self.file.write(line)
        return item

    def close_spider(self, spider):
        self.file.close()
        #Open the file automatically to the user (optional) :
        subprocess.run(['start', 'UnivRanking.txt'], check=True, shell=True) 