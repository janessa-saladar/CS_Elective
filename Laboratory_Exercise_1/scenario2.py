from collections import Counter

physics = {
    "Speeds" : [4, 6, 5, 7, 5, 6, 4, 8]
}

physics["highest"] = max(physics["Speeds"])
physics["lowest"] = min(physics["Speeds"])
physics["duplicate_values"] = set(physics["Speeds"])
physics["value_counts"] = Counter(physics["Speeds"])

print("Speeds of rolling ball:", physics["Speeds"])
print("No Duplicates:", physics["duplicate_values"])
print("Highest:", physics["highest"])
print("Lowest:", physics["lowest"])
print("Value Counts:", physics["value_counts"])