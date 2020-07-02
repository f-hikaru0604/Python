print("身長を入力してください")
height = int(input())/100
print("体重を入力してください")
weight = int(input())
bmi = weight / (height ** 2)
if bmi < 18.5 :
    figure = "やせ"
elif bmi < 25 :
    figure = "標準"
elif bmi < 30 :
    figure = "肥満"
else:
    figure = "高度肥満"
print("あなたは「" + str(taikei) + "」です。")