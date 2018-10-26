
# this is my second python project

# 本次解决python集合和元祖的生成

b = input("请输入你要生成的集合的数列的个数：")
b = int(b)
str = input("请输入你要生成的对象：如：list，tuple")

def connection(b,str):
    if ""==str:
        raise Error("你还没有输入类型")
    elif "list"==str:
        return list(range(b))
    elif "tuple"==str:
        return tuple(range(b))
    elif "set"==str:
        return set(list(range(b)))
print (connection(b,str))




