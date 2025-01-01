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
def choose_timeline(input_tl, timeline):
  if input_tl == 0.5:
    return f'highest views in 30 minutes: {max(timeline[0])}'
  elif input_tl == 1:
    return f'highest views in 1 hours: {max(timeline[1])}'
  elif input_tl == 2:
    return f'highest views in 2 hours: {max(timeline[2])}'
  elif input_tl == 24:
    return f'highest views in 24 hours: {max(timeline[3])}'

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

    print("choose timeline: ")
    print(f'| 0.5 hours | 1 hour | 2 hours | 24 hours')
    input_timeline = float(input("input by typing the number: "))
    print(choose_timeline(input_timeline, [half_hour_arr, an_hr_arr, two_hrs_arr, twfo_hrs_arr]))

print('=== welcome to simple analyst app for content creator =====')
print('(click 1 to continue)')

def start():
  let_continue = int(input(">>> "))

  if let_continue == 1:
    open_csv()
  else:
    print("try again")

start()