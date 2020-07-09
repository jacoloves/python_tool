a = int(input())

B = []

for i in range(a):
    B.append(input())

AC = 0
TLE = 0
WA = 0
RE = 0

for i in range(a):
    if B[i] == "AC":
        AC += 1
    elif B[i] == "TLE":
        TLE += 1
    elif B[i] == "WA":
        WA += 1
    elif B[i] == "RE":
        RE += 1

print(f"AC x {AC}")
print(f"WA x {WA}")
print(f"TLE x {TLE}")
print(f"RE x {RE}")
