BOOM="boom!"

def boomify(i):
	if((i%7 == 0) or ('7' in str(i))):
		return BOOM
	else:
		return i

for i in range(1, 101):
	digits_sum=sum(int(digit) for digit in str(i))
	i_boomified=boomify(i)
	digits_sum_boomified=boomify(digits_sum)
	if((i_boomified == BOOM) and (digits_sum_boomified == BOOM)):
		print(str(i)+" "+ str(digits_sum))
	else:
		print(str(i_boomified)+" "+ str(digits_sum_boomified))

