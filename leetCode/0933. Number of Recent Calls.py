from collections import deque


class RecentCounter:
    def __init__(self):
        # 建立佇列存放空間
        self.queue = deque()

    def ping(self, t: int) -> int:
        queue = self.queue
        # 把每次呼叫 ping 時間點紀錄到 deque
        queue.append(t)
        # 判斷前面時間呼叫是否有超過3000毫秒
        while queue[0] < t - 3000:
            queue.popleft()
        return len(queue)


# 測試程式碼
if __name__ == "__main__":
    recentCounter = RecentCounter()
    print(recentCounter.ping(1))    # 輸出應為 1
    print(recentCounter.ping(100))  # 輸出應為 2
    print(recentCounter.ping(3001))  # 輸出應為 3
    print(recentCounter.ping(3002))  # 輸出應為 3
