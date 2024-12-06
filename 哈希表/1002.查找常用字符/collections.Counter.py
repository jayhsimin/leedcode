from typing import List
from collections import Counter
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # 使用 Counter 計算第一個字串中每個字母的頻率
        tmp = Counter(words[0])
        result = []  # 用於存儲結果的列表

        # 遍歷其餘的字串，計算每個字串的字母頻率，並與 tmp 取交集
        for i in range(1, len(words)):
            # 使用 & 取字母頻率的交集，保留每個字母在所有字串中的最小頻率
            tmp = tmp & Counter(words[i])

        # 遍歷交集結果中的每個字符
        for char in tmp:
            # 取出字符的頻率
            count = tmp[char]
            # 根據頻率將字符添加到結果列表中
            result.extend([char] * count)

        return result
