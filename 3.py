from matplotlib import pyplot

kunlar = ["1-noy", "2-noy", "3-noy", "4-noy", "5-noy", "6-noy", "7-noy"]
haroratlar = [18, 21, 19, 20, 18, 23, 24]

pyplot.plot(kunlar, haroratlar, marker="o", linestyle="-")

pyplot.title("7 kunlik havo harorati")
pyplot.xlabel("Kunlar")
pyplot.ylabel("Harorat (°C)")

pyplot.grid(True)

pyplot .legend()

pyplot.savefig("haroratlar.png")
pyplot.show()