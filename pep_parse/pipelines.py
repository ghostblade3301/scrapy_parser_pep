import csv
import datetime

from .constants import BASE_DIR, DATETIME_FORMAT


class PepParsePipeline:
    def open_spider(self, spider):
        pass

    def process_item(self, item, spider):
        return item

    def close_spider(self, spider):
        pass
