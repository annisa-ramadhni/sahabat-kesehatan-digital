# Sahabat Kesehatan Digital

**Sahabat Kesehatan Digital** adalah aplikasi desktop berbasis Python yang dibuat sebagai proyek mata kuliah **Pemrograman Dasar**. Aplikasi ini mensimulasikan alur layanan apotek digital mulai dari input data pengguna, pemilihan keluhan, pemilihan penyakit, hingga tampilan rekomendasi obat dan pembuatan pengingat konsumsi obat.

> **Catatan penting:** Proyek ini merupakan prototipe pembelajaran. Informasi obat dan rekomendasi di dalam aplikasi bersifat data yang telah ditentukan untuk keperluan demonstrasi dan **bukan** pengganti diagnosis, resep, atau konsultasi tenaga kesehatan.

## Fitur

- Input data pengguna: nama, umur, berat badan, dan tinggi badan.
- Pemilihan kategori keluhan.
- Pemilihan penyakit berdasarkan kategori.
- Menampilkan informasi rekomendasi obat, dosis/frekuensi, harga, dan waktu konsumsi dari data prototipe.
- Menyimpan data transaksi ke file Excel.
- Membuat file kalender `.ics` sebagai pengingat konsumsi obat.
- Antarmuka desktop menggunakan Tkinter.

## Teknologi

- **Python**
- **Tkinter** — graphical user interface
- **Pillow** — pemrosesan dan tampilan gambar
- **OpenPyXL** — penyimpanan data ke Excel
- **iCalendar** — pembuatan file pengingat `.ics`

## Struktur Repository

```text
sahabat-kesehatan-digital/
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
├── assets/
│   ├── backgrounds/
│   └── diseases/
└── screenshots/
```

## Cara Menjalankan

### 1. Clone repository

```bash
git clone https://github.com/USERNAME/sahabat-kesehatan-digital.git
cd sahabat-kesehatan-digital
```

### 2. Buat virtual environment (opsional tetapi disarankan)

```bash
python -m venv .venv
```

Aktifkan environment:

**macOS/Linux**
```bash
source .venv/bin/activate
```

**Windows**
```powershell
.venv\Scripts\activate
```

### 3. Install dependency

```bash
pip install -r requirements.txt
```

> Tkinter biasanya sudah tersedia pada instalasi Python desktop. Jika instalasi Python Anda tidak menyertakannya, pasang paket Tk/Tkinter sesuai sistem operasi yang digunakan.

### 4. Jalankan aplikasi

```bash
python app.py
```

## Alur Aplikasi

```text
Input Data Pengguna
        ↓
Pilih Keluhan
        ↓
Pilih Penyakit
        ↓
Tampilkan Rekomendasi
        ↓
Tampilkan Struk
        ↓
Simpan Data ke Excel
        ↓
Buat Pengingat .ics
```

## Catatan Implementasi

Versi repository ini menggunakan **path relatif terhadap repository**, bukan path lokal seperti `/Users/.../Downloads/...`. Dengan demikian, asset gambar dapat ditemukan setelah repository di-clone ke komputer lain.

Kategori keluhan pada versi repository menggunakan tombol teks. Hal ini dilakukan agar aplikasi tidak bergantung pada beberapa file ilustrasi kategori yang tidak tersedia dalam paket proyek yang dikumpulkan, sementara seluruh gambar penyakit yang digunakan pada tahap berikutnya tetap disertakan.

## Screenshot

Screenshot aplikasi tersedia di folder [`screenshots/`](screenshots/).

## Konteks Pembelajaran

Proyek ini dibuat untuk menerapkan konsep dasar pemrograman, antara lain:

- struktur program berbasis class,
- fungsi dan event handling,
- validasi input,
- pengelolaan file,
- penggunaan library eksternal,
- pembuatan GUI,
- serta integrasi penyimpanan data dan file kalender.

## Disclaimer

Aplikasi ini dibuat untuk tujuan pendidikan dan demonstrasi pemrograman. Jangan menggunakan hasil rekomendasi aplikasi sebagai dasar untuk menentukan diagnosis atau pengobatan.
