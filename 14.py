class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""


        first_str = strs[0]

    
        for i in range(len(first_str)):
            char = first_str[i]

           
            for j in range(1, len(strs)):
                current_str = strs[j]

                
                if i == len(current_str) or current_str[i] != char:
                 
                    return first_str[:i]
        
    
        return first_str
