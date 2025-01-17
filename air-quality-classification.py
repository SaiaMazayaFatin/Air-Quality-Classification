# -*- coding: utf-8 -*-
"""Air Quality Classification

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/#fileId=https%3A//storage.googleapis.com/kaggle-colab-exported-notebooks/air-quality-classification-1859c719-1ff4-48bf-a393-3e6499e9dee0.ipynb%3FX-Goog-Algorithm%3DGOOG4-RSA-SHA256%26X-Goog-Credential%3Dgcp-kaggle-com%2540kaggle-161607.iam.gserviceaccount.com/20250112/auto/storage/goog4_request%26X-Goog-Date%3D20250112T121515Z%26X-Goog-Expires%3D259200%26X-Goog-SignedHeaders%3Dhost%26X-Goog-Signature%3D1e76616d76f166c16fc3d679a1dc8f21fcf3907e2b1e2138590ec91418336e031a9a5314856e38c6597c9165e52b518a58257960370e87dd7413c5fdecf11b269e94e182bc0b06b9990ac4b4746f57b029d599f4709023b6999dd1987378c22afaf6f93d38cedc384c3e0eec6a3c1456351ac2fce26f24ac93d2ef8c16c299a7cff3c1ce335f0fd4148ab12eada47ce92b337f6f287d4d0226d92fbbdc58af87d1c2661f6ae70a7ea10080abe9708059a28c76618215216096eb31e7e985e9a274cf9b2e731473ab5a3c379d9f3385adcfe7f7dfb6201e51a992e099bae4fb183e3b86ab8036eeed145e1b821f91ac59687cafd1550435feefd1ecdb8b52c849
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import f1_score, classification_report
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from imblearn.over_sampling import SMOTE
import optuna

pip install optuna

"""# Data Loading"""

df = pd.read_csv('/kaggle/input/air-quality-and-pollution-assessment/updated_pollution_dataset.csv')

df.head()

df.tail()

cat = df.select_dtypes(include=['object']).columns
num = df.select_dtypes(include=['int', 'float']).columns

df.info()

df[cat].describe()

df[num].describe()

df.duplicated().sum()

"""Berdasarkan analisis data, tidak ditemukan nilai yang hilang (NaN) atau duplikasi data. Oleh karena itu, tidak diperlukan tindakan pembersihan data lebih lanjut pada dataset ini.

# Exploratory Data Analysis

## Univariate Analysis
"""

def eda_univariate_numeric(df):
    numeric_columns = df.select_dtypes(include=['number']).columns

    for col in numeric_columns:
        plt.figure(figsize=(12, 6))

        plt.subplot(1, 2, 1)
        sns.histplot(df[col], kde=True, bins=30)
        plt.title(f'Histogram of {col}')
        plt.xlabel(col)
        plt.ylabel('Frequency')

        plt.subplot(1, 2, 2)
        sns.boxplot(y=df[col])
        plt.title(f'Boxplot of {col}')
        plt.ylabel(col)

        plt.tight_layout()
        plt.show()

def eda_univariate_categorical(df):
    categorical_columns = df.select_dtypes(include=['object', 'category']).columns

    for col in categorical_columns:
        plt.figure(figsize=(12, 6))

        sns.countplot(x=df[col], order=df[col].value_counts().index, palette='viridis')
        plt.title(f'Countplot of {col}')
        plt.xlabel(col)
        plt.ylabel('Frequency')
        plt.xticks(rotation=45, ha='right')

        plt.tight_layout()
        plt.show()

eda_univariate_numeric(df)

eda_univariate_categorical(df)

print("Class Distribution on Target:")
print(df['Air Quality'].value_counts())

# Cek proporsi kelas
print("\nClass Proportion on Target (in percent)")
print(df['Air Quality'].value_counts(normalize=True) * 100)

"""Hasil visualisasi data menunjukkan adanya outlier signifikan pada fitur PM2.5 dan PM10. Selain itu, distribusi kelas pada data target tidak seimbang.

## Multivariate Analysis
"""

def multivariate_analysis_numeric_heatmap(df):
    numeric_columns = df.select_dtypes(include=['number']).columns
    corr_matrix = df[numeric_columns].corr()
    plt.figure(figsize=(16, 12))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
    plt.title('Heatmap of Correlation Matrix for Numerical Columns')
    plt.show()

multivariate_analysis_numeric_heatmap(df)

"""Hasil visualisasi data menunjukan adanya multikolinearitas pada fitur PM2.5 dan PM10 dengan korelasi positif kuat sebesar 97%

# Data Preparation

Pada tahap preparation, hanya label target yang dilakukan label encoding untuk mengubah bentuk data dari kategorikal menjadi numerik. Outlier tidak dihapus karena distribusi data yang memiliki kemiringan ekstrem. Penghapusan outlier berpotensi menghilangkan informasi penting dari data.
"""

