borrowing = 250000
annual_rate = 0.14
repayment_amount = 30000
month = 1
while repayment_amount < borrowing:
    month_interest = borrowing * annual_rate / 12
    borrowing -= repayment_amount - month_interest
    print(str(month),"ヶ月目：返済額=",str(repayment_amount),"円、残り",str(borrowing),"円")
    month += 1
print(str(month),"ヶ月目：返済額=",str(borrowing + (borrowing * annual_rate /12)),"、返済完了")
        
