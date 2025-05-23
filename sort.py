def sorted1(num):
    i=0
    n=len(num)
    while i<n-1:
        m=i
        j=i+1
        while j<n:
            if num[j]<num[m]:
                m=j
            j+=1
        num[i], num[m]=num[m], num[i]
        i+=1
    return num
print(sorted1([29, 10, 14, 37, 13]))