# link: https://leetcode.com/problems/relative-ranks/description/?envType=problem-list-v2&envId=d5qblqpi
class Solution(object):
    def findRelativeRanks(self, score):
        ans=[]
        a=score[::]
        d={}
        j=1
        a.sort(reverse=True)
        for i in range(len(a)):
            if a[i] not in d:
                d[a[i]]=j
                j+=1
        for i in score:
            if d[i]==1:
                ans.append("Gold Medal")
            elif(d[i]==2):
                ans.append("Silver Medal")
            elif(d[i]==3):
                ans.append("Bronze Medal")
            else:
                ans.append(str(d[i]))
        return ans