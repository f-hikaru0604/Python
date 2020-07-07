import datetime
def leap(year):
    if year % 100 == 0 and year % 400 != 0:
        result = False
    elif year % 4 == 0:
        result = True
    else:
        result = False
    return result

today = datetime.date.today()
this_year = today.year
i = -1
while i <= 1 :
    year = this_year + i
    if leap(year):
        print(str(year),'年は閏年です。')
    else:
        print(str(year),'年は閏年ではないです。')
    i += 1

