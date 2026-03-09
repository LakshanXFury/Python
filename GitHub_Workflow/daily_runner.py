import datetime

current_time = datetime.datetime.now()
print(f"The current date is {current_time.strftime('%d')} of {current_time.strftime('%b')} "
      f"and time is {current_time.strftime('%H:%M:%S')}")