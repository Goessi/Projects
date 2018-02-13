import read
from dateutil.parser import parse
import datetime
data = read.load_data()

def get_date(da):
    date = parse(da)
    return date.hour

data['h'] = data['submission_time'].apply(get_date)
result = data['h'].value_counts()
print(result)
