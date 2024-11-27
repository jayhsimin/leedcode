def generate_spiral_matrix_with_steps(n):
    # 初始化一个 n x n 的矩阵，所有元素为 0
    matrix = [[0] * n for _ in range(n)]
    
    # 初始化边界
    top, bottom = 0, n - 1  # 上边界和下边界
    left, right = 0, n - 1  # 左边界和右边界
    # 定義下標
    
    # 当前填充的数字
    num = 1
    
    # 当 num <= n^2 时，继续填充
    while num <= n * n:
        print(f"开始循环：num = {num}, top = {top}, bottom = {bottom}, left = {left}, right = {right}")
        
        # 从左到右填充当前 top 行
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1  # 更新上边界
        print(f"填充从左到右后，矩阵状态：")
        for row in matrix:
            print(row)
        
        # 从上到下填充当前 right 列
        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1  # 更新右边界
        print(f"填充从上到下后，矩阵状态：")
        for row in matrix:
            print(row)
        
        # 从右到左填充当前 bottom 行（如果还在范围内）
        if top <= bottom:
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = num
                num += 1
            bottom -= 1  # 更新下边界
            print(f"填充从右到左后，矩阵状态：")
            for row in matrix:
                print(row)
        
        # 从下到上填充当前 left 列（如果还在范围内）
        if left <= right:
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1  # 更新左边界
            print(f"填充从下到上后，矩阵状态：")
            for row in matrix:
                print(row)
    
    print(f"最终生成的矩阵：")
    for row in matrix:
        print(row)
    return matrix

# 测试代码
n = 3
generate_spiral_matrix_with_steps(n)
