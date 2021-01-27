# 1
def tvakan_girq(hexinak, **kwargs):
    list1 = list(kwargs.keys())
    list2 = list(kwargs.values())
    list3 = []
    for i in range(len(list2)):
        if hexinak in list2[i]:
            list3.append((list2[i][list2[i].index(hexinak) + 1], list1[i]))
    list3.sort()
    for i in range(len(list3)):
        print(list3[i][1])


tvakan_girq('mark lutz', book1 = ['mark lutz', 1998], book2 = ['Tolstoy ', 1706], book3 = ['mark lutz', 1985])


# 2
list1 = [9,5,8,5,20,1,2,-3,-2,-1,0]
list1.sort()
if list1[0] * list1[1] * list1[-1] > list1[-1] * list1[-2] * list1[-3]:
    print(list1[0] * list1[1] * list1[-1])
else:
    print(list1[-1] * list1[-2] * list1[-3])









# 3
#def non_decreasing_sequence(*nums):
    #nums1 = list(nums)
    #for i in range(2, len(nums1)):
        #if nums1[i - 2] >= nums1[i - 1] >= nums1[i]:
            #nums1[i - 2] = 0 - nums1[i - 2]
        #if nums1[i - 2] <= nums1[i - 1] >= nums1[i]:
            #nums1[i - 1] = 0 - nums1[i - 1]
        #if nums1[i - 2] <= nums1[i - 1] <= nums1[i]:
            #nums1[i] = 0 - nums1[i]
    #if nums1 == sorted(nums1):
        #return 'Yes', nums1
    #return 'No'


#print(non_decreasing_sequence(1, -1, -2, 3, 6))