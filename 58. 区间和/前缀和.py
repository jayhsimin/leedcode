
import sys
input = sys.stdin.read  # 使用 sys.stdin.read 來讀取所有輸入數據

def main():
    data = input().split()  # 將輸入的數據按空格分割成列表
    index = 0  # 初始化索引，用於追踪當前讀取到的數據位置
    n = int(data[index])  # 讀取第一個數據，表示數組的長度
    index += 1  # 索引向後移動一位
    vec = []  # 初始化數組，用於存儲輸入的數據
    for i in range(n):
        vec.append(int(data[index + i]))  # 將字符串轉換為整數後添加到數組中
    index += n  # 索引向後移動n位，跳過已經讀取的數據

    p = [0] * n  # 初始化前綴和數組，長度為n
    presum = 0  # 初始化前綴和變量
    for i in range(n):
        presum += vec[i]  # 累加當前元素到前綴和中
        p[i] = presum  # 將當前的前綴和存儲到前綴和數組中

    results = []  # 初始化結果列表，用於存儲區間和的結果
    while index < len(data):  # 當索引小於數據長度時，處理每一對區間
        a = int(data[index])  # 讀取區間起始位置
        b = int(data[index + 1])  # 讀取區間結束位置
        index += 2  # 索引向後移動兩位，跳過已經讀取的區間數據

        if a == 0:
            sum_value = p[b]  # 如果起始位置為0，直接取前綴和數組中的第b個元素
        else:
            sum_value = p[b] - p[a - 1]  # 否則計算區間[a, b]的和

        results.append(sum_value)  # 將計算結果添加到結果列表中

    for result in results:
        print(result)  # 輸出所有的區間和結果

if __name__ == "__main__":
    main()
