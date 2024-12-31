''' you can delete:

 import os from dotenv import load_env
 and also load_dotenv
 '''

import os
from dotenv import load_dotenv

import csv

load_dotenv()

isDev = os.getenv('isDev')

data_sheets_use = None

# you can ignore this block code bellow, only use template_sheets
if isDev == 'dev':
  data_sheets_use = 'priv/data_test.csv'
else:
  data_sheets_use = 'data/template_sheets.csv'

with open(data_sheets_use, newline='') as csvfile:
  csv_reader = csv.reader(csvfile)
  
  next(csv_reader)
  next(csv_reader)

  for row in csv_reader:
    date = row[2]
    links = row[3]
    posted_time = row[4]
    after_half_hour = row[5]
    print(f'| {date} | {links} | {posted_time} | {after_half_hour} | ')