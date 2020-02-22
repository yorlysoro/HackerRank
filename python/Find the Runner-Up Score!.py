def up_score(arr):
	prev = 0
	for i in arr:
		if i < prev and prev != 0:
			return i
		elif i < prev and i < 0 and prev != 0:
			return i
		else:
			prev = i 
		
		
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr_sort = list(sorted(arr, reverse=True))
    print(up_score(arr_sort))
