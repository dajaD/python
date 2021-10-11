blocks = int(input("Enter the number of blocks: "))
height = 0
counter = 0
total = 0


while total <= blocks:
    total = total + counter + 1
    counter = counter + 1
    height = counter - 1
#
# Write your code here.
#	

print("The height of the pyramid:", height)
