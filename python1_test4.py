borrowing = 250000
annual_rate = 0.14
repayment = 30000
month = 1
while 0 < borrowing:
    borrowing = borrowing * (1 + annual_rate / 12)
    if repayment < borrowing:
        borrowing -= repayment
        print(str(month),"ヶ月目：返済額=",str(repayment),"円、残り",str(borrowing),"円")
        
    else: 
        repayment = borrowing
        borrowing = 0
        print(str(month),"ヶ月目：返済額=",str(repayment),"、返済完了")
    month += 1