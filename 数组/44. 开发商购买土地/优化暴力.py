def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    n = int(data[idx])  # 读取行数
    idx += 1
    m = int(data[idx])  # 读取列数
    idx += 1
    sum = 0  # 初始化总和为0
    vec = []  # 初始化矩阵存储数据
    for i in range(n):
        row = []
        for j in range(m):
            num = int(data[idx])  # 读取矩阵中的每个数
            idx += 1
            row.append(num)  # 将数添加到当前行
            sum += num  # 累加到总和中
        vec.append(row)  # 将当前行添加到矩阵中

    result = float('inf')  # 初始化结果为无穷大
    
    count = 0  # 初始化行或列的累加和
    # 行切分
    for i in range(n):
        for j in range(m):
            count += vec[i][j]  # 累加当前行的值
            # 遍历到行末尾时候开始统计
            if j == m - 1:
                result = min(result, abs(sum - 2 * count))  # 更新最小差值

    count = 0  # 重置累加和，用于列切分
    # 列切分
    for j in range(m):
        for i in range(n):
            count += vec[i][j]  # 累加当前列的值
            # 遍历到列末尾时候开始统计
            if i == n - 1:
                result = min(result, abs(sum - 2 * count))  # 更新最小差值

    print(result)  # 输出最终的最小差值

if __name__ == "__main__":
    main()