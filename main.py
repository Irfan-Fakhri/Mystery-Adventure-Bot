import time
import random

# ===== ASCII ART =====
def tampilkan_pedang():
    """Menampilkan ASCII art pedang kemenangan"""
    print_dramatis("", 0.2)
    print_dramatis("         ⚔️  KEMENANGAN BERKILAU!  ⚔️", 0.2)
    print_dramatis("", 0.2)
    print_dramatis("           /|\\", 0.2)
    print_dramatis("          / | \\", 0.2)
    print_dramatis("         /  |  \\", 0.2)
    print_dramatis("            |", 0.2)
    print_dramatis("            |", 0.2)
    print_dramatis("           /|\\", 0.2)
    print_dramatis("          / | \\", 0.2)
    print_dramatis("         /  |  \\", 0.2)
    print_dramatis("        /   |   \\", 0.2)
    print_dramatis("       /    |    \\", 0.2)
    print_dramatis("      /     |     \\", 0.2)
    print_dramatis("     /      |      \\", 0.2)
    print_dramatis("    /       |       \\", 0.2)
    print_dramatis("   /        |        \\", 0.2)
    print_dramatis("  /_________|_________\\", 0.2)
    print_dramatis("", 0.2)

def tampilkan_tengkorak():
    """Menampilkan ASCII art tengkorak kekalahan"""
    print_dramatis("", 0.2)
    print_dramatis("         💀 KEKALAHAN MUTLAK 💀", 0.2)
    print_dramatis("", 0.2)
    print_dramatis("           .-\"\"\"-.  ", 0.2)
    print_dramatis("          /       \\", 0.2)
    print_dramatis("         | () () |", 0.2)
    print_dramatis("         |   >   |", 0.2)
    print_dramatis("         |  \\_/  |", 0.2)
    print_dramatis("          \\       /", 0.2)
    print_dramatis("           '-----'", 0.2)
    print_dramatis("", 0.2)

# ===== FUNGSI HELPER: Print dengan efek jeda (dramatis) =====
def print_dramatis(text="", delay=0.5):
    """Fungsi untuk print teks dengan jeda otomatis agar lebih dramatis"""
    print(text)
    time.sleep(delay)

# ===== CLASS: Item dalam inventory =====
class Item:
    """Representasi item dalam inventory pemain"""
    def __init__(self, nama, deskripsi, tipe="konsumsi"):
        self.nama = nama
        self.deskripsi = deskripsi
        self.tipe = tipe  # konsumsi, senjata, armor, dll
    
    def __str__(self):
        return f"📦 {self.nama} - {self.deskripsi}"

