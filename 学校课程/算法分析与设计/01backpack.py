import numpy as np
#多个（n）物品，每种物品都有自己的重量（w_i）和价值（v_i），在限定的总重量/总容量（C）内，
#选择其中若干个（也即每种物品可以选0个或1个），设计选择方案使得物品的总价值最高。

#setting parameters
value_list = [1,6,18,22,28]
weight_list = [1,2,5,6,7]
n = 5
w = 11

#p(i,W):在前 i 个物品中挑选总重量不超过W的物品，每种物品最多只能1个
#最优值为 m（i，W） = max{m（i-1，W），m（i-1，W-wi）+vi}
'''
def solve(vlist,wlist,totalWeight,totalLength):
    m = np.zeros((totalLength + 1,totalWeight + 1),dtype = np.int32)
    for i in range(1,totalLength + 1):
        for j in range(1,totalWeight + 1):
            if wlist[i] <= j:
                m[i,j] = max(m[i-1,j],m[i-1,j-wlist[i]]+vlist[i])
            else:
                m[i,j] = m[i-1,j]
    print(m)
    return m[-1,-1] 
'''
def bag(n, c, w, v):
    """
    n 物品的数量，
    c 书包能承受的重量，
    w 每个物品的重量，
    v 每个物品的价值
    """
    # 置零，表示初始状态
    value = [[0 for j in range(c + 1)] for i in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, c + 1):
            value[i][j] = value[i - 1][j]
            # 背包总容量够放当前物体，遍历前一个状态考虑是否置换
            if j >= w[i - 1] and value[i][j] < value[i - 1][j - w[i - 1]] + v[i - 1]:
                value[i][j] = value[i - 1][j - w[i - 1]] + v[i - 1]
    for x in value:
        print(x)
    return value

def show(n, c, w, value):
    print('最大价值为:', value[n][c])
    x = [False for i in range(n)]
    j = c
    for i in range(n, 0, -1):
        if value[i][j] > value[i - 1][j]:
            x[i - 1] = True
            j -= w[i - 1]
    print('背包中所装物品为:')
    for i in range(n):
        if x[i]:
            print('第', i+1, '个,', end='')

#print(solve(value_list,weight_list,w,n))
print("初始的背包如下：价值、重量")
print(value_list)
print(weight_list)
print("装背包表格")
show(n,w,weight_list,bag(n,w,weight_list,value_list))
