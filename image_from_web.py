
from bing_image_downloader import downloader
apple="apple"
for fruit in fruit_names:
  downloader.download(fruit, limit=20,  output_dir='dataset', adult_filter_off=True, force_replace=False, timeout=60, verbose=True)
