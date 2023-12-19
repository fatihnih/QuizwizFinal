import customtkinter as ctk  
from CTkMessagebox import CTkMessagebox
import tkinter
from CTkListbox import *

judul_soal = {}
tingkat_kesulitan = {} 
soal = []
jawaban = []
deskJawaban = []
penjelasan = []
judul_dipilih = '' 

judulEsai={}
kesulitanEsai={}
soalEsai=[]
jawabanEsai=[]
deskEsai=[]
judul_dipilihEsai= ''

def main():
    clear_frame()
    judul = ctk.CTkLabel(frame, text="WELCOME TO QUIZWIZ")
    judul.pack(pady=20)

    label1 = ctk.CTkLabel(frame, text="SILAHKAN LOGIN")
    label1.pack(pady=10)

    username_label = ctk.CTkLabel(frame, text="Username:")
    username_label.pack(pady=(12, 0))

    global username_entry
    username_entry= ctk.CTkEntry(frame)
    username_entry.pack(pady=(0, 10))

    password_label = ctk.CTkLabel(frame, text="Password:")
    password_label.pack(pady=(12, 0))

    global password_entry
    password_entry = ctk.CTkEntry(frame, show="*") 
    password_entry.pack(pady=(0, 10))

    login_button = ctk.CTkButton(frame, text="Login", command=login)
    login_button.pack(pady=(30, 10))

def login():
    userid = username_entry.get()
    password = password_entry.get()

    if userid == "guru" and password == "123":
        adminPage()
    elif userid == "murid" and password == "321":
        userPage()
    elif userid == "" and password == "":
        CTkMessagebox(title="Login Failed", message="Masukkan username dan password!!")
    elif (userid != "admin" or userid != "user") and (password == "123" or password == "321"):
        CTkMessagebox(title="Login Failed", message="Username salah!!")
    elif (userid == "admin" or userid == "user") and (password != "123" or password != "321"):
        CTkMessagebox(title="Login Failed", message="Password salah!!")
    else:
        CTkMessagebox(title="Login Failed", message="Invalid username or password")

def adminPage():
    clear_frame()
    label1 = ctk.CTkLabel(
        frame,
        text="MAIN MENU",
        padx=20,
        pady=20
    ).pack()

    tombol1 = ctk.CTkButton(
        frame, 
        text="Buat Soal",
        command=buat_soalPage
        ).pack(pady=20)
    
    tombol2 = ctk.CTkButton(
        frame, 
        text="Hapus Soal",
        command=pilihHapus
        ).pack(pady=20)

    tombol3 = ctk.CTkButton(
        frame, 
        text="Halaman Login",
        command=main
        ).pack(pady=(120,20))

def pilihHapus():
    clear_frame()
    judul = ctk.CTkLabel(frame, text="Pilih Jenis Soal:")
    judul.pack(pady=10)

    optionmenu_var = ctk.StringVar(value="Pilih Jenis Soal")  # set initial value
    combobox = ctk.CTkOptionMenu(master=frame,
                                       values=["Pilihan Ganda", "Essai"],
                                       command=delete_callback,
                                       variable=optionmenu_var)
    combobox.pack(padx=20, pady=10)

    submitHapus = ctk.CTkButton(frame, text="SUBMIT", command=Hapus)
    submitHapus.pack(side='bottom')

def Hapus():
    if tipesoalHapus == "Pilihan Ganda":
        hapus_soalPage()
    elif tipesoalHapus == "Essai":
        hapus_essai()
    else:
        CTkMessagebox(title="Login Failed", message="Pilih Jenis Terlebih Dahulu")

def delete_callback(choice):
    global tipesoalHapus
    tipesoalHapus = choice
    
def hapus_soalPage():
    clear_frame()
    global selected_delete
    selected_delete = ctk.StringVar()

    judul = ctk.CTkLabel(frame, text="PILIH JUDUL YANG INGIN DIHAPUS :")
    judul.pack(pady=(20,10))

    global listbox1
    listbox1 = CTkListbox(frame, command=delete_value)
    listbox1.pack(fill="both", expand=True, padx=5)

    for i, (judul, jumlah) in enumerate(judul_soal.items()):
        listbox1.insert(i, judul)

    tombolBack = ctk.CTkButton(frame, text="Kembali", command=adminPage)
    tombolBack.pack(pady=10)

def delete_value(selected_option):
    selected_delete.set(selected_option)
    hapus = selected_delete.get()

    indeks_awal = 0
    for judul, jumlah_soal in judul_soal.items():
        if judul == hapus:
            break
        indeks_awal += jumlah_soal
    
    indeks_akhir = indeks_awal + judul_soal[hapus]
    
    listbox1.delete(indeks_awal, indeks_akhir)
    del judul_soal[hapus]
    del tingkat_kesulitan[hapus]

    for i in range(indeks_awal,indeks_akhir):
        del soal[indeks_awal]
        del jawaban[indeks_awal]
        del deskJawaban[indeks_awal]   

    hapus_soalPage()   

def hapus_essai():
    clear_frame()
    global selected_deleteEssai
    selected_deleteEssai = ctk.StringVar()

    judul = ctk.CTkLabel(frame, text="PILIH JUDUL YANG INGIN DIHAPUS :")
    judul.pack(pady=(20,10))

    global listbox2
    listbox2 = CTkListbox(frame, command=delete_value_esai)
    listbox2.pack(fill="both", expand=True, padx=5)

    for i, (judul, jumlah) in enumerate(judulEsai.items()):
        listbox2.insert(i, judul)

    tombolBack = ctk.CTkButton(frame, text="Kembali", command=adminPage)
    tombolBack.pack(pady=10)      

def delete_value_esai(selected):
    selected_deleteEssai.set(selected)
    hapus = selected_deleteEssai.get()

    indeks_awal = 0
    for judul, jumlah_soal in judulEsai.items():
        if judul == hapus:
            break
        indeks_awal += jumlah_soal
    
    indeks_akhir = indeks_awal + judulEsai[hapus]
    
    listbox2.delete(indeks_awal, indeks_akhir)
    del judulEsai[hapus]
    del kesulitanEsai[hapus]

    for i in range(indeks_awal,indeks_akhir):
        del soalEsai[indeks_awal]
        del jawabanEsai[indeks_awal]
        del deskEsai[indeks_awal]   

    hapus_essai()

