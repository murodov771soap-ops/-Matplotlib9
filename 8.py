import matplotlib.pyplot as plt

# Yillar ro'yxati
yil = [
    2010,
    2011,
    2012,
    2013,
    2014,
    2015,
    2016,
    2017,
    2018,
    2019,
    2020,
]


ahol = [28.0, 28.5, 29.2, 29.9, 30.7, 31.5, 32.1, 32.6, 33.2, 33.9, 34.4]

# Grafik chizish
plt.plot(yil, ahol, marker="o", linestyle="-", color="b")


plt.title("2010–2020yillar oralig'ida aholi soni dinamikasi")
plt.xlabel("Yillar")
plt.ylabel("Aholi soni")


plt.grid(True)


plt.show()