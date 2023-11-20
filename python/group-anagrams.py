# Time: O(n * n log n)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # brute force: sort each string and add to a dictionary
        # go through each letter and see if there exists a value with the same?
        hashMap = {}

        for string in strs:
            sortedString = ''.join(sorted(string))

            if sortedString in hashMap:
                hashMap[sortedString].append(string)
            
            else:
                hashMap[sortedString] = [string]
        
        res = []

        for sortedString in hashMap:
            arr = []

            for string in hashMap[sortedString]:
                arr.append(string)
            
            res.append(arr)
        
        return res
