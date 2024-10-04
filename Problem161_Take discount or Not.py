t = int(input())

while t > 0:
    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))
    sum_without_coupon=0
    for i in a:
        sum_without_coupon+=i
    
    sum_with_coupon=x 
    for i in a:
        if i>y:
            sum_with_coupon+=(i-y)
    
    if sum_with_coupon<sum_without_coupon:
        print("COUPON")
    else:
        print("NO COUPON")
            
    
    
    t -= 1

