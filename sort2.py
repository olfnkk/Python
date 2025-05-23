def sorted2(num):
    i=1
    while i < len(num):
        key=num[i]
        j=i-1
        while j>=0 and num[j] > key:
            num[j+1]=num[j]
            j-=1
        num[j+1]=key
        i+=1
    return num
print(sorted2([29, 10, 14, 37, 13]))