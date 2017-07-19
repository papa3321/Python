from random import randint

pubA = [55, 40, 33, 28, 439]
pubB = [88, 92, 104, 95, 100]
pubA.sort()
pubB.sort()
sub = 0

for i in pubA:
    sub = sub + i
print(sub)
print(sub / len(pubA))
sub = 0
for j in pubB:
    sub = sub + j
print(sub)
print(sub / len(pubB))

print("  *  ")
print(" ***  ")
print("*****  ")
print("    *    ")
print("   ***   ")
print("  *****  ")
print(" ******* ")
print("*********")

for i in range(1,11):
    print(randint(1,100))


