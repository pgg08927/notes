import random

# all funtions in module
print(dir(random))

# Help on any function
print(help(random.random))


# random.random
value = random.random() # automatically generate the value bet 0 & 1
print(value)

# random.random
value = random.uniform(3,7) # float values
print(value)

#normal variate
value = random.normalvariate(3,0.2) # pass mean & standard deviation
print(value)

#randint
value= random.randint(1,6)   # int value
print(value)

#random.choice
colors=['Red','Black','Green']
results=random.choice(colors)    # choice form the list

# random.choices
results=random.choices(colors,
                       weights=[18,18,2],      # how many chance out of total
                       k=10)    # how many results
print(results)

#random.shuffle

deck=list(range(1,53))
random.shuffle(deck)

#random.sample
hand=random.sample(deck,k=5)    # unique values from the list
print(hand)


