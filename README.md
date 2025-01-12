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

## **Data Preparation**

### **Langkah Data Preparation**
1. **Handling Missing Values**: Tidak ada nilai hilang dalam dataset.
2. **Handling Multicollinearity**: Menggunakan analisis korelasi untuk memahami hubungan antar fitur.
3. **Scaling Data**: Tidak diperlukan scaling karena algoritma tree-based seperti Random Forest dan XGBoost tidak sensitif terhadap skala data.
4. **Balancing Data**: Menggunakan **SMOTE** untuk menangani ketidakseimbangan kelas.
5. **Encoding Target Variable**: Menggunakan **LabelEncoder** untuk mengubah target variabel menjadi format numerik.

**Alasan**:
- Teknik-teknik di atas membantu meningkatkan akurasi model dan mencegah bias terhadap kelas mayoritas.

---

## **Modeling**

### **Model yang Digunakan**
1. **Random Forest**:
   - **Kelebihan**: Stabil, tidak mudah overfit, dan bekerja dengan baik pada dataset dengan fitur yang banyak.
   - **Kekurangan**: Performa bisa lebih rendah dibandingkan XGBoost pada dataset kompleks.
2. **XGBoost**:
   - **Kelebihan**: Kemampuan boosting iteratif membuatnya unggul dalam menangani dataset kompleks dan ketidakseimbangan kelas.
   - **Kekurangan**: Lebih rentan overfit tanpa regularisasi yang tepat.

### **Improvement dengan Hyperparameter Tuning**
- **Optuna** digunakan untuk mengoptimalkan parameter seperti:
  - Random Forest: **n_estimators**, **max_depth**, **min_samples_split**, **min_samples_leaf**, dan **max_features**.
  - XGBoost: **n_estimators**, **learning_rate**, **max_depth**, **subsample**, **colsample_bytree**, **reg_alpha**, dan **reg_lambda**.

### **Rekomendasi**
Gunakan **XGBoost** untuk prediksi kualitas udara karena performanya yang lebih tinggi pada data pengujian dan kemampuannya menangani kelas minoritas dengan baik.

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

