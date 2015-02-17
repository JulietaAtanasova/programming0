from itertools import permutations

n = int(input("Enter number: "))

z = list(map(list, permutations(str(n), 3)))

results = []

for number in z:
    results.append(int("".join(number)))

print("The largest number: %d" % max(results))
print("The smallest number: %d" % min(results))