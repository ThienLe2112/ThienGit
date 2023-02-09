a=[1,2,3,'a','b','c',3,6,8]
temp=0
i=0
while i< len(a)+1:
    try:
        temp=temp+a[i]
        i=i+1
    except:
        i=i+1
print('tong cac so trong mang cho san la: ' + str(temp) + ' don vi')