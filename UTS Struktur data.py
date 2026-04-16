#Sistem Antrian Rumah sakit
#Mendefinisikan Linked list dan membuat struktur queue list hingga dequeue
#Rio Teguh Priyo Utomo -2501010063 -Kelas C
class node:
    def __init__(self,nama,keluhan):
        self.nama = nama
        self.keluhan = keluhan
        self.next = None
class Queuelinkedlist:
    def __init__(self):
        self.front = None
        self.rear = None
    def enqueue(self, nama, keluhan):
        node_baru = node(nama,keluhan)
        if self.rear is None:
            self.front = self.rear = node_baru
            return
        self.rear.next = node_baru
        self.rear = node_baru
    def dequeue(self):
        if self.front is None:
            return None
        temp = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return temp.nama, temp.keluhan
#Andi Pratama  NIM 2501010092 - Kelas C 
#Membuat fungsi peek dan tampilkan untuk melihat data(antrian) serta membuat tampilan menu utama
    def peek(self):
        if self.front is None:
            return None
        return self.front.nama, self.front.keluhan
    def tampilkan(self):
        if self.front is None:
            print("Queue Kosong")
            return
        current = self.front
        no = 1
        print(f"{'No' :<5} {'Nama':<20} {'keluhan'}")
        print("-"*40)
        while current:
            print(f"{no:<5} {current.nama:<21}{current.keluhan}")
            current = current.next
            no += 1  
qll = Queuelinkedlist()
while True:
    print("\n=== MENU ANTRIAN ===")
    print("1. Tambah antrian (Enqueue)")
    print("2. Keluarkan antrian (Dequeue)")
    print("3. Lihat antrian terdepan (Peek)")
    print("4. Tampilkan semua antrian")
    print("5. Keluar")

#Membuat logika if untuk pilihan menu utama
#Marvyn
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        n = int(input("Berapa orang yang antri  : "))
        for i in range (n):
            nama = str(input(f"Masukkan nama ke {i+1}   :"))
            keluhan = str(input("Masukkan keluhan anda : "))
            qll.enqueue(nama,keluhan)
            print(f"{nama}({keluhan}) berhasil masuk antrian.")

    elif pilihan == "2":
        keluar = qll.dequeue()
        if keluar:
            print(f"{keluar} keluar dari antrian.")
        else:
            print("Antrian kosong!")

    elif pilihan == "3":
        depan = qll.peek()
        if depan:
            print(f"Antrian terdepan: {depan}")
        else:
            print("Antrian kosong!")

    elif pilihan == "4":
        print("\nIsi antrian:")
        qll.tampilkan()


    elif pilihan == "5":
        print("Keluar.")
        break

    else:
        print("Pilihan tidak valid!")
