# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik.

### Permasalahan Bisnis
Baru-baru ini, Jaya Jaya Institut mendeteksi kenaikan jumlah mahasiswa yang tidak menyelesaikan pendidikannya alias dropout. Dari total 4424 mahasiswa, sebanyak 1421 (32.7%) telah dropout dan 2209 (49.9%) telah lulus, sedangkan sisanya sebanyak 794 (17.9%) masih dalam tahap kuliah.

Untuk melihat lebih lanjut terkait pola mahasiswa yang dropout, Jaya Jaya Institut menyimpan informasi yang cukup detail dari tiap-tiap mahasiswanya, seperti nilai per semester, kebangsaan, course yang diambil, dll.

Dengan tujuan untuk mencari penyebab dropout tersebut, terdapat beberapa pertanyaan dasar yang dapat dijadikan acuan, yaitu: 

1. Berapa kemungkinan suatu mahasiswa akan dropout?
2. Apa faktor-faktor utama yang menyebabkan suatu mahasiswa dropout?
3. Apa yang bisa diterapkan untuk mengurangi jumlah mahasiswa dropout?

Lalu, apabila dirinci secara lebih detail, pertanyaan nomor 2 dapat dipecah lagi menjadi beberapa pertanyaan:

**Internal/Individu**

1. Apakah gender, usia, dan status pernikahan mempengaruhi dropout?
2. Apakah mahasiswa jalur/kelompok tertentu lebih unggul daripada kelompok lainnya?
    1. Apakah jalur dan order pendaftaran mempengaruhi dropout?
    2. Apakah pendidikan dan nilai mahasiswa sebelumnya (pre-admission) mempengaruhi dropout?
    3. Apakah kursus dan attendance time yang diambil saat ini mempengaruhi dropout?
    4. Apakah pendidikan dan nilai mahasiswa saat ini (post-admission) mempengaruhi dropout?
3. Apakah mahasiswa yang memperoleh scholarship lebih banyak graduate?
    1. Bagaimana perbandingannya dengan mahasiswa biasa atau yang memiliki hutang (debtor)?
    2. Bagaimana scholarship mempengaruhi mahasiswa migran/internasional?

**Eksternal**

1. Apakah latar belakang keluarga/asal mahasiswa mempengaruhi jumlah dropout?
    1. Apakah kestabilan negara (GDP, unemployment rate, dsb) turut mempengaruhi dropout?
    2. Apakah mahasiswa migran dan/atau internasional memiliki isu tertentu (performa, dll) yang tidak dialami mahasiswa setempat?
2. Apakah background pendidikan/pekerjaan orang tua mempengaruhi dropout?
3. Apakah faktor lainnya seperti (aksesibilitas) kebutuhan khusus dan biaya kuliah mempengaruhi dropout?

### Cakupan Proyek

1. Mengekspor data dari file CSV ke format database (Supabase) agar dapat diakses secara realtime dengan berbagai tools
2. Membuat dashboard (Metabase) untuk mengawasi faktor-faktor penyebab dropout
3. Membuat model prediksi (machine learning) yang interaktif dan dapat diakses melalui browser (Streamlit)

### Persiapan

**Sumber data:**

Database student yang tersimpan di Supabase (PostgreSQL). Kredensial database disimpan dalam file `database.txt` dan akan terbaca otomatis oleh script `notebook.ipynb`

**Setup environment:**

A. Setup Metabase v0.49.6

