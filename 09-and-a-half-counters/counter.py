class Counter:
    pass

# CARLA BOUNDARY
# Fill in the blanks in the Counter class to make
# the following code work. You are *not* allowed
# to change any code under the Carla Boundary.
# -----------------------------------------------


pies_eaten = Counter()
pies_eaten.add()
pies_eaten.add()
# You have eaten 2 pies
print(f'You have eaten {pies_eaten.total()} pies')
pies_eaten.add()
# You have eaten 3 pies
print(f'You have eaten {pies_eaten.total()} pies')

days_since_accident = Counter()
# It has been 0 days since an accident
print(f'It has been {days_since_accident.total()} days since an accident')
for i in range(10):
    days_since_accident.add()
# It has been 10 days since an accident
print(f'It has been {days_since_accident.total()} days since an accident')
# Goddamnit, Irene
print('Oh no! Due to Irene running in a no running zone, Colin has lost both legs!')
days_since_accident.reset()
# It has been 0 days since an accident
print(f'It has been {days_since_accident.total()} days since an accident')

pies_eaten.add()
# You have eaten 4 pies
print(f'You have eaten {pies_eaten.total()} pies')


