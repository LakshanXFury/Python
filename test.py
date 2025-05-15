# def shout(text):
#     return text.upper()
#
# print(shout('Hello'))
#
# yell = shout
#
# print(yell('Hello bro '))

import time

curr_time = time.ctime()
split = curr_time.split()

# Reorder to: DayNumber Month DayName → 15 May Thu
formatted_date = f"{split[2]} {split[1]} {split[0]}"
print(formatted_date)
