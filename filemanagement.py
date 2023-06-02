import os
import urllib.request
print(os.getcwd())
os.makedirs('./data', exist_ok=True)
print(os.listdir('.'))
print(os.listdir('./data'))

url1 = 'https://www.kaggle.com/c/hpa-single-cell-image-classification/data?select=sample_submission.csv'

urllib.request.urlretrieve(url1,'./data')

