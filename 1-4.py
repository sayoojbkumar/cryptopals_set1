import binascii
a=[]
b=[]
for i in range(327):
   s=input()
   a.append(s)
for j in a:
   nums = binascii.unhexlify(j)
   key = max(nums, key=nums.count) ^ ord(' ')
   print(''.join(chr(num ^ key) for num in nums))
   print(key)
