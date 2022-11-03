import random

tickets = []
for i in range(100):
    tickets.append(random.randrange(1000000000, 9999999999))
winn = random.sample(tickets, 2)
print(winn)