class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        result = [0] * n
        prev_time = 0

        for log in logs:
            func_id, action, timestamp = log.split(':')
            func_id, timestamp = int(func_id), int(timestamp)

            if action == 'start':
                if stack:
                    result[stack[-1]] += timestamp - prev_time
                stack.append(func_id)
                prev_time = timestamp
            else:
                result[stack.pop()] += timestamp - prev_time + 1
                prev_time = timestamp + 1

        return result