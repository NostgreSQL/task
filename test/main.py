










a = input()
count = 0
one = (a.find('е'))
for i in range(one, len(a)):
     if a[i] == 'е':
         print(i)
         break
print(one)