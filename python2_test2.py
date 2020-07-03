def leap(year):
    if year % 100 == 0 and year % 400 != 0:
        result = '閏年ではないです。'
    elif year % 4 == 0:
        result = '閏年です。'
    else:
        result = '閏年ではないです。'
    return result

print('西暦4桁を入力してください')
year0 = int(input())
i = -1
while i <= 1 :
    year = year0 + i
    print(str(year),'年は',leap(year))
    i += 1

