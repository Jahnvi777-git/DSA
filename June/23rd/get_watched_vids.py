# link: https://leetcode.com/problems/get-watched-videos-by-your-friends/description/?envType=problem-list-v2&envId=d5qblqpi
from collections import deque
class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        n = len(watchedVideos)
        q = deque([id])
        used = [False for _ in range(n)]
        used[id] = True
        for _ in range(level):
            s = len(q)
            for x in range(s):
                node = q.popleft()
                for t in friends[node]:
                    if not used[t]:
                        q.append(t)
                        used[t] = True
        print(q)
        f = {}
        for x in q:
            for t in watchedVideos[x]:
                if t not in f: f[t] = 1
                else: f[t] += 1
        return sorted(f.keys(), key=lambda x: (f[x], x))
        