def buat_soalPage():
    clear_frame()
    judul = ctk.CTkLabel(frame, text="BUAT SOALWLEOWLEO")
    judul.pack(pady=(20,10))

    label1 = ctk.CTkLabel(frame, text="MATERI : ")
    label1.pack(pady=10)

    global e1
    e1 = ctk.CTkEntry(frame)
    e1.pack(pady=10)

    optionmenu_var = ctk.StringVar(value="Tipe Soal")  # set initial value
    combobox = ctk.CTkOptionMenu(master=frame,
                                       values=["Pilihan Ganda", "Essai"],
                                       command=opsiSoal,
                                       variable=optionmenu_var)
    combobox.pack(pady=10)

    submit = ctk.CTkButton(frame, text="SUBMIT", command=sub_create)
    submit.pack(pady=(120,5),padx=10,side="right")

    tombolBack = ctk.CTkButton(frame, text="Kembali", command=adminPage)
    tombolBack.pack(padx=10, pady=(120,5), side="left")

def opsiSoal(choice):
     global tipesoal
     if choice != '':
        tipesoal = choice
     else:
        CTkMessagebox(title="Error", message="Masukkan tipe soal")

def sub_create():
    a = e1.get()
    materi = a.lower()
    if (materi != "") and (tipesoal == "Pilihan Ganda"):
        formSoalPage()
    elif (materi != "") and (tipesoal == "Essai"):
        formEsai()
    elif (materi != "") and (tipesoal == "Tipe Soal"):
        CTkMessagebox(title="Error", message="Masukkan tipe soal")
    else:
        CTkMessagebox(title="Error", message="Masukkan materi")

def kesulitan(choice):
    kesulitanEsai[entry3.get()] = choice

def formEsai():
    clear_frame()
    judul = ctk.CTkLabel(frame,text="Judul Soal").pack()

    global entry3
    entry3 = ctk.CTkEntry(frame)
    entry3.pack(pady=(0,5))

    optionmenu_var = ctk.StringVar(value="Kesulitan")  # set initial value
    combobox = ctk.CTkOptionMenu(master=frame,
                                       values=["Sulit", "Mudah"],
                                       command=kesulitan,
                                       variable=optionmenu_var)
    combobox.pack(padx=20, pady=10)

    Scrollframe = ctk.CTkScrollableFrame(master=frame, width=200, height=200)
    Scrollframe.pack(padx=5, fill="both", expand=True)

    global esai1
    esai1 = ctk.CTkEntry(Scrollframe, width=300, placeholder_text="Soal 1")
    esai1.pack()
    global jawab1
    jawab1 = ctk.CTkEntry(Scrollframe, width=150, placeholder_text="Jawaban 1")
    jawab1.pack()
    global desk1
    desk1 = ctk.CTkEntry(Scrollframe, width=300, placeholder_text="Penjelasan 1")
    desk1.pack(pady=(0,10))

    global esai2
    esai2 = ctk.CTkEntry(Scrollframe, width=300, placeholder_text="Soal 2")
    esai2.pack()
    global jawab2
    jawab2 = ctk.CTkEntry(Scrollframe, width=150, placeholder_text="Jawaban 2")
    jawab2.pack()
    global desk2
    desk2 = ctk.CTkEntry(Scrollframe, width=300, placeholder_text="Penjelasan 2")
    desk2.pack(pady=(0,10))

    global esai3
    esai3 = ctk.CTkEntry(Scrollframe, width=300, placeholder_text="Soal 3")
    esai3.pack()
    global jawab3
    jawab3 = ctk.CTkEntry(Scrollframe, width=150, placeholder_text="Jawaban 3")
    jawab3.pack()
    global desk3
    desk3 = ctk.CTkEntry(Scrollframe, width=300, placeholder_text="Penjelasan 3")
    desk3.pack(pady=(0,10))

    global esai4
    esai4 = ctk.CTkEntry(Scrollframe, width=300, placeholder_text="Soal 4")
    esai4.pack()
    global jawab4
    jawab4 = ctk.CTkEntry(Scrollframe, width=150, placeholder_text="Jawaban 4")
    jawab4.pack()
    global desk4
    desk4 = ctk.CTkEntry(Scrollframe, width=300, placeholder_text="Penjelasan 4")
    desk4.pack(pady=(0,10))

    global esai5
    esai5 = ctk.CTkEntry(Scrollframe, width=300, placeholder_text="Soal 5")
    esai5.pack()
    global jawab5
    jawab5 = ctk.CTkEntry(Scrollframe, width=150, placeholder_text="Jawaban 5")
    jawab5.pack()
    global desk5
    desk5 = ctk.CTkEntry(Scrollframe, width=300, placeholder_text="Penjelasan 5")
    desk5.pack(pady=(0,10))

    global esai6
    esai6 = ctk.CTkEntry(Scrollframe, width=300, placeholder_text="Soal 6")
    esai6.pack()
    global jawab6
    jawab6 = ctk.CTkEntry(Scrollframe, width=150, placeholder_text="Jawaban 6")
    jawab6.pack()
    global desk6
    desk6 = ctk.CTkEntry(Scrollframe, width=300, placeholder_text="Penjelasan 6")
    desk6.pack(pady=(0,10))

    global esai7
    esai7 = ctk.CTkEntry(Scrollframe, width=300, placeholder_text="Soal 7")
    esai7.pack()
    global jawab7
    jawab7 = ctk.CTkEntry(Scrollframe, width=150, placeholder_text="Jawaban 7")
    jawab7.pack()
    global desk7
    desk7 = ctk.CTkEntry(Scrollframe, width=300, placeholder_text="Penjelasan 7")
    desk7.pack(pady=(0,10))

    global esai8
    esai8 = ctk.CTkEntry(Scrollframe, width=300, placeholder_text="Soal 8")
    esai8.pack()
    global jawab8
    jawab8 = ctk.CTkEntry(Scrollframe, width=150, placeholder_text="Jawaban 8")
    jawab8.pack()
    global desk8
    desk8 = ctk.CTkEntry(Scrollframe, width=300, placeholder_text="Penjelasan 8")
    desk8.pack(pady=(0,10))

    global esai9
    esai9 = ctk.CTkEntry(Scrollframe, width=300, placeholder_text="Soal 9")
    esai9.pack()
    global jawab9
    jawab9 = ctk.CTkEntry(Scrollframe, width=150, placeholder_text="Jawaban 9")
    jawab9.pack()
    global desk9
    desk9 = ctk.CTkEntry(Scrollframe, width=300, placeholder_text="Penjelasan 9")
    desk9.pack(pady=(0,10))

    global esai10
    esai10 = ctk.CTkEntry(Scrollframe, width=300, placeholder_text="Soal 10")
    esai10.pack()
    global jawab10
    jawab10 = ctk.CTkEntry(Scrollframe, width=150, placeholder_text="Jawaban 10")
    jawab10.pack()
    global desk10
    desk10 = ctk.CTkEntry(Scrollframe, width=300, placeholder_text="Penjelasan 10")
    desk10.pack(pady=(0,10))

    tombol_submit = ctk.CTkButton(frame, text="SUBMIT", command=submitEsai)
    tombol_submit.pack(pady=10)

