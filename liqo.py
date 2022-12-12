import random
import itertools

nama = ['Sami', 'Fawwaz', 'Faiz', 'Rifki', 'Azzam', 'Rijal']
tugas = ['MC', 'Tilawah', 'Doa', 'Materi']
jadwal = []
#Add comment

data = random.sample(nama, len(tugas))
jadwal.append(data)

for i in tugas:
    print("{:9}".format(i) + ":" + data.pop())