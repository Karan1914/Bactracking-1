class Solution:
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.output = []
        
        
        candidates.sort()
        
        self.helper(0,[],target, candidates,0)
    
        return self.output
        
        
        
    def helper(self,currsum,out,target, candidates,index):
        # Base Case
        
        if currsum>target:
            return
        if currsum==target:
            self.output.append(list(out))
            #print(self.output)
            return
        for i in range(index,len(candidates)):
            val = candidates[i]
            out.append(val)
            #print(out)
            
            self.helper(currsum + val,out,target, candidates,i)
            
            out.pop()
            
            
        
        
        
            