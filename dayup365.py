#dayup365.py
def f(dayfactor):
    end=1
    for i in range(365):
        if i %7 in [0,6]:
            end*=(1-0.01)
        else:
            end*=(1+dayfactor)
    return end
dayfactor=0.001
def fn(factor):
    end=1
    for i in range(365):
        end*=(1+factor)
    return end
while f(dayfactor)<fn(0.01):
    dayfactor+=0.001
print(f(dayfactor))
print(dayfactor)
print(fn(0.01))#0.01是每天1%的收益
