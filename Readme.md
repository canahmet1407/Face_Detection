# OpenCV ile Gerçek Zamanlı Yüz Tanıma (Face Detection)

Bu proje, Python ve OpenCV kütüphanesini kullanarak bilgisayar kamerasından alınan canlı video akışı üzerinde **Haar Cascade** algoritması ile gerçek zamanlı yüz tanıma işlemi gerçekleştirir.

---

## Özellikler

* **Canlı Video İşleme:** Bilgisayar kamerasından (`cv2.VideoCapture`) anlık görüntü alır.
* **Ayna Efekti:** Kullanıcı deneyimini iyileştirmek için kamera görüntüsünü yatay olarak ters çevirir (`cv2.flip`).
* **Haar Cascade Sınıflandırıcısı:** OpenCV'nin önceden eğitilmiş `haarcascade_frontalface_default.xml` modelini kullanarak yüzleri yüksek doğrulukla tespit eder.
* **Görsel Geri Feedback:** Tespit edilen yüzlerin etrafına dinamik olarak renkli dikdörtgenler çizer.

---

## Gereksinimler ve Kurulum

Projeyi yerel bilgisayarınızda çalıştırmak için aşağıdaki adımları sırasıyla terminalinizde çalıştırabilirsiniz:

```bash
# 1. Depoyu Klonlayın
git clone [https://github.com/canahmet1407/Face_detection.git](https://github.com/canahmet1407/Face_detection.git)

# 2. Proje Klasörüne Geçiş Yapın
cd Face_detection

# 3. Gerekli Kütüphaneyi Kurun
pip install opencv-python

# 4. Projeyi çalıştırma komutu
python main.py