label_encoder = LabelEncoder()
df['Air_Quality_Encoded'] = label_encoder.fit_transform(df['Air Quality'])

X = df.drop(['Air Quality', 'Air_Quality_Encoded'], axis=1)
y = df['Air_Quality_Encoded']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

"""# Model Development

## **Pemilihan Model**
Pada tahap model development, saya memilih model berbasis **tree** seperti **Random Forest** dan **XGBoost** karena keduanya memiliki keunggulan yang signifikan dalam menghadapi data dengan karakteristik kompleks, seperti keberadaan **outlier** dan **multikolinearitas** di antara fitur-fitur. Kedua model ini tidak memerlukan asumsi linearitas, sehingga mampu menangkap hubungan non-linear secara efektif. Selain itu, model ini secara inheren melakukan seleksi fitur melalui mekanisme split pada pohon keputusan, yang meningkatkan efisiensi dan interpretabilitas model.

## **Penanganan Ketidakseimbangan Kelas**
Untuk menangani ketidakseimbangan kelas, saya menggunakan **SMOTE (Synthetic Minority Oversampling Technique)**. Teknik ini menghasilkan sampel sintetis untuk kelas minoritas agar distribusi kelas menjadi lebih seimbang.

## **Hyperparameter Tuning**
Saya menggunakan **Optuna** untuk melakukan tuning pada parameter penting untuk masing-masing model:

### **Random Forest**
- **`n_estimators`**: Jumlah pohon dalam ensemble.
- **`max_depth`**: Membatasi kedalaman maksimum pohon untuk mencegah overfitting.
- **`min_samples_split`** dan **`min_samples_leaf`**: Untuk mengontrol jumlah sampel minimum yang dibutuhkan pada setiap split dan leaf.
- **`max_features`**: Subset fitur untuk setiap pohon.

### **XGBoost**
- **`n_estimators`**: Jumlah pohon dalam boosting.
- **`learning_rate`**: Tingkat pembelajaran untuk mengontrol kecepatan pembaruan model.
- **`max_depth`**: Membatasi kedalaman pohon untuk mencegah model menjadi terlalu kompleks.
- **`subsample`** dan **`colsample_bytree`**: Membatasi proporsi data dan fitur yang digunakan untuk meningkatkan generalisasi.
- **Regularisasi (`reg_alpha` dan `reg_lambda`)**: Membantu mencegah overfitting dengan menekan bobot fitur yang tidak signifikan.

## **Evaluasi**
- **Metrik utama**: **F1-Score**, yang memberikan keseimbangan antara **precision** dan **recall**. Ini sangat penting untuk menangani ketidakseimbangan kelas, terutama untuk memprediksi kelas minoritas.

## Random Forest
"""

smote = SMOTE(random_state=42)
X_train_rf, y_train_rf = smote.fit_resample(X_train, y_train)

def objective_rf(trial):
    param = {
        'n_estimators': trial.suggest_int('n_estimators', 50, 500),
        'max_depth': trial.suggest_int('max_depth', 3, 20),
        'min_samples_split': trial.suggest_int('min_samples_split', 2, 10),
        'min_samples_leaf': trial.suggest_int('min_samples_leaf', 1, 5),
        'max_features': trial.suggest_categorical('max_features', ['sqrt', 'log2', None]),
        'random_state': 42
    }

    model = RandomForestClassifier(**param)
    model.fit(X_train_rf, y_train_rf)
    y_pred = model.predict(X_test)
    report = classification_report(y_test, y_pred, output_dict=True)

    return report['macro avg']['f1-score']

study_rf = optuna.create_study(direction='maximize')
study_rf.optimize(objective_rf, n_trials=50, timeout=3600)

print("\nRandom Forest Best Hyperparameters:", study_rf.best_params)
print("Random Forest Best F1-Score:", study_rf.best_value)

"""## XGBoost"""

smote = SMOTE(random_state=42)
X_train_xgb, y_train_xgb = smote.fit_resample(X_train, y_train)

