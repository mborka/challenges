##  Reverse String Challenge
##  https://www.coderbyte.com/results/Mborka:First%20Reverse:Python
##  Points: 10/10 || Time: 5.00 min
##
string = input("String ?;" )
def FirstReverse(str): 
    length = len(str)
    currentl = int(length)-1
    finalstring = ""
    while currentl >= 0:
        finalstring += str[currentl]
        currentl += (-1)
    return finalstring
    
print FirstReverse(string)
