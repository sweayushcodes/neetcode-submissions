class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        # Initialize the result array with 0s. 
        # If a day never gets a warmer temperature, it naturally stays 0.
        res = [0] * n
        stack = []  # This will store only *indices*

        for i in range(n):
            current_temp = temperatures[i]
            
            # While stack is not empty AND current temp is warmer than the temp at the top of the stack
            while stack and current_temp > temperatures[stack[-1]]:
                prev_index = stack.pop()
                # Calculate the distance between the days
                res[prev_index] = i - prev_index
                
            # Push the current day's index onto the stack
            stack.append(i)
            
        return res
            