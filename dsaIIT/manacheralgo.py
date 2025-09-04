class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        # Preprocess the string: insert '#' between characters
        # This handles both odd and even length palindromes uniformly
        processed = '#'.join('^{}$'.format(s))
        n = len(processed)
        
        # Array to store radius of palindrome at each position
        P = [0] * n
        center = 0  # Center of the rightmost palindrome
        right = 0   # Right boundary of the rightmost palindrome
        
        max_len = 0
        center_index = 0
        
        for i in range(1, n - 1):
            # Mirror of i with respect to center
            mirror = 2 * center - i
            
            # If i is within the right boundary, we can use previously computed values
            if i < right:
                P[i] = min(right - i, P[mirror])
            
            # Try to expand palindrome centered at i
            try:
                while processed[i + (1 + P[i])] == processed[i - (1 + P[i])]:
                    P[i] += 1
            except IndexError:
                pass
            
            # If palindrome centered at i extends past right, update center and right
            if i + P[i] > right:
                center = i
                right = i + P[i]
            
            # Update maximum length palindrome
            if P[i] > max_len:
                max_len = P[i]
                center_index = i
        
        # Extract the actual palindrome from original string
        start = (center_index - max_len) // 2
        return s[start:start + max_len]


class SolutionDetailed:
    """More detailed version with comments and visualization"""
    
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        # Step 1: Preprocess string
        # "abb" -> "^#a#b#b#$"
        processed = self._preprocess(s)
        n = len(processed)
        
        # Step 2: Initialize arrays and variables
        P = [0] * n  # P[i] = radius of palindrome centered at i
        center = 0   # Center of rightmost palindrome so far
        right = 0    # Right edge of rightmost palindrome so far
        
        max_len = 0
        center_index = 0
        
        print(f"Original: {s}")
        print(f"Processed: {processed}")
        print(f"Positions: {' '.join(str(i) for i in range(n))}")
        print()
        
        # Step 3: Main algorithm
        for i in range(1, n - 1):
            mirror = 2 * center - i  # Mirror of i across center
            
            # Use symmetry if possible
            if i < right:
                P[i] = min(right - i, P[mirror])
            
            # Expand around center i
            try:
                while processed[i + 1 + P[i]] == processed[i - 1 - P[i]]:
                    P[i] += 1
            except IndexError:
                pass
            
            # Update center and right if we expanded past right
            if i + P[i] > right:
                center = i
                right = i + P[i]
            
            # Track longest palindrome
            if P[i] > max_len:
                max_len = P[i]
                center_index = i
            
            print(f"i={i}, char='{processed[i]}', P[i]={P[i]}, center={center}, right={right}")
        
        print(f"\nP array: {P}")
        print(f"Max length: {max_len} at center {center_index}")
        
        # Extract result
        start = (center_index - max_len) // 2
        result = s[start:start + max_len]
        print(f"Result: '{result}' (start={start}, length={max_len})")
        
        return result
    
    def _preprocess(self, s: str) -> str:
        """Convert 'abb' to '^#a#b#b#$'"""
        return '^#' + '#'.join(s) + '#$'


# Test both implementations
def test_manacher():
    solution = Solution()
    detailed = SolutionDetailed()
    
    test_cases = ["babad", "cbbd", "abb", "a", "ac"]
    
    for test in test_cases:
        print("=" * 50)
        print(f"Testing: '{test}'")
        print("=" * 50)
        
        result = solution.longestPalindrome(test)
        print(f"Result: '{result}'\n")
        
        # Uncomment below for detailed trace
        # detailed.longestPalindrome(test)
        # print()

test_manacher()