import time

print("Execution Time:")
start_time = time.time()

number = 153
temp_store = number

# Find number of digits
length = len(str(temp_store))

result = 0

while number > 0:
    modulus = number % 10
    result += pow(modulus, length)
    number //= 10  # Integer division

# Check Armstrong condition
if result == temp_store:
    print(result, "is an Armstrong number")
else:
    print(temp_store, "is not an Armstrong number")

end_time = time.time()
print(f"Execution Time: {round((end_time - start_time) * 1000, 4)} ms")
