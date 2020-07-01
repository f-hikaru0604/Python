print("身長を入力してください")
height = int(input())
print("体重を入力してください")
weight = int(input())
BMI = weight / (height**2)
taikei = "やせ"
if BMI < 18.5 :
    taikei = "やせ"
elif 18.5 <= BMI < 25 :
    taikei = "標準"
elif 25 <= BMI < 30 :
    taikei = "肥満"
else:
    taikei = "高度肥満"
print("あなたは「" + str(taikei) + "」です。")