def submitEsai():
    judul = entry3.get()

    if esai10.get() != '' :
            soalEsai.append(esai1.get())
            soalEsai.append(esai2.get())
            soalEsai.append(esai3.get())
            soalEsai.append(esai4.get())
            soalEsai.append(esai5.get())
            soalEsai.append(esai6.get())
            soalEsai.append(esai7.get())
            soalEsai.append(esai8.get())
            soalEsai.append(esai9.get())
            soalEsai.append(esai10.get())
            judulEsai[judul] = 10
            jawabanEsai.append(jawab1.get())
            jawabanEsai.append(jawab2.get())
            jawabanEsai.append(jawab3.get())
            jawabanEsai.append(jawab4.get())
            jawabanEsai.append(jawab5.get())
            jawabanEsai.append(jawab6.get())
            jawabanEsai.append(jawab7.get())
            jawabanEsai.append(jawab8.get())
            jawabanEsai.append(jawab9.get())
            jawabanEsai.append(jawab10.get())
            deskEsai.append(desk1.get())
            deskEsai.append(desk2.get())
            deskEsai.append(desk3.get())
            deskEsai.append(desk4.get())
            deskEsai.append(desk5.get())
            deskEsai.append(desk6.get())
            deskEsai.append(desk7.get())
            deskEsai.append(desk8.get())
            deskEsai.append(desk9.get())
            deskEsai.append(desk10.get())
            
    elif esai9.get() != '':
            soalEsai.append(esai1.get())
            soalEsai.append(esai2.get())
            soalEsai.append(esai3.get())
            soalEsai.append(esai4.get())
            soalEsai.append(esai5.get())
            soalEsai.append(esai6.get())
            soalEsai.append(esai7.get())
            soalEsai.append(esai8.get())
            soalEsai.append(esai9.get())
            judulEsai[judul] = 9
            jawabanEsai.append(jawab1.get())
            jawabanEsai.append(jawab2.get())
            jawabanEsai.append(jawab3.get())
            jawabanEsai.append(jawab4.get())
            jawabanEsai.append(jawab5.get())
            jawabanEsai.append(jawab6.get())
            jawabanEsai.append(jawab7.get())
            jawabanEsai.append(jawab8.get())
            jawabanEsai.append(jawab9.get())
            deskEsai.append(desk1.get())
            deskEsai.append(desk2.get())
            deskEsai.append(desk3.get())
            deskEsai.append(desk4.get())
            deskEsai.append(desk5.get())
            deskEsai.append(desk6.get())
            deskEsai.append(desk7.get())
            deskEsai.append(desk8.get())
            deskEsai.append(desk9.get())
            
    elif esai8.get() != '':
            soalEsai.append(esai1.get())
            soalEsai.append(esai2.get())
            soalEsai.append(esai3.get())
            soalEsai.append(esai4.get())
            soalEsai.append(esai5.get())
            soalEsai.append(esai6.get())
            soalEsai.append(esai7.get())
            soalEsai.append(esai8.get())
            judulEsai[judul] = 8
            jawabanEsai.append(jawab1.get())
            jawabanEsai.append(jawab2.get())
            jawabanEsai.append(jawab3.get())
            jawabanEsai.append(jawab4.get())
            jawabanEsai.append(jawab5.get())
            jawabanEsai.append(jawab6.get())
            jawabanEsai.append(jawab7.get())
            jawabanEsai.append(jawab8.get())
            deskEsai.append(desk1.get())
            deskEsai.append(desk2.get())
            deskEsai.append(desk3.get())
            deskEsai.append(desk4.get())
            deskEsai.append(desk5.get())
            deskEsai.append(desk6.get())
            deskEsai.append(desk7.get())
            deskEsai.append(desk8.get())
            
    elif esai7.get() != '':
            soalEsai.append(esai1.get())
            soalEsai.append(esai2.get())
            soalEsai.append(esai3.get())
            soalEsai.append(esai4.get())
            soalEsai.append(esai5.get())
            soalEsai.append(esai6.get())
            soalEsai.append(esai7.get())
            judulEsai[judul] = 7
            jawabanEsai.append(jawab1.get())
            jawabanEsai.append(jawab2.get())
            jawabanEsai.append(jawab3.get())
            jawabanEsai.append(jawab4.get())
            jawabanEsai.append(jawab5.get())
            jawabanEsai.append(jawab6.get())
            jawabanEsai.append(jawab7.get())
            deskEsai.append(desk1.get())
            deskEsai.append(desk2.get())
            deskEsai.append(desk3.get())
            deskEsai.append(desk4.get())
            deskEsai.append(desk5.get())
            deskEsai.append(desk6.get())
            deskEsai.append(desk7.get())
            
    elif esai6.get() != '':
            soalEsai.append(esai1.get())
            soalEsai.append(esai2.get())
            soalEsai.append(esai3.get())
            soalEsai.append(esai4.get())
            soalEsai.append(esai5.get())
            soalEsai.append(esai6.get())
            judulEsai[judul] = 6
            jawabanEsai.append(jawab1.get())
            jawabanEsai.append(jawab2.get())
            jawabanEsai.append(jawab3.get())
            jawabanEsai.append(jawab4.get())
            jawabanEsai.append(jawab5.get())
            jawabanEsai.append(jawab6.get())
            deskEsai.append(desk1.get())
            deskEsai.append(desk2.get())
            deskEsai.append(desk3.get())
            deskEsai.append(desk4.get())
            deskEsai.append(desk5.get())
            deskEsai.append(desk6.get())
            
    elif esai5.get() != '':
            soalEsai.append(esai1.get())
            soalEsai.append(esai2.get())
            soalEsai.append(esai3.get())
            soalEsai.append(esai4.get())
            soalEsai.append(esai5.get())
            judulEsai[judul] = 5
            jawabanEsai.append(jawab1.get())
            jawabanEsai.append(jawab2.get())
            jawabanEsai.append(jawab3.get())
            jawabanEsai.append(jawab4.get())
            jawabanEsai.append(jawab5.get())
            deskEsai.append(desk1.get())
            deskEsai.append(desk2.get())
            deskEsai.append(desk3.get())
            deskEsai.append(desk4.get())
            deskEsai.append(desk5.get())
            
    elif esai4.get() != '':
            soalEsai.append(esai1.get())
            soalEsai.append(esai2.get())
            soalEsai.append(esai3.get())
            soalEsai.append(esai4.get())
            judulEsai[judul] = 4
            jawabanEsai.append(jawab1.get())
            jawabanEsai.append(jawab2.get())
            jawabanEsai.append(jawab3.get())
            jawabanEsai.append(jawab4.get())
            deskEsai.append(desk1.get())
            deskEsai.append(desk2.get())
            deskEsai.append(desk3.get())
            deskEsai.append(desk4.get())
            
            
    elif esai3.get() != '':
            soalEsai.append(esai1.get())
            soalEsai.append(esai2.get())
            soalEsai.append(esai3.get())
            judulEsai[judul] = 3
            jawabanEsai.append(jawab1.get())
            jawabanEsai.append(jawab2.get())
            jawabanEsai.append(jawab3.get())
            deskEsai.append(desk1.get())
            deskEsai.append(desk2.get())
            deskEsai.append(desk3.get())
            
    elif esai2.get() != '':
            soalEsai.append(esai1.get())
            soalEsai.append(esai2.get())
            judulEsai[judul] = 2
            jawabanEsai.append(jawab1.get())
            jawabanEsai.append(jawab2.get())
            deskEsai.append(desk1.get())
            deskEsai.append(desk2.get())
            
    elif esai1.get() != '':
            soalEsai.append(esai1.get())
            judulEsai[judul] = 1
            jawabanEsai.append(jawab1.get())
            deskEsai.append(desk1.get())

    ask_questionAdmin()

