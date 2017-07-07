##동전 바꿔주기 17.7.7

import os, sys

T = int(input('T원의 지폐 : '))
K = int(input('동전의 가짓수 K : '))

p=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
num = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

i = 1
while (i <= K):
    p[i] = int(input('동전하나의 금액 p : '))
    num[i]= int(input('그 동전의 갯수 n : '))
    ##[int(y) for y in input("그 동전의 갯수 n : ").split()]
    i = i+1

arr = []
for i in range(T*K):
    arr.append([0]*T*K)

arr[0][0] = 1
i =1
while (i <= K):
    j=0
    for j in range(T+1):
        k=0
        while ((j >= k*p[i]) and (k <= num[i])):
            arr[i][j] += arr[i-1][j- k*p[i]]
            k = k+1   
    i = i+1
    
print("경우의 수는 : ",int(arr[K][T]),"개!")

	



