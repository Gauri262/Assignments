ls=[1,5,6,2,3,7,8,4]
print("sum is: ",sum(ls))
print("largest is: ",max(ls))
print("smallest is: ",min(ls))
ls.sort()
print("Ascending: ",ls)
ls.sort(reverse=True)
print("Descending is: ",ls)
t=tuple(ls)
print("Tuple: ",t)
del ls
print(ls)