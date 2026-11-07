import matplotlib.pyplot as plt

oquvchilar = ["Ali", "Vali", "Sobir", "Bobir", "Komil", "Akmal"]
matematika = [85, 78, 90, 60, 50, 62]
tarix = [65, 78, 93, 90, 100, 53]

a = plt.bar(oquvchilar, matematika, align="center", width=0.3, label="Matematika", color="green")
b = plt.bar(oquvchilar, tarix, align="edge", width=0.3, label="Tarix", color="red")

plt.bar_label(a)
plt.bar_label(b)

plt.legend()
plt.title("O'quvchilar natijalari")

plt.show()