def formSoalPage():
    clear_frame()
    global var_values
    var_values = []
    global listDeskripsi
    listDeskripsi = []

    judul = ctk.CTkLabel(frame,text="Judul Soal").pack()

    global entry2
    entry2 = ctk.CTkEntry(frame)
    entry2.pack(pady=(0,5))

    optionmenu_var = ctk.StringVar(value="Kesulitan")  # set initial value
    combobox = ctk.CTkOptionMenu(master=frame,
                                       values=["Sulit", "Mudah"],
                                       command=optionmenu_callback,
                                       variable=optionmenu_var)
    combobox.pack(padx=20, pady=10)

    Scrollframe = ctk.CTkScrollableFrame(master=frame, width=200, height=200)
    Scrollframe.pack(padx=5, fill="both", expand=True)

    global soal1
    soal1 = ctk.CTkEntry(Scrollframe, width=300, placeholder_text="Soal 1")
    soal1.pack()

    for i in range(3):
            frame_check_entry = ctk.CTkFrame(Scrollframe)
            frame_check_entry.pack(side="top", pady=5)

            deskripsi_entry1 = ctk.CTkEntry(frame_check_entry, width=300)
            deskripsi_entry1.pack(side="right", padx=5)
            listDeskripsi.append(deskripsi_entry1)
            
            # CTkCheckBox
            var1 = ctk.IntVar()
            var_values.append(var1)
            ctk.CTkCheckBox(frame_check_entry, text=chr(i + 65), variable=var1, onvalue=1, offvalue=0).pack(side="left")

    global penjelasan1
    penjelasan1 = ctk.CTkEntry(Scrollframe, width=300, placeholder_text="Penjelasan 1")
    penjelasan1.pack(pady=5)

    global soal2
    soal2 = ctk.CTkEntry(Scrollframe, width=300, placeholder_text="Soal 2")
    soal2.pack()

    for i in range(3):
            frame_check_entry = ctk.CTkFrame(Scrollframe)
            frame_check_entry.pack(side="top", pady=5)

            deskripsi_entry2 = ctk.CTkEntry(frame_check_entry, width=300)
            deskripsi_entry2.pack(side="right", padx=5)
            listDeskripsi.append(deskripsi_entry2)
            
            # CTkCheckBox
            var2 = ctk.IntVar()
            var_values.append(var2)
            ctk.CTkCheckBox(frame_check_entry, text=chr(i + 65), variable=var2, onvalue=1, offvalue=0).pack(side="left")

    global penjelasan2
    penjelasan2 = ctk.CTkEntry(Scrollframe, width=300, placeholder_text="Penjelasan 2")
    penjelasan2.pack(pady=5)

    global soal3
    soal3 = ctk.CTkEntry(Scrollframe, width=300, placeholder_text="Soal 3")
    soal3.pack()

    for i in range(3):
            frame_check_entry = ctk.CTkFrame(Scrollframe)
            frame_check_entry.pack(side="top", pady=5)

            deskripsi_entry3 = ctk.CTkEntry(frame_check_entry, width=300)
            deskripsi_entry3.pack(side="right", padx=5)
            listDeskripsi.append(deskripsi_entry3)
            
            # CTkCheckBox
            var3 = ctk.IntVar()
            var_values.append(var3)
            ctk.CTkCheckBox(frame_check_entry, text=chr(i + 65), variable=var3, onvalue=1, offvalue=0).pack(side="left")

    global penjelasan3
    penjelasan3 = ctk.CTkEntry(Scrollframe, width=300, placeholder_text="Penjelasan 3")
    penjelasan3.pack(pady=5)

    global soal4
    soal4 = ctk.CTkEntry(Scrollframe, width=300,placeholder_text="Soal 4")
    soal4.pack()

    for i in range(3):
            frame_check_entry = ctk.CTkFrame(Scrollframe)
            frame_check_entry.pack(side="top", pady=5)

            deskripsi_entry4 = ctk.CTkEntry(frame_check_entry, width=300)
            deskripsi_entry4.pack(side="right", padx=5)
            listDeskripsi.append(deskripsi_entry4)
            
            # CTkCheckBox
            var4 = ctk.IntVar()
            var_values.append(var4)
            ctk.CTkCheckBox(frame_check_entry, text=chr(i + 65), variable=var4, onvalue=1, offvalue=0).pack(side="left")

    global penjelasan4
    penjelasan4 = ctk.CTkEntry(Scrollframe, width=300, placeholder_text="Penjelasan 4")
    penjelasan4.pack(pady=5)

    global soal5
    soal5 = ctk.CTkEntry(Scrollframe, width=300, placeholder_text="Soal 5")
    soal5.pack()

    for i in range(3):
            frame_check_entry = ctk.CTkFrame(Scrollframe)
            frame_check_entry.pack(side="top", pady=5)

            deskripsi_entry5 = ctk.CTkEntry(frame_check_entry, width=300)
            deskripsi_entry5.pack(side="right", padx=5)
            listDeskripsi.append(deskripsi_entry5)
            
            # CTkCheckBox
            var5 = ctk.IntVar()
            var_values.append(var5)
            ctk.CTkCheckBox(frame_check_entry, text=chr(i + 65), variable=var5, onvalue=1, offvalue=0).pack(side="left")

    global penjelasan5
    penjelasan5 = ctk.CTkEntry(Scrollframe, width=300, placeholder_text="Penjelasan 5")
    penjelasan5.pack(pady=5)

    global soal6
    soal6 = ctk.CTkEntry(Scrollframe, width=300, placeholder_text="Soal 6")
    soal6.pack()

    for i in range(3):
            frame_check_entry = ctk.CTkFrame(Scrollframe)
            frame_check_entry.pack(side="top", pady=5)

            deskripsi_entry6 = ctk.CTkEntry(frame_check_entry, width=300)
            deskripsi_entry6.pack(side="right", padx=5)
            listDeskripsi.append(deskripsi_entry6)
            # CTkCheckBox
            var6 = ctk.IntVar()
            var_values.append(var6)
            ctk.CTkCheckBox(frame_check_entry, text=chr(i + 65), variable=var6, onvalue=1, offvalue=0).pack(side="left")

    global penjelasan6
    penjelasan6 = ctk.CTkEntry(Scrollframe, width=300, placeholder_text="Penjelasan 6")
    penjelasan6.pack(pady=5)

    global soal7
    soal7 = ctk.CTkEntry(Scrollframe, width=300, placeholder_text="Soal 7")
    soal7.pack()

    for i in range(3):
            frame_check_entry = ctk.CTkFrame(Scrollframe)
            frame_check_entry.pack(side="top", pady=5)

            deskripsi_entry7 = ctk.CTkEntry(frame_check_entry, width=300)
            deskripsi_entry7.pack(side="right", padx=5)
            listDeskripsi.append(deskripsi_entry7)
            
            # CTkCheckBox
            var7 = ctk.IntVar()
            var_values.append(var7)
            ctk.CTkCheckBox(frame_check_entry, text=chr(i + 65), variable=var7, onvalue=1, offvalue=0).pack(side="left")
    
    global penjelasan7
    penjelasan7 = ctk.CTkEntry(Scrollframe, width=300, placeholder_text="Penjelasan 7")
    penjelasan7.pack(pady=5)

    global soal8
    soal8 = ctk.CTkEntry(Scrollframe, width=300, placeholder_text="Soal 8")
    soal8.pack()

    for i in range(3):
            frame_check_entry = ctk.CTkFrame(Scrollframe)
            frame_check_entry.pack(side="top", pady=5)

            deskripsi_entry8 = ctk.CTkEntry(frame_check_entry, width=300)
            deskripsi_entry8.pack(side="right", padx=5)
            listDeskripsi.append(deskripsi_entry8)
            
            # CTkCheckBox
            var8 = ctk.IntVar()
            var_values.append(var8)
            ctk.CTkCheckBox(frame_check_entry, text=chr(i + 65), variable=var8, onvalue=1, offvalue=0).pack(side="left")
    
    global penjelasan8
    penjelasan8 = ctk.CTkEntry(Scrollframe, width=300, placeholder_text="Penjelasan 8")
    penjelasan8.pack(pady=5)

    global soal9
    soal9 = ctk.CTkEntry(Scrollframe, width=300, placeholder_text="Soal 9")
    soal9.pack()

    for i in range(3):
            frame_check_entry = ctk.CTkFrame(Scrollframe)
            frame_check_entry.pack(side="top", pady=5)

            deskripsi_entry9 = ctk.CTkEntry(frame_check_entry, width=300)
            deskripsi_entry9.pack(side="right", padx=5)
            listDeskripsi.append(deskripsi_entry9)
            
            # CTkCheckBox
            var9 = ctk.IntVar()
            var_values.append(var9)
            ctk.CTkCheckBox(frame_check_entry, text=chr(i + 65), variable=var9, onvalue=1, offvalue=0).pack(side="left")

    global penjelasan9
    penjelasan9 = ctk.CTkEntry(Scrollframe, width=300, placeholder_text="Penjelasan 9")
    penjelasan9.pack(pady=5)

    global soal10
    soal10 = ctk.CTkEntry(Scrollframe, width=300, placeholder_text="Soal 10")
    soal10.pack()

    for i in range(3):
            frame_check_entry = ctk.CTkFrame(Scrollframe)
            frame_check_entry.pack(side="top", pady=5)

            deskripsi_entry10 = ctk.CTkEntry(frame_check_entry, width=300)
            deskripsi_entry10.pack(side="right", padx=5)
            listDeskripsi.append(deskripsi_entry10)
            
            # CTkCheckBox
            var10 = ctk.IntVar()
            var_values.append(var10)
            ctk.CTkCheckBox(frame_check_entry, text=chr(i + 65), variable=var10, onvalue=1, offvalue=0).pack(side="left")

    global penjelasan10
    penjelasan10 = ctk.CTkEntry(Scrollframe, width=300, placeholder_text="Penjelasan 10")
    penjelasan10.pack(pady=5)

    tombol_submit = ctk.CTkButton(frame, text="SUBMIT", command=submit)
    tombol_submit.pack(pady=10)

def ask_questionAdmin():
    msg = CTkMessagebox(title="Exit?", message="Back to Menu?",
                            icon="question", option_1="Cancel", option_2="Yes")
    response = msg.get()
        
    if response=="Yes": 
        adminPage()

def optionmenu_callback(choice):
    tingkat_kesulitan[entry2.get()] = choice

def submit():
        judul = entry2.get()
        for i, var in enumerate(var_values):
                # Append the index of the selected option (A, B, C, etc.) to the list
            if var.get() == 1:
                jawaban.append(chr(i % 3 + 65))

        if soal10.get() != '' :
            soal.append(soal1.get())
            soal.append(soal2.get())
            soal.append(soal3.get())
            soal.append(soal4.get())
            soal.append(soal5.get())
            soal.append(soal6.get())
            soal.append(soal7.get())
            soal.append(soal8.get())
            soal.append(soal9.get())
            soal.append(soal10.get())
            judul_soal[judul] = 10
            penjelasan.append(penjelasan1.get())
            penjelasan.append(penjelasan2.get())
            penjelasan.append(penjelasan3.get())
            penjelasan.append(penjelasan4.get())
            penjelasan.append(penjelasan5.get())
            penjelasan.append(penjelasan6.get())
            penjelasan.append(penjelasan7.get())
            penjelasan.append(penjelasan8.get())
            penjelasan.append(penjelasan9.get())
            penjelasan.append(penjelasan10.get())
            
        elif soal9.get() != '':
            soal.append(soal1.get())
            soal.append(soal2.get())
            soal.append(soal3.get())
            soal.append(soal4.get())
            soal.append(soal5.get())
            soal.append(soal6.get())
            soal.append(soal7.get())
            soal.append(soal8.get())
            soal.append(soal9.get())
            judul_soal[judul] = 9
            penjelasan.append(penjelasan1.get())
            penjelasan.append(penjelasan2.get())
            penjelasan.append(penjelasan3.get())
            penjelasan.append(penjelasan4.get())
            penjelasan.append(penjelasan5.get())
            penjelasan.append(penjelasan6.get())
            penjelasan.append(penjelasan7.get())
            penjelasan.append(penjelasan8.get())
            penjelasan.append(penjelasan9.get())
            
        elif soal8.get() != '':
            soal.append(soal1.get())
            soal.append(soal2.get())
            soal.append(soal3.get())
            soal.append(soal4.get())
            soal.append(soal5.get())
            soal.append(soal6.get())
            soal.append(soal7.get())
            soal.append(soal8.get())
            judul_soal[judul] = 8
            penjelasan.append(penjelasan1.get())
            penjelasan.append(penjelasan2.get())
            penjelasan.append(penjelasan3.get())
            penjelasan.append(penjelasan4.get())
            penjelasan.append(penjelasan5.get())
            penjelasan.append(penjelasan6.get())
            penjelasan.append(penjelasan7.get())
            penjelasan.append(penjelasan8.get())
            
        elif soal7.get() != '':
            soal.append(soal1.get())
            soal.append(soal2.get())
            soal.append(soal3.get())
            soal.append(soal4.get())
            soal.append(soal5.get())
            soal.append(soal6.get())
            soal.append(soal7.get())
            judul_soal[judul] = 7
            penjelasan.append(penjelasan1.get())
            penjelasan.append(penjelasan2.get())
            penjelasan.append(penjelasan3.get())
            penjelasan.append(penjelasan4.get())
            penjelasan.append(penjelasan5.get())
            penjelasan.append(penjelasan6.get())
            penjelasan.append(penjelasan7.get())
            
        elif soal6.get() != '':
            soal.append(soal1.get())
            soal.append(soal2.get())
            soal.append(soal3.get())
            soal.append(soal4.get())
            soal.append(soal5.get())
            soal.append(soal6.get())
            judul_soal[judul] = 6
            penjelasan.append(penjelasan1.get())
            penjelasan.append(penjelasan2.get())
            penjelasan.append(penjelasan3.get())
            penjelasan.append(penjelasan4.get())
            penjelasan.append(penjelasan5.get())
            penjelasan.append(penjelasan6.get())
            
        elif soal5.get() != '':
            soal.append(soal1.get())
            soal.append(soal2.get())
            soal.append(soal3.get())
            soal.append(soal4.get())
            soal.append(soal5.get())
            judul_soal[judul] = 5
            penjelasan.append(penjelasan1.get())
            penjelasan.append(penjelasan2.get())
            penjelasan.append(penjelasan3.get())
            penjelasan.append(penjelasan4.get())
            penjelasan.append(penjelasan5.get())
            
        elif soal4.get() != '':
            soal.append(soal1.get())
            soal.append(soal2.get())
            soal.append(soal3.get())
            soal.append(soal4.get())
            judul_soal[judul] = 4
            penjelasan.append(penjelasan1.get())
            penjelasan.append(penjelasan2.get())
            penjelasan.append(penjelasan3.get())
            penjelasan.append(penjelasan4.get())
            
            
        elif soal3.get() != '':
            soal.append(soal1.get())
            soal.append(soal2.get())
            soal.append(soal3.get())
            judul_soal[judul] = 3
            penjelasan.append(penjelasan1.get())
            penjelasan.append(penjelasan2.get())
            penjelasan.append(penjelasan3.get())
            
            
        elif soal2.get() != '':
            soal.append(soal1.get())
            soal.append(soal2.get())
            judul_soal[judul] = 2
            penjelasan.append(penjelasan1.get())
            penjelasan.append(penjelasan2.get())
            
        elif soal1.get() != '':
            soal.append(soal1.get())
            judul_soal[judul] = 1
            penjelasan.append(penjelasan1.get())

        for i in range(10):  # Ubah sesuai dengan jumlah maksimum pertanyaan (10)
            current_soal = globals()[f"soal{i + 1}"]
            current_penjelasan = globals()[f"penjelasan{i + 1}"]
            current_desc_list = []
            if current_soal.get() != '':
                soal.append(current_soal.get())
                penjelasan.append(current_penjelasan.get())

                for j in range(3):
                    current_desc = listDeskripsi[i * 3 + j].get()
                    current_desc_list.append(current_desc)

                deskJawaban.append(current_desc_list)
        
        ask_questionAdmin()

def userPage():
    clear_frame()
    label1 = ctk.CTkLabel(
    frame,
    text="PILIH CABANG MATA PELAJARAN",
    padx=40,
    pady=20
    ).pack()

    tombol1 = ctk.CTkButton(
        frame,
        text="TPS",
        command=enter_tps
        ).pack(pady=(40,10))

    tombol2 = ctk.CTkButton(
        frame,
        text="TLB dan PMTK",
        command=enter_tlb
        ).pack(pady=(10,50))
    
    tombolBack = ctk.CTkButton(
        frame, 
        text="Back to Login", 
        command=main
        ).pack(pady=(90, 20))

def enter_tps():
    clear_frame()
    w = ctk.CTkLabel(
    frame,
    text="PILIH MATA PELAJARAN")
    w.pack(pady=(20,10))

    tombol1 = ctk.CTkButton(
        frame,
        text="PENALARAN UMUM",
        command=jenisSoal,
        width=250
    ).pack(pady=(10))

    tombol2 = ctk.CTkButton(
        frame,
        text="KEMAMPUAN KUANTITATIF",
        command=jenisSoal,
        width=250
    ).pack(pady=(10))

    tombol3 = ctk.CTkButton(
        frame,
        text="PENGETAHUAN DAN PENALARAN UMUM",
        command=jenisSoal,
        width=250
    ).pack(pady=(10))

    tombol4 = ctk.CTkButton(
        frame,
        text="KEMAMPUAN BACA TULIS",
        command=jenisSoal,
        width=250
    ).pack(pady=(10))

    tombolBack = ctk.CTkButton(
        frame,
        text="BACK",
        command=userPage
    ).pack(pady=(70,20))

def enter_tlb():
    clear_frame()
    w = ctk.CTkLabel(
    frame,
    text="PILIH MATA PELAJARAN")
    w.pack(pady=(20,10))

    tombol1 = ctk.CTkButton(
        frame,
        text="literasi bahasa indonesia",
        command=jenisSoal,
        width=170
    ).pack(pady=(10))

    tombol2 = ctk.CTkButton(
        frame,
        text="penalaran bahasa inggris",
        command=jenisSoal,
        width=170
    ).pack(pady=(10))

    tombol3 = ctk.CTkButton(
        frame,
        text="penalaran MTK",
        command=jenisSoal,
        width=170
    ).pack(pady=(10))

    tombolBack = ctk.CTkButton(
        frame,
        text="kembali",
        command=userPage
    ).pack(pady=(100,20))

