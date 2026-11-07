import matplotlib.pyplot as plt

baholar = [60, 75, 80, 70, 90]
nazoratlar = [1, 2, 3, 4, 5]

plt.plot(nazoratlar, baholar, marker='o', color='blue')
plt.title("O'quvchilarning nazorat ishlaridagi baholari")
plt.xlabel("Nazorat ishlari")
plt.ylabel("Baholar")
plt.grid(True)
plt.show()