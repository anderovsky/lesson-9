Country Capitals
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
import json

def load_data(filename="countries.json"):
    """Load the dictionary from a JSON file."""
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_data(data, filename="countries.json"):
    """Save the dictionary to a JSON file."""
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

def add_country(data, country, capital):
    """Add a new country and its capital."""
    data[country] = capital
    save_data(data)

def delete_country(data, country):
    """Delete a country from the dictionary."""
    if country in data:
        del data[country]
        save_data(data)
    else:
        print("Country not found.")

def find_capital(data, country):
    """Find the capital of a given country."""
    return data.get(country, "Country not found.")

def edit_country(data, country, new_capital):
    """Edit the capital of an existing country."""
    if country in data:
        data[country] = new_capital
        save_data(data)
    else:
        print("Country not found.")

# Example usage
data = load_data()
add_country(data, "France", "Paris")
add_country(data, "Germany", "Berlin")
delete_country(data, "Spain")  # Example deletion
print(find_capital(data, "France"))  # Outputs: Paris
edit_country(data, "Germany", "Munich")
print(find_capital(data, "Germany"))  # Outputs: Munich