def jenisSoal():
    clear_frame()

    label1 = ctk.CTkLabel(frame, text="Pilih Jenis Soal")
    label1.pack(pady=10)

    optionmenu_var = ctk.StringVar(value="Jenis Soal")  # set initial value
    combobox = ctk.CTkOptionMenu(master=frame,
                                       values=["Pilihan Ganda", "Essai"],
                                       command=jenis,
                                       variable=optionmenu_var)
    combobox.pack(padx=20, pady=10)

    tombolSub = ctk.CTkButton(frame, text="SUBMIT", command=soaltipe)
    tombolSub.pack(pady=(50,0))

def jenis(choice):
    global tipe
    tipe = choice

def soaltipe():
    if tipe == "Pilihan Ganda":
        pilihJudul()
    elif tipe == "Essai":
        pilihJudulEsai()
    else:
        CTkMessagebox(title="Error", message="Pilih Jenis Soal")
        
def pilihJudulEsai():
    clear_frame()
    global selected
    selected = ctk.StringVar()

    judul = ctk.CTkLabel(frame, text="PILIH JUDUL MATERI :")
    judul.pack(pady=(20,10))

    optionmenu_var = ctk.StringVar(value="Pilih Kesulitan")  # set initial value
    combobox = ctk.CTkOptionMenu(master=frame,
                                       values=["Sulit", "Mudah"],
                                       command=filterEsai,
                                       variable=optionmenu_var)
    combobox.pack(padx=20, pady=10)

    global listbox
    listbox = CTkListbox(frame, command=show_esai)
    listbox.pack(fill="both", expand=True, padx=5)

    tombolBack = ctk.CTkButton(frame, text="Kembali", command=userPage)
    tombolBack.pack()

def show_esai(selected_option):
    selected.set(selected_option)
    finalEsai = selected.get()
    global judul_dipilihEsai
    judul_dipilihEsai = finalEsai
    kerjakanEsai(judul_dipilihEsai = finalEsai)

def filterEsai(choice):
    filtered_soal = {judul: kesulitan for judul, kesulitan in kesulitanEsai.items() if kesulitan == choice}
    for i, (judul, jumlah) in enumerate(filtered_soal.items()):
        listbox.insert(i, judul)

def kerjakanEsai(judul_dipilihEsai):
    clear_frame()
    global entriesJawab
    entriesJawab = []
    global var_values
    var_values = []

    title = ctk.CTkLabel(frame, text=judul_dipilihEsai)
    title.pack(pady=10)

    frameScroll = ctk.CTkScrollableFrame(master=frame, width=200, height=200)
    frameScroll.pack(pady=10, padx=10, fill="both", expand=True)

    # Cari indeks awal dan akhir soal sesuai dengan judul yang dipilih
    indeks_awal = 0
    for judul, jumlah_soal in judulEsai.items():
        if judul == judul_dipilihEsai:
            break
        indeks_awal += jumlah_soal
    
    indeks_akhir = indeks_awal + judulEsai[judul_dipilihEsai]
    
    # Tampilkan soal sesuai dengan judul yang dipilih
    nomorSoal = 0
    for i in range(indeks_awal,indeks_akhir):
        nomorSoal+=1
        text = ctk.CTkTextbox(frameScroll, wrap="word", width=300, height=100)
        text.pack(fill="both", expand=True)

        text.tag_config("center", justify="center")

        text.insert("end", f"Nomor {nomorSoal}:\n{soalEsai[i]}", "center")
        
        entryJawab = ctk.CTkEntry(frameScroll)
        entryJawab.pack(pady=(0,20))
        entriesJawab.append(entryJawab)

    tombolSubmit = ctk.CTkButton(frame,text="SUBMIT ANSWER",command=submitJawabanEsai)
    tombolSubmit.pack(pady=10)

def submitJawabanEsai():
    global nilaiEsai
    nilaiEsai = 0
    jawabanPerSoal = []

    indeks_awal = 0
    for judul, jumlah_soal in judulEsai.items():
        if judul == judul_dipilihEsai:
            break
        indeks_awal += jumlah_soal
    
    indeks_akhir = indeks_awal + judulEsai[judul_dipilihEsai]

    for i in range(indeks_awal,indeks_akhir):
        jawabanPerSoal.append(jawabanEsai[i])

    for i, entry in enumerate(entriesJawab):
        if entry.get() == jawabanPerSoal[i]:
            print(f"nomor {i}: Benar!")
            nilaiEsai += 100/judulEsai[judul_dipilihEsai]
        else:
            print(f"nomor {i}: Salah!!")
        
    if len(entriesJawab) == judulEsai[judul_dipilihEsai]:
        # Display a message with the selected answers
        ask_questionEsai()
    else:
        CTkMessagebox(title="Error", message="Anda belum mengerjakan semua soal!")

def ask_questionEsai():
    msg = CTkMessagebox(title="Exit?", message="Lihat Nilai?",
                        icon="question", option_1="Cancel", option_2="Back to Menu", option_3="Yes")
    response = msg.get()
    
    if response=="Yes": 
        msg2 = CTkMessagebox(title="Nilai", message=f"Nilai yang anda peroleh : {nilaiEsai}. Tampilkan Pembahasan?",
                            icon="question", option_1="No", option_2="Yes")
        response2 = msg2.get()
        if response2 == "Yes":
            pembahasanEsai()
        else:
            userPage()
    elif response == "Back to Menu":
        userPage()
    else:
        print("Click 'Yes' to exit!")
    
def pembahasanEsai():
    clear_frame()
    title = ctk.CTkLabel(frame, text=f"Pembahasan {judul_dipilihEsai}")
    title.pack(pady=10)

    frameScroll = ctk.CTkScrollableFrame(master=frame, width=200, height=200)
    frameScroll.pack(pady=10, padx=10, fill="both", expand=True)

    indeks_awal = 0
    for judul, jumlah_soal in judulEsai.items():
        if judul == judul_dipilihEsai:
            break
        indeks_awal += jumlah_soal
    
    indeks_akhir = indeks_awal + judulEsai[judul_dipilihEsai]

    nomorSoal = 0
    for i in range(indeks_awal,indeks_akhir):
        nomorSoal+=1
        text = ctk.CTkTextbox(frameScroll, wrap="word", width=300, height=100)
        text.pack(fill="both", expand=True)

        text.tag_config("center", justify="center")

        text.insert("end", f"Nomor {nomorSoal}:\n{deskEsai[i]}", "center")

    tombolBack = ctk.CTkButton(frame, text="Kembali ke Menu", command=userPage)
    tombolBack.pack()

