def q3(start,end,divisor):
    result = []
    for i in range(start, end+1):
        if i%divisor == 0:
            result.append(i)
    return result

print(q3(0,30,3))