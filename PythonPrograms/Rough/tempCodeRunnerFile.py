9, 5, 18, 2, 75, 45, 30, 55, 12, 80]
for i in range(len(lst)):
     for j in range(i+1,len(lst)):
          if lst[i]>lst[j]:
               lst[i],lst[j]  = lst[j],lst[i]

print(lst)