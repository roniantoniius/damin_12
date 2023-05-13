import matplotlib.pyplot as plt

def damin_model():
    candy_names = ['Kit Kat', 'Snickers', 'Milky Way', 'Toblerone', 'Twix']
    candy_counts = [52, 39, 78, 13, 78]

    # Menampilkan pie chart
    plt.pie(candy_counts, labels=candy_names, autopct='%1.1f%%')
    plt.title('Persentase Peluang Memilih Permen Snickers')
    plt.show()
