
from task_5_1 import london_co

device = input('Enter device name: ')
print('Available parameters:', ', '.join(london_co[device].keys()))
parameter = input('Enter parameter name: ')

print(london_co[device].get(parameter, 'No such parameter'))
