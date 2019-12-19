from fuzzywuzzy import process

with open("cities.txt", "r") as f:
    cities = f.read().split("\n")

def get_matches(query, choices, limit=3):
    results = process.extract(query, choices, limit=limit)
    return results

rawcity = input("Insert searched city: i")

predict = get_matches(rawcity, cities)

print("Predicted cities...")
print(predict)