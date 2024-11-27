population ={"China":143,"India":136,"USA":32,"Pakistan":21}
print(population)

for key in population:
    print(key,"==>",population[key])

country =input("write the country: ")

if country in population:
    print("it exist and do nothing")
else:
    num = input("input the number: ")
    population[country]=num
print(population)
