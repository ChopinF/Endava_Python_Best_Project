testing = {"Ana", "Bob", "Charlie", "Diana"}
development = {"Charlie", "Eve", "Frank", "Ana"}
devops = {"George", "Ana", "Bob", "Eve"}
all_three = testing & development & devops
print("Attended all three sessions:", all_three)
only_one = (
    (testing - development - devops) |
    (development - testing - devops) |
    (devops - testing - development)
)
print("Attended only one session:", only_one)
subset_check = testing.issubset(devops)
print("All testing attendees are also in devops:", subset_check)
all_attendees = testing | development | devops
sorted_attendees = sorted(all_attendees)
print("All unique attendees (sorted):", sorted_attendees)



