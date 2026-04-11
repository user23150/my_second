#斐波那契数列.py
try:
    def f(n):
        if n in [1,2]:
            return 1
        else:
            return f(n-1)+f(n-2)
    a=eval(input('请输入一个正整数：'))
    print(f(a))
except:
    print('输入错误')
