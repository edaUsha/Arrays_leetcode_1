class Solution:
    def findValidPair(self, s: str) -> str:
        # Step 1: Create the frequency map
        freq_map = {}
        for char in s:
            freq_map[char] = freq_map.get(char, 0) + 1
        
        # Step 2: Iterate through all adjacent pairs
        # Stop at len(s) - 1 so s[i+1] is always safe
        for i in range(len(s) - 1):
            first_digit = s[i]
            second_digit = s[i+1]
            
            # The two adjacent digits must be distinct
            if first_digit != second_digit:
                # Each digit's frequency must match its integer value
                if freq_map[first_digit] == int(first_digit) and freq_map[second_digit] == int(second_digit):
                    return s[i:i+2]
                    
        return ""
