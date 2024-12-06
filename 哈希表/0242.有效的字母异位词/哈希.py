class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 建立一個長度為26的列表來記錄每個字母出現的次數
        # 因為英文字母一共有26個（a到z）
        record = [0] * 26

        # 遍歷字串s，統計每個字母的出現次數
        for i in s:
            # 將字母轉換成索引值 (相對於字母 'a')
            # 比如字母 'a' 對應索引 0，'b' 對應索引 1，以此類推
            record[ord(i) - ord("a")] += 1

        # 遍歷字串t，減少每個字母的出現次數
        for i in t:
            # 同樣通過索引值定位，將對應位置的計數減一
            record[ord(i) - ord("a")] -= 1

        # 檢查record陣列中的所有元素是否為0
        # 如果有任何一個元素不為0，表示字母出現次數不同
        for i in range(26):
            if record[i] != 0:
                # 若發現某個字母出現次數不同，返回False
                return False

        # 如果所有字母的出現次數都相等，返回True
        return True
