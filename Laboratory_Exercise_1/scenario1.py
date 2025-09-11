from collections import Counter

biology = {
    "mmHg" : [120, 135, 118, 140, 128, 135, 122, 130]
}

biology["average_mmHg"] = sum(biology["mmHg"]) / len(biology["mmHg"])
biology["unique_values"] = set(biology["mmHg"])
biology["value_counts"] = Counter(biology["mmHg"])

print("Blood Pressure Readings:", biology["mmHg"])
print("Unique Values:", biology["unique_values"])
print("Value Counts:", biology["value_counts"])