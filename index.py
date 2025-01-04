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
def choose_timeline(input_tl, timeline_views, posted_time):
  if input_tl == 0.5:
    key_val = dict(zip(posted_time, timeline_views[0]))
    return show_table_time_span(key_val)
  elif input_tl == 1:
     key_val = dict(zip(posted_time, timeline_views[1]))
     return show_table_time_span(key_val)
  elif input_tl == 2:
     key_val = dict(zip(posted_time, timeline_views[2]))
     return show_table_time_span(key_val)
  elif input_tl == 24:
     key_val = dict(zip(posted_time, timeline_views[3]))
     return show_table_time_span(key_val)

# table time span data print
def show_table_time_span(data):
  result = []
  for key, value in data.items():
    result.append(f"| {key} | {value} |")
  return "\n".join(result)

# todo, find max value and posted_time that it associated with
# max: 1000 at 19:00

def prompt(prompt_input, timespan, posted_time):
  if prompt_input == 0:
    print('not yet implemented')
  elif prompt_input == 1:
    print("choose timeline: ")
    print(f'| 0.5 hours | 1 hour | 2 hours | 24 hours')
    input_timeline = float(input("input by typing the number: "))
    print(choose_timeline(input_timeline, timespan, posted_time))
  elif prompt_input == 2:
    print('not yet implemented')

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

      timespan_arr = [half_hour_arr, an_hr_arr, two_hrs_arr, twfo_hrs_arr]

    print('hello, welcome to simple analysis app')
    print('\nSelect: | show all table [0] | show time span [1] | show max views | [2]')
    inp_prompt = int(input(">>> "))

    prompt(inp_prompt, timespan_arr, posted_time_arr)
     
    

print('=== welcome to simple analyst app for content creator =====')
print('(click 1 to continue)')

def start():
  let_continue = int(input(">>> "))

  if let_continue == 1:
    open_csv()
  else:
    print("try again")

start()