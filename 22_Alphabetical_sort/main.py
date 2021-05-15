def alph(A, n):
	for i in range(n):
		for j in range(n):
			if chck(A[j],A[i]):
				A[i], A[j] = A[j], A[i]
	return A

def chck(w1, w2):
	dw1 = len(w1)
	dw2 = len(w2)
	
	if dw1 <= dw2:
		for i in range(dw1):
			if ord(w1[i]) > ord(w2[i]):
				return True
			else:
				return False
		return False
		
	if dw1 > dw2:
		for i in range(dw2):
			if ord(w1[i]) > ord(w2[i]):
				return True
			else:
				return False
		return True
				

A = ['DEF', 'DEFAAAA', 'ZBC', 'ABC', 'AABD']
print(alph(A, len(A)))
