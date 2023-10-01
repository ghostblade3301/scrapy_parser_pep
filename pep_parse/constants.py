from pathlib import Path

URL = 'https://peps.python.org/'
ALLOWED_DOMAIN = 'peps.python.org'

BASE_DIR = Path(__file__).parent.parent
RESULTS = 'results'
DATETIME_FORMAT = '%Y-%m-%d_%H:-%M:-%S'

SUMMARY_FILE_NAME = 'status_summary'
TABLE_HEADER = ('Статус', 'Количество')
