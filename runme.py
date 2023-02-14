from csetup import csetup
from binsetup import binsetup
from inv import inv
from time_func import time

#Assumtions
a_i = 2
b_i = 3

#Constants
cstorage= 10   # 1000 cups per day
cost8 = 50     # Rs.
cost16 = 70    # Rs.
cost24 = 120   # Rs.

#Note - range(1, 5) will loop from 1 to 4. (5 will be excluded)

part_1 = 0
for i in range(1, 7):
    for j in range(1, 18):
        for l in range(j+1, 19):
            part_1 += (csetup(j, l)*binsetup(i, j, l))

part_2 = 0
for i in range(1, 7):
    for j in range(1, 19):
        part_2 += (inv(i, j)*cstorage)

part_3 = 0
for i in range(1, 7):
    part_3 += (cost8*time(i))

part_4 = 0
for i in range(1, 7):
    part_4 += ((cost16-cost8) * (time(i) - 8 + a_i))

part_5 = 0
for i in range(1, 7):
    part_5 += ((cost24-cost16) * (time(i) - 16 + b_i))


final_ans = part_1 + part_2 + part_3 + part_4 + part_5

print("Part 1 = {}".format(part_1))
print("Part 2 = {}".format(part_2))
print("Part 3 = {}".format(part_3))
print("Part 4 = {}".format(part_4))
print("Part 5 = {}".format(part_5))
print("Final Answer = {}".format(final_ans))