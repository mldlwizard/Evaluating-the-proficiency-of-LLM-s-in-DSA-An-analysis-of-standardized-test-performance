from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas = 0
        total_cost = 0
        curr_gas = 0
        start_idx = 0

        for i in range(len(gas)):
            total_gas += gas[i]
            total_cost += cost[i]
            curr_gas += gas[i] - cost[i]

            if curr_gas < 0:
                start_idx = i + 1
                curr_gas = 0
        
        return start_idx if total_gas >= total_cost else -1
