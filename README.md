# Sahabat Kesehatan Digital

### Digital Pharmacy & Medication Reminder Prototype

**Sahabat Kesehatan Digital** adalah aplikasi desktop berbasis Python yang dikembangkan sebagai proyek mata kuliah **Pemrograman Dasar**. Aplikasi ini mensimulasikan alur layanan apotek digital, mulai dari input data pengguna, pemilihan keluhan dan penyakit, hingga menampilkan rekomendasi obat, membuat transaksi, serta menghasilkan pengingat konsumsi obat.

> **Disclaimer:** Proyek ini merupakan prototipe pembelajaran. Informasi obat dan rekomendasi yang tersedia di dalam aplikasi menggunakan data yang telah ditentukan untuk keperluan demonstrasi dan **bukan** pengganti diagnosis, resep, atau konsultasi dengan tenaga kesehatan.

---

## 📌 Project Overview

Proyek ini dibuat untuk menerapkan konsep dasar pemrograman melalui sebuah aplikasi desktop dengan antarmuka grafis.

Pengguna dapat memasukkan informasi dasar, memilih kategori keluhan, memilih penyakit yang sesuai, kemudian melihat informasi obat yang telah ditentukan dalam data prototipe. Setelah proses pemilihan obat, aplikasi dapat menampilkan informasi transaksi, menyimpan data transaksi ke dalam file Excel, serta membuat file kalender `.ics` yang dapat digunakan sebagai pengingat waktu konsumsi obat.

Selain menerapkan konsep dasar pemrograman, proyek ini juga mengintegrasikan beberapa library Python untuk membangun GUI, mengelola gambar, menyimpan data, dan menghasilkan file kalender.

---

## ✨ Features

- Input data pengguna:
  - Nama
  - Umur
  - Berat badan
  - Tinggi badan
- Validasi input pengguna.
- Pemilihan kategori keluhan.
- Pemilihan penyakit berdasarkan kategori.
- Menampilkan informasi rekomendasi obat berdasarkan data prototipe.
- Menampilkan informasi dosis atau frekuensi konsumsi.
- Menampilkan harga obat.
- Menampilkan waktu konsumsi obat.
- Menampilkan ringkasan transaksi atau struk.
- Menyimpan data transaksi ke file Excel.
- Membuat file kalender `.ics` sebagai pengingat konsumsi obat.
- Antarmuka desktop menggunakan Tkinter.
- Penggunaan asset gambar untuk mendukung tampilan aplikasi.

---

## 🔄 Application Workflow

```text
Input Data Pengguna
        ↓
Validasi Input
        ↓
Pilih Kategori Keluhan
        ↓
Pilih Penyakit
        ↓
Tampilkan Rekomendasi Obat
        ↓
Tampilkan Informasi Dosis & Harga
        ↓
Tampilkan Struk Transaksi
        ↓
Simpan Data ke Excel
        ↓
Buat Pengingat Konsumsi (.ics)
```

---

## 🧩 Technical Implementation

### Object-Oriented Programming

Aplikasi menggunakan pendekatan **Object-Oriented Programming (OOP)** melalui beberapa class utama, antara lain:

- `ApotekDigital` — mengatur alur utama aplikasi dan interaksi antarmuka.
- `ExcelDataManager` — menangani penyimpanan data transaksi ke file Excel.
- `CalendarManager` — menangani pembuatan file kalender `.ics` untuk pengingat konsumsi obat.

### Input Validation

Aplikasi menerapkan validasi terhadap data yang dimasukkan pengguna, seperti:

- Nama hanya menerima karakter alfabet dan spasi.
- Umur menggunakan input numerik.
- Berat badan menggunakan input numerik.
- Tinggi badan menggunakan input numerik.

Validasi digunakan untuk membantu memastikan data yang dimasukkan sesuai dengan format yang dibutuhkan aplikasi.

### Data & File Management

Aplikasi menggunakan beberapa bentuk pengelolaan file:

- **Excel (`.xlsx`)** untuk menyimpan data transaksi.
- **Calendar (`.ics`)** untuk menghasilkan pengingat konsumsi obat.
- **Image assets** untuk mendukung tampilan antarmuka aplikasi.

Path asset pada repository menggunakan **relative path**, sehingga aplikasi tidak bergantung pada lokasi folder tertentu di komputer pengembang dan dapat dijalankan setelah repository di-clone ke lokasi lain.

### GUI & Event Handling

Antarmuka aplikasi dibangun menggunakan **Tkinter** dengan sistem event handling untuk mengatur interaksi pengguna, seperti pemilihan kategori, penyakit, serta proses menuju halaman atau tahapan berikutnya.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| **Python** | Main programming language |
| **Tkinter** | Desktop graphical user interface |
| **Pillow** | Image processing and image display |
| **OpenPyXL** | Excel file creation and data storage |
| **iCalendar** | `.ics` calendar and reminder generation |

---

## 📂 Repository Structure

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

### Main Files & Folders

| Path | Description |
|---|---|
| `app.py` | Main application source code |
| `requirements.txt` | Python dependencies |
| `assets/` | Application images and visual assets |
| `assets/backgrounds/` | Background images used by the application |
| `assets/diseases/` | Disease-related images |
| `screenshots/` | Application screenshots |
| `README.md` | Project documentation |

---

## 📷 Application Preview

Screenshots of the application are available in the [`screenshots/`](screenshots/) directory.

The application interface covers several stages of the workflow, including:

- User information input
- Complaint category selection
- Disease selection
- Medication recommendation
- Transaction summary

---

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/annisa-ramadhni/sahabat-kesehatan-digital.git
cd sahabat-kesehatan-digital
```

### 2. Create a virtual environment

Creating a virtual environment is optional but recommended.

```bash
python -m venv .venv
```

Activate the environment:

**macOS / Linux**

```bash
source .venv/bin/activate
```

**Windows**

```powershell
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

> Tkinter is commonly included with desktop Python installations. If Tkinter is not available in your Python installation, install the corresponding Tk/Tkinter package for your operating system.

### 4. Run the application

```bash
python app.py
```

---

## 🎓 Academic Context

**Course:** Basic Programming  
**Project Type:** Desktop Application  
**Development Language:** Python

This project was developed as part of coursework to practice fundamental programming concepts and basic software development.

### Concepts Applied

- Variables and data types
- Conditional statements
- Functions
- Loops
- Classes and objects
- Event handling
- Input validation
- File management
- External Python libraries
- GUI development
- Excel data storage
- Calendar file generation

---

## 📚 Learning Outcomes

Through this project, several foundational programming and application development concepts were practiced, including:

1. Designing a simple desktop application workflow.
2. Implementing user input validation.
3. Applying object-oriented programming concepts.
4. Managing application data and external files.
5. Integrating third-party Python libraries.
6. Building a graphical user interface with Tkinter.
7. Connecting user interactions with data storage and calendar generation.

---

## ⚠️ Disclaimer

This application is developed **for educational and programming demonstration purposes only**.

The medication information and recommendations displayed by the application are predefined prototype data and should **not** be used as a basis for diagnosis, medication decisions, or medical treatment.

For actual medical concerns, consult a qualified healthcare professional.

---

## 👩‍💻 Author

**Annisa Ramadhani**

Data Science Student
