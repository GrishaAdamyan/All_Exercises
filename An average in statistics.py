#list1 = [float(n) for n in input().split()]
#list1.sort()
#if len(list1) % 2 == 0:
    #print(sum(list1)/len(list1),(list1[len(list1)//2]+list1[len(list1)//2-1])/2)
#else:
    #print(sum(list1)/len(list1),list1[len(list1)//2])


numbers = [float(n) for n in input().split()] # [0, 1, 2, 3, 4]
mijtv = sum(numbers) / len(numbers)
numbers.sort()
kes = len(numbers) // 2 # 2
if len(numbers) % 2 == 0:
    mijn = (numbers[kes - 1] + numbers[kes]) / 2
    print(mijtv, mijn)
else:
    mijn = numbers[kes]
    print(f"{(mijtv):.2f}",f"{(mijn):.2f}")


#4 4 5 6 7
#5.2 5.0