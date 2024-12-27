# Cosmetic
bold = '\033[1m'
end = '\033[0m'
green = '\033[92m'
italic = '\033[3m'
red = '\033[31m'

# User Input Values
D1 = float(input(italic + bold + "D1 = "))
D2 = float(input(italic + bold + "D2 = "))
D3 = float(input(italic + bold + "D3 = "))
Weight = float(input(italic + bold + "Weight = "))

# Condition checking if X, Y, or Z are negative
def negative_check(value): 
		if value < 0:
				return 0
		else:
				return value

# Output Values and Threshold Messages
def value_check_1(name, value, threshold):
		if value == 0:
				print(italic+bold+green+f"{name} = 0" + end)
				print(italic+bold+green + f"Recheck {name}, otherwise {name} passed"+ end)
		elif value > threshold:
				print(bold+italic+red +f"{name} = {value:.4f}"+end)
				print(bold+italic+red+f"{name} failed"+end)
		else:
				print(bold+italic+green + f"{name} = {value:.4f}"+end)
				print(bold+italic+green + f"{name} Passed"+end)

def value_check_2(name, value, threshold):
		if value > threshold:
				print(bold+italic+red+f"{name} = {value:.4f}"+end)
				print(bold+italic+red + f"{name} failed" + end)
		else:
				print(bold+italic+green+f"{name} = {value:.4f}"+end)
				print(bold+italic+green+f"{name} passed"+end)

# Calculations
X = negative_check(D1 - (Weight * 0.0000155))
Y = negative_check(D2 - (Weight * 0.0000155))
Z = negative_check((D3 * 1.25) - (Weight * 0.0000318))
H = Z + ((X + Y) / 2)

# Threshold Checks
value_check_1("X", X, 0.060)
value_check_1("Y", Y, 0.060)
value_check_1("Z", Z, 0.050)
value_check_2("H", H, 0.051)