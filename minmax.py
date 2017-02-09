def max_min(alist):
	if isinstance(alist,list):
		for x in range(len(alist)-1, 0, -1):

       maxValue = 0
       minValue = alist[0]

       for i in range(1,x+1):
           if alist[i] > alist[maxValue]:
               maxValue = x

       temp = alist[x]
       alist[x] = alist[maxValue]
       alist[maxValue] = temp()

alist = [54,26,93,17,77,31,44,55,20]
max_min(alist)

print(minValue, alist[maxValue])