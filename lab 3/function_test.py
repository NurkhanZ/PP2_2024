#14

#Program takes input of integers, finds unique nums and then output histograms of unique lenghts
lst = list(map(int, input().split()))

def unique_list(nums):
    unique = []
    for x in nums:
        if x not in unique:
            unique.append(x)
    return(unique)
ulst = unique_list(lst)

def histogram(nums):
    for i in nums:
        print('*'*i)
histogram(ulst)

