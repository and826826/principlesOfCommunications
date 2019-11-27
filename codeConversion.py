# 将输入比特流变为HDB3码
import random

# 随机生成信源 100bit
def bit():
    number = []
    for i in range(0, 100):
        num = random.randint(0, 1)
        number.append(num)
    return number

#将信源进行码型变换
print(bit())
