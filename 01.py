arr = list(map(int, str(input())[1:-1].split(",")))
n = len(arr)
if n < 2:
    print(0)
minVal=abs(arr[1]-arr[0])
for i in range(2,n):
    minVal = min(minVal, abs(arr[i]-arr[i-1]))
print(minVal)