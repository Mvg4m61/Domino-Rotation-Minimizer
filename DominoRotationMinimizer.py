def equalRows():
    A = []
    B = []
    i = 0
    while True:
        n = int(input("\nEnter the length of rows (between 2 and 20000): "))
        if 2<=n<=20000:
            break
        else:
            print("\nPlease follow instructions.")
            continue
    while i<n:
        
        try: 
            up,down = [int(x) for x in input().split()]
            if 0<up<7 and 0<down<7:
                A.append(up)
                B.append(down)
                i = i+1
            else:
                print("Value out of range, try again.")
                
        except:
            print("Value out of range, try again.")
    count = [0,0]
    a = A[0]
    b = B[0]
    for i in range(n):
        
        if A[i] == a:
            pass
        elif B[i] == a:
            count[0] = count[0] + 1
        else:
            count[0]=n
            break
          
            
    for i in range(n):
        if B[i] == b:
            pass
        elif A[i] == b:
            count[1] = count[1] + 1
        else:
            count[1]=n
            break
    if count == [n,n]:
        return -1
    
    else:
        return min(count)
            
#main environment
y = equalRows()
print("\nMinimum Rotations: ",y)