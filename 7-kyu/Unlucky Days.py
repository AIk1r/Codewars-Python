from datetime import date

def unlucky_days(year):
	return sum(date(year, month, 13).isoweekday() == 5 for month in range(1, 13))
