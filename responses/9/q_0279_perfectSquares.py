front_matter = {
    "qid": 279,
    "title": "Perfect Squares",
    "titleSlug": "perfect-squares",
    "difficulty": "Medium",
    "tags": ["Math", "Dynamic Programming", "Breadth-First Search"],
}
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
class Solution:
    """Given an integer `n`, return *the least number of perfect square numbers that sum to* `n`.

    A **perfect square** is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, `1`, `4`, `9`, and `16` are perfect squares while `3` and `11` are not.



    **Example 1:**

    ```
    Input: n = 12
    Output: 3
    Explanation: 12 = 4 + 4 + 4.
    ```
    **Example 2:**

    ```
    Input: n = 13
    Output: 2
    Explanation: 13 = 4 + 9.
    """


    def numSquares(self, n: int) -> int:
        dp = [0] + [float('inf')] * n
        for i in range(1, n+1):
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j*j] + 1)
                j += 1
        return dp[n]