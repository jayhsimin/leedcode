class Solution:
    def isHappy(self, n: int) -> bool:
        """
        判斷一個數是否為快樂數。
        定義：
        - 快樂數是一個正整數，對其進行每位數字平方和的計算，重複該過程，
          最終結果如果為 1，則為快樂數；如果進入循環，則不是快樂數。
        """
        # 使用集合記錄出現過的數字，避免無窮循環
        record = set()

        while n not in record:  # 當 n 尚未出現在集合中時，繼續處理
            record.add(n)  # 將 n 加入集合
            new_num = 0  # 初始化新的平方和結果
            n_str = str(n)  # 將數字轉為字串，方便逐位遍歷

            # 計算每位數字的平方和
            for digit in n_str:
                new_num += int(digit) ** 2  # 將每個位數轉為整數後平方，累加到新結果
            
            if new_num == 1:  # 如果平方和結果為 1，表示是快樂數
                return True
            else:
                n = new_num  # 否則更新 n 為新的平方和結果，繼續下一輪計算
        
        # 如果出現循環（n 已經在集合中），則不是快樂數
        return False
