n = int(input())
a=0
for i in range(n): 
    for k in range(n-i-1):
        print(' ', end='')
    for k in range(i+1):
        print('*', end='')
    print()