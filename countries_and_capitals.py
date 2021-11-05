with open('country_capital.txt', 'r') as fin:
    country = open('countries.txt','w')
    capital = open('capital.txt','w')
    for line in fin:
        new_line = line.split(' - ')
        print(new_line)
        country.write(new_line[0] + '\n')
        capital.write(new_line[1])
