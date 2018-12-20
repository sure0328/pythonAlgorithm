def main():
    d = [0.01,0.02,0.05,0.1,0.2,0.5,1.0] # 零钱的不同面值list
    d_num=[5,10,4,6,6,8,9] # 不同面值零钱数量
    s = 0 # 店家拥有的钱数总和
    for i in range(0, len(d_num)):
        s += d[i] * d_num[i] # 计算店家总共拥有的钱数
    charge = float(input("请输入需要找的零钱金额："))
    if charge > s:
	   # 当输入的金额比店家所拥有的总金额多时，无法进行找零
        print("找零金额过大")
        return 0
    # 我们的目的是用的钱币数量最少，需要最大限度利用所有面值大的钱币，
    # 因此从数组的面值大的元素开始遍历，如果未按顺序排列，需要首先进行排序。
    i = 6
    while i >= 0: 
        if sum >= d[i]:
            n = int(sum / d[i])
            if n >= d_num[i]:
                n = d_num[i] # 更新n
            sum -= n * d[i] # 贪心的关键步骤，令sum动态的改变
            print("需要使用%d个%1.2f元硬币"%(n, d[i]))
        i -= 1
if __name__ == "__main__":
    main()