# ===== CLASS: Player (Karakter Pemain) =====
class Player:
    """Kelas utama untuk merepresentasikan pemain dalam dunia fantasi"""
    
    def __init__(self, nama, hp=100, mana=50):
        self.nama = nama
        self.hp = hp
        self.hp_max = hp
        self.mana = mana
        self.mana_max = mana
        self.inventory = []
        self.level = 1
        self.xp = 0
    
    def lihat_status(self):
        """Menampilkan status karakter dengan narasi puitis"""
        print_dramatis("\n✨" + "="*60, 0.4)
        print_dramatis("║ 🌟 CAHAYA JIWA PETUALANGMU 🌟", 0.5)
        print_dramatis("✨" + "="*60, 0.3)
        
        # Narasi puitis untuk nama
        print_dramatis(f"\n📜 Nama Pemilik Takdir: {self.nama}", 0.4)
        
        # HP dengan visual bar
        hp_bar = self._buat_bar_status(self.hp, self.hp_max, "❤️")
        print_dramatis(f"❤️  NYAWA (Life Force):  {hp_bar} {self.hp}/{self.hp_max}", 0.4)
        
        # Mana dengan visual bar
        mana_bar = self._buat_bar_status(self.mana, self.mana_max, "💎")
        print_dramatis(f"💎 MANA (Energi Gaib):  {mana_bar} {self.mana}/{self.mana_max}", 0.4)
        
        # Level dan XP
        print_dramatis(f"⭐ Level Kebijaksanaan:  {self.level}", 0.3)
        print_dramatis(f"🎯 Pengalaman Perjalanan: {self.xp} XP", 0.4)
        
        # Inventory
        print_dramatis(f"\n🎒 Harta Terkumpul ({len(self.inventory)} item):", 0.4)
        if len(self.inventory) == 0:
            print_dramatis("   → Tas Kosong, menunggu untuk diisi dengan harta karun", 0.4)
        else:
            for idx, item in enumerate(self.inventory, 1):
                print_dramatis(f"   {idx}. {item}", 0.3)
        
        print_dramatis("\n✨" + "="*60 + "\n", 0.4)
    
    def _buat_bar_status(self, current, maximum, emoji):
        """Helper untuk membuat visual bar status"""
        persen = (current / maximum) * 10
        filled = "█" * int(persen)
        empty = "░" * (10 - int(persen))
        return f"{emoji} [{filled}{empty}]"
    
    def ambil_item(self, item):
        """Menambahkan item ke inventory dengan narasi puitis"""
        self.inventory.append(item)
        
        # Narasi puitis saat mengambil item
        print_dramatis("", 0.3)
        print_dramatis("✨💫 Cahaya emas bersinar terang! 💫✨", 0.6)
        print_dramatis(f"—═─ Anda menemukan: {item.nama} ─═—", 0.5)
        print_dramatis(f"📖 \"{item.deskripsi}\"", 0.5)
        print_dramatis("", 0.3)
        print_dramatis(f"🎒 Item disimpan dalam tas petualanganmu.", 0.4)
        print_dramatis("", 0.3)
    
    def gunakan_mana(self, jumlah):
        """Menggunakan mana dengan efek dramatis"""
        if self.mana >= jumlah:
            self.mana -= jumlah
            print_dramatis(f"💎 Energi gaib mengalir melalui tubuhmu... (-{jumlah} Mana)", 0.5)
            return True
        else:
            print_dramatis("❌ Energi gaibmu tidak cukup untuk memikul kekuatan ini!", 0.5)
            return False
    
    def ambil_damage(self, damage):
        """Menerima damage dengan narasi dramatis"""
        self.hp -= damage
        print_dramatis(f"💥 Serangan mengenai! Nyawamu terguncang... (-{damage} HP)", 0.6)
        print_dramatis(f"❤️  Nyawa tersisa: {self.hp}/{self.hp_max}", 0.4)
        return self.hp > 0
    
    def ambil_healing(self, healing):
        """Penyembuhan dengan narasi magis"""
        old_hp = self.hp
        self.hp = min(self.hp + healing, self.hp_max)
        actual_healing = self.hp - old_hp
        print_dramatis(f"✨ Cahaya penyembuh membungkus tubuhmu... (+{actual_healing} HP)", 0.5)
        print_dramatis(f"❤️  Nyawa dipulihkan: {self.hp}/{self.hp_max}", 0.4)

# ===== FUNGSI UTAMA GAME =====
def game_utama():
    print_dramatis("--- MEMULAI PETUALANGAN DIGITAL ---", 1)
    print_dramatis("\n", 0.3)
    
    # ===== INPUT: Mengambil informasi pemain =====
    nama = input("Siapa namamu, Programmer Petualang? ")
    
    # ===== INISIALISASI: Membuat objek Player =====
    pemain = Player(nama, hp=100, mana=50)
    
    print_dramatis(f"\n🎮 Selamat datang, {pemain.nama}!", 0.5)
    print_dramatis("Benang takodirmu dimulai dengan kilau cahaya yang misterius...", 0.7)
    time.sleep(1)
    
    # Cerita pembuka dengan narasi megah
    print_dramatis("\n" + "═"*60, 0.3)
    print_dramatis("📜 LEGENDA DIMULAI KEMBALI...", 0.6)
    print_dramatis("═"*60, 0.3)
    
    print_dramatis(f"\n🌌 Seorang {pemain.nama} muncul di tengah kegelapan tak terbatas.", 0.5)
    print_dramatis("Aroma kuno tertiup angin—aroma petualangan dan misteri.", 0.5)
    print_dramatis("Di hadapanmu, dua jalur bersinar dengan cahaya berbeda:", 0.5)
    
    print_dramatis("\n🌍 Sebelah Kiri: LEMBAH CODING", 0.4)
    print_dramatis("   Tempat di mana algoritma mengalir seperti air kehidupan.", 0.4)
    print_dramatis("   Kristal-kristal pengetahuan menunggu untuk diambil.", 0.4)
    
    print_dramatis("\n🏔️  Sebelah Kanan: GUNUNG BUG", 0.4)
    print_dramatis("   Puncak yang berselimut kabut kejadian aneh dan mengerikan.", 0.4)
    print_dramatis("   Hanya yang berani akan menemukan kebenaran di sana.", 0.4)
    
    print_dramatis("\n" + "-"*60, 0.3)
    pilihan = input("\n🤔 Pilihan mu akan menentukan nasibmu. Jalan mana? ('Lembah Coding' atau 'Gunung Bug'): ").strip()
    
    print_dramatis("\n" + "═"*60, 0.5)
    
    # ===== LOGIC: IF-ELSE untuk menentukan jalur cerita =====
    if pilihan.lower() == "lembah coding":
        cerita_lembah_coding(pemain)
    elif pilihan.lower() == "gunung bug":
        cerita_gunung_bug(pemain)
    else:
        print_dramatis("❌ Pilihan tidak jelas! Dunia digital bergerak membingungkan...", 0.5)
        print_dramatis("🌪️  Badai energi melanda tubuhmu!", 0.6)
        if pemain.ambil_damage(20):
            print_dramatis("Petualangan dimulai ulang dengan lebih berhati-hati...\n", 0.5)
        else:
            print_dramatis("\n" + "═"*60, 0.3)
            print_dramatis("💀 CAHAYA HIDUPMU PADAM!", 0.8)
            print_dramatis("═"*60, 0.5)
            print_dramatis(f"Legenda {pemain.nama} berakhir di sini. Petualangan gagal.\n", 0.5)

