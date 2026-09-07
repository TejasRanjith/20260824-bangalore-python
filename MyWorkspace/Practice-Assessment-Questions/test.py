l = [
    {
        "Name":1,
        "Class":2
    },
    {
            "Name":3,
            "Class":4
    },
    {
        "Name":5,
        "Class":6
    },
    {
        "Name":7,
        "Class":8
    },
    {
        "Name":9,
        "Class":10
    }
]
for item in l:
    if item["Name"] == 3:
        l.remove(item)
print(l)