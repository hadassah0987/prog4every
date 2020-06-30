def greaterOf(val1, val2):
    if val1 > val2 : 
        return val1
    else:
        return val2

h = float(input("Enter Hours:"))
rate = input("Enter hour per rate:")
rt = float(rate)
total = h * rt
overtimeHrs = greaterOf(h - 40, 0)
total += overtimeHrs * rt * .5
print(total)    
    