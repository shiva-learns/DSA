# https://leetcode.com/problems/sort-characters-by-frequency/description/
class Solution:
    def frequencySort(self, s: str) -> str:      
        
        num_dict = {}
        for x in s:
            if x not in num_dict:
                num_dict[x] = 1
            else:
                num_dict[x] += 1
            
        rev_dict = {}
        for key,val in num_dict.items():
            if val not in rev_dict:
                rev_dict[val] = [key]
            else:
                rev_dict[val].append(key)

        key_sorted = sorted(rev_dict.keys(),reverse=True)
        
        result = []
        for x in key_sorted:
            for y in rev_dict[x]:
                result.append(y*x)
        
        return "".join(result)


"""
T.C -> O(nlogn)
S.C -> O(n)

Approach: Frequency Counting + Grouping + Sorting

"""


