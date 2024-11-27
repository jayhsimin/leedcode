def main():
    import sys
    # 将 input 变量赋值为 sys.stdin.read 函数
    # 这样做的目的是为了从标准输入流中读取所有输入直到 EOF
    # 使用方法：data = input() 会读取所有输入内容并返回一个字符串
    # 将 input 变量赋值为 sys.stdin.read 函数，允许从标准输入流中一次性读取所有输入直到 EOF
    input = sys.stdin.read
    data = input().split()

    idx = 0
    n = int(data[idx])  # 从输入数据中读取行数n
    idx += 1
    m = int(data[idx])  # 从输入数据中读取列数m
    idx += 1
    sum = 0  # 初始化矩阵元素总和为0
    vec = []  # 初始化矩阵列表
    for i in range(n):
        row = []
        for j in range(m):
            num = int(data[idx])  # 读取矩阵中的元素
            idx += 1
            row.append(num)  # 将元素添加到当前行
            sum += num  # 将元素值累加到总和中
        vec.append(row)  # 将当前行添加到矩阵列表中

    # 统计横向各行的和
    horizontal = [0] * n
    for i in range(n):
        for j in range(m):
            horizontal[i] += vec[i][j]  # 累加第i行的元素和

    # 统计纵向各列的和
    vertical = [0] * m
    for j in range(m):
        for i in range(n):
            vertical[j] += vec[i][j]  # 累加第j列的元素和

    result = float('inf')  # 初始化最小差值为无穷大
    horizontalCut = 0  # 初始化横向切割的累计和为0
    for i in range(n):
        horizontalCut += horizontal[i]  # 累加横向切割的行和
        result = min(result, abs(sum - 2 * horizontalCut))  # 更新最小差值

    verticalCut = 0  # 初始化纵向切割的累计和为0
    for j in range(m):
        verticalCut += vertical[j]  # 累加纵向切割的列和
        result = min(result, abs(sum - 2 * verticalCut))  # 更新最小差值

    print(result)  # 输出最终计算的最小差值

if __name__ == "__main__":
    main()