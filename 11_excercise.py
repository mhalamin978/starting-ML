population = {
    'china': 143,
    'india': 136,
    'usa': 32,
    'pakistan': 21
}

def add():
    country=input("Enter country name to add:")
    country=country.lower()
    if country in population:
        print("Country already exist in our dataset. Terminating")
        return
    p=input(f"Enter population for {country}")
    p=int(p)
    population[country]=p # Adds new key value pair to dictionary
    print(population)

def print_all():
    for country,p in population.items():
        print(f"{country}==>{p}")
print_all()
