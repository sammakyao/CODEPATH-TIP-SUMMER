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