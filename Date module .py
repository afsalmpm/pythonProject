# Import date class from datetime module
from datetime import date
# Returns the current local date
today = date.today()
x = str(today)
[year, month, day] = x.split("-")
date = f'{day}/{month}/{year}'