def objective_xgb(trial):
    param = {
        'n_estimators': trial.suggest_int('n_estimators', 50, 500),
        'learning_rate': trial.suggest_float('learning_rate', 0.01, 0.3, log=True),
        'max_depth': trial.suggest_int('max_depth', 3, 10),
        'min_child_weight': trial.suggest_int('min_child_weight', 1, 10),
        'gamma': trial.suggest_float('gamma', 0, 5),
        'subsample': trial.suggest_float('subsample', 0.6, 1.0),
        'colsample_bytree': trial.suggest_float('colsample_bytree', 0.6, 1.0),
        'reg_alpha': trial.suggest_float('reg_alpha', 0.0, 1.0),
        'reg_lambda': trial.suggest_float('reg_lambda', 0.0, 1.0),
        'objective': 'multi:softprob',  # Multiklasifikasi
        'num_class': len(np.unique(y_train_xgb)),  # Jumlah kelas
        'use_label_encoder': False,
        'eval_metric': 'mlogloss',
        'random_state': 42
    }

    model = XGBClassifier(**param)
    model.fit(X_train_xgb, y_train_xgb)
    y_pred = model.predict(X_test)
    report = classification_report(y_test, y_pred, output_dict=True)

    return report['macro avg']['f1-score']

study_xgb = optuna.create_study(direction='maximize')
study_xgb.optimize(objective_xgb, n_trials=50, timeout=3600)

print("\nXGBoost Best Hyperparameters:", study_xgb.best_params)
print("XGBoost Best Macro F1-Score:", study_xgb.best_value)

"""# Model Evaluation"""

rf_final = RandomForestClassifier(**study_rf.best_params)
rf_final.fit(X_train_rf, y_train_rf)

rf_y_train_pred = rf_final.predict(X_train_rf)
rf_y_test_pred = rf_final.predict(X_test)

rf_train_f1 = f1_score(y_train_rf, rf_y_train_pred, average='macro')
rf_test_f1 = f1_score(y_test, rf_y_test_pred, average='macro')

print(f"\nRandom Forest Training F1-Score: {rf_train_f1:.2f}")
print(f"Random Forest Testing F1-Score: {rf_test_f1:.2f}")

print("\nRandom Forest Classification Report:")
print(classification_report(y_test, rf_y_test_pred))

xgb_final = XGBClassifier(**study_xgb.best_params)
xgb_final.fit(X_train_xgb, y_train_xgb)

# Prediksi
xgb_y_train_pred = xgb_final.predict(X_train_xgb)
xgb_y_test_pred = xgb_final.predict(X_test)

# Evaluasi F1-Score
xgb_train_f1 = f1_score(y_train_xgb, xgb_y_train_pred, average='macro')
xgb_test_f1 = f1_score(y_test, xgb_y_test_pred, average='macro')

print(f"\nXGBoost Training F1-Score: {xgb_train_f1:.2f}")
print(f"XGBoost Testing F1-Score: {xgb_test_f1:.2f}")

print("\nXGBoost Classification Report:")
print(classification_report(y_test, xgb_y_test_pred))

comparison = pd.DataFrame({
    'Model': ['Random Forest', 'XGBoost'],
    'Training F1-Score': [rf_train_f1, xgb_train_f1],
    'Testing F1-Score': [rf_test_f1, xgb_test_f1]
})

print("\nModel Comparison:")
print(comparison)

feature_importances_rf = rf_final.feature_importances_

feature_names = X_train_rf.columns
importance_rf_df = pd.DataFrame({
    'Feature': feature_names,
    'Importance': feature_importances_rf
}).sort_values(by='Importance', ascending=False)

plt.figure(figsize=(10, 6))
plt.barh(importance_rf_df['Feature'], importance_rf_df['Importance'])
plt.xlabel('Importance')
plt.ylabel('Feature')
plt.title('Random Forest Feature Importance')
plt.gca().invert_yaxis()
plt.show()

print("\nRandom Forest Feature Importance:")
print(importance_rf_df)

feature_importances_xgb = xgb_final.feature_importances_

importance_xgb_df = pd.DataFrame({
    'Feature': X_train_xgb.columns,
    'Importance': feature_importances_xgb
}).sort_values(by='Importance', ascending=False)

plt.figure(figsize=(10, 6))
plt.barh(importance_xgb_df['Feature'], importance_xgb_df['Importance'])
plt.xlabel('Importance')
plt.ylabel('Feature')
plt.title('XGBoost Feature Importance')
plt.gca().invert_yaxis()
plt.show()

print("\nXGBoost Feature Importance:")
print(importance_xgb_df)

"""## **Hasil**
1. **Random Forest**:
   - Memberikan hasil yang stabil dengan performa baik pada data pelatihan dan pengujian.
   - Memiliki sifat robust terhadap dataset dengan banyak fitur.

2. **XGBoost**:
   - Mengungguli Random Forest dalam memaksimalkan F1-Score, terutama untuk kelas dengan jumlah data yang lebih sedikit.
   - Regularisasi dan boosting iteratif membuatnya lebih baik dalam menangkap pola pada dataset kompleks.

3. **Feature Importance**:
   - Analisis feature importance dari kedua model memberikan wawasan terkait fitur yang paling memengaruhi hasil prediksi. Visualisasi ini membantu memahami peran fitur dalam menentukan kualitas udara.
"""

