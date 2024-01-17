from datetime import datetime
from time import strftime


data = f'{datetime.now()}'

def convert_date_from_text(date):
    return datetime.strptime(date, '%d.%m.%Y').timestamp()

print(convert_date_from_text(data))

def convert_date_in_text(date):
   
    return strftime(datetime.fromtimestamp(convert_date_from_text(date)).strftime('%d.%m.%Y')) 

print(convert_date_in_text(data))