def cerita_lembah_coding(pemain):
    """Jalur 1: Lembah Coding - Tempat Pengetahuan & Item"""
    print_dramatis("\n✨ Cahaya hijau membungkus tubuhmu... LEMBAH CODING menyambutmu! ✨", 0.7)
    
    print_dramatis(f"\n{pemain.nama} melangkah ke dalam lembah yang penuh dengan cahaya emerald.", 0.5)
    print_dramatis("Pohon-pohon bergerak mengikuti ritme loop tanpa henti.", 0.5)
    print_dramatis("Air dengan struktur kode yang sempurna mengalir di sungai kehidupan.", 0.7)
    
    print_dramatis("\n📚 Tiga kristal bersinar dengan cahaya berbeda di depanmu:", 0.5)
    print_dramatis("  1️⃣  KRISTAL BIRU 💙 - Cahaya VARIABLE (Pengetahuan Dasar)", 0.3)
    print_dramatis("  2️⃣  KRISTAL HIJAU 💚 - Cahaya FUNCTION (Kekuatan Hakiki)", 0.3)
    print_dramatis("  3️⃣  KRISTAL EMAS 🟡 - Tantangan Dewa Kode (Risiko Tinggi)", 0.5)
    
    kristal = input("\n🎯 Kristal mana yang akan kau pegang untuk membuka hakikatnya? (1/2/3): ").strip()
    
    # Randomness: Tambahkan elemen keberuntungan
    keberuntungan = random.randint(1, 100)
    
    if kristal == "1":
        print_dramatis("\n💙 Kristal biru bersinar dengan cahaya lembut...", 0.6)
        print_dramatis("Pengetahuan mengalir masuk ke dalam pikiranmu seperti air terjun ilmu.", 0.5)
        print_dramatis("🧠 Kau memahami: VARIABLE adalah tempat di mana jiwa data berdiam!", 0.5)
        print_dramatis(f"   Contoh puitis: nama = '{pemain.nama}'", 0.4)
        print_dramatis("   → Di sini nama pemilik takdir disimpan selamanya.", 0.5)
        
        # Tambah item dengan narasi puitis
        item_book = Item("Grimoire Pengetahuan", "Buku berisi rahasia Variable yang tersembunyi")
        pemain.ambil_item(item_book)
        pemain.xp += 100
        print_dramatis(f"⭐ Pengalaman bertambah: +100 XP\n", 0.7)
        
    elif kristal == "2":
        print_dramatis("\n💚 Kristal hijau meledak dengan energi magis!", 0.6)
        print_dramatis("Cahaya berputar-putar mengelilingimu dalam spiral tak terbatas.", 0.5)
        print_dramatis("🔮 Kau memahami: FUNCTION adalah kekuatan yang bisa dipanggil berkali-kali!", 0.5)
        print_dramatis(f"   Contoh puitis: def {pemain.nama.lower()}_magic():", 0.4)
        print_dramatis("   → Sebuah mantra yang dapat dilucutkan kapan saja!", 0.5)
        
        # Tambah item dengan narasi puitis
        item_staff = Item("Tongkat Fungsi Abadi", "Tongkat bertenaga yang memungkinkan pemanggilkan kekuatan berkali-kali")
        pemain.ambil_item(item_staff)
        pemain.xp += 150
        print_dramatis(f"⭐ Pengalaman bertambah: +150 XP\n", 0.7)
        
    elif kristal == "3":
        print_dramatis("\n🟡 Kristal emas berkilau dengan intensitas menyilaukan!", 0.7)
        print_dramatis("Gelombang energi membanjiri sekitarmu... Ini terlalu berbahaya!", 0.6)
        print_dramatis("⚡ LEDAKAN ENERGI MURNI!", 0.6)
        
        # Randomness: Tambahkan elemen keberuntungan untuk kristal emas
        # Jika keberuntungan tinggi (> 40), pemain selamat
        if keberuntungan > 40:
            print_dramatis("\n💫 TAPI—Nasib berpihak padamu! Perlindungan mistis muncul!", 0.6)
            if pemain.ambil_damage(15):
                item_trophy = Item("Trofi Keberanian", "Simbol telah menghadapi tantangan Dewa Kode")
                pemain.ambil_item(item_trophy)
                pemain.ambil_healing(20)
                pemain.xp += 250
                print_dramatis(f"🏆 Keberanianmu luar biasa! Dewa-dewa pun terpukau...", 0.5)
                print_dramatis(f"⭐ Pengalaman bertambah: +250 XP (Bonus Keberuntungan!)\n", 0.7)
            else:
                print_dramatis("Akan tetapi perlindungan itu tidak cukup...", 0.5)
                tampilkan_tengkorak()
                return
        else:
            # Keberuntungan rendah, pemain meninggal
            print_dramatis("\n⚠️  Nasib tidak berpihak padamu... Kasih sayang dewa tidak cukup.", 0.6)
            pemain.hp = 0
            tampilkan_tengkorak()
            return
    else:
        print_dramatis("\n❌ Kristal yang kau maksud tidak terlihat jelas!", 0.6)
        print_dramatis("Kemarahan lembah menyergapmu dari kegelapan!", 0.5)
        if pemain.ambil_damage(20):
            print_dramatis("Kau berhasil melarikan diri dari kemarahan itu.\n", 0.5)
        else:
            print_dramatis("Jiwa-mu tidak bertahan...", 0.5)
            return
    
    # Tampilkan status pemain setelah cerita Lembah Coding
    pemain.lihat_status()