1. Download `metabase.jar` di [sini](https://www.metabase.com/start/oss/jar) dan Java (JRE/JDK) di [sini](https://adoptium.net/temurin/archive/)
2. Letakkan `metabase.jar` pada folder `dashboard` (di root folder proyek ini)
3. Buka shell terminal (Zsh, Git Bash, dsb) dan jalankan `run_metabase.sh` (atau `java -jar metabase.jar`)
4. Akses Metabase dengan membuka URL `localhost:3000`
5. Jika menggunakan database bawaan proyek ini, gunakan email `admin@example.com` dan password `admin456`

B. Setup Python v3.11.5

1. Download Python di [sini](https://www.python.org/downloads/)
2. Pastikan tambahkan Python ke `PATH` saat instalasi
3. Buka folder proyek ini lewat IDE/code editor (misal VS Code)
4. Buat virtual environment dan install dependensi proyek pada terminal di IDE: 
    ``` bash
    python -m venv .venv
    source .venv/Scripts/activate
    pip install -r requirements.txt
    ```
5. Jalankan notebook dengan kernel virtual environment pada IDE (bila diperlukan)
6. Untuk menjalankan aplikasi/sistem prediksi ML, lihat bagian "Menjalankan Sistem Machine Learning"
7. Bila terdapat error dependensi, pastikan virtual environment sudah diaktifkan pada terminal. Bila terminal diganti/ditutup, maka perlu diaktifkan kembali sesuai perintah step 4 baris 2

## Business Dashboard

Dashboard dibagi menjadi 4 bagian untuk memantau status dropout mahasiswa dari sudut pandang yang berbeda:

- **Berdasarkan informasi umum:** Berisi visualisasi dari segi kebangsaan, gender, umur, status pernikahan, course yang diambil, dll
- **Berdasarkan informasi lainnya:** Berisi visualisasi dari segi scholarship, international student, debt/hutang, disabilitas, dll yang bersifat 2 arah (ya/tidak)
- **Berdasarkan nilai/kualifikasi:** Berisi visualisasi dari segi nilai per semester, nilai saat pendaftaran, latar belakang pendidikan sebelumnya, dll
- **Berdasarkan latar belakang keluarga/negara asal:** Berisi visualisasi dari segi pendidikan/pekerjaan orang tua, GDP negara asal, unemployment rate negara asal, dll

## Menjalankan Sistem Machine Learning

Untuk menjalankan aplikasi/sistem prediksi ML secara lokal, maka:

1. Pastikan telah mengikuti setup environment Python pada bagian sebelumnya 
2. Jalankan script `app.py` dengan perintah `streamlit run app.py` (tidak wajib menjalankan notebook sebelumnya)
3. Bila script sudah dijalankan, akses aplikasi tersebut secara interaktif dengan membuka URL `localhost:8501` pada browser
4. Upload file CSV atau isi form informasi mahasiswa secara manual untuk memprediksi status dropout mahasiswa. Urutan baris file input akan selalu sama dengan urutan baris file prediksi

Untuk mengakses aplikasi secara online, cukup membuka URL [berikut](https://stud-evdgvjxrixagvawcczpydw.streamlit.app/).

## Conclusion

Berdasarkan pertanyaan-pertanyaan sebelumnya dan hasil visualisasi dashboard, didapatkan jawaban/konklusi berupa:

1. Mahasiswa perempuan cenderung lebih banyak graduate (57%) jika dibandingkan dengan gender laki-laki (35%)
    - Jumlah mahasiswa perempuan 2x lipat lebih banyak dari mahasiwa laki-laki, meski begitu jumlah dropout mahasiswa laki-laki (701 orang/45%) cukup sama dengan mahasiswa perempuan (720 orang/25%)
2. Mahasiswa dengan usia 20 tahun atau di bawahnya memiliki dropout yang jauh lebih rendah (22%) daripada usia diatasnya
    - Semakin tinggi usia maka semakin tinggi pula dropout rate-nya (30-50% untuk usia 21-25 tahun, >50% untuk usia diatasnya). Namun, bila dilihat spesifik dari gendernya, perempuan tetap memiliki dropout rate lebih rendah
        - Kecenderungan untuk mengambil kelas sore juga semakin besar, terutama bila diantara usia 23-40 tahun (30% mengambil kelas sore)
    - Mahasiswa laki-laki setara/diatas 22 tahun memiliki dropout rate (>40%) yang hampir selalu lebih tinggi daripada graduate rate, dan jika dibandingkan dengan mahasiswa perempuan
3. Mahasiswa yang single memiliki dropout rate paling rendah (30%) jika dibandingkan lainnya, dan merupakan golongan yang paling banyak (88% dari total mahasiswa)
    - Mahasiswa single rata-rata berusia 18 tahun (23% dari total mahasiswa)
    - Status relationship lainnya terlihat kurang berpengaruh terhadap dropout rate karena sebaran dropout rate (~45%) di golongan selain single masih terlihat cukup merata
4. Mahasiswa dengan application mode bertipe "diatas 23 tahun" atau "pemegang edukasi lebih tinggi" memiliki dropout rate yang lebih besar (55-60%) daripada golongan lainnya
    - Application order tidak terlalu berpengaruh terhadap dropout (relatif merata dikisaran 30%). Namun, kebanyakan yang memiliki application order tinggi merupakan mahasiswa migran (displaced)
    - Untuk mahasiswa laki-laki, dropout rate akan selalu tinggi untuk latar belakang pendidikan (prev. qualification) apapun. Namun, mahasiswa yang tidak tamat pendidikan 12 tahun terlihat selalu dropout (100%) baik untuk laki-laki ataupun perempuan (meskipun totalnya hanya 11 orang)
4. Mahasiswa yang mengambil kelas sore/malam memiliki dropout rate (+15%) yang lebih tinggi dari kelas pagi/siang
    - Hanya 2 mata kuliah (course) yang memiliki opsi sore/malam, yaitu manajemen dan social service, dengan jumlah 10% dari total mahasiswa
    - Mata kuliah informatika (52%), manajemen (sore, 60%), biofuel (77%), dan equinculture (64%) merupakan mata kuliah yang paling banyak dropout untuk golongan laki-laki. Meski begitu, dropout rate untuk mata kuliah lainnya juga cukup tinggi (>40%)
    - Mata kuliah informatika (85%), equinculture (48%), basic education (44%), dan manajemen (sore, 40%) merupakan mata kuliah yang paling banyak dropout untuk golongan perempuan
    - Mata kuliah dengan dropout rate tinggi umumnya memiliki pengambilan SKS yang rendah pula untuk rata-rata mahasiswanya (misal total SKS mahasiswa IT selalu kurang dari 10, jika dibandingkan desain komunikasi yang bisa mencapai 18 dalam 1 semester). Meski begitu, grade SKS akhir yang diterima umumnya sama (sekitar 18 SKS tertinggi)
5. Semakin tinggi SKS (curr. units approved) yang di-approve, maka kecenderungan graduate akan semakin besar terutama bila setara/diatas 5 SKS (~50-70%), baik laki-laki maupun perempuan
    - Semakin tinggi nilai SKS (curr. units grade), maka kecenderungan graduate akan semakin besar terutama bila totalnya setara/diatas 13 SKS (>55%), baik laki-laki maupun perempuan
    - Semakin tinggi admission grade, semakin kecil pula kecenderungan dropout rate untuk mahasiswa perempuan (namun tetap tinggi untuk mahasiswa laki-laki)
6. Mahasiswa yang memiliki scholarship memiliki dropout rate yang lebih rendah dibandingkan mahasiswa biasa (10% untuk perempuan, 19% untuk laki-laki)
    - Hanya 2 negara di luar Portugis yang mahasiswanya merupakan pemegang scholarship (Brazil & Guinea, total 11 orang), namun dropout rate-nya sangat rendah untuk kedua negara tersebut (11% Brazil, 0% Guinea)
    - Mahasiswa yang memiliki hutang (debtor) memiliki dropout rate yang tinggi (62% untuk perempuan, 72% untuk laki-laki), namun turun ke kisaran 60% untuk kedua gender bila hanya mencakup mahasiswa migran, dan turun ke 50% bila hanya mahasiswa internasional
    - Dengan begitu, status migran/internasional tidak mempengaruhi performa mahasiswa ke arah negatif, baik untuk debtor ataupun pemegang scholarship
7. Mahasiswa internasional memiliki dropout rate yang relatif setara (~30%) atau lebih rendah dengan mahasiswa asli Portugis, namun total mahasiswa internasional ini hanya berjumlah 110 orang
    - Tidak ada keterkaitan signifikan antara GDP, unemployment rate, atau inflation rate terhadap dropout rate mahasiswa
8. Background pendidikan orang tua rata-rata didominasi oleh pendidikan dasar (12 tahun atau dibawahnya), dengan persentase 82% untuk ibu dan 86% untuk ayah
    - Background pendidikan orang tua terlihat tidak mempengaruhi dropout rate dan cukup merata dikisaran 30%. Namun, dropout rate tertinggi berada pada pendidikan kelas 4/5 SD (35%) jika mengacu pada pendidikan dasar 12 tahun
    - Kebanyakan orang tua memiliki pekerjaan unskilled worker (35% ibu, 22% ayah), disusul staff administratif untuk ibu (18%) dan skilled industry worker untuk ayah (15%). Graduate rate mahasiswa untuk tiap golongan pekerjaan orang tua cukup merata diangka 45-50%
    - Scholarship mahasiswa juga terlihat tidak dipengaruhi background pendidikan/pekerjaan orang tua dan cukup merata untuk tiap golongan
9. Faktor lainnya
    - Hanya terdapat 1 mahasiswa dengan kebutuhan khusus dan statusnya telah lulus, sehingga pengaruhnya terhadap dropout rate tidak dapat disimpulkan karena kurangnya sampel
    - UKT (tuition fees) yang tidak up-to-date akan sangat berpengaruh terhadap dropout rate mahasiswa, dan bisa menambah dropout rate hingga 70% (dari persentase awalnya)

**Catatan:** terdapat beberapa hal yang perlu didiskusikan kembali dengan dosen dan tenaga pendidik, terutama konklusi terhadap mata kuliah tertentu

### Rekomendasi Action Items

Dengan mengacu pada korelasi variabel dan konklusi yang ditemukan, dapat diterapkan beberapa rekomendasi untuk mengurangi dropout rate mahasiswa, yaitu:

- Selalu memperbarui biaya UKT (tuition fees) sesuai dengan kondisi ekonomi saat ini dan menginformasikannya ke mahasiswa (86% dropout rate bila tidak up-to-date) [^1]
    - Tuition fees yang tidak up-to-date juga berdampak negatif terhadap mahasiswa pemegang scholarship (60% dropout rate)
    - 46% dari mahasiswa dengan UKT tidak up-to-date telah memiliki hutang (debtor)
- Beberapa mata kuliah memiliki tingkat kesulitan dan/atau biaya yang lebih tinggi (jika dilihat dari sebaran SKS mahasiswanya), sehingga perlu dievaluasi dengan kampus/tenaga pendidik secara lebih lanjut
    - Untuk laki-laki:
        - Biofuel (78% dropout): Dari 9 orang, 7 dropout dan 2 sisanya belum graduate
        - Informatika (52% dropout): Dari 163 orang, 14 graduate dan 86 dropout
        - Manajemen (sore, 60% dropout): Dari 136 orang, 38 graduate dan 82 dropout
        - Equinculture (64% dropout): Dari 62 orang, 15 graduate dan 40 dropout
        - Banyak juga mata kuliah lainnya dengan dropout rate lebih dari 40% (agronomi, tourism, advertising, dll)
    - Untuk perempuan:
        - Informatika (86% dropout): Dari 7 orang, 6 dropout dan 1 sisanya belum lulus
        - Equinculture (48% dropout): Dari 78 orang, 27 graduate dan 39 dropout
        - Basic education (44% dropout): Dari 183 orang, 55 graduate dan 81 dropout
        - Manajemen (sore, 40% dropout): Dari 132 orang, 40 graduate dan 54 dropout
- Masih berkaitan dengan poin-poin sebelumnya, mahasiswa laki-laki umumnya memiliki dropout rate yang jauh lebih tinggi dari perempuan (45% berbanding 25%), ditambah beberapa faktor lainnya:
    - Bila umur mahasiswa setara/diatas 22 tahun, maka dropout rate akan selalu >40%
    - Kelas sore terbukti tidak terlalu efektif dalam menurunkan dropout rate, tetapi malah mempertinggi persentase dropout hingga +15% (yang dipengaruhi juga oleh faktor umur)
    - Sebagian besar orang tua mahasiswa berasal dari golongan pekerja unskilled worker (35% ibu, 22% ayah)

    Dengan asumsi bahwa kebanyakan mahasiswa (bukan hanya gender laki-laki) memiliki background ekonomi yang tidak mumpuni dan/atau perlu bekerja sambil berkuliah, maka:
    - Diperlukan kelas khusus untuk kalangan pekerja dimana materi yang diajarkan tidak sama dengan mahasiswa biasa, melainkan disesuaikan dengan beban dan praktik kerja saat ini
    - Meringankan biaya kuliah atau memberi beasiswa dengan kriteria-kriteria tertentu (misal mahasiswa berprestasi atau golongan miskin yang sedang bekerja), atau dalam bentuk lomba/pameran bila secara tidak langsung
    - Bekerja sama dengan perusahaan atau lembaga tertentu lainnya dalam rangka memperoleh dana sponsor (subsidi biaya UKT/lomba) ataupun untuk memberi materi yang lebih relevan kepada golongan pekerja
- Memperhatikan faktor lainnya saat pendaftaran seperti melakukan survei keuangan calon mahasiswa karena mahasiswa yang berencana/telah mengambil hutang lebih berisiko mengalami dropout (62%)
- Bila mahasiswa sudah dalam posisi terdaftar/berkuliah, maka risiko dropout dapat diprediksi dengan model ML yang telah dibuat, dan dapat dikonsultasikan dengan mahasiswa yang bersangkutan sebelum terlambat (dropout)

[^1]: Quinn, Jocey. Drop-Out and Completion in Higher Education in Europe Among Students from Under-Represented Groups. European Union, 2013, https://nesetweb.eu/en/resources/library/drop-out-and-completion-in-higher-education-in-europe-among-students-from-under-represented-groups/.