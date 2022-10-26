# P1_Komnum_A7

#### Kelompok 7 :
- Muhammad Razan Athallah - 5025211008
- Alexander Weynard Samsico - 5025211014
- Revanantyo Dwigantara - 5025211113
- Apta Rasendriya Wijaya - 5025211139
- Akhmad Mustofa Solikin - 5025211230

#### Problem
Implementasikan algoritma metode Bolzano menjadi sebuah program komputer yang dapat menampilkan proses iteratif numerik, lengkap dengan grafik fungsinya.

Persamaan yang kami gunakan adalah:
```
x^3 - 4x^2 - 7x + 10
```

#### Penjelasan Formula Bolzano
1. Cek terlebih dahulu apakah batas bawah (xl/xlower) dan batas atas (xu/xupper) memenuhi syarat metode Bolzano. Jika f(xl) * f(xu) ≥ 0, maka batasan tidak memenuhi syarat.
```py
if (func(xl) * func(xu) >= 0): print("Batas bawah dan batas atas tidak memenuhi syarat metode bolzano.")
```
2. Taksiran pertama akar (root) atau baru: 
```py
xr = (xl + xu) / 2
```
3. Untuk mencari subinterval berikutnya:
```py
if (fl * fr == 0): print("akar: " + "{:.2f}".format(xr)) # akar = xr, berhenti
elif (fl * fr < 0): root(xl, xr) # xu = xr
elif (fl * fr > 0): root(xr, xu) # xl = xr
```
4. Kembali ke langkah pertama dengan input baru sampai akar ditemukan
  
#### How to use
1. Install dependencies yang dibutuhkan
```
$ pip install matplotlib
$ pip install numpy
$ pip install tabulate
```

2. Run `komnum-gemink.py`.

3. Input:
  - Input pertama batasan bawah (xl/xlower)
  - Input kedua batasan atas (xu/xupper)
  - Input ketiga maksimal iterasi
  
4. Output dan grafik akan muncul.

- Sample input:
```
-1
2
100
```

- Output:

<img src="https://user-images.githubusercontent.com/34641833/197456858-1a3342ee-fc81-4303-9da8-318bb959e1ec.png" width="60%">
<img src="https://user-images.githubusercontent.com/34641833/197457403-6181cc6e-1c1e-409b-9009-cf924a6f876b.png" width="60%">
<img src="https://user-images.githubusercontent.com/34641833/197458220-33607ae3-7583-4d42-b95b-5d8e89a8bf90.png" width="50%">


