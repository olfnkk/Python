def find_min(num):
    min_value=num[0]
    i_min=0
    for i in range(1, len(num)):
        if min_value>num[i]:
            min_value=num[i]
            i_min = i
    return min_value
print(find_min([1,2,3,4,5]))