def cerita_gunung_bug(pemain):
    """Jalur 2: Gunung Bug - Tempat Tantangan & Bahaya"""
    print_dramatis("\n⚡ Langit berselimut kegelapan... GUNUNG BUG memanggil-mu! ⚡", 0.7)
    
    print_dramatis(f"\n{pemain.nama} memulai pendakian gunung yang berselimut kabut merah gelap.", 0.5)
    print_dramatis("Setiap langkah terasa lebih berat dari yang sebelumnya.", 0.5)
    print_dramatis("Suara ERROR terdengar dari ketinggian—itu adalah seruan dewa error itu sendiri!", 0.7)
    
    print_dramatis("\n🐛 Setelah berjam-jam pendakian, kau tiba di gua misteri yang dalam.", 0.5)
    print_dramatis("Dua jalur cahaya membentang di depanmu:", 0.5)
    
    print_dramatis("\n🔦 JALUR A: Cahaya Terang - Ikuti panduan dengan hati-hati", 0.4)
    print_dramatis("   → Lebih aman, namun pengetahuan terbatas.", 0.3)
    
    print_dramatis("\n🌑 JALUR B: Kegelapan Abadi - Jelajahi sendiri dengan berani", 0.4)
    print_dramatis("   → Lebih berbahaya, namun hadiah lebih besar.", 0.3)
    
    jalan = input("\n🚶 Jalan mana yang akan kau ambil? (A/B): ").strip().upper()
    
    # Randomness: Elemen keberuntungan untuk perjalanan
    keberuntungan = random.randint(1, 100)
    
    if jalan == "A":
        print_dramatis("\n🔦 Kau memilih cahaya terang dengan bijaksana.", 0.5)
        print_dramatis("Panduan kode bersinar di dinding gua, menerangi jalanmu:", 0.5)
        
        print_dramatis("\n📜 MANTRA KESELAMATAN:", 0.4)
        print_dramatis("   if pemain_sehat:", 0.3)
        print_dramatis("       pemain.lanjut_petualangan()", 0.3)
        print_dramatis("   else:", 0.3)
        print_dramatis("       pemain.istirahat_panjang()", 0.3)
        
        print_dramatis("\n✨ Kebijaksanaan mengalir melalui pikiranmu!", 0.5)
        print_dramatis("Kau memahami logika dalam dan keluar.", 0.5)
        
        # Tambah item dan healing
        item_amulet = Item("Amulet Nazar Selamat", "Perlindungan dari para dewa dalam gua")
        pemain.ambil_item(item_amulet)
        pemain.ambil_healing(15)
        pemain.xp += 120
        print_dramatis(f"⭐ Pengalaman bertambah: +120 XP\n", 0.7)
        
    elif jalan == "B":
        print_dramatis("\n🌑 Kau memilih untuk menjelajahi kegelapan dengan keberanian murni!", 0.5)
        print_dramatis("Langkahmu goyah, namun kau tidak mundur.", 0.5)
        
        print_dramatis("\n💥 TIBA-TIBA—Sebuah tentakel bug shadow menyergapmu!", 0.6)
        print_dramatis("⚔️  Pertarungan mistis dimulai!", 0.6)
        
        # Randomness: Kesempatan menang dalam pertarungan (50% kesempatan)
        if keberuntungan > 50:
            # Pemain menang pertarungan
            if pemain.gunakan_mana(20):
                print_dramatis("✨ Kau mengarahkan energi gaib dengan presisi sempurna!", 0.5)
                print_dramatis("Setiap pukulan mengenai sasaran dengan tepat...", 0.5)
                
                # Setelah beberapa round, monster terbang
                print_dramatis("\n🏆 MONSTER MENGUNDUR! Kau telah menang!", 0.6)
                tampilkan_pedang()
                
                # Hadiah untuk kemenangan
                item_sword = Item("Pedang Kemenangan", "Senjata yang terbentuk dari energi kemenangan")
                pemain.ambil_item(item_sword)
                pemain.ambil_healing(25)
                pemain.xp += 300
                print_dramatis(f"\n⭐ Pengalaman bertambah: +300 XP (Bonus Kemenangan Epik!)\n", 0.7)
            else:
                print_dramatis("Mana-mu tidak cukup! Tapi keberuntunganmu masih ada!", 0.5)
                pemain.ambil_damage(15)
                print_dramatis("Kau berhasil lari walaupun dengan luka!", 0.5)
        else:
            # Pemain kalah atau selamat dengan luka parah
            print_dramatis("Pertarungan berlangsung sengit...", 0.5)
            if pemain.gunakan_mana(20):
                print_dramatis("✨ Kau berusaha sekarang! Tapi monster terlalu kuat!", 0.5)
                if pemain.ambil_damage(35):
                    print_dramatis("Kau berhasil melarikan diri dengan luka sangat parah!", 0.5)
                    pemain.xp += 100  # XP minimal karena gagal
                else:
                    print_dramatis("Monster mengunci cengkeramannya... Cahayamu memudar...", 0.5)
                    tampilkan_tengkorak()
                    return
            else:
                print_dramatis("Mana-mu habis! Tentakel menyergapmu dengan kuat!", 0.6)
                if pemain.ambil_damage(50):
                    print_dramatis("Kau berhasil lolos dengan luka kritis!", 0.5)
                else:
                    print_dramatis("Kau tidak mampu bertahan... Kesadaran memudar...", 0.5)
                    tampilkan_tengkorak()
                    return
    else:
        print_dramatis("\n❌ Pilihan yang kau buat tidak jelas dalam kegelapan!", 0.6)
        print_dramatis("🌪️  Badai energi chaos menyergapmu!", 0.5)
        if pemain.ambil_damage(30):
            print_dramatis("Kau berhasil selamat namun dengan luka serius.\n", 0.5)
        else:
            print_dramatis("Energi chaos terlalu kuat... Jiwa-mu padam...", 0.5)
            return
    
    # Tampilkan status pemain setelah cerita Gunung Bug
    pemain.lihat_status()

def main():
    """Fungsi utama dengan looping game"""
    main_loop = True
    
    while main_loop:
        game_utama()
        
        # Pertanyaan: Main lagi?
        print_dramatis("\n" + "="*60, 0.3)
        print_dramatis("🎮 PETUALANGAN BERAKHIR...", 0.5)
        print_dramatis("="*60, 0.3)
        print_dramatis("\n🔄 Apakah nasibmu akan membawamu kembali untuk petualangan baru?", 0.7)
        
        ulang = input("\n💫 Main lagi? (y/n): ").strip().lower()
        
        if ulang == "y" or ulang == "ya":
            print_dramatis("\n✨ Cahaya baru bersinar di langit... Petualangan dimulai kembali! ✨\n", 0.8)
            time.sleep(1)
        else:
            print_dramatis("\n🌙 Terima kasih telah berpetualang dalam dunia digital ini...", 0.5)
            print_dramatis("Semoga namamu akan dikenang dalam legenda selamanya.", 0.5)
            print_dramatis("\n👋 Selamat tinggal, Petualang Pemberani! 👋\n", 0.7)
            main_loop = False
    
if __name__ == "__main__":
    main()
