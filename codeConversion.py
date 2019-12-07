# 误码率在53%左右
import random
import math




# 随机生成信源 100bit 双极性不归零码
def bit():
    number = []
    for i in range(0, 100):
        num = random.randint(0, 1)
        number.append(num)
    return number


# 将信源进行AMI码型变换
def AMI(a):
    lenth = len(a)
    num = 0
    for i in range(0, lenth):
        if(a[i] == 1):
            num = num+1
            if(num % 2 == 0):
                a[i] = a[i]*(-1)
    return a


# 仿高斯信道，产生大小范围为-50到50的随机噪声 加到信号上
def noises():
    noise=random.normalvariate(0,1)   #生成均值为0 方差为1 的随机数
    return noise

#sa函数
def sinc(x):
    if(3.14*x==0):
        y=1
    else:
        y=math.sin(3.14*x)/(3.14*x)
    return y

def rcosdesign (beta,span, sps):
    delay=int(span*sps/2)
    # print(delay)
    t=[]
    denom=[]
    for i in range(-delay,delay+1):
        a=(i/sps)
        t.append(a)
    # print(t)
    for i in t:
        a=((1-math.pow(2*beta*i,2)))
        denom.append(a)
    # print(denom)
    flage=1.4901e-08
    idx1=[]
    idx2=[]
    b=[]
    for i in range(0,len(t)):
        if(abs(denom[i])>flage):
            idx1.append(i-12)   #idx存储分母非零的时间点
        else:
            idx2.append(i-12)
    # print("非零时刻：")
    # print(idx1)
    # print("零时刻：")
    # print(idx2)
    for i in range(0,len(t)):
        q=i-12
        if q in  idx1:
            a=sinc(t[i])*(math.cos(3.14*beta*t[i])/denom[i])/sps
        if q not in idx1:
            a=beta*math.sin(3.14/(2*beta))/(2*sps)
        b.append(a)
    # print(b)
    return b

def show():
    b=bit()
    p1=[]
    print(b)
    for i in range(0,100):
        first=b[i]+noises()
        p1.append(first)
    all=AMI(p1)
    p=rcosdesign(0.15,16,8)
    c=[]
    for i in range(0,100):
        a=0
        # for j in range(0,len(p)):
        a=all[i]*p[i]+a
        c.append(a)
    print(c)
    # print(c)
    for i in range(0,100):
        if(c[i]>0.0055):
            c[i]=1
        else:
            c[i]=0
    print(c)
    l=0
    for i in range(0,100):
        if(c[i]==b[i]):
            l=l+1
        
    final=l/100
    print(final)
    return final
    

                



def main():
    a=0
    for i in range(0,20):
        a=show()+a
    print(a/20)
main()
