Quick select code
```
k =len (nums)-k
def quickselect(l,r):
pivot,p = nums[r],l
for i in range(l,r):
if nums[i]<=pivot:
nums[p],nums[i]= nums[i],nums[p]
p+=1
nums[p],nums[r]= nums[r],nums[p]
if p>k: return quickselect(1,p-1)
elif p<k: return quickselect(p+l,r)
else: return nums[p]
return quickselect(0,len(nums)-1)
```