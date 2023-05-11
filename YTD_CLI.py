from pytube import YouTube

# fungsi untuk menampilkan list resolusi yang tersedia
def tampilkan_resolusi(yt):
    print("Resolusi yang tersedia: ")
    streams = yt.streams.filter(progressive=True).order_by('resolution').desc()
    for i in range(len(streams)):
        print(f"{i+1}. {streams[i].resolution}")

# meminta input dari pengguna
url = input("Masukkan URL video YouTube: ")
yt = YouTube(url)

# menampilkan judul video
print("Judul video: ", yt.title)

# menampilkan list resolusi yang tersedia
tampilkan_resolusi(yt)

# meminta pengguna memilih resolusi yang diinginkan
while True:
    pilihan_res = input("Pilih nomor resolusi yang diinginkan: ")
    if pilihan_res.isdigit() and int(pilihan_res) <= len(yt.streams.filter(progressive=True).order_by('resolution').desc()):
        pilihan_res = int(pilihan_res)
        break
    else:
        print("Input tidak valid, silakan coba lagi.")

# mendownload video dengan resolusi yang dipilih
streams = yt.streams.filter(progressive=True).order_by('resolution').desc()
res = streams[pilihan_res - 1].resolution
print("Sedang mendownload video dengan resolusi ", res)
streams[pilihan_res - 1].download("C:\\Users\\ASUS\\OneDrive\\Dokumen\\COCODING\\PHY\\TUGAS BESAR") ## gunakan ("C:\\contoh") bukan ("C:\contoh")

print("Download selesai!")
