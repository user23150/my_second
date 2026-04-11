import turtle as t  # 导入turtle模块并简写为t
def xuehua(order,length):  # 定义雪花绘制函数
    if order==0:
        t.fd(length)
    else:
        for i in [0,60,-120,60]:
            
            t.left(i)
            xuehua(order-1,length/3)
def main(order,length=300):  # 定义主函数
    t.speed(0) #  设置海龟绘图速度为最快（0）
    t.pensize(2)
    t.hideturtle()
    t.bgcolor("black")
    t.color("red") #  设置背景颜色为黑色
    t.penup()
    t.goto(200,0)
    t.pendown()
    for i in range(3):
        t.left(-120)
        xuehua(order,length)
    
    t.done()
main(order=2)

    