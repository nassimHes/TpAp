
temperature = int(input("Please type in the temperature: "))

# Check the conditions and print warnings/messages
if temperature < 0:
    print("It's freezing!")
if temperature < 10:
    print("It's cold!")
if temperature < 20:
    print("It's cool!")

# Always print the final message
print("Stay safe!")
