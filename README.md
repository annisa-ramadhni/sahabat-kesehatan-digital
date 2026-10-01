# Sahabat Kesehatan Digital

### Digital Pharmacy & Medication Reminder Prototype

**Sahabat Kesehatan Digital** adalah aplikasi desktop berbasis Python yang dikembangkan sebagai proyek mata kuliah **Pemrograman Dasar**. Aplikasi ini mensimulasikan alur layanan apotek digital, mulai dari input data pengguna, pemilihan keluhan dan penyakit, hingga menampilkan rekomendasi obat, membuat transaksi, dan menghasilkan pengingat konsumsi obat.

> **Disclaimer:** Proyek ini merupakan prototipe pembelajaran. Informasi obat dan rekomendasi yang tersedia di dalam aplikasi menggunakan data yang telah ditentukan untuk keperluan demonstrasi dan **bukan** pengganti diagnosis, resep, atau konsultasi dengan tenaga kesehatan.

---

## 📌 Project Overview

Proyek ini dibuat untuk menerapkan konsep dasar pemrograman melalui pengembangan aplikasi desktop dengan antarmuka grafis.

Pengguna dapat memasukkan informasi dasar, memilih kategori keluhan, memilih penyakit, kemudian melihat informasi obat yang telah ditentukan dalam data prototipe. Setelah proses pemilihan obat, aplikasi dapat menampilkan ringkasan transaksi, menyimpan data transaksi ke file Excel, serta menghasilkan file kalender `.ics` yang dapat digunakan sebagai pengingat waktu konsumsi obat.

Proyek ini juga mengintegrasikan beberapa library Python untuk membangun antarmuka pengguna, mengelola gambar, menyimpan data, dan menghasilkan file kalender.

---

## ✨ Features

* **User Information**

  * Input nama
  * Input umur
  * Input berat badan
  * Input tinggi badan
  * Validasi data pengguna

* **Health Complaint & Disease Selection**

  * Pemilihan kategori keluhan
  * Pemilihan penyakit berdasarkan kategori

* **Medication Recommendation**

  * Menampilkan obat berdasarkan data prototipe
  * Menampilkan dosis atau frekuensi konsumsi
  * Menampilkan harga obat
  * Menampilkan waktu konsumsi

* **Transaction Management**

  * Menampilkan ringkasan transaksi
  * Menyimpan data transaksi ke file Excel

* **Medication Reminder**

  * Menghasilkan file kalender `.ics`
  * Membuat jadwal pengingat berdasarkan waktu konsumsi obat

* **Desktop GUI**

  * Antarmuka berbasis Tkinter
  * Penggunaan gambar dan background sebagai bagian dari tampilan aplikasi

---

## 🔄 Application Workflow

```text
┌─────────────────────────┐
│   Input User Information│
└────────────┬────────────┘
             ↓
┌─────────────────────────┐
│     Input Validation    │
└────────────┬────────────┘
             ↓
┌─────────────────────────┐
│ Select Complaint Category│
└────────────┬────────────┘
             ↓
┌─────────────────────────┐
│      Select Disease     │
└────────────┬────────────┘
             ↓
┌─────────────────────────┐
│ Medication Recommendation│
└────────────┬────────────┘
             ↓
┌─────────────────────────┐
│   Transaction Summary   │
└────────────┬────────────┘
             ↓
      ┌──────┴──────┐
      ↓             ↓
┌─────────────┐ ┌──────────────┐
│ Save to Excel│ │Generate .ics │
└─────────────┘ └──────────────┘
```

---

## 🧩 Technical Implementation

### 1. Object-Oriented Programming

Aplikasi menggunakan pendekatan **Object-Oriented Programming (OOP)** dengan beberapa class utama:

* `ApotekDigital`
  Mengatur alur utama aplikasi, tampilan, dan interaksi pengguna.

* `ExcelDataManager`
  Menangani penyimpanan data transaksi ke dalam file Excel.

* `CalendarManager`
  Menangani pembuatan file kalender `.ics` untuk pengingat konsumsi obat.

Penggunaan class membantu memisahkan tanggung jawab setiap bagian aplikasi dan membuat struktur program lebih terorganisasi.

### 2. Input Validation

Aplikasi menerapkan validasi terhadap data pengguna sebelum melanjutkan ke tahap berikutnya.

Contohnya:

* Nama hanya menerima karakter alfabet dan spasi.
* Umur menggunakan input numerik.
* Berat badan menggunakan input numerik.
* Tinggi badan menggunakan input numerik.

Validasi ini digunakan untuk mengurangi kesalahan format input selama aplikasi dijalankan.

### 3. Predefined Medication Data

Informasi penyakit dan obat pada aplikasi menggunakan **data yang telah ditentukan di dalam program**.

Data tersebut digunakan untuk mendemonstrasikan alur:

