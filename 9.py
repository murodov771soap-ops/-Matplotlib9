from matplotlib import pyplot
turlar = ["Fayllar","Rasmlar","Videolar","Ilovalar","Tizim","Boshqa","Bo'sh"]
hajm = [2,10,28,1,40,11,8,28]


pyplot.pie(
    hajm, labeldistance=turlar, autopct="%1.2f%%",
    startangle=0,
    explode=[0.1,0.1,0.1,0.3,0.1,0.1,0.1]
    
)

pyplot.show()