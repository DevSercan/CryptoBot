[![ccxt](https://img.shields.io/pypi/v/ccxt)](https://pypi.org/project/ccxt/)
[![colorama](https://img.shields.io/pypi/v/colorama)](https://pypi.org/project/colorama/)

# CryptoBot

Bu proje, 'ccxt' kütüphanesini kullanarak kripto para işlemlerini kolaylaştırmak için geliştirilmiştir.

---

### Gereksinimler
- Python 3.x
- `ccxt` kütüphanesi (Kurulum yönergeleri aşağıda belirtilmiştir)

### API Anahtarı Nasıl Alınır?
MEXC borsasında API anahtarı almak için aşağıdaki adımları takip edin:
  1. [mexc.com](https://www.mexc.com/tr-TR/user/openapi) adresinden profilinize giriş yapın.
  2. **API Yönetimi** sayfasını açın.
  3. **Yeni API Anahtarı Oluştur** seçeneğini kullanarak, gerekli yetkileri belirleyin ve API anahtarınızı oluşturun.

### API Anahtarını Yapılandırma
1. Proje kök dizininde bulunan `keys.json` dosyasını açın.
2. `keys.json` dosyasına aldığınız API anahtarını şu şekilde ekleyin:
   ```json
   {
       "accessKey": "YOUR_API_KEY",
       "secretKey": "YOUR_API_SECRET"
   }
> Not: API anahtarınızın güvenliğini sağlamak için keys.json dosyasını güvenli bir ortamda saklayın ve bu dosyayı paylaşmayın.

---

### Kurulum
1. **Python Yüklü Sistemler İçin**  
   Python bilgisayarınızda yüklü ise, öncelikle `requirements.txt` dosyasındaki bağımlılıkları yüklemeniz gerekmektedir. Bağımlılıkları yüklemek için kök dizinde bir terminal açın ve `pip install -r requirements.txt` komutunu girin. Kurulum işlemini tamamladıktan sonra `main.py` dosyasını çalıştırarak yazılımı başlatabilirsiniz.
   
2. **Python Yüklü Olmayan Sistemler İçin**  
   Python yüklü değilse, doğrudan `main.exe` uygulamasını çalıştırarak programı başlatabilirsiniz.

---

### Kullanım
Yazılım, konsol arayüzünden kullanıcı etkileşimi ile çalışmaktadır. Aşağıdaki komut numaraları ile işlevlere erişebilirsiniz:
- 0: Konsolu temizler.

- 1: Kripto para alım işlemini başlatır.
  - İşlem Çifti: İşlem yapmak istediğiniz çift, örneğin BTC/USDC.
  - Miktar: Almak istediğiniz miktarı girin. Ondalık sayı girecekseniz nokta kullanın, örneğin 0.14.

- 2: Kripto para satım işlemini başlatır.
  - İşlem Çifti: Satmak istediğiniz işlem çiftini girin, örneğin BTC/USDC.
  - Miktar: Satmak istediğiniz miktarı girin. Ondalık sayı için nokta kullanın, örneğin 0.14.

- 3: Mevcut bakiye bilgilerinizi görüntüler.