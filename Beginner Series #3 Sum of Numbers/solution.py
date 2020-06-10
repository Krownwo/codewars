def get_sum(a,b):
    ans = 0
    if a == b:
        return a
    elif a > b:
        for i in range(b,a+1):
            ans += i
    else:
        for i in range(a,b+1):
            ans += i
    
    return ans