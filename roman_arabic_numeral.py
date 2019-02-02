#github.com/mborka
#roman-arabic numberal converter

def value(roman):
	if roman == "I":
		return 1
	if roman == "V":
		return 5
	if roman == "X":
		return 10
	if roman == "L":
		return 50
	if roman == "C":
		return 100
	if roman == "D":
		return 500
	if roman == "M":
		return 1000

def sum(numbers):
	 val = 0
	 for i in range(len(numbers)):
	 	val += numbers[i]
	 return val

def intro():
	print ("""
	__________________________________
	MBorka´s;
	Roman - Arabic numberal converter
		- Type exit to leave program
		- Type ether a roman or arabic
			number to get it converted
			to the other numeral system
	""")

def start(string):
	string_list = list(string)
	local = 0
	for i in range(len(string_list)):
		local += value(roman = string_list[i-1])
	print (local)

def roman_convert(string):
	x = list(string)
	loc = []
	for i in range(len(x)):
		loc += [value(x[i])]
	for i in range(len(loc)-1):
		if loc[i] < loc[i+1] and loc[i] != loc[i+1]:
			loc[i+1] = loc[i+1]-loc[i]
			loc[i] = 0
	print ((string) + " |    " + str(sum(numbers = loc)))
	print ("")


def arab_roman(value):
	list_1 = list(value)
	splited = []
	for i in range(3):
		splited.append((int(list_1[i]) * (10**(i))))
	print (splited)

def arab_rom_single(number, table, lg):
    x = (number / (10**lg))
    values = ["-",table[0]*1,table[0]*2,table[0]*3,
    table[1] + table[0],table[1],table[0]*1 + table[1],
    table[0]*2+ table[1],table[0]*3+ table[1],table[2] + table[0],]
    return values[int(x)]

def parameters_rom(place):
    if place == 0:
        return ["I","V","X"]
    if place == 1:
        return ["X","L","C"]
    if place == 2:
        return ["C","D","M"]

def arab_roman(value):
	list_1 = list(value[::-1])
	rearrange = []
	splited = []
	for i in range(len(list_1)):rearrange.append((int(list_1[i]) * (10**(i))))
	for i in range(len(rearrange)):splited.append(arab_rom_single(number = rearrange[i], table = parameters_rom(i), lg = i))
	print (str(value) + " |    " + cleaner(splited))
	print ("")

def cleaner(unclean):
    clean = ""
    for i in range(len(unclean)):
        if unclean[i] == "-":
            pass
        else:
            clean += unclean[i]
    return clean[::-1]


def go(input):
	if input.lower() == "exit":
		exit()
	if input.isalpha() == True:
		roman_convert(string = input)
	else:
		arab_roman(value = input)

intro()
global mode
mode = 1
while 1==1:
	inp = input("Enter : ")
	go(input = inp)
