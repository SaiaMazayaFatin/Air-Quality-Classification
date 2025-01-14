# Laporan Proyek Machine Learning - Saia Mazaya Fatin

## Domain Proyek

### **Latar Belakang**
Kualitas udara menjadi isu lingkungan yang semakin penting di tengah pesatnya urbanisasi dan industrialisasi. Polusi udara berdampak langsung pada kesehatan manusia, menyebabkan penyakit pernapasan, kardiovaskular, hingga peningkatan risiko kanker. Organisasi Kesehatan Dunia (WHO) melaporkan bahwa lebih dari 7 juta kematian setiap tahun terkait dengan polusi udara. Masalah ini tidak hanya terbatas pada area perkotaan, tetapi juga mulai memengaruhi kawasan suburban dan pedesaan akibat aliran udara dan aktivitas manusia.

Dalam konteks ini, pengumpulan dan analisis data kualitas udara menjadi langkah penting untuk memahami pola penyebaran polusi, faktor penyebabnya, serta dampaknya terhadap kesehatan masyarakat. Data yang kaya dengan variabel lingkungan seperti suhu, kelembaban, konsentrasi partikel (PM2.5 dan PM10), dan jarak dari area industri, digabungkan dengan variabel demografis seperti kepadatan populasi, memberikan peluang untuk menganalisis hubungan yang kompleks antara aktivitas manusia dan kualitas udara.

### **Mengapa dan Bagaimana Masalah Ini Harus Diselesaikan**
Polusi udara tidak hanya menjadi masalah lingkungan tetapi juga masalah sosial-ekonomi. Dampaknya meliputi:
1. Kesehatan Publik: Udara berkualitas buruk dapat meningkatkan kasus penyakit pernapasan seperti asma, bronkitis, hingga penyakit jantung.
2. Biaya Ekonomi: Biaya pengobatan dan hilangnya produktivitas akibat penyakit yang terkait dengan polusi udara memberikan beban besar pada sistem kesehatan dan ekonomi.
3. Perubahan Iklim: Gas-gas polutan seperti NO₂ dan CO berkontribusi pada pemanasan global, memperburuk dampak lingkungan secara keseluruhan.
Masalah ini perlu diselesaikan dengan pendekatan berbasis data. Dengan memanfaatkan dataset yang mencakup faktor-faktor kunci seperti yang disediakan, dapat dilakukan analisis prediktif dan pengambilan keputusan berbasis bukti. Pendekatan ini akan membantu:

Masalah ini perlu diselesaikan dengan pendekatan berbasis data. Dengan memanfaatkan dataset yang mencakup faktor-faktor kunci seperti yang disediakan, dapat dilakukan analisis prediktif dan pengambilan keputusan berbasis bukti. Pendekatan ini akan membantu:
1. Mengidentifikasi Sumber Utama Polusi: Analisis mendalam dapat mengungkap pengaruh jarak dari kawasan industri, aktivitas manusia, dan faktor lainnya.
2. Mengembangkan Kebijakan yang Tepat Sasaran: Pemerintah dapat menetapkan regulasi yang lebih efisien berdasarkan temuan ini, seperti perencanaan zona industri atau pengendalian emisi kendaraan.
3. Memberikan Informasi kepada Masyarakat: Data kualitas udara dapat digunakan untuk meningkatkan kesadaran masyarakat akan dampak polusi terhadap kesehatan.


### **Hasil Riset Terkait**
1.	Fine-Particulate Air Pollution and Life Expectancy in the United States (https://www.nejm.org/doi/pdf/10.1056/NEJMsa0805646)
2.	Machine Learning-Based Prediction of Air Quality (https://www.researchgate.net/publication/347831458_Machine_Learning-Based_Prediction_of_Air_Quality)
3. Impact of population, age structure, and urbanization on carbon emissions/energy consumption: evidence from macro-level, cross-country analyses (https://link.springer.com/article/10.1007/s11111-013-0198-4)

---

## **Business Understanding**

### **Problem Statements**
1. **Pernyataan Masalah 1**: Bagaimana cara memprediksi kualitas udara di berbagai wilayah berdasarkan faktor lingkungan dan demografis yang tersedia?
2. **Pernyataan Masalah 2**: Bagaimana menangani ketidakseimbangan kelas pada target variabel untuk memastikan prediksi yang akurat pada kelas minoritas, seperti udara dengan kualitas "Hazardous"?
3. **Pernyataan Masalah 3**: Fitur apa yang paling berpengaruh dalam menentukan kualitas udara, dan bagaimana model dapat memberikan interpretasi yang dapat digunakan untuk pengambilan keputusan?

### **Goals**
1. **Jawaban Pernyataan Masalah 1**:
   - Mengembangkan model machine learning yang dapat memprediksi kualitas udara dengan akurasi tinggi.
2. **Jawaban Pernyataan Masalah 2**:
   - Mengatasi ketidakseimbangan kelas menggunakan teknik oversampling, seperti SMOTE, untuk meningkatkan performa pada kelas minoritas.
3. **Jawaban Pernyataan Masalah 3**:
   - Mengidentifikasi fitur-fitur utama yang memengaruhi kualitas udara melalui analisis feature importance.

---

## **Data Understanding**

### **Informasi Dataset**
Dataset yang digunakan berisi 5000 sampel dan mencakup berbagai faktor lingkungan dan demografis yang memengaruhi kualitas udara. Data ini memiliki **target variabel**: **Air Quality Levels**, yang terbagi menjadi empat kelas:
- **Good**: Udara bersih dengan tingkat polusi rendah.
- **Moderate**: Udara dapat diterima tetapi terdapat beberapa polutan.
- **Poor**: Udara tercemar yang dapat menyebabkan masalah kesehatan pada kelompok sensitif.
- **Hazardous**: Udara sangat tercemar dengan risiko kesehatan serius.

**Sumber Dataset**: https://www.kaggle.com/datasets/mujtabamatin/air-quality-and-pollution-assessment/data

### **Deskripsi Variabel**
- **Temperature (°C)**: Suhu rata-rata wilayah.
- **Humidity (%)**: Kelembaban relatif wilayah.
- **PM2.5 Concentration (µg/m³)**: Konsentrasi partikel halus (PM2.5).
- **PM10 Concentration (µg/m³)**: Konsentrasi partikel kasar (PM10).
- **NO2 Concentration (ppb)**: Konsentrasi nitrogen dioksida.
- **SO2 Concentration (ppb)**: Konsentrasi sulfur dioksida.
- **CO Concentration (ppm)**: Konsentrasi karbon monoksida.
- **Proximity to Industrial Areas (km)**: Jarak ke area industri terdekat.
- **Population Density (people/km²)**: Kepadatan populasi di wilayah tersebut.

### **Exploratory Data Analysis (EDA)**
- **Distribusi Kelas**: Target variabel menunjukkan ketidakseimbangan dengan kelas "Hazardous" memiliki proporsi data terkecil (10%).
- **Korelasi Fitur**: Variabel PM2.5 dan PM10 menunjukkan korelasi kuat positif (0.97), yang perlu diperhatikan dalam modeling.
- **Kemiringan Ekstrem**: Variabel PM2.5 dan PM10 memiliki distribusi yang sangat miring ke kiri, dengan mayoritas nilainya adalah nol.

---

## Data Preparation

### Langkah Data Preparation

1. **Split Data**  
   Data dibagi menjadi **X** (fitur) dan **y** (target). Kemudian dilakukan pembagian data menjadi **training** dan **testing set** menggunakan `train_test_split` dengan rasio 80:20.  
   **Alasan**:
   - Memastikan evaluasi model dilakukan pada data yang tidak terlihat selama pelatihan.
   - Rasio 80:20 adalah standar umum untuk menjaga keseimbangan antara data pelatihan dan pengujian.

2. **Encoding Target Variable**  
   Menggunakan **LabelEncoder** untuk mengubah variabel target `Air Quality` ke format numerik yang dapat dimengerti oleh model.  
   **Alasan**:
   - Model Machine Learning hanya dapat bekerja dengan data numerik.

3. **Handling Class Imbalance**  
   Data pelatihan diseimbangkan menggunakan **SMOTE (Synthetic Minority Oversampling Technique)**.  
   **Alasan**:
   - Untuk mencegah model bias terhadap kelas mayoritas. Teknik ini mensintesis data baru untuk kelas minoritas agar proporsi antar kelas lebih seimbang.

4. **Scaling Data**  
   Tidak dilakukan scaling karena algoritma **tree-based** seperti Random Forest dan XGBoost tidak sensitif terhadap skala data.  
   **Alasan**:
   - Efisiensi waktu dan kesesuaian dengan algoritma yang digunakan.

5. **Handling Multicollinearity**  
   Tidak dilakukan karena algoritma **tree-based** mampu menangani multikolinearitas secara internal. Namun, korelasi antar fitur dianalisis untuk informasi tambahan.

---

## Model Development

## Model 1: Random Forest

### Cara Kerja

Random Forest adalah algoritma ensemble berbasis pohon keputusan yang membangun beberapa pohon keputusan secara acak dan menggabungkan hasilnya.  
**Langkah Kerja**:
1. Membagi data pelatihan secara acak ke dalam subset untuk membangun beberapa pohon keputusan.
2. Setiap pohon dilatih menggunakan subset data yang berbeda.
3. Untuk prediksi akhir, model mengambil rata-rata (regresi) atau melakukan voting (klasifikasi) dari semua pohon.

### Parameter

- **`n_estimators`**: Jumlah pohon dalam hutan (dioptimalkan dengan Optuna).
- **`max_depth`**: Kedalaman maksimum pohon (dioptimalkan dengan Optuna).
- **`min_samples_split`**: Jumlah minimum sampel yang diperlukan untuk membagi node (dioptimalkan dengan Optuna).
- **`min_samples_leaf`**: Jumlah minimum sampel pada setiap leaf node (dioptimalkan dengan Optuna).
- **`max_features`**: Jumlah maksimum fitur yang dipertimbangkan untuk pembagian di setiap node.

**Catatan**: Parameter lainnya menggunakan **default**.

### Kelebihan:
- Tidak mudah overfit karena rata-rata prediksi dari banyak pohon.
- Dapat menangani data dengan banyak fitur tanpa scaling.

### Kekurangan:
- Relatif lebih lambat dibanding algoritma sederhana.
- Tidak selalu memberikan performa terbaik pada dataset kompleks dibandingkan XGBoost.

---

## Model 2: XGBoost

### Cara Kerja

XGBoost adalah algoritma **gradient boosting** yang meningkatkan performa dengan mengurangi kesalahan dari prediksi sebelumnya.  
**Langkah Kerja**:
1. Membuat model dasar (tree) untuk memprediksi data.
2. Menghitung kesalahan dari prediksi sebelumnya (residual).
3. Membangun tree baru yang difokuskan pada residual untuk meminimalkan kesalahan.
4. Proses ini diulangi secara iteratif hingga jumlah tree yang ditentukan tercapai.

### Parameter

- **`n_estimators`**: Jumlah pohon yang dibangun (dioptimalkan dengan Optuna).
- **`learning_rate`**: Mengontrol kontribusi setiap pohon terhadap prediksi akhir (dioptimalkan dengan Optuna).
- **`max_depth`**: Kedalaman maksimum pohon (dioptimalkan dengan Optuna).
- **`min_child_weight`**: Kontrol overfitting melalui jumlah minimum bobot leaf (dioptimalkan dengan Optuna).
- **`subsample`**: Proporsi data pelatihan yang digunakan untuk membangun setiap tree.
- **`colsample_bytree`**: Proporsi fitur yang digunakan untuk setiap tree.
- **`gamma`**: Minimum loss reduction untuk membagi node.

### Kelebihan:
- Performa tinggi pada data kompleks dengan ketidakseimbangan kelas.
- Mendukung regularisasi untuk mencegah overfitting.

### Kekurangan:
- Lebih rentan terhadap overfit jika parameter tidak diatur dengan benar.
- Memerlukan waktu pelatihan lebih lama dibanding Random Forest.

---

## Pemilihan Model Terbaik

- **Kriteria**: Model dipilih berdasarkan **F1-Score** (macro average) karena dataset memiliki kelas tidak seimbang.
- **Hasil**: XGBoost memiliki **F1-Score** yang lebih tinggi dibandingkan Random Forest setelah proses tuning. Oleh karena itu, **XGBoost** dipilih sebagai model terbaik.

**Rekomendasi**: 

Gunakan **XGBoost** untuk prediksi kualitas udara, terutama jika dataset memiliki ketidakseimbangan kelas dan fitur kompleks.

---

## **Evaluation**

### **Metrik Evaluasi**
- **F1-Score** digunakan sebagai metrik utama karena penting untuk keseimbangan antara precision dan recall, terutama untuk menangani kelas minoritas.

### **Hasil Evaluasi**
1. **Model Comparison**:

   | Model          | Training F1-Score | Testing F1-Score |
   |----------------|--------------------|------------------|
   | Random Forest  | 0.995284           | 0.932304         |
   | XGBoost        | 0.998585           | 0.939735         |

2. **Analisis Hasil**:
   - **Random Forest** memberikan hasil yang stabil dengan F1-Score tinggi pada data testing, tetapi sedikit kalah dibandingkan XGBoost.
   - **XGBoost** memberikan performa terbaik pada testing dengan memaksimalkan F1-Score, terutama pada kelas minoritas.

3. **Feature Importance**:
   - **Random Forest Feature Importance**:

     | Feature                         | Importance |
     |---------------------------------|------------|
     | CO                              | 0.371486   |
     | Proximity to Industrial Areas   | 0.207491   |
     | NO2                             | 0.123998   |
     | Temperature                     | 0.089115   |
     | SO2                             | 0.088277   |
     | Population Density              | 0.049228   |
     | Humidity                        | 0.036582   |
     | PM10                            | 0.021271   |
     | PM2.5                           | 0.012552   |

   - **XGBoost Feature Importance**:

     | Feature                         | Importance |
     |---------------------------------|------------|
     | CO                              | 0.496040   |
     | Proximity to Industrial Areas   | 0.231128   |
     | NO2                             | 0.075034   |
     | Temperature                     | 0.045931   |
     | SO2                             | 0.044596   |
     | Population Density              | 0.039659   |
     | Humidity                        | 0.033412   |
     | PM10                            | 0.018300   |
     | PM2.5                           | 0.015901   |

---

## **Kesimpulan**

### **Ringkasan**
- **Random Forest** memberikan hasil yang stabil dan cocok untuk baseline model.
- **XGBoost** unggul dalam memaksimalkan F1-Score, terutama untuk kelas minoritas, menjadikannya pilihan terbaik untuk dataset ini.

