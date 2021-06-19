def findremainder(arr, lens, n):
	mul = 1

	for i in arr:
		mul = mul * (i % n)

	return mul % n


arr = [100, 10, 5, 25, 35, 14]
lens = len(arr)
n = 11

print(findremainder(arr, lens, n))
