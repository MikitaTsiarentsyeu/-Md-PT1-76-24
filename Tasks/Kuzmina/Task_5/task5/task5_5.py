def get_ranges(nums):
    if not nums: 
        return ""

    ranges = []  
    start = nums[0] 
    end = nums[0]    

    for i in range(1, len(nums)):
        if nums[i] == end + 1:  
            end = nums[i]  
        else:  
            if start == end:
                ranges.append(str(start)) 
            else:
                ranges.append(f"{start}-{end}")  
            start = end = nums[i] 

    if start == end:
        ranges.append(str(start))
    else:
        ranges.append(f"{start}-{end}")

    return ", ".join(ranges)

print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]))