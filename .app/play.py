from datetime import datetime as dt
from library.c_date import Date

print("""


===================================
PLAYGROUND
===================================
""")

date_today = Date(dt.now())

print([date_today.string, date_today.date])

print("-------")

first_day_of_week = date_today.day_week(day=3)
print(first_day_of_week)

# print(f'Name of month = {get_month(end_date)}')
print(f'First day of the week = {date_today.day_week()}')
print(f'Last day of the week = {date_today.day_week(7)}')
print(f'Past week = {date_today.past_days(days=7)}')
print(f'Future week = {date_today.future_days(days=7)}')

past_6_weeks = date_today.past_days(days=36)
print(past_6_weeks)
print(f'Past 6 weeks first day = {Date(past_6_weeks).day_week(1)}')
# print(f'First day of previous 12 weeks = {dates_previous_weeks(end_date,12, output=3)}')
print(f'First day of the month = {date_today.day_month()}')
print(f'First day of the year = {date_today.day_month_year()}')
print(f'Past month= {date_today.past_months()}')
print(f'Future month= {date_today.future_months()}')
print(f'Last day of month= {date_today.last_day_month()}')
# print(f'Last day of the month = {last_day_of_month(end_date)}')
# print(f'First day of previous month = {dates_previous_months(end_date, 1, output=3)}')
#print(f'First day of previous 6 months = {Date(datetime_now_string).past_months()}')
print(f'Past 6 months = {date_today.past_months(6)}')
print(f'Past 12 months = {date_today.past_months(12)}')
print(f'Past 12 months first day = {Date(date_today.past_months(12)).day_month()}')
print(f'Past 12 months first day = {Date(date_today.past_months(12)).last_day_month()}')
# print(f'First day of previous 12 months = {dates_previous_months(end_date, 12, output=3)}')

stop

title = f'## [pc2565](https://mrwayneo.github.io/)    '
author = f'by wayneo   '
description = f'Description: Punters started February 2020, based on $10 per tip.   '
url = f'URL: https://mrwayneo.github.io/   '
comment = f'[{datetime_now}] Tips are up in.   '

punters = """
* moechilli
* benny
* yoda
"""

tips =f'''
23:50 2021-07-16 killarney R3 7 Baltinglass Hill(8)   
15:15 2021-07-16 taree R6 1 Cool Missile(11)   
'''
resulted = f':boom: 2021-07-08 grafton R4 6 Far Too Easy(5)   '

todo = """
- [ ] Review/fix order of dated tables.
- [ ] Refactor punters app.
"""

leaderboard = """
|               |   runs |   wins |   profit |   sr |   roi |
|:--------------|-------:|-------:|---------:|-----:|------:|
| moechilli     |    124 |     65 |   5178.5 | 0.52 |  4.18 |
| yoda          |   3901 |    852 |  43207.9 | 0.22 |  1.11 |
| benny         |   1152 |    280 |   4038.3 | 0.24 |  0.35 |
| looseknot     |   1150 |    204 |   2660.5 | 0.18 |  0.23 |
| pangea        |   6054 |   1266 |   7281.8 | 0.21 |  0.12 |
| cosmo         |   8770 |    510 |   8733   | 0.06 |  0.1  |
| overthrow     |   2978 |    792 |   1526.8 | 0.27 |  0.05 |
| evenodds      |    210 |     87 |     54.7 | 0.41 |  0.03 |
| icyhot        |   1580 |    381 |   -675.4 | 0.24 | -0.04 |
| midnightrider |  13689 |   3340 |  -5067.8 | 0.24 | -0.04 |
| bender        |   1957 |    566 |  -1304.3 | 0.29 | -0.07 |
| shadowchaser  |   4409 |    811 |  -3902.3 | 0.18 | -0.09 |
| reaper        |  15783 |   5703 | -19009.5 | 0.36 | -0.12 |
| prometheus    |   4605 |   1582 |  -6277.1 | 0.34 | -0.14 |
| ghostball     |   4780 |   1642 |  -6594.8 | 0.34 | -0.14 |
"""

filename = f'/home/wayneo/play.markdown'

lines = [title, author, description, url, comment, punters, tips, resulted, 
	todo, leaderboard]

with open(filename, mode='wt', encoding='utf-8') as myfile:
    myfile.write('\n\n'.join(lines))
myfile.close()
