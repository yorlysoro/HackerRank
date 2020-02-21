def up_score(arr):
	prev = 0
	for i in range(len(arr)):
		print(prev)
		if arr[i] < prev:
			return arr[i]
		else:
			prev = arr.pop() 
		
		
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr_sort = list(sorted(arr, reverse=True))
    print(arr_sort)
    print(up_score(arr_sort))
