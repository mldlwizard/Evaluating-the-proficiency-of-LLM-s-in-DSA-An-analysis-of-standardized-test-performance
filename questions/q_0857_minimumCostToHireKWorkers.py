front_matter = {
    "qid": 857,
    "title": "Minimum Cost to Hire K Workers",
    "titleSlug": "minimum-cost-to-hire-k-workers",
    "difficulty": "Hard",
    "tags": ["Array", "Greedy", "Sorting", "Heap (Priority Queue)"],
}
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
class Solution:
    """There are `n` workers. You are given two integer arrays `quality` and `wage` where `quality[i]` is the quality of the `i^{th}` worker and `wage[i]` is the minimum wage expectation for the `i^{th}` worker.

    We want to hire exactly `k` workers to form a paid group. To hire a group of `k` workers, we must pay them according to the following rules:

    1. Every worker in the paid group should be paid in the ratio of their quality compared to other workers in the paid group.
    2. Every worker in the paid group must be paid at least their minimum wage expectation.

    Given the integer `k`, return *the least amount of money needed to form a paid group satisfying the above conditions*. Answers within `10^{-5}` of the actual answer will be accepted.



    **Example 1:**

    ```
    Input: quality = [10,20,5], wage = [70,50,30], k = 2
    Output: 105.00000
    Explanation: We pay 70 to 0^{th} worker and 35 to 2^{nd} worker.
    ```
    **Example 2:**

    ```
    Input: quality = [3,1,10,10,1], wage = [4,8,2,2,7], k = 3
    Output: 30.66667
    Explanation: We pay 4 to 0^{th} worker, 13.33333 to 2^{nd} and 3^{rd} workers separately.
    ```


    **Constraints:**

    * `n == quality.length == wage.length`
    * `1 <= k <= n <= 10^{4}`
    * `1 <= quality[i], wage[i] <= 10^{4}`
    """

    def mincostToHireWorkers(
        self, quality: List[int], wage: List[int], k: int
    ) -> float:
        pass

    # If you have multiple solutions, add them all here as methods of the same class.