class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = sorted(zip(difficulty, profit))
        worker.sort()
        
        max_profit = 0
        job_index = 0
        n = len(jobs)
        total_profit = 0
        
        for w in worker:
            while job_index < n and jobs[job_index][0] <= w:
                max_profit = max(max_profit, jobs[job_index][1])
                job_index += 1
            total_profit += max_profit
            
        return total_profit