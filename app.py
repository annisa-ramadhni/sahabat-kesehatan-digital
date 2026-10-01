import os
import tkinter as tk
from tkinter import messagebox
from icalendar import Calendar, Event
from datetime import datetime, timedelta
from PIL import Image, ImageTk
import openpyxl

# Project-relative asset paths so the application works after cloning the repository.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BACKGROUND_DIR = os.path.join(BASE_DIR, "assets", "backgrounds")
DISEASE_DIR = os.path.join(BASE_DIR, "assets", "diseases")


def asset_path(directory, filename):
    return os.path.join(directory, filename)


"""======================================= Class Calender Manager =============================="""

class CalendarManager:
    def __init__(self, rekomendasi_obat, waktu_konsumsi, nama):
        self.rekomendasi_obat = rekomendasi_obat
        self.waktu_konsumsi = waktu_konsumsi
        self.nama = nama
    
    def create_ics_file(self):
        cal = Calendar()
        waktu_list = self.waktu_konsumsi.split(", ")

        for waktu in waktu_list:
            jam, menit = map(int, waktu.split(":"))

            now = datetime.now()
            event_start = now.replace(hour=jam, minute=menit, second=0, microsecond=0)
            event_end = event_start + timedelta(minutes=30)

            event = Event()
            event.add("summary", f"Konsumsi {self.rekomendasi_obat}")
            event.add("dtstart", event_start)
            event.add("dtend", event_end)
            event.add("description", f"Jangan lupa konsumsi {self.rekomendasi_obat}.")
            event.add("location", "Rumah")
            cal.add_component(event)

        filename = f"{self.nama}_pengingat_obat.ics"
        with open(filename, "wb") as f:
            f.write(cal.to_ical())

        messagebox.showinfo("Pengingat", f"File .ics berhasil dibuat: {os.path.abspath(filename)}")

"""======================================= Batas Class Calender Manager =============================="""



"""======================================= Class Excel Data Manager =============================="""

class ExcelDataManager:
    def __init__(self, filename="Pembeli Apotek Digital.xlsx"):
        self.filename = filename

    def save_to_excel(self, data):
        header = ["Nama", "Umur", "Berat Badan", "Tinggi Badan", "Keluhan", "Obat", "Harga"]

        try:
            workbook = openpyxl.load_workbook(self.filename)
            sheet = workbook.active
        except FileNotFoundError:
            workbook = openpyxl.Workbook()
            sheet = workbook.active
            sheet.append(header)

        sheet.append(data)
        workbook.save(self.filename)
        messagebox.showinfo("Info", "Data berhasil disimpan ke Excel.")

"""=======================================  Batas Class Excel Data Manager =============================="""



"""======================================= Class Apotek Digital =============================="""

class ApotekDigital:
    
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Keluhan dan Rekomendasi Obat")
        self.root.geometry("1435x780")
                    
        self.nama_var = tk.StringVar()
        self.umur_var = tk.StringVar()
        self.berat_var = tk.StringVar()
        self.tinggi_var = tk.StringVar()
        self.keluhan_var = tk.StringVar()
        self.rekomendasi_var = tk.StringVar()
        self.struk_var = tk.StringVar()

        self.rekomendasi_obat = ""
        self.rekomendasi_harga = 0
        self.frekuensi_konsumsi = ""
        self.waktu_konsumsi = ""

        self.current_frame = None
        self.excel_manager = ExcelDataManager()
        self.calendar_manager = None
    
        self.init_frames()
        self.show_frame(self.frame_slide1)
                       
    def init_frames(self):
        self.frame_slide1 = self.create_slide1()
        self.frame_slide2 = self.create_slide2()
        self.frame_slide3 = tk.Frame(self.root)
        self.frame_slide4 = self.create_slide4()
        self.frame_slide5 = self.create_slide5()
        
    def create_slide1(self):
        frame = tk.Frame(self.root)

        def validate_name(char):
            return char.isalpha() or char.isspace() 

        def validate_number(char):
            return char.isdigit()  

        validate_name_cmd = self.root.register(validate_name)
        validate_number_cmd = self.root.register(validate_number)

        bg_image = Image.open(asset_path(BACKGROUND_DIR, "Slide 1 Apotek Digital.png"))
        bg_photo = ImageTk.PhotoImage(bg_image)

        bg_label = tk.Label(frame, image=bg_photo)
        bg_label.image = bg_photo
        bg_label.place(relwidth=1, relheight=1)

        content_frame = tk.Frame(frame, bg="pink")
        content_frame.place(relx=0.5, rely=0.5, anchor="center", width=430, height=450)

        tk.Label(content_frame, text="Data Pembeli", font=("Times New Roman", 45, "bold"), fg="white", bg="pink").pack(pady=20)
        tk.Label(content_frame, text="Nama:", bg="pink").pack(anchor="w", padx=80)
        tk.Entry(content_frame, textvariable=self.nama_var, validate="key", validatecommand=(validate_name_cmd, '%S')).pack(fill="x", padx=80, pady=8)
        tk.Label(content_frame, text="Umur:", bg="pink").pack(anchor="w", padx=80)
        tk.Entry(content_frame, textvariable=self.umur_var, validate="key", validatecommand=(validate_number_cmd, '%S')).pack(fill="x", padx=80, pady=8)
        tk.Label(content_frame, text="Berat Badan (Kg):", bg="pink").pack(anchor="w", padx=80)
        tk.Entry(content_frame, textvariable=self.berat_var, validate="key", validatecommand=(validate_number_cmd, '%S')).pack(fill="x", padx=80, pady=8)
        tk.Label(content_frame, text="Tinggi Badan (Cm):", bg="pink").pack(anchor="w", padx=80)
        tk.Entry(content_frame, textvariable=self.tinggi_var, validate="key", validatecommand=(validate_number_cmd, '%S')).pack(fill="x", padx=80, pady=8)
        tk.Button(content_frame, text="Lanjut", command=self.save_data_and_next).pack(pady=20)
        
        return frame
    
    def create_slide2(self):
        frame = tk.Frame(self.root)

        bg_image = Image.open(asset_path(BACKGROUND_DIR, "Keluhan Utama.png"))
        bg_photo = ImageTk.PhotoImage(bg_image)

        bg_label = tk.Label(frame, image=bg_photo)
        bg_label.image = bg_photo  
        bg_label.place(relwidth=1, relheight=1)

        tk.Label(frame, text="Keluhan Utama", font=("Times New Roman", 45, "bold"), fg="white", bg="pink").pack(pady=20)

        # The original project referenced category illustration files that were not
        # included in the submitted folder. Text buttons keep this repository portable.
        categories = [
            ["Kulit", "Batuk", "Pernapasan", "Sakit Kepala"],
            ["Gigi", "Sendi", "Otot", "Diabetes", "Penyakit Kelamin"],
            ["Pencernaan", "Darah", "Saraf", "Penyakit Dalam"],
        ]

        grid_frame = tk.Frame(frame, bg="pink")
        grid_frame.pack(pady=20)

        def create_buttons(frame, categories):
            for row_index, row in enumerate(categories):
                for col_index, keluhan in enumerate(row):
                    button = tk.Button(
                        frame,
                        text=keluhan,
                        command=lambda k=keluhan: self.show_detail_keluhan(k),
                        bg="pink",
                        font=("Times New Roman", 16, "bold"),
                        width=18,
                        height=3,
                    )
                    button.grid(row=row_index, column=col_index, padx=10, pady=10)

        create_buttons(grid_frame, categories)

        return frame
    
    def create_slide4(self):
        frame = tk.Frame(self.root)
        
        bg_image = Image.open(asset_path(BACKGROUND_DIR, "Slide 4 Apotek Digital.png"))
        bg_photo = ImageTk.PhotoImage(bg_image)

        bg_label = tk.Label(frame, image=bg_photo)
        bg_label.image = bg_photo  
        bg_label.place(relwidth=1, relheight=1)
        
        tk.Label(frame, text="Rekomendasi Obat", font=("Times New Roman", 20, "bold"), bg="pink").pack(pady=20)
        tk.Label(frame, textvariable=self.rekomendasi_var, font=("Courier", 12), justify="left", bg="pink").pack(pady=50)
        tk.Button(frame, text="Lanjut ke Struk", command=self.tampilkan_struk).pack(pady=20)
        return frame

    def create_slide5(self):
        frame = tk.Frame(self.root)
        bg_image = Image.open(asset_path(BACKGROUND_DIR, "Slide 5 Apotek Digital .png"))
        bg_photo = ImageTk.PhotoImage(bg_image)

        bg_label = tk.Label(frame, image=bg_photo)
        bg_label.image = bg_photo  
        bg_label.place(relwidth=1, relheight=1)
                
        tk.Label(frame, textvariable=self.struk_var, font=("Courier", 20), justify="left", bg="pink").pack(pady=50)
        tk.Button(frame, text="Selesai", command=self.selesai).pack(pady=20)
        return frame

    def save_data_and_next(self):
        if self.nama_var.get() and self.umur_var.get() and self.berat_var.get() and self.tinggi_var.get():
            try:
                float(self.berat_var.get())
                float(self.tinggi_var.get())
                self.show_frame(self.frame_slide2)
            except ValueError:
                messagebox.showwarning("Peringatan", "Berat dan Tinggi Badan harus berupa angka!")
        else:
            messagebox.showwarning("Peringatan", "Mohon isi Nama, Umur, Berat Badan, dan Tinggi Badan!")

    def show_detail_keluhan(self, keluhan):
        print(f"show_detail_keluhan dipanggil dengan keluhan: {keluhan}")
        detail_keluhan = {
            "Kulit": [
                {"nama": "Jerawat", "gambar": asset_path(DISEASE_DIR, "Jerawat.png")},
                {"nama": "Cacar Air", "gambar": asset_path(DISEASE_DIR, "Cacar Air.png")},
                {"nama": "Kudis", "gambar": asset_path(DISEASE_DIR, "Kudis.png")},
                {"nama": "Kurap", "gambar": asset_path(DISEASE_DIR, "Kurap.png")},
                {"nama": "Kutil", "gambar": asset_path(DISEASE_DIR, "Kutil.png")},
            ],
            "Batuk": [
                {"nama": "Batuk Berdahak", "gambar": asset_path(DISEASE_DIR, "Berdahak.png")},
                {"nama": "Batuk Tidak Berdahak", "gambar": asset_path(DISEASE_DIR, "Tidak Berdahak.png")},
            ],
            "Pernapasan": [
                {"nama": "Asma", "gambar": asset_path(DISEASE_DIR, "Asma.png")},
                {"nama": "Flu", "gambar": asset_path(DISEASE_DIR, "Flu.png")},
                {"nama": "ISPA", "gambar": asset_path(DISEASE_DIR, "Ispa.png")},
            ],
            "Sakit Kepala": [
                {"nama": "Sakit Kepala Tegang", "gambar": asset_path(DISEASE_DIR, "Kepala Tegang.png")},
                {"nama": "Sakit Kepala Cluster", "gambar": asset_path(DISEASE_DIR, "Kepala Cluster.png")},
            ],
            "Gigi": [
                {"nama": "Gigi Berlubang", "gambar": asset_path(DISEASE_DIR, "Gigi Berlubang.png")},
                {"nama": "Periodontitis", "gambar": asset_path(DISEASE_DIR, "Periodontitis.png")},
            ],
            "Sendi": [
                {"nama": "Osteoarthritis", "gambar": asset_path(DISEASE_DIR, "Osteoarthritis.png")},
            ],
            "Otot": [
                {"nama": "Myositis", "gambar": asset_path(DISEASE_DIR, "Myositis.png")},
                {"nama": "Fibromyalgia", "gambar": asset_path(DISEASE_DIR, "Fibromyalgia.png")},
            ],
            "Diabetes": [
                {"nama": "Diabetes Tipe 1", "gambar": asset_path(DISEASE_DIR, "Diabetes Tipe-1.png")},
                {"nama": "Diabetes Tipe 2", "gambar": asset_path(DISEASE_DIR, "Diabetes Tipe-2.png")},
            ],
            "Penyakit Kelamin": [
                {"nama": "Klamidia", "gambar": asset_path(DISEASE_DIR, "Klamidia.png")},
                {"nama": "Herpes Genital", "gambar": asset_path(DISEASE_DIR, "Herpes Genital.png")},
            ],
            "Pencernaan": [
                {"nama": "Maag", "gambar": asset_path(DISEASE_DIR, "Maag.png")},
                {"nama": "Kram Perut", "gambar": asset_path(DISEASE_DIR, "Kram Perut.png")},
            ],
            "Darah": [
                {"nama": "Anemia", "gambar": asset_path(DISEASE_DIR, "Anemia.png")},
            ],
            "Saraf": [
                {"nama": "Parkinson", "gambar": asset_path(DISEASE_DIR, "Parkinson.png")},
                {"nama": "Multiple Sclerosis", "gambar": asset_path(DISEASE_DIR, "Multiple Sclerosis.png")},
            ],
            "Penyakit Dalam": [
                {"nama": "Jantung", "gambar": asset_path(DISEASE_DIR, "Jantung.png")},
            ],
        }

        self.keluhan_var.set(keluhan)
        for widget in self.frame_slide3.winfo_children():
            widget.destroy()
        
        bg_image = Image.open(asset_path(BACKGROUND_DIR, "Slide 4 Apotek Digital.png"))
        bg_photo = ImageTk.PhotoImage(bg_image)

        bg_label = tk.Label(self.frame_slide3, image=bg_photo)
        bg_label.image = bg_photo
        bg_label.place(relwidth=1, relheight=1)
        
        tk.Label(
            self.frame_slide3, 
            text=f"Keluhan: {keluhan}", 
            font=("Times New Roman", 45, "bold"), 
            bg="pink"
        ).pack(pady=20)

        grid_frame = tk.Frame(self.frame_slide3, bg="pink")
        grid_frame.pack(pady=20)


        if keluhan in detail_keluhan:
            for index, detail in enumerate(detail_keluhan[keluhan]):
                
                image_path = detail["gambar"]
                penyakit_image = Image.open(image_path).resize((245, 245)) 
                penyakit_photo = ImageTk.PhotoImage(penyakit_image)

                penyakit_frame = tk.Frame(grid_frame, bg="pink", padx=10, pady=10)
                penyakit_frame.grid(row=index // 3, column=index % 3)

                image_label = tk.Label(penyakit_frame, image=penyakit_photo, bg="pink")
                image_label.image = penyakit_photo
                image_label.pack()

                tk.Label(
                    penyakit_frame,
                    text=detail["nama"],
                    font=("Times New Roman", 20, "bold"),
                    bg="pink"
                ).pack()
                
                tk.Button(
                    penyakit_frame,
                    text="Pilih",
                    command=lambda d=detail["nama"]: self.show_rekomendasi_obat(f"{keluhan} -> {d}"),
                    bg="pink",
                    font=("Times New Roman", 15, "bold")
                ).pack(pady=5)

        tk.Button(
            self.frame_slide3, 
            text="Kembali", 
            command=lambda: self.show_frame(self.frame_slide2), 
            bg="pink", 
            font=("Times New Roman", 20, "bold")
        ).pack(pady=20)

        self.show_frame(self.frame_slide3)
            
    def show_rekomendasi_obat(self, option):
        self.rekomendasi_obat, self.rekomendasi_harga, self.frekuensi_konsumsi, self.waktu_konsumsi = rekomendasi[option]
        self.rekomendasi_var.set(self.format_rekomendasi())
        self.show_frame(self.frame_slide4)

    def tampilkan_struk(self):
        self.struk_var.set(self.format_struk())
        self.excel_manager.save_to_excel([
            self.nama_var.get(),
            self.umur_var.get(),
            self.berat_var.get(),
            self.tinggi_var.get(),
            self.keluhan_var.get(),
            self.rekomendasi_obat,
            self.rekomendasi_harga,
        ])
        self.calendar_manager = CalendarManager(self.rekomendasi_obat, self.waktu_konsumsi, self.nama_var.get())
        self.calendar_manager.create_ics_file()
        self.show_frame(self.frame_slide5)

    def selesai(self):
        messagebox.showinfo("Pengingat", "Harap konsumsi obat sesuai petunjuk Dokter!")
        self.root.quit()

    def show_frame(self, frame):
        if self.current_frame:
            self.current_frame.pack_forget()
        self.current_frame = frame
        self.current_frame.pack(fill="both", expand=True)

    def format_rekomendasi(self):
        garis = "=" * 41
        rekomendasi_info = (
            f"{garis}\n"
            f"            REKOMENDASI OBAT\n"
            f"{garis}\n"
            f"Nama         : {self.nama_var.get()}\n"
            f"Umur         : {self.umur_var.get()} tahun\n"
            f"Berat Badan  : {self.berat_var.get()} kg\n"
            f"Tinggi Badan : {self.tinggi_var.get()} cm\n"
            f"{garis}\n"
            f"Keluhan      : {self.keluhan_var.get()}\n"
            f"Obat         : {self.rekomendasi_obat}\n"
            f"Dosis        : {self.frekuensi_konsumsi}\n"
            f"Harga        : Rp {self.rekomendasi_harga}\n"
            f"Waktu        : {self.waktu_konsumsi}\n"
            f"{garis}\n"
            f"Pastikan mematuhi petunjuk dokter!\n"
            f"{garis}"
        )
        return rekomendasi_info

    def format_struk(self):
        garis = "=" * 35
        nama = f"Nama        : {self.nama_var.get()}"
        umur = f"Umur        : {self.umur_var.get()} tahun"
        berat = f"Berat Badan : {self.berat_var.get()} kg"
        tinggi = f"Tinggi Badan: {self.tinggi_var.get()} cm"
        keluhan = f"Keluhan     : {self.keluhan_var.get()}"
        obat = f"Obat        : {self.rekomendasi_obat}"
        harga = f"Harga       : Rp {self.rekomendasi_harga}"
        footer = "Terima kasih telah berbelanja!"

        return (
            f"{garis}\n"
            f"          STRUK PEMBAYARAN\n"
            f"{garis}\n"
            f"{nama}\n"
            f"{umur}\n"
            f"{berat}\n"
            f"{tinggi}\n"
            f"\n"
            f"{keluhan}\n"
            f"{obat}\n"
            f"{harga}\n"
            f"{garis}\n"
            f"{footer}\n"
            f"{garis}"
        )

detail_keluhan = {
    "Kulit": ["Jerawat", "Cacar air", "Kudis", "Kurap", "Kutil"],
    "Batuk": ["Batuk berdahak", "Batuk tidak berdahak"],
    "Pernapasan": ["Asma", "Flu", "ISPA"],
    "Sakit Kepala": ["Sakit kepala tegang", "Sakit kepala cluster"],
    "Gigi": ["Gigi Berlubang", "Periodontitis"],
    "Sendi": ["Osteoarthritis"],
    "Otot": ["Myositis", "Fibromyalgia"],
    "Diabetes": ["Diabetes tipe 1", "Diabetes tipe 2"],
    "Penyakit Kelamin": ["Klamidia", "Herpes genital"],
    "Pencernaan": ["Maag", "Kram perut"],
    "Darah": ["Anemia"],
    "Saraf": ["Parkinson", "Multiple sclerosis"],
    "Penyakit Dalam": ["Jantung"] 
}

rekomendasi = {
    "Kulit -> Jerawat": ["Dermatix Acne Spot Care", 120000, "2 kali sehari", "10:34, 20:21"],
    "Kulit -> Cacar Air": ["Acyclovir", 50000, "3 kali sehari", "08:00, 14:00, 20:00"],
    "Kulit -> Kudis": ["Scabimite Cream", 45000, "1 kali sehari", "20:00"],
    "Kulit -> Kurap": ["Ketoconazole Cream", 40000, "2 kali sehari", "07:00, 19:00"],
    "Kulit -> Kutil": ["Salicylic Acid Ointment", 35000, "1 kali sehari", "21:00"],
    "Batuk -> Batuk Berdahak": ["Ambroxol Syrup", 30000, "3 kali sehari", "08:00, 13:00, 20:00"],
    "Batuk -> Batuk Tidak Berdahak": ["Dextromethorphan", 25000, "3 kali sehari", "08:00, 13:00, 20:00"],
    "Pernapasan -> Asma": ["Salbutamol Inhaler", 120000, "1 kali sehari", "20:00"],
    "Pernapasan -> Flu": ["Paracetamol", 20000, "3 kali sehari", "08:00, 14:00, 20:00"],
    "Pernapasan -> ISPA": ["Amoxicillin", 50000, "3 kali sehari", "08:00, 14:00, 20:00"],
    "Sakit Kepala -> Sakit Kepala Tegang": ["Ibuprofen", 30000, "2 kali sehari", "10:00, 22:00"],
    "Sakit Kepala -> Sakit Kepala Cluster": ["Sumatriptan", 100000, "1 kali sehari", "20:00"],
    "Gigi -> Gigi Berlubang": ["Metronidazole", 50000, "2 kali sehari", "09:00, 21:00"],
    "Gigi -> Periodontitis": ["Clindamycin", 60000, "2 kali sehari", "08:00, 20:00"],
    "Sendi -> Osteoarthritis": ["Meloxicam", 70000, "2 kali sehari", "08:00, 20:00"],
    "Otot -> Myositis": ["Methylprednisolone", 80000, "1 kali sehari", "21:00"],
    "Otot -> Fibromyalgia": ["Duloxetine", 120000, "1 kali sehari", "20:00"],
    "Diabetes -> Diabetes Tipe 1": ["Insulin Injection", 150000, "2 kali sehari", "07:00, 19:00"],
    "Diabetes -> Diabetes Tipe 2": ["Metformin", 60000, "2 kali sehari", "08:00, 20:00"],
    "Penyakit Kelamin -> Klamidia": ["Azithromycin", 80000, "1 kali sehari", "20:00"],
    "Penyakit Kelamin -> Herpes Genital": ["Acyclovir Oral", 70000, "3 kali sehari", "08:00, 14:00, 20:00"],
    "Pencernaan -> Maag": ["Omeprazole", 40000, "1 kali sehari", "08:00"],
    "Pencernaan -> Kram Perut": ["Buscopan", 35000, "3 kali sehari", "08:00, 13:00, 20:00"],
    "Darah -> Anemia": ["Ferrous Sulfate", 30000, "2 kali sehari", "08:00, 20:00"],
    "Saraf -> Parkinson": ["Levodopa", 120000, "3 kali sehari", "07:00, 13:00, 19:00"], 
    "Saraf -> Multiple Sclerosis": ["Interferon beta", 150000, "1 kali sehari", "20:00"], 
    "Penyakit Dalam -> Jantung": ["Bisoprolol", 50000, "1 kali sehari", "08:00"]
}
if __name__ == "__main__":
    root = tk.Tk()
    app = ApotekDigital(root)
    root.mainloop()
    
"""======================================= Batas Class Apotek Digital =============================="""
