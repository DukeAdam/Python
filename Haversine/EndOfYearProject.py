from haversine import haversine

a = open("northings.txt", "r")
b = open("westings.txt", "r")
coordinates = []
shop = (53.38195, -6.59192)

for x in range(101):
    if x == 0:
        coordinates.append(shop)  # Place shop at position 0
    else:
        N = a.readline()
        n = float(N.rstrip())
        W = b.readline()
        w = float(W.rstrip())
        place = (n, w)
        coordinates.append(place)
    # print(str(x) + str(coordinates[x]))

# print(haversine(coordinates[65], coordinates[68]))


cur_shortest_distance = 100
cur_shortest_location = 0
final_list = ""
tot_distance = 0
for x in range(100):
    if x == 0:
        for y in range(1, 101):
            distA = haversine(coordinates[0], coordinates[y])
            if distA < cur_shortest_distance:
                cur_shortest_distance = distA
                cur_shortest_location = y
        final_list += (" " + str(cur_shortest_location) + ",")
        tot_distance += cur_shortest_distance
    else:
        for y in range(1, 101):
            distB = haversine(coordinates[cur_shortest_location], coordinates[y])
            if distB < cur_shortest_distance and (final_list.find(" " + str(y) + ",") == -1):
                cur_shortest_distance = distB
                cur_shortest_location = y
        final_list += (" " + str(cur_shortest_location) + ",")
        tot_distance += cur_shortest_distance
        cur_shortest_distance = 100


print("Tot dist: " + str(tot_distance) + " km")
print("Tot time: " + str(tot_distance / 80) + " hours")
print("Tot time: " + str((tot_distance / 80) * 60) + " mins")
print("Final route: " + final_list)

