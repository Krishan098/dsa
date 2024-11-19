for i in range(0,4):
    for j in range(0,i):
        print('#',end='')
    print()

for i in range(6):
    for j in range(1,i):
        print(j,end='')
    print()

for i in range(6):
    for j in range(i):
        print(i,end=' ')
    print()

for i in range(4,-1,-1):
    for j in range(0,i+1):
        print('*',end=' ')
    print()

for i in range(0,5):
    for j in range(1,5-i+1):
        print(j,end=' ')
    print()

for i in range(5,-1,-1):
    for j in range(1,i+1):
        print(j,end='')
    print()

for i in range(5):
    for j in range(5-i-1):
        print(' ',end='')
    for j in range(2*i+1):
        print('*',end='')
    for j in range(5-i-1):
        print('',end='')
    print()
    
for i in range(5):
    for j in range(i):
        print(' ',end='')
    for j in range((2*5)-((2*i)+1)):
        print('*',end='')
    for j in range(i):
        print(' ',end='')
    print()

def pattern(n):
    for i in range(2*n):
        stars=i
        if i>n:
            stars=2*n-i
        for j in range(stars):
            print('*',end='')
        print()
pattern(5)

def pattern2(n):
    for i in range(n):
        s=1
        if(i%2==0):
            s=1
        else:
            s=0
        for j in range(i+1):
            print(s,end='')
            s=1-s
        print()
pattern2(5)