
def n_integers(n):
    integers = tuple( i+1 for i in range(n))
    return integers
if __name__ == '__main__':
	n = int(input())
	for i in n_integers(n):
		print(i, end='')
	
