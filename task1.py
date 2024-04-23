import json

class CountryCapitals:
    def __init__(self):
        self.data = {}

    def add_data(self, country, capital):
        self.data[country] = capital

    def delete_data(self, country):
        if country in self.data:
            del self.data[country]
        else:
            print(f"{country} not found.")

    def find_data(self, country):
        if country in self.data:
            return self.data[country]
        else:
            return f"{country} not found."

    def edit_data(self, country, new_capital):
        if country in self.data:
            self.data[country] = new_capital
        else:
            print(f"{country} not found.")

    def save_data(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.data, file)

    def load_data(self, filename):
        with open(filename, 'r') as file:
            self.data = json.load(file)


cc = CountryCapitals()

# Adding data
cc.add_data("Ukraine", "Kyiv")
cc.add_data("Czech Republic", "Praha")
cc.add_data("France", "Paris")

# Deleting data
cc.delete_data("France")

# Finding data
print(cc.find_data("Ukraine"))  # Output: Washington D.C.
print(cc.find_data("UK"))   # Output: UK not found.

# Editing data
cc.edit_data("France", "Marseille")

# Saving data
cc.save_data("countries.json")

# Loading data
cc.load_data("countries.json")
