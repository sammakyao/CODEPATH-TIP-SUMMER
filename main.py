# create a function that returns the sum of
# two integers a and b
# then double the sum, then print the console
'''

def sum(a, b):
  return a + b
print(sum(20, 8) * 2)

'''
#   write a function that returns product of
# two integers a and b
'''
def product(a, b):
  return a * b
result = product(22, 7)
print(result)

'''
# write a function classify_age()
'''
def classify_age(age):
  if age < 18:
    return "child"
  else:
    return "adult"

output = classify_age(18)
print(output)
output = classify_age(7)
print(output)
output = classify_age(50)
print(output)

'''

# write a function what_time_is_it, takes int hour as parameter 

'''
def what_time_is_it(hour):
  if hour == 2:
    return "taco time"
  elif hour == 12:
    return "peanut butter jelly time"
  else:
    return "nap time"

time = what_time_is_it(2)
print(time)
time = what_time_is_it(7)
print(time)
time = what_time_is_it(12)
print(time)

'''

# Blackjack problem 

'''
def blackjack(score):
	if score < 17:
	    print("Hit Me!")
	elif score < 21:
	    print("Nice hand!")
	elif score >= 21:
	    print("Bust!")
	else:
	    print("Blackjack!")

blackjack(24)
blackjack(19)
blackjack(21)
blackjack(10)

'''

# 10- last item, write a function that takes in a list as parameter, returns last item in the list. 

'''
def get_last(lst):
  if lst == []:
    return None
  else: 
    return lst[-1] 
    
result = get_last([])
print(result)

'''
# 9 - write a function get_first() that takes in a list as a parameter and returns the first item in the list. return None if empty.

'''

def get_first(lst):
  if lst == []:
    return None
  else:
    return lst[0]

result = get_first([3,1,6,7,5])
print(result)

'''

# 11 - counter, function that uses range function to print numbers between 1 and a given stop value inclusive 

'''
def counter(stop):
  for i in range(1, stop + 1):
    print(i)
counter(10)

'''

# 12 sum of 1 to 10

'''
def sum_ten():
    return sum(range(1, 10 + 1))

output = sum_ten()
print(output)
#result = sum_ten()
#print(result)

'''

# 13 - total sum given range inclusive

'''
def sum_positive_range(stop):
  return sum(range(1, stop + 1))

sum = sum_positive_range(6)
print(sum)

'''

# 14 - total sum in range

'''
def sum_range(start, stop):
  return sum(range(start, stop + 1))

sum = sum_range(3,9)
print(sum)

'''

# 15 n