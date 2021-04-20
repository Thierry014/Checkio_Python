def long_repeat(line):
    count = 1 
    max_count = 1
    
    if not line:
        return 0
    
    cur = line[0]

    for i in range(1,len(line)):
        if line[i] == cur:
            count += 1
            max_count = max(count, max_count)
        else:
            count = 1 
            cur = line[i]
    return max_count


print(long_repeat('sdsffffse'))