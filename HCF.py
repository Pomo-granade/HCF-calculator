num1 = int(input("Enter first number\n"))
num2 = int(input("Enter second number\n"))

if num2<num1:
    mn = num2

else:
    mn = num1

for i in range (1 , mn+1):
    if num1%i == 0 and num2%i == 0:
        hcf  = i

print(f"The HCF of {num1} and {num2} is {hcf}")