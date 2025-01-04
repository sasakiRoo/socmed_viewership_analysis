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

  result.append(f'| time | views |')
  result.append('-' * 17)

  for key, value in data.items():
    result.append(f"| {key} | {value} |")

  print("\n".join(result))
  print(get_max_views(posted_time, views_amount, timespan))

# get maxium views for each timespan
def get_max_views(posted_time, views, timespan):
  combined = list(zip(posted_time, views))
  max_time, max_val = max(combined, key=lambda x: x[1])
  return f'maximum views in {timespan} hours is {max_val} video posted at {max_time}'

''' asking user to choose 
Select: | show all table [0] | show time span [1] |
'''
def input_prompt(prompt_input, views_amount, posted_time):
  if prompt_input == 0:
    print('not yet implemented') # TODO NEXT: show all tables. showing csv to terminal
  elif prompt_input == 1:
    choose_timeline(views_amount, posted_time)

# function to open csv_file
def open_csv():
  with open(data_sheets_use, newline='') as csvfile:
    csv_reader = csv.reader(csvfile)
    
    next(csv_reader)
    next(csv_reader)

    half_hour_arr = []
    an_hr_arr = []
    two_hrs_arr = []
    twfo_hrs_arr = []
    posted_time_arr = []

    for col in csv_reader:
      date = col[2] #for next update
      links = col[3] #for next update
      posted_time = col[4] #for next update
      after_half_hour = int(col[5]) if col[5].isdigit() else 0
      after_an_hr = int(col[6]) if col[6].isdigit() else 0
      after_two_hrs = int(col[7]) if col[7].isdigit() else 0
      after_twfo_hrs = int(col[8]) if col[8].isdigit() else 0

      half_hour_arr.append(after_half_hour)
      an_hr_arr.append(after_an_hr)
      two_hrs_arr.append(after_two_hrs)
      twfo_hrs_arr.append(after_twfo_hrs)
      posted_time_arr.append(posted_time)

      timespan_views_arr = [half_hour_arr, an_hr_arr, two_hrs_arr, twfo_hrs_arr]

    print('hello, welcome to simple analysis app')
    print('\nSelect: | show all table [0] | show time span [1] |')
    get_input = int(input(">>> "))

    input_prompt(get_input, timespan_views_arr, posted_time_arr)
     
    

print('=== welcome to simple analyst app for content creator =====')
print('(click 1 to continue)')

def start():
  let_continue = int(input(">>> "))

  if let_continue == 1:
    open_csv()
  else:
    print("try again")

start()

