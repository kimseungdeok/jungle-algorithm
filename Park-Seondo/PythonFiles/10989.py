import sys
sys.stdin = open('inputfile.txt','r')
input = sys.stdin.readline
testcase = int(input())
arr =  [0] * 10000

for i in range(testcase):
    a = int(input())
    arr[a - 1] += 1

for i in range(10000):
    if arr[i] != 0:
        for j in range(arr[i]):
            print(i + 1)