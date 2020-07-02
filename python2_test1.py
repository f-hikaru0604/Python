def cal(speed,distance):
    time = distance / speed
    return time

print('速度を入力してください(km/h)')
speed = int(input())
print('距離を入力してください(km)')
distance = int(input())
print(str(cal(speed,distance)),"時間")

