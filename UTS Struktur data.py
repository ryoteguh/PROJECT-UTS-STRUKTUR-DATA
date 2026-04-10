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