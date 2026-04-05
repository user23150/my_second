'''
import random as r
t=0
n=0
pi=1
while 1:
        x,y=r.random(),r.random()
        t+=1
        if pow(x,2)+pow(y,2)<=1:
            n+=1
        pi=n*4/t
        if 3.13>=pi>=3.14:
            break
        if t>=1000000:
            break
print(t)
print(pi)
'''
import random as r

# --- 设置目标 ---
target_pi = 3.1415926
# 我们希望误差小于这个值，这决定了我们的精度
tolerance = 0.0001
# 设置一个非常大的上限，防止程序永远跑不完
max_iterations = 500000000  # 5亿次

t = 0  # 总点数
n = 0  # 圆内点数

print(f"开始计算，目标精度：误差 < {tolerance}")

while t < max_iterations:
    t += 1
    x, y = r.random(), r.random()

    if pow(x, 2) + pow(y, 2) <= 1:
        n += 1

    # 每投1000万次，汇报一次进度
    if t % 10000000 == 0:
        pi = n * 4 / t
        error = abs(pi - target_pi)
        print(f"已投点 {t:,} 次 -> π ≈ {pi:.7f} (误差: {error:.7f})")

    # 判断是否达到精度要求
    pi = n * 4 / t
    if abs(pi - target_pi) < tolerance:
        print("\n🎉 达到目标精度！")
        break

# 最终结果
print("\n=== 最终结果 ===")
print(f"总投点次数: {t:,}")
print(f"计算出的π值: {pi:.7f}")
print(f"与真实值的误差: {abs(pi - target_pi):.7f}")
