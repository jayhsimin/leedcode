class Solution:
    def isHappy(self, n: int) -> bool:
        """
        判斷一個數是否為快樂數。
        快樂數定義：對一個正整數，重複對它的每個位數平方求和，
        如果最終結果為 1，則該數是快樂數；否則會進入循環，該數不是快樂數。
        """
        record = set()  # 用於記錄出現過的中間結果，防止陷入死循環

        while True:
            n = self.get_sum(n)  # 計算當前數字的每位平方和
            if n == 1:  # 如果結果為 1，返回 True
                return True
            
            if n in record:  # 如果當前數字已經出現過，說明陷入死循環
                return False
            else:
                record.add(n)  # 記錄當前數字

    def get_sum(self, n: int) -> int:
        """
        計算一個數字的每位數字平方和。
        例如：19 → 1^2 + 9^2 = 82
        """
        new_num = 0
        while n > 0:
            n, r = divmod(n, 10)  # 使用 divmod 分別獲取商和餘數
            # n是商，r是餘，用divmod做除法除以10
            new_num += r ** 2  # 累加每位數字的平方
        return new_num
sol=Solution()
a=sol.isHappy(789)
print(a)