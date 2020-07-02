print("身長を入力してください")
height = int(input())/100
print("体重を入力してください")
weight = int(input())
BMI = weight / (height**2)
if BMI < 18.5 :
    taikei = "やせ"
elif BMI < 25 :
    taikei = "標準"
elif BMI < 30 :
    taikei = "肥満"
else:
    taikei = "高度肥満"
print("あなたは「" + str(taikei) + "」です。")