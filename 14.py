import matplotlib.pyplot as plt

kunlar = ["Dush", "Sesh", "Chor", "Pay", "Juma"]
savdo = [10, 15, 8, 20, 18]

plt.bar(kunlar, savdo, color='skyblue', edgecolor='black')
plt.title("Haftalik savdo hajmi")
plt.xlabel("Hafta kunlari")
plt.ylabel("Savdo miqdori")
plt.show()