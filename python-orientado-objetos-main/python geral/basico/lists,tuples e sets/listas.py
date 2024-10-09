nums = [1,2,3,4,True,"antony"]
print(type(nums))

nums.append(3)
nums.append(float(input("meu numero ")))
nums.append(int(input("meu int ")))
nums.append([4,5,6,7,8])
nums.remove(4)
print(nums.reverse())
print(len(nums))

print(dir(nums))

nums[2]=122         #substitui a posição
nums.insert(1,22)   #insere o valor na posição especificada sem substituir o valor
print(nums)
nukes = [1,2,3,4,5,[1,90,50]]   #pode ser usado listas em listas
nukes = [1,2,3,4,5,1,90,50]
nakes = [1.3,2.1,3.33,4.22,5.2,[1.0,90.1,50.10]] #com floats tambem
nakes = [1.3,2.1,3.33,4.22,5.2,1.0,90.1,50.10] #com floats tambem
print("max",max(nukes))   #somente com listas ou de doubles ou de floats
print("min",min(nukes))   #somente com listas ou de doubles ou de floats
print("sum",sum(nukes))   #somente com listas ou de doubles ou de floats
print(nums[-1])
print(nums[-2])
print(nums[1])
print(nums[1:3])
print(nums[1:-1])
print(nums[1:])
print(nums[:-1])
print(nums[:])
print(nums[::2])
print(nums[::-1])
print(nums.index(3))
del nums[3]
print(help(nums))
del nums


