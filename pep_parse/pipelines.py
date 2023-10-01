import csv
import datetime as dt

from collections import defaultdict
from pep_parse.constants import (
    BASE_DIR,
    DATETIME_FORMAT,
    RESULTS,
    SUMMARY_FILE_NAME,
    TABLE_HEADER,
)


class PepParsePipeline:
    def open_spider(self, spider):
        self.results = defaultdict(int)
        self.results_dir = BASE_DIR / RESULTS
        self.results_dir.mkdir(exist_ok=True)

    def close_spider(self, spider):
        time_now = dt.datetime.now()
        time_format = time_now.strftime(DATETIME_FORMAT)
        file_path = f'{self.results_dir}/{SUMMARY_FILE_NAME}_{time_format}.csv'
        self.results['Total'] = sum(self.results.values())

        with open(file_path, 'w', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(TABLE_HEADER)
            writer.writerows(self.results.items())

    def process_item(self, item, spider):
        self.results[item['status']] += 1
        return item
