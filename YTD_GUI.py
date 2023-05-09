# Mengimport library yang dibutuhkan
import pytube
import streamlit as st
import os

# Membuat fungsi untuk mengunduh video
def download_video(url, resolusi):
    # Menampilkan pesan bahwa proses pengunduhan sedang berlangsung
    st.write("Memproses...")
    
    # Menginisialisasi objek YouTube dengan URL video yang diberikan
    youtube = pytube.YouTube(url)
    
    # Mencari stream dengan resolusi yang diinginkan dari video tersebut
    video = youtube.streams.filter(res=resolusi, progressive=True).order_by('resolution').desc().first()
    
    # Menentukan direktori tempat penyimpanan video yang akan diunduh
    direktori_download = r"C:\Users\ASUS\OneDrive\Dokumen\COCODING\PHY\TUGAS BESAR\OUTPUT"
    
    # Menentukan nama file yang akan diunduh
    nama_file = video.download(direktori_download)
    
    # Mengembalikan path file yang telah berhasil diunduh
    return nama_file

# Menampilkan judul aplikasi
st.title("Download Video YouTube")

# Mengambil URL video YouTube dari pengguna melalui input teks
url = st.text_input("Masukkan URL Video YouTube")

# Menampilkan judul video dan jumlah suka jika URL video telah dimasukkan
if url:
    st.write("Mencari judul video")
    try:
        # Menginisialisasi objek YouTube dengan URL video yang diberikan
        youtube = pytube.YouTube(url)
        
        # Mengambil judul video
        judul_video = youtube.title
        
        # Menampilkan judul video
        st.subheader(f"Judul Video : \"{judul_video}\" ")
    except pytube.exceptions.VideoUnavailable:
        # Menampilkan pesan error jika video tidak tersedia
        st.write("Video tidak tersedia.")

# Mencari opsi resolusi video dari URL yang diberikan
if url:
    st.write("Mencari Resolusi yang Tersedia...")
    
    # Menginisialisasi objek YouTube dengan URL video yang diberikan
    youtube = pytube.YouTube(url)
    
    # Mencari opsi resolusi video
    opsi_resolusi = [str(stream.resolution) for stream in youtube.streams.filter(progressive=True)]
    
    # Menghapus resolusi duplikat
    opsi_resolusi = list(set(opsi_resolusi))
    
    # Mengurutkan opsi resolusi dari yang tertinggi
    opsi_resolusi.sort(key=lambda s: [int(u) for u in s.split("p") if u.isdigit()], reverse=True)
    
    # Menambahkan pilihan "Pilih Resolusi" ke opsi resolusi
    opsi_resolusi.insert(0, "Pilih Resolusi")

    # Menampilkan dropdown resolusi
    resolusi_terpilih = st.selectbox("Pilih Resolusi", opsi_resolusi)

    # Menampilkan tombol unduh jika resolusi telah dipilih
    if resolusi_terpilih != "Pilih Resolusi":
        if st.button("Download"):
            # Memanggil fungsi download_video untuk mengunduh video dengan resolusi yang dipilih
            file_path = download_video(url, resolusi_terpilih)
            
            # Menampilkan pesan berhasil jika video telah berhasil diunduh
            st.write(f"Video telah berhasil diunduh")
