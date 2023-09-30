from pathlib import Path


BASE_DIR = Path(__file__).parent.parent
RESULTS = 'results'
RESULTS_DIR = BASE_DIR.parent / RESULTS
DATETIME_FORMAT = '%Y-%m-%d_%H:-%M:-%S'
