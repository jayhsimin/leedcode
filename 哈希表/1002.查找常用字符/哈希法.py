from typing import List

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # 如果輸入的列表為空，直接返回空列表
        if not words:
            return []

        # 初始化結果列表
        result = []

        # 初始化一個長度為26的陣列，紀錄第1個字串中每個字母的出現次數
        # 'a' 對應索引0, 'b' 對應索引1，依此類推
        hash = [0] * 26
        for c in words[0]:  # 遍歷第1個字串
            hash[ord(c) - ord('a')] += 1  # 計算每個字母的出現次數

        # 遍歷剩餘的字串，更新 `hash` 陣列
        for i in range(1, len(words)):
            # 為當前字串初始化一個新的計數陣列
            hashOtherStr = [0] * 26
            for c in words[i]:  # 計算當前字串的每個字母出現次數
                hashOtherStr[ord(c) - ord('a')] += 1
            
            # 更新 `hash` 陣列，保留每個字母在所有字串中出現的最小次數
            for k in range(26):
                hash[k] = min(hash[k], hashOtherStr[k])

        # 將 `hash` 中的字符次數轉換為結果
        for i in range(26):
            while hash[i] > 0:  # 如果該字母在所有字串中都有出現
                result.append(chr(i + ord('a')))  # 將字母添加到結果列表
                hash[i] -= 1  # 減少該字母的計數

        return result
solution = Solution()
print(solution.commonChars(["bella", "label", "roller"]))  # Output: ['e', 'l', 'l']
print(solution.commonChars(["cool", "lock", "cook"]))      # Output: ['c', 'o']
print(solution.commonChars(["abcd", "efgh", "ijkl"]))      # Output: []
