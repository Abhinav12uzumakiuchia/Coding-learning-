import datetime as d
today = d.date.today()

one = d.timedelta(days = 1)
yesterday = today - one
print(yesterday)