```text
Complaint Category
        ↓
Disease
        ↓
Medication
        ↓
Dosage / Frequency
        ↓
Price
        ↓
Consumption Schedule
```

Karena data bersifat predefined, aplikasi **tidak melakukan diagnosis medis atau machine learning untuk menentukan obat**.

### 4. Excel Data Management

Data transaksi dapat disimpan menggunakan **OpenPyXL** ke dalam file Excel.

Data yang disimpan mencakup informasi seperti:

* Nama pengguna
* Umur
* Berat badan
* Tinggi badan
* Keluhan
* Obat
* Harga

### 5. Calendar Reminder Generation

Aplikasi menggunakan library **iCalendar** untuk menghasilkan file `.ics`.

File tersebut berisi event pengingat konsumsi obat berdasarkan jadwal yang ditentukan pada data prototipe.

### 6. Relative File Paths

Repository menggunakan **relative path** untuk mengakses asset aplikasi.

Dengan pendekatan ini, aplikasi tidak bergantung pada lokasi folder tertentu di komputer pengembang sehingga asset tetap dapat ditemukan ketika repository di-clone ke lokasi lain.

### 7. GUI & Event Handling

Antarmuka aplikasi dikembangkan menggunakan **Tkinter**.

Event handling digunakan untuk mengatur berbagai interaksi pengguna, termasuk:

* Input data
* Pemilihan kategori
* Pemilihan penyakit
* Navigasi antar tahap aplikasi
* Menampilkan hasil rekomendasi
* Menyimpan transaksi
* Membuat pengingat

---

## 🛠️ Tech Stack

| Technology    | Purpose                                       |
| ------------- | --------------------------------------------- |
| **Python**    | Main programming language                     |
| **Tkinter**   | Desktop graphical user interface              |
| **Pillow**    | Image processing and image display            |
| **OpenPyXL**  | Excel file creation and transaction storage   |
| **iCalendar** | Calendar event and `.ics` reminder generation |

---

## 📂 Repository Structure

```text
sahabat-kesehatan-digital/
│
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
│
├── assets/
│   ├── backgrounds/
│   └── diseases/
│
└── screenshots/
```

### Main Files & Folders

| Path                  | Description                                     |
| --------------------- | ----------------------------------------------- |
| `app.py`              | Main application source code                    |
| `requirements.txt`    | Python package dependencies                     |
| `.gitignore`          | Files and folders excluded from version control |
| `assets/`             | Visual assets used by the application           |
| `assets/backgrounds/` | Background images                               |
| `assets/diseases/`    | Disease-related images                          |
| `screenshots/`        | Screenshots of the application                  |
| `README.md`           | Project documentation                           |

---

## 📷 Application Preview

Screenshots of the application are available in the [`screenshots/`](screenshots/) directory.

The screenshots document the main stages of the application interface:

1. User information input
2. Complaint category selection
3. Disease selection
4. Medication recommendation
5. Transaction summary

---

## 🚀 How to Run

### Prerequisites

Make sure the following are available on your computer:

* Python 3.x
* `pip`
* Tkinter

### 1. Clone the repository

```bash
git clone https://github.com/annisa-ramadhni/sahabat-kesehatan-digital.git
cd sahabat-kesehatan-digital
```

### 2. Create a virtual environment

Creating a virtual environment is recommended to keep project dependencies isolated.

**Windows:**

```powershell
python -m venv .venv
.venv\Scripts\activate
```

**macOS / Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python app.py
```

> **Note:** Tkinter is commonly included with desktop Python installations. If Tkinter is not available, install the corresponding Tk/Tkinter package for your operating system.

---

## 🎓 Academic Context

**Course:** Basic Programming
**Project Type:** Desktop Application
**Programming Language:** Python

This project was developed as part of coursework to practice fundamental programming concepts and basic desktop application development.

### Concepts Applied

* Variables and data types
* Conditional statements
* Functions
* Loops
* Classes and objects
* Object-oriented programming
* Event handling
* Input validation
* File management
* External Python libraries
* GUI development
* Excel data storage
* Calendar file generation

---

## 📚 Learning Outcomes

Through this project, the following programming and application development concepts were practiced:

* Designing a multi-step desktop application workflow.
* Implementing input validation.
* Applying object-oriented programming concepts.
* Organizing application logic using classes and functions.
* Managing external files and application assets.
* Integrating third-party Python libraries.
* Building a graphical user interface with Tkinter.
* Storing structured transaction data in Excel.
* Generating calendar files for scheduled reminders.

---

## ⚠️ Disclaimer

This application was developed **for educational and programming demonstration purposes only**.

The medication information and recommendations displayed by the application are based on predefined prototype data. They should **not** be used as a basis for diagnosis, medication decisions, prescriptions, or medical treatment.

For actual medical concerns, consult a qualified healthcare professional.

---

## 👩‍💻 Author

**Annisa Ramadhani**

Data Science Student
