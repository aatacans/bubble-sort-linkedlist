# Bubble Sort ile LinkedList

Bu proje, Python’da hem yerleşik listeler (`list`) hem de bağlı listeler (`LinkedList`) veri yapısı üzerinde **Bubble Sort** algoritmasını uygulamaktadır. Ayrıca, proje kapsamında otomatik birim testleri (`pytest`) ve GitHub Actions kullanılarak sürekli entegrasyon (CI/CD) desteği sağlanmıştır.

## 🔧 Özellikler

- `bubble_sort(collection)` fonksiyonu:
  - Python’un yerleşik `list` veri tipini sıralar.
  - Özel tanımlı `LinkedList` sınıfı ile oluşturulmuş bağlı listeleri sıralar.
- `LinkedList` sınıfı:
  - İç içe `Node` yapısını içerir.
  - Dinamik olarak düğüm ekleme ve gezinme işlevi sunar.
  - Python iteratör protokolü ile uyumludur (`__iter__`).
- `pytest` ile kapsamlı birim testleri yapılmıştır.
- GitHub Actions ile CI/CD entegrasyonu yapılmıştır.

## 🧠 Bubble Sort Nedir?

Bubble Sort, karşılaştırmalı bir sıralama algoritmasıdır. Her bir öğe, yanındakiyle karşılaştırılarak gerekirse yer değiştirilir. Bu işlem tüm liste sıralanana kadar tekrarlanır.

### Örnek Görsel:

![Bubble Sort Adımları](images/bubble_sort.gif)

> `images/` klasörü altına `.gif` uzantılı sıralama adımlarını gösteren bir animasyon yerleştirebilirsiniz.

## 📁 Proje Dosya Yapısı

```bash
.
├── linked_list.py         # LinkedList sınıfı ve bubble_sort fonksiyonu
├── test_bubble_sort.py    # pytest birim testleri
├── .github/
│   └── workflows/
│       └── python-app.yml # GitHub Actions CI dosyası
├── images/
│   └── bubble_sort.gif     # Readme içinde kullanılan görsel
└── README.md
