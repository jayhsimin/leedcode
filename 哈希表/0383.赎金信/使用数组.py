class Soiution:
    def canConstruct(self,ransomNote: str, magazine: str) ->bool:
        """
        解題思路:
        1. 使用兩個長度為26的數組分別記錄ransomNote和magazine中每個字母出現的次數
        2. 遍歷ransomNote和magazine,統計每個字母出現的次數
        3. 判斷ransomNote中的每個字母出現次數是否都不超過magazine中對應字母的出現次數
        時間複雜度: O(n), 空間複雜度: O(1)
        """
        # 創建兩個長度為26的數組,用於記錄字母出現次數
        ransom_count=[0]*26
        magazine_count=[0]*26
        
        # 統計ransomNote中每個字母出現的次數
        for c in ransomNote:
            # ord()函數返回字符的Unicode碼點值
            # ord(c)獲取字符c的ASCII碼值
            # ord('a')獲取字母'a'的ASCII碼值(97)
            # 相減得到字母c在字母表中的索引(0-25)
            ransom_count[ord(c)-ord('a')] += 1
            # ord('a') 則是返回字母 'a' 的 ASCII 代碼，這個代碼是 97。
            # ord('z') 代碼是 110。
            
        # 統計magazine中每個字母出現的次數
        for c in magazine:
            magazine_count[ord(c) - ord('a')] += 1
            
        # 判斷ransomNote中的每個字母出現次數是否都不超過magazine中對應字母的出現次數
        return all(ransom_count[i] <= magazine_count[i] for i in range(26))