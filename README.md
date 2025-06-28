# Pacmann Super Cashier
## Latar Belakang
Seorang pemilik supermarket memiliki rencana untuk melakukan improvement terhadap bisnisnya, yaitu pembuatan sistem kasir yang self-service.

## Requirements
Membuat program sederhana yang memiliki fungsi:
- Add : menambah item baru, jumlahnya, dan harga item tersebut ke program
- Update : merubah item yang sudah masuk ke dalam program (nama, jumlah, harga)
- Delete : menghapus sebuah item di dalam program
- Reset : menghapus semua item dalam program
- Check order : mengecek semua item yang sudah dimasukkan ke dalam program
- Menghitung jumlah harga belanja yang sudah dikurangi oleh discount yang sudah ditetapkan

## Flowchart
1. Pastikan main.py dan module.py berada pada folder yang sama
2. jalankan main.py di terminal
3. main.py akan berfungsi sebagai menu interaktif yang dapat menggunakan seluruh fungsi dari module.py

## Functions
### module.py
merupakan file python yang mengandung class Transaction, kelas ini merupakan kelas utama yang digunakan di seluruh program
1. add_item(nama_item, jumlah_item, harga_item): berfungsi untuk menambahkan item ke class Transaction
2. update_item_<name,qty,price>(nama_item, <nama_baru,jumlah_baru,harga_baru>) : 3 fungsi yang digunakan untuk merubah nama, jumlah, atau harga item dalam kelas Transaction
3. delete_item(nama_item): menghapus sebuah item yang sudah ada dalam kelas Transaction
4. reset_transaction(): menghapus seluruh item dalam kelas
5. Check_order(): menampilkan tabel yang berisikan semua item, jumlah, dan harga nya beserta total harga keseluruhan (tanpa discount)
6. total_price(): menampilkan total harga seluruh item, discount yang didapat, dan total yang harus dibayarkan
7. calculate_total_price()* : menghitung harga total seluruh item dan menyimpannya dalam self.total_price
8. check_cart()*: menampilkan tabel yang berisikan semua item, jumlah, dan harga nya tanpa harga total per item dan harga total keseluruhan
*ket : fungsi tambahan

### main.py
Fungsi utama dari file ini adalah membuat menu interaktif dimana user bisa berinteraksi secara langsung. fungsi lainnya adalah program ini memaksa user untuk melakukan input yang benar untuk mengurangi kemungkinan program error.

## Demo (Test-Case)
1. Penambahan Item:

jalankan program main.py

![image](https://github.com/user-attachments/assets/f66f5979-49dd-4e3b-8456-397db9c473d3)

tambahkan item dengan menginput command 1 dan tambahkan nama(str), jumlah(int), dan harga item(int)

![image](https://github.com/user-attachments/assets/2cf20f9b-59fd-455e-82e8-97a72c3af95b)

output (check order):

![image](https://github.com/user-attachments/assets/749ce9df-0fe2-4cea-9810-92b8c7ba0fc9)

2. Penghapusan Item(delete_item):

command input 3, input nama item(str):

![image](https://github.com/user-attachments/assets/679a8e0f-fc62-42ac-b78a-2db7eac64c36)

output:

![image](https://github.com/user-attachments/assets/a1e10347-f75b-415f-b859-05acb89185f1)

3. Reset transaksi:

command input 4:

![image](https://github.com/user-attachments/assets/5cbfcf9d-15b9-45b2-9763-c435cdbdd914)

output:
kembali ke menu awal:

![image](https://github.com/user-attachments/assets/4613a38f-1bd5-42f2-be9c-6b720cd5d49c)

4. checkout (Total_price):

command input 6:
![image](https://github.com/user-attachments/assets/823d07a1-988a-49cc-97a8-7e04dded6a06)

5. Update Item:

command input 2, pilih nama item, pilih bagian yang ingin dirubah (name, qty, price), masukkan perubahan:

![image](https://github.com/user-attachments/assets/59558b9d-6864-48ef-8678-a85738e46200)

output (check_order):

![image](https://github.com/user-attachments/assets/8246bb68-81ac-43b7-adbf-12baa18ea6cb)


## Conclusion
Sistem cashier self_service ini merupakan program sederhana yang interaktif yang dapat membantu customer untuk melakukan input pembelian barang secara mudah.

- Further improvement : Save transaction into database
