borrowing = 250000
annual_rate = 0.14
repayment_amount = 30000
month = 1
while 0 < borrowing:
    month_interest = borrowing * annual_rate / 12
    borrowing += month_interest
    if borrowing < repayment_amount:
        print(str(month),"ヶ月目：返済額=",str(borrowing),"、返済完了")
        break 
    borrowing = borrowing - repayment_amount
    print(str(month),"ヶ月目：返済額=",str(repayment_amount),"円、残り",str(borrowing),"円")
    month += 1