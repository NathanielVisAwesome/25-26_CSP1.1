n1 = 100
n2 = 200
n3 = int(n1 / n2)

if n3 > 0:
    n2 = n1
    n1 = n2

else:
    n1 = n2
    n2 = n1

print(str(n1) + " ",str(n2))

# prints: 100 100

x = 0
y = 0

for x in range(5):
    y += 1
y += 1

print("y= " + str(y)),

# prints 6

# for x in range(5):
#   y += 1
#   y += 1
#
# print("y= " + srt(y))
#
# in this case, it will print 10

j = 1
k = 0

while j < 30:
    k = 2 * j
    j *= 3
    print(j)

# prints ?

n = 0
v = 0
MtnDewBajaBlast = int(0)

for n in range(3):
    MtnDewBajaBlast += 1
    for v in range(2):
        MtnDewBajaBlast *= 2

print(MtnDewBajaBlast)

# prints 7 because it increments MtnDewBajaBlast is starting at 0, 1 is added then multiplied to 4, adds 1 (5 now) then multiplied to 10 (3*2), then for the 3rd and final add 1, (11 now) multiplied to 22 (11*2)