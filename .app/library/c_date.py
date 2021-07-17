from datetime import datetime as dt
from datetime import timedelta as td 
from datetime import date as dt_date
import calendar

class Date():
	"""
	Receive date and convert to string or object.
	Base format: 01-01-2021
	output: 0 = string 
			1 = object 
	"""

	def __init__(self, date):
		self.date_format = "%Y-%m-%d"
		if isinstance(date, str):
			self.date = self.as_object(date)
		else:
			self.date = date
		self.string = self.as_string(self.date) 

	def output(self, date, out=0):
		as_string = [0, "as_string", "string", "str"]
		as_object = [1, "as_object", "object", "obj"]
		if out in as_string:
			return self.as_string(date)
		elif out in as_object:
			return self.as_object
		else:
			print(f'{date} format is out of range.')

	def print(self):
		return self.output(self.date)

	def as_string(self, date):
		if isinstance(date, str):
			return date
		else:
			return date.strftime(self.date_format)

	def as_object(self, date):
		if isinstance(date, str):
			return dt.strptime(date, self.date_format)
		else:
			return date

	def day_week(self, day=1, out=0):
		d = self.date
		day_of_week = calendar.weekday(d.year, d.month, d.day)
		first_day_week = d - td(days=day_of_week)
		new_day_of_week = 0 + day
		day_week = first_day_week + td(days=new_day_of_week)
		self.date = day_week
		return self.output(day_week, out)

	def day_month(self, day=1):
		d = self.date
		first_day_month = d.replace(day=1)
		return self.output(first_day_month)

	def day_month_year(self, month=1, day=1):
		d = self.date
		first_day_year = d.replace(month=1, day=1)
		return self.output(first_day_year)

	def past_days(self, days=1):
		d = self.date
		return self.output(d - td(days))

	def future_days(self, days=1):
		d = self.date
		return self.output(d + td(days))

	def past_months(self, months=1):
		d = self.date
		day = d.day
		month = (d.month - months) % 12
		year = d.year + ((d.month - months) // 12)
		new_date = dt_date(year, month, day)
		return self.output(new_date)

	def future_months(self, months=1):
		d = self.date
		day = d.day
		month = (d.month + months) % 12
		year = d.year + ((d.month + months) // 12)
		new_date = dt_date(year, month, day)
		return self.output(new_date)

	def last_day_month(self):
		d = self.date
		m = d.month
		y = d.year
		m_range = calendar.monthrange(y, m)[-1]
		last_day_month = dt_date(y, m, m_range)
		return self.output(last_day_month)


# Custom functions

def date_range_string(start_date, end_date, sep="|"):
	""



