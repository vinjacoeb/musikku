link: musikku-info-dcab28ccf745.herokuapp.com


1. Dataset

Dataset yang digunakan diperoleh melalui teknik crawling dari penyedia musik. Dataset berisi Penyanyi,Judul,Lirik, yang telah dipreprocessing sehingga menjadi datamusik.csv yang tersimpan pada /musikku/datamusik.csv

2. Rumusan Masalah/Tujuan

Sistem layanan informasi, atau sering disebut sebagai layanan informasi, adalah suatu sistem yang  secara otomatis mencari informasi yang relevan dengan kebutuhan pengguna dari berbagai sumber informasi yang tersedia. Salah satu bentuk penerapan sistem temu kembali informasi adalah melalui mesin pencari atau search-engine. Sistem pencarian ini menggunakan dokumen sebagai objek data atau sumber informasi, dan dokumen ini diindeks oleh sistem menggunakan metode seperti TF-IDF. Sistem temu kembali informasi yang efektif mampu menampilkan dokumen yang sesuai dengan query yang dimasukkan pengguna, mengurutkan hasil, dan menghilangkan dokumen yang tidak relevan. Terdapat berbagai metode yang dapat digunakan untuk melakukan indeksasi dan pencarian dokumen yang berkaitan. Dengan latar belakang ini, ada kebutuhan yang signifikan untuk mengembangkan sistem temu kembali informasi yang dapat memfasilitasi pencarian dokumen khusus yang berisi file judul lagu MP3. Maka akhirnya melakukan penyusunan proposal yang berjudul "Implementasi Vector Space Model pada Sistem Pencarian Judul Lagu MP3."

3. Model

Vector Space Model(VSM) adalah model invormation retrival yang berbasis token untuk memungkinkan untuk partial making dan pemeringkatan dokumen. Dengan prinsip dasar mengubah suatu dokumen menjadi kumpulan token-token. Query dan dokumen dianggap sebagai vector-vector pada ruang n-dimensi di = (ti,1, ti,2, …, ti,k) dimana t adalah jumlah dari seluruh term yang ada dalam leksikon(daftar semua term yang ada dalam indeks).

 3.1 TF/IDF

Untuk setiap term tidak hanya dilihat ada atau tidak ada dalam dokumen namun diberi bobot menggunakan TF atau TF-IDF. TF-IDF merupakan skema pembobotan yang sering digunakan dalam VSM bersama dengan cosine similarity untuk menentukan kesamaan antara dua buah dokumen. TF (Term Frequency) merupakan frekuensi kemunculan term (t) pada dokumen (d). DF (Document Frequency) merupakan banyaknya dokumen dimana suatu term (t) muncul. Atau sebuah dokumen mengandung term(t).

 3.2 Cosine Similarity

Fungsi similarity adalah fungsi yang menerima dua buah objek dan mengembalikan nilai kemiripan (similarity) antara kedua objek tersebut berupa bilangan riil. Umumnya, nilai yang dihasilkan oleh fungsi similarity berkisar pada interval [0...1]. Namun, ada juga yang menghasilkan nilai yang berada diluar interval tersebut. Maka untuk memetakannya dapat dilakukan normalisasi. Cosine similarity adalah perhitungan kesamaan antara dua vector n dimensi dengan mencari kosinus dari sudut diantara keduanya dansering digunakan untuk membandingkan dokumen dalam text mining.

   3.3 N-gram

Penggunaan N-Gram untuk pendeteksian bahasa didasarkan pada asumsi bahwa pola distribusi N-gram suatu bahasa bersifat unik karena berkaitan dengan frekuensi penggunaan huruf, atau pasangan huruf, baik vokal maupun konsonan dari suatu bahasa yang umumnya berbeda dengan bahasa lain.  N-Gram memiliki beberapa pendekatan dalam memotong karakter. Untuk membantu dalam pengambilan potongan kata berupa karakter huruf tersebut, padding dilakukan dengan memberikan karakter “_” di awal dan akhir kata.

4. Uji Performa


