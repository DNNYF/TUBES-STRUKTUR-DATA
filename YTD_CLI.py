from pytube import YouTube

# fungsi untuk menampilkan list resolusi yang tersedia
def show_resolutions(yt):
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
show_resolutions(yt)

# meminta pengguna memilih resolusi yang diinginkan
while True:
    selected_res = input("Pilih nomor resolusi yang diinginkan: ")
    if selected_res.isdigit() and int(selected_res) <= len(yt.streams.filter(progressive=True).order_by('resolution').desc()):
        selected_res = int(selected_res)
        break
    else:
        print("Input tidak valid, silakan coba lagi.")

# mendownload video dengan resolusi yang dipilih
streams = yt.streams.filter(progressive=True).order_by('resolution').desc()
res = streams[selected_res - 1].resolution
print("Sedang mendownload video dengan resolusi ", res)
streams[selected_res - 1].download("C:\\Users\\ASUS\\Documents\\temp~\\ImageAI\\output")

print("Download selesai!")
