

# this is my first python


# 这是解决一元二次方程的解

first = input("请输入第一个数字：")
a = int(first)
second = input("请输入第二个数字：")
b = int(second)
third = input("请输入第三个数字：")
c = int(third)
def quadratic(a, b, c):
    if not isinstance(a,(int)):
        raise TypeError("bad operand type")
    if a ==0:
        return -c/b
    else:
        y1=(-b-math.sqrt(abs(b*b-4*a*c)))/2*a
        y2=(-b+math.sqrt(abs(b*b-4*a*c)))/2*a
        if y1==y2:
            return y1
        else:
            return y1,y2

print (quadratic(a,b,c))
