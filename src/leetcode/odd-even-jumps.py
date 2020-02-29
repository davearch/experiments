class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        n = len(A)
        next_higher, next_lower = [0] * n, [0] * n
        
        # construct next_higher list
        stack = [] # monotonic stack -> always decreasing
        # sort indexes by value -> smallest to largest
        for v,i in sorted([v,i] for i,v in enumerate(A)):
            # while the stack is not empty and the current index is greater than the last element in the stack:
            while stack and i > stack[-1]:
                # from the last index of the stack, i is the next higher value
                next_higher[stack.pop()] = i
            stack.append(i) # place indexes into stack smallest first (monotonic stack)
        
        # construct next_lower list
        stack = []
        for v,i in sorted([-v,i] for i,v in enumerate(A)): # sort indexes by value -> smallest to largest
            while stack and i > stack[-1]:
                next_lower[stack.pop()] = i
            stack.append(i)
        
        odd, even = [0] * n, [0] * n
        odd[-1] = even[-1] = 1 # last index is always good
        
        # dynamic programming -> move backwards through array and keep track of good indexes
        for i in range(n-1)[::-1]:
            odd[i] = even[next_higher[i]] # if we are odd at this index -> we look to see if the next highest index of an even jump will be good. if it is then this index is good also.
            even[i] = odd[next_lower[i]]
        return sum(odd) # only return the sum of odd because odd is from the starting index