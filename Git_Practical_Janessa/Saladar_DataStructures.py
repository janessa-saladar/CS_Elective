students = {"Zach", "Angie", "Jam", "Hailey", "Shanan"}
Zach = ("Zach", 15, 10, "Graviton")
Angie = ("Angie", 15, 10, "Tau")
Jam = ("Jam", 15, 10, "Tau")
Hailey = ("Hailey", 15, 10, "Graviton")
Shanan = ("Shanan", 16, 10, "Tau")

print(Jam[0], Jam[2], Jam[3])

grades = {
    "Zach" : [99],
    "Angie" : [97],
    "Jam" : [98],
    "Hailey" : [95],
    "Shanan" : [96]
}

print(grades["Zach"])
grades["Zach"] = [90]
grades["Audrey"] = [100]