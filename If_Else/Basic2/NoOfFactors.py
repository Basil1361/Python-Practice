def noOffactors(n):
    count = 0
    for i in range(1,n+1):
        if n % i == 0:
            count += 1
        else:
            continue
    print(count)
        
noOffactors(6)