
```markdown
# Öğrenci Yönetim Sistemi - Backend (Django)

Bu proje, Öğrenci Yönetim Sistemi'nin sunucu (backend) tarafını oluşturur. Hem Flutter mobil uygulaması için bir REST API sunar hem de tarayıcı üzerinden erişilebilen HTML tabanlı bir Web Arayüzü (CRUD) barındırır.

## Özellikler
* **RESTful API:** Flutter (istemci) ile haberleşmek için `djangorestframework` kullanılarak geliştirilmiş JSON tabanlı API.
* **Web Arayüzü:** Django'nun Sınıf Tabanlı Görünümleri (Class-Based Views) kullanılarak oluşturulmuş, tarayıcı üzerinden çalışan öğrenci ekleme, silme, güncelleme ve listeleme paneli.
* **CORS Desteği:** Mobil ve web istemcilerin API'ye sorunsuz bağlanabilmesi için `django-cors-headers` entegrasyonu.

## Kurulum ve Çalıştırma

Projeyi yerel makinenizde çalıştırmak için aşağıdaki adımları izleyin:

### 1. Gereksinimler
* Python 3.8+
* pip (Python paket yöneticisi)

### 2. Ortam Kurulumu
Projeyi klonladıktan veya indirdikten sonra terminali açın ve proje dizinine gidin:

```bash
# Sanal ortam oluşturun
python -m venv venv

# Sanal ortamı aktifleştirin
# Windows için:
venv\Scripts\activate
# macOS/Linux için:
source venv/bin/activate

# Gerekli kütüphaneleri kurun
pip install django djangorestframework django-cors-headers
```

### 3. Veritabanını Hazırlama
Django'nun varsayılan SQLite veritabanını oluşturmak için:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Sunucuyu Başlatma
```bash
python manage.py runserver
```

Sunucu çalıştıktan sonra:
* **Web Arayüzü:** `http://127.0.0.1:8000/`
* **API Uç Noktası (Endpoint):** `http://127.0.0.1:8000/api/ogrenciler/` adreslerinden projeye erişebilirsiniz.
* <img width="1097" height="1074" alt="image" src="https://github.com/user-attachments/assets/8d49842d-1a9a-4394-b4ef-e40a554c2ac8" />

* <img width="1275" height="855" alt="Ekran Görüntüsü 2026-03-26 10-14-26" src="https://github.com/user-attachments/assets/7f7c76be-508b-4fa7-8e67-d1a690d2934b" />

```

---
