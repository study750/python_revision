list =[1,2,3,4,5]
list2 = [i for i in list if i%2==0]
list3 = [i*i for i in list if i%2==0]
print(list2)
print(list3)



dict={num:sq for num,sq in zip(list2,list3) }
print(dict)
