
# WordFinder - Terminalde Kelime Arama Aracı 🚀

WordFinder, terminalde hızlı ve kolayca kelime arayıp anlamlarını bulmanı sağlayan renkli, kullanışlı ve sağlam bir Python uygulamasıdır.

---

## Özellikler

- **Hızlı ve duyarlı** kelime arama
- Renkli ve okunabilir terminal arayüzü (`rich` kütüphanesi kullanıldı)
- `dataset.parquet` formatında veritabanı ile çalışır
- Boş girişlerde ve hatalı dosya durumlarında kullanıcı dostu uyarılar
- `Ctrl+C` veya `q/exit` komutları ile kolayca çıkış yapabilme
- Genişletilebilir, temiz ve sade kod yapısı

---

## Gereksinimler

- Python 3.8+
- Pandas
- Rich
- PyArrow (Parquet dosyalarını okumak için)

---

## Kurulum

```bash
pip install pandas rich pyarrow
```

---

## Kullanım

1. Projeyi klonla veya indir:
    ```bash
    git clone https://github.com/hakankygsz/wordfinder.git
    cd wordfinder3000
    ```

2. `dataset.parquet` dosyanı proje klasörüne koy.

3. Uygulamayı çalıştır:
    ```bash
    python word_search.py
    ```

4. Terminale kelimeni yaz, anlamlarını anında gör!

5. Çıkmak için `q`, `exit`, `quit` yazabilir veya `Ctrl+C` yapabilirsin.

---

## Dataset Oluşturma (Opsiyonel)

Eğer hazır datasetin yoksa, şu ufak scripti kullanarak oluşturabilirsin:

```python
import pandas as pd

data = {
    'word': ['apple', 'banana', 'orange', 'grape', 'lemon'],
    'meaning': ['Elma', 'Muz', 'Portakal', 'Üzüm', 'Limon']
}

df = pd.DataFrame(data)
df.to_parquet('dataset.parquet')
```

---

## İletişim

Her türlü soru, öneri ve katkı için [hakankaygusuzdev@gmail.com](mailto:hakankaygusuzdev@gmail.com) adresinden bana ulaşabilirsin.

---

## Lisans

MIT License © 2025 Hakan

---

🚀 **wordfinder** ile kelime dünyasında kaybolma, keşfet!
