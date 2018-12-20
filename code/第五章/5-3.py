def isvalid(str):
    count = 0  # 创建一个变量记录括号的数量
    for c in str:
        if c == '(':  # 遇到左括号就让变量加一
            count += 1
        elif c == ')':
            count -= 1  # 遇到右括号就让变量减一
            if count < 0:
                return False
    return count == 0


def bfs(str):
    res = []  # res存放最终结果
    queue = [str]  # 先把初始字符串加入队列
    while len(queue) > 0:  # 队列不为空的时候就开始广度优先遍历。
        for i in range(len(queue)):  # 依次从队列中取出字符串开始分析
            if isvalid(queue[i]):
                res.append(queue[i])  # 发现合法字符串就放到结果集里
            if len(res) > 0:
                return list(set(res))  # 如果发现合法字符串就结束掉循环返回结果，并用集合去重
        temp = []  # 建立临时结果集
        for s in queue:  # 取出队列中每一个字符串
            for i in range(len(s)):  # 对于每个字符串，分别查看每个字符
                if s[i] == '(' or s[i] == ')':
                    temp.append(s[:i] + s[i + 1:])
        queue = list(set(temp))  # 把新生成的字符串赋值给队列，并用set()函数去重
        return list(set(res))  # 先把数组转换为集合，再转换回数组来去重
