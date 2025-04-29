print("Name: Krishna Mishra ")
print("Roll No: 24BEE109")
namesset = {"America", "Africa", "Boston", "Atlanta", "Bahamas", "Australia", "Bahrain"}
anames = {name for name in namesset if name.startswith("A")}
bnames = {name for name in namesset if name.startswith("B")}
print("Names starting with A:", anames)
print("Names starting with B:", bnames)

