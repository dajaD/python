def is_prime(num):
    checker = 2
    while checker < num:
        if num % checker == 0:
            return False
        checker += 1
    return True
        
#
# Write your code here.
#

for i in range(1, 30):
	if is_prime(i + 1):
			print(i + 1, end=" ")
print()
