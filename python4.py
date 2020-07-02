kariire = 250000
nennritu = 0.14
hennsaigaku = 30000
zanngaku = kariire
i = 1
while hennsaigaku < zanngaku:
    risi = zanngaku * 0.14 / 12
    gannkinnbunn = hennsaigaku - risi
    zanngaku -= gannkinnbunn
    print(str(i),"ヶ月目：返済額=",str(hennsaigaku),"円、残り",str(zanngaku),"円")
    i += 1
    if zanngaku < hennsaigaku:
        
        print(str(i),"ヶ月目：返済額=",str(zanngaku + (zanngaku * 0.14 / 12)),"、返済完了。")