l = []
player = ["Mesii",10,True]
list("Happy")
list((1125,2436))
print(list({"menu":"pizza","price":10000})) #키만 리스트에 저장
list({"사과","배"})
nums = list(range(3))
print('nums : {0}'.format(nums)) #[0,1,2]

nums += [10,11]
nums += [10,11]
nums.append(20)
print(nums)
nums.append([30,31]) #append 그대로 끝에 값 추가, extend는 리스트 해제하여 값 추가
print(nums)
nums.insert(2,40)               
print(f'insert : {nums}') #index 2번에 40값 추가
nums.extend([50,51])
print(nums)

nums[7] = 60
print(nums[7])

del nums[2]

nums.remove(20)
print(nums)
print(nums.pop(5))

nums.append(10)
print(nums)
nums.remove(10)
print(nums)
nums.clear()
print(nums)

nums = list(range(3))
nums += [100,10]
nums[3]

print(len(nums))
print(nums.sort())

