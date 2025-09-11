from collections import Counter

envisci = {
    "AQI" : [50, 65, 55, 80, 70, 65, 90, 100]
}
envisci["average_AQI"] = sum(envisci["AQI"]) / len(envisci["AQI"])
envisci["unique_values"] = set(envisci["AQI"])
envisci["value_counts"] = Counter(envisci["AQI"])

print("Average of Daily Air Quality Index:", envisci["average_AQI"])
print("Unique Values:", envisci["unique_values"])
print("Value Counts:", envisci["value_counts"])