fin = open('daily_revenues.txt','r')
numbers = []

for line in fin:
    number = int(line)
    numbers.append(number)

print(f'In total {len(numbers)} days analyzed')
print(f'Maximum daily revenue is {max(numbers)} €')
print(f'Minimum daily revenue is {min(numbers)} €')

fin.close()