def pilihJudul():
    clear_frame()
    global selected_value
    selected_value = ctk.StringVar()

    judul = ctk.CTkLabel(frame, text="PILIH JUDUL MATERI :")
    judul.pack(pady=(20,10))

    optionmenu_var = ctk.StringVar(value="Pilih Kesulitan")  # set initial value
    combobox = ctk.CTkOptionMenu(master=frame,
                                       values=["Sulit", "Mudah"],
                                       command=filterSoal,
                                       variable=optionmenu_var)
    combobox.pack(padx=20, pady=10)

    global listbox
    listbox = CTkListbox(frame, command=show_value)
    listbox.pack(fill="both", expand=True, padx=5)

    tombolBack = ctk.CTkButton(frame, text="Kembali", command=userPage)
    tombolBack.pack()

def filterSoal(choice):
    filtered_soal = {judul: kesulitan for judul, kesulitan in tingkat_kesulitan.items() if kesulitan == choice}
    for i, (judul, jumlah) in enumerate(filtered_soal.items()):
        listbox.insert(i, judul)
         
def show_value(selected_option):
    selected_value.set(selected_option)
    final = selected_value.get()
    global judul_dipilih
    judul_dipilih = final
    kerjakanSoal(judul_dipilih = final)
    
def kerjakanSoal(judul_dipilih):
    clear_frame()
    total_soal = sum(judul_soal.values())
    global var_values
    var_values = []

    title = ctk.CTkLabel(frame, text=judul_dipilih)
    title.pack(pady=10)
    
    frameScroll = ctk.CTkScrollableFrame(master=frame, width=200, height=200)
    frameScroll.pack(pady=10, padx=10, fill="both", expand=True)

    # Cari indeks awal dan akhir soal sesuai dengan judul yang dipilih
    indeks_awal = 0
    for judul, jumlah_soal in judul_soal.items():
        if judul == judul_dipilih:
            break
        indeks_awal += jumlah_soal
    
    indeks_akhir = indeks_awal + judul_soal[judul_dipilih]
    
    # Tampilkan soal sesuai dengan judul yang dipilih
    for i in range(indeks_awal, indeks_akhir):
        pertanyaan = soal[i]
        print(f"Soal {i - indeks_awal + 1}: {pertanyaan}")
        soal1 = ctk.CTkLabel(frameScroll, text=soal[i])
        soal1.pack(pady=10)

        for j in range(3):
            frame_check_entry = ctk.CTkFrame(frameScroll)
            frame_check_entry.pack(side="top", pady=5)

            # CTkEntry untuk deskripsi
            deskripsiJawaban= ctk.CTkLabel(frame_check_entry, width=300, text=deskJawaban[i][j])
            deskripsiJawaban.pack(side="right", padx=5)

            # CTkCheckBox
            var = ctk.IntVar()
            var_values.append(var)
            ctk.CTkCheckBox(frame_check_entry, text=chr(j + 65), variable=var, onvalue=1, offvalue=0).pack(side="left")

    tombolSubmit = ctk.CTkButton(frame,text="SUBMIT ANSWER",command=submitSoal)
    tombolSubmit.pack(pady=10)

def submitSoal():
     # Collect answers from the checkboxes
    selected_answers = []
    global nilai 
    nilai = 0
    JawabanSoal = []
    
    indeks_awal = 0
    for judul, jumlah_soal in judul_soal.items():
        if judul == judul_dipilih:
            break
        indeks_awal += jumlah_soal
    
    indeks_akhir = indeks_awal + judul_soal[judul_dipilih]

    for i in range(indeks_awal, indeks_akhir):
        JawabanSoal.append(jawaban[i])

    for i, var in enumerate(var_values):
        # Append the index of the selected option (A, B, C, etc.) to the list
            if var.get() == 1:
                selected_answers.append(chr(i % 3 + 65))

                # Additional logic to check each answer
                # Example: Check if the selected answer is correct for the current question
                correct_answer = JawabanSoal[i // 3] # Assuming data.jawaban contains correct answers

                if selected_answers[-1] == correct_answer:
                    print(f"Question {i // 3 + 1}: Correct!")
                    nilai += 100/judul_soal[judul_dipilih]
                else:
                    print(f"Question {i // 3 + 1}: Incorrect!")
                    print(correct_answer)
                
    # Check if all questions have been answered
    if len(selected_answers) == judul_soal[judul_dipilih]:
        # Display a message with the selected answers
        ask_question()
    elif len(selected_answers) > judul_soal[judul_dipilih]:
        # Display an error message if not all questions are answered
        CTkMessagebox(title="Error", message="Satu soal hanya berisi satu jawaban!")
    else:
        CTkMessagebox(title="Error", message="Anda belum mengerjakan semua soal!")

def ask_question():
    # get yes/no answers
    msg = CTkMessagebox(title="Exit?", message="Lihat Nilai?",
                        icon="question", option_1="Cancel", option_2="Back to Menu", option_3="Yes")
    response = msg.get()
    
    if response=="Yes": 
        msg2 = CTkMessagebox(title="Nilai", message=f"Nilai yang anda peroleh : {nilai}. Tampilkan Pembahasan?",
                            icon="question", option_1="No", option_2="Yes")
        response2 = msg2.get()
        if response2 == "Yes":
            pembahasan()
        else:
            userPage()
    elif response == "Back to Menu":
        userPage()
    else:
        print("Click 'Yes' to exit!")

def pembahasan():
    clear_frame()
    title = ctk.CTkLabel(frame, text=f"Pembahasan {judul_dipilih}")
    title.pack(pady=10)
    frameScroll = ctk.CTkScrollableFrame(master=frame, width=200, height=200)
    frameScroll.pack(pady=10, padx=10, fill="both", expand=True)
    indeks_awal = 0
    for judul, jumlah_soal in judul_soal.items():
        if judul == judul_dipilih:
            break
        indeks_awal += jumlah_soal
    
    indeks_akhir = indeks_awal + judul_soal[judul_dipilih]

    nomorSoal = 0
    for i in range(indeks_awal,indeks_akhir):
        nomorSoal+=1
        text = ctk.CTkTextbox(frameScroll, wrap="word", width=300, height=100)
        text.pack(fill="both", expand=True)

        text.tag_config("center", justify="center")

        text.insert("end", f"Nomor {nomorSoal}:\n{penjelasan[i]}", "center")

    tombolBack = ctk.CTkButton(frame, text="Kembali ke Menu", command=userPage)
    tombolBack.pack()

def clear_frame():
        for widget in frame.winfo_children():
            widget.destroy()

parent = ctk.CTk()
parent.title("QuizWizzzz")
parent.geometry("400x400")
ctk.set_appearance_mode("dark") 
ctk.set_default_color_theme("dark-blue") 

frame = ctk.CTkFrame(parent)
frame.pack(pady=10, padx=10, fill="both", expand=True)

main()

parent.mainloop()
