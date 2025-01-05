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


# function for user to chose time line
def choose_timeline(views_amount, posted_time):
  print("choose timeline: ")
  print(f'| 0.5 hours | 1 hour | 2 hours | 24 hours')
  get_input_timespan = float(input("input by typing the number: "))

  if get_input_timespan == 0.5:
    key_val = dict(zip(posted_time, views_amount[0]))
    return show_table_time_span(key_val, posted_time, views_amount[0], get_input_timespan)

  elif get_input_timespan == 1:
     key_val = dict(zip(posted_time, views_amount[1]))
     return show_table_time_span(key_val, posted_time, views_amount[1], get_input_timespan)

  elif get_input_timespan == 2:
     key_val = dict(zip(posted_time, views_amount[2]))
     return show_table_time_span(key_val, posted_time, views_amount[2], get_input_timespan)

  elif get_input_timespan == 24:
     key_val = dict(zip(posted_time, views_amount[3]))
     return show_table_time_span(key_val, posted_time, views_amount[3], get_input_timespan)


# table time span data print
def show_table_time_span(data, posted_time, views_amount, timespan):
  result = []

  result.append('| {:<9} | {:<9} |'.format('posted at', 'views'))
  result.append('-' * 27)

  for key, value in data.items():
    result.append('| {:<9} | {:<9} |'.format(key, value))

  print("\n".join(result))
  print(get_max_views(posted_time, views_amount, timespan))


# show all data table
def show_all_data_table(data): 
  result = []
  result.append('| {:<8} | {:<12} | {:<10} | {:<12} | {:<5} | {:<5} | {:<5} | {:<5}'.format('date', 'link', 'posted at', 'views 30 mis', 'views 1 hr', 'views 2 hrs', 'views 24 hrs', 'post type'))
  for row in data:
    result.append('| {:<5} | {:<12} | {:<10} | {:<12} | {:<5} | {:<5} | {:<5} | {:<5} |'.format(row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]))
  print("\n".join(result))


# get maxium views for each timespan
def get_max_views(posted_time, views, timespan):
  combined = list(zip(posted_time, views))
  max_time, max_val = max(combined, key=lambda x: x[1])
  return f'maximum views in {timespan} hours is {max_val} video posted at {max_time}'


''' asking user to choose 
Select: | show all table [0] | show time span [1] |
'''
def input_prompt(prompt_input, views_amount, posted_time, data):
  if prompt_input == 0:
    show_all_data_table(data)
  elif prompt_input == 1:
    choose_timeline(views_amount, posted_time)


# function to open csv_file
def open_csv():
  last_row = []
  with open(data_sheets_use, newline='') as csvfile:
    csv_reader = csv.reader(csvfile)
    
    next(csv_reader)
    next(csv_reader)

    half_hour_arr = []
    an_hr_arr = []
    two_hrs_arr = []
    twfo_hrs_arr = []
    posted_time_arr = []
    date = []
    links = []

    for row in csv_reader:
      half_hour_arr.append(int(row[5]) if row[5].isdigit() else 0)
      an_hr_arr.append(int(row[6]) if row[6].isdigit() else 0)
      two_hrs_arr.append(int(row[7]) if row[7].isdigit() else 0)
      twfo_hrs_arr.append(int(row[8]) if row[8].isdigit() else 0)
      posted_time_arr.append(row[4])
      date.append(row[2])
      links.append(row[3])
      timespan_views_arr = [half_hour_arr, an_hr_arr, two_hrs_arr, twfo_hrs_arr]
      last_row.append(row)


    print('hello, welcome to simple analysis app')
    print('\nSelect: | show all table [0] | show time span [1] |')
    get_input = int(input(">>> "))

    input_prompt(get_input, timespan_views_arr, posted_time_arr, last_row)
     
    
print('=== welcome to simple analyst app for content creator =====')
print('(click 1 to continue)')


def start():
  let_continue = int(input(">>> "))

  if let_continue == 1:
    open_csv()
  else:
    print("try again")

start()

