import matplotlib.pyplot as plt

harorat = [20, 22, 24, 21, 25, 27, 23]
kunlar = ["Du", "Se", "Ch", "Pa", "Ju", "Sh", "Ya"]

plt.plot(kunlar, harorat, marker='o', color='red', linestyle='-')
plt.title("Bir haftalik harorat o'zgarishi")
plt.xlabel("Kunlar")
plt.ylabel("Harorat (°C)")
plt.grid(True)
plt.show()