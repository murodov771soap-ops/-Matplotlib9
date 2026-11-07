from matplotlib import pyplot

kunlar = ["07.11", "08.11", "09.11", "10.11", "11.11", "12.11", "13.11"]
seoul = [9, 8, 12, 12, 15, 16, 16]
fargona = [19, 20, 18, 18, 13, 12, 10]

pyplot.plot(kunlar, seoul, marker="o", color="red", label="Seoul")
pyplot.plot(kunlar, fargona, marker="p", color="green", linestyle="-", label="Farg'ona")

pyplot.legend() 

pyplot.title("Havo harorati taqqoslash")
pyplot.xlabel("Kunlar")
pyplot.ylabel("Harorat (°C)")
pyplot.grid(True)

pyplot.show()