class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        while tickets[k] != 0:
            for i in range(len(tickets)):
                if tickets[i] >= 1 and tickets[k] != 0:
                    tickets[i] -= 1
                    time += 1
        return time