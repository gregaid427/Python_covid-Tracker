import requests
import csv
from io import StringIO

# from app import URL

def get_csv_reader(csv_url):
    res=requests.get(csv_url)
    data =res.content.decode('ascii', 'ignore')
    
    return csv.reader(StringIO(data))
