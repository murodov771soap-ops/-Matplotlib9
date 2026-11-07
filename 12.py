from matplotlib import pyplot
import csv

with open("Dars9/users.csv", "r") as f:
    data = csv.DictReader(f)
    users = list(data)

ismalar = []
yoshlar = []

for user in users:
    print(user)
    ismalar.append(user["ism"])
    yoshlar.append(int(user["yosh"]))

print(ismalar)
print(yoshlar)

pyplot.plot(ismalar, yoshlar)
pyplot.show()