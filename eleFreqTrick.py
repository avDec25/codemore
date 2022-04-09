nums = [0, 1, 3, 4, 5]
n = len(nums)

for i in range(len(nums)): #delete those useless elements
    if nums[i]<0 or nums[i]>=n:
        nums[i]=0
print(nums)

fp = open("output.txt", "w")
fp.write(f"{nums}\n")
fp.write(f"=======================\n\n")

for i in range(len(nums)): #use the index as the hash to record the frequency of each number
    fp.write(f"i = {i}\n")
    fp.write(f"nums[nums[{i}]%{n}] += n\n")
    fp.write(f"nums[{nums[i]}%{n}] += n\n")
    fp.write(f"nums[{nums[i]%n}] += n\n")
    nums[nums[i]%n]+=n
    fp.write(f"{nums}\n")
    fp.write(f"=======================\n\n")
# at this point if we do nums[i]%n then we will get back the original nums, 
# on which this loop was performed

for i in range(1,len(nums)):
    # this is giving the frequency of elements
    if nums[i]/n==0:
        fp.write(f"\n{i}")
        break
print(nums)