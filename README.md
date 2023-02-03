# kripto Tugas 1 (Chiper)]
- Tugas Kecil II4031	Kriptografi dan Koding	
- NIM/Nama: 18220031/Muhammad Raihan Aulia

## Requirement 
- Python 3.10.7 (recommended karena di develop dengan menggunakan versi ini)
- envnya harusnya ada tkinter tapi ngga tahu kenapa tkinternya jalannya bukan dari venv tapi langsung dari global jadi harus install tkinter dulu. untuk installnya bisa lihat disini https://www.geeksforgeeks.org/how-to-install-tkinter-in-windows/  

## Run the program
untuk run programnya bisa buka terminal pada directory main.gui lalu run
>python main_gui.py

## How To Use
![Screenshot Menu utama](http://url/to/img.png)  
### Text Encryption and Decryption
Jika ingin melakukan enkripsi text:
1. isi text box plaintext atau tekan tombol load text dan pilih file teks berisi plaintext
2. pilih cipher
2. pilih cipher yang akan mengenkripsi plaintext
3. isi text box key
4. tekan tombol enkripsi text  

Jika ingin melakukan dekripsi text: 
1. isi text box ciphertext atau tekan tombol load text dan pilih file teks berisi ciphertext
2. pilih cipher yang akan mendekripsi ciphertext
3. isi text box key atau tekan tombol load key dan pilih file teks berisi plaintext
4. tekan tombol decrypt text dan hasil akan ditampilkan pada area plaintext

Jika tombol Encrypt Text ditekan sebanyak dua kali, akan mengubah hasil enkripsi menjadi memiliki spasi. Dan jika ditekan sekali lagi akan kembali seperti semula. Begitu juga ketika tombol Decrypt Text ditekan dua kali ketika melakukan dekripsi.

### File Encryption and Decryption
Cipher yang digunakan untuk proses enkripsi adalah cipher Extended Vigenere Cipher

Jika ingin melakukan enkripsi file sembarang (biner):
1. isi text box file plaintext file dengan url file atau tekan tombol upload file untuk membuka dialog open file dan pilih file yang ingin dienkripsi
2. tekan tombol Encrypt File dan tunggu beberapa saat sampai dialog untuk menyimpan file hasil enkripsi muncul
3. Isi nama file dan tekan simpan.

Jika ingin melakukan enkripsi file sembarang hasil enkripsi (biner):
1. isi text box file chipertext file dengan url file atau tekan tombol upload file untuk membuka dialog open file dan pilih file yang ingin didekripsi
2. tekan tombol Decrypt File dan tunggu beberapa saat sampai dialog untuk menyimpan file hasil enkripsi muncul
3. Isi nama file dan tekan simpan.

untuk melakukan testing file dapat digunakan file yang sudah disediakan pada direktori yang sama dengan readme ini yaitu file "sussy_gavial.gif"
