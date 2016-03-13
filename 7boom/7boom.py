BOOM="boom!"

#This file can be found at: https://github.com/evidence26/sandbox/tree/master/7boom

"""
Gets an int and returns its' 'boomified' version
Args:
    param1 (int): a non negative integer
    
    Returns the string defined by BOOM iff only one of the following conditions are met:
         - If the number has a 7 in it
         - The remainder of the number after division in 7 is zero

         In any othe case, this method will return the given number

"""
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

