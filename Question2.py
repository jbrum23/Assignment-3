preferences = ["coffee", "tea", "coffee", "soda"]

counts = {}

# Count each preference
for item in preferences:
    if item in counts:
        counts[item] += 1
    else:
        counts[item] = 1

total = len(preferences)

# Print percentages
for item in counts:
    percentage = (counts[item] / total) * 100
    print(f"{item}: {percentage:.0f}%")