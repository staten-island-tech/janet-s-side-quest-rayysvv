temperatures = ["Label", 32, 50, 77, 104]

fahrenheit = map(lambda x: x * 9 / 5 + 32, temperatures[1:])

print(list(fahrenheit))