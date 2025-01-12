class Solution:
    """Given a string `s`, return *the longest* *palindromic* *substring* in `s`.

    **Example 1:**

    ```
    Input: s = "babad"
    Output: "bab"
    Explanation: "aba" is also a valid answer.
    ```
    **Example 2:**

    ```
    Input: s = "cbbd"
    Output: "bb"
    ```

    **Constraints:**

    * `1 <= s.length <= 1000`
    * `s` consist of only digits and English letters.
    """

    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2 or s == s[::-1]:
            return s

        start = 0
        max_len = 1

        for i in range(1, len(s)):
            even = s[i - max_len:i+1]
            odd = s[i - max_len - 1:i + 1]

            if i - max_len - 1 >= 0 and odd == odd[::-1]:
                start = i - max_len - 1
                max_len += 2
            elif i - max_len >= 0 and even == even[::-1]:
                start = i - max_len
                max_len += 1

        return s[start:start + max_len]
