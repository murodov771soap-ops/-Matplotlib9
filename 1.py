from matplotlib import pyplot

darslar = ["01.11", "02.11", "03.11", "04.11", "05.11", "06.11", "07.11"]
ballar = [85, 90, 78, 74, 78, 88, 95]

pyplot.plot(darslar, ballar, marker="p", linestyle="-.")

pyplot.title("O'quvchining 7 kunlik ballari")
pyplot.xlabel("Kunlar")
pyplot.ylabel("Ballar")

pyplot.grid(True)

pyplot.savefig("natijalar.png")
pyplot.show()