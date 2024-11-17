import random

hewan = [
    {"nama": "Gajah", "ciri": ["Memiliki belalai", "Bertubuh besar", "Telinga lebar"]},
    {"nama": "Jerapah", "ciri": ["Lehernya panjang", "Tinggi menjulang", "Memiliki bercak di tubuhnya"]},
    {"nama": "Singa", "ciri": ["Raja hutan", "Berbulu lebat di leher", "Hewan karnivora"]},
    {"nama": "Kanguru", "ciri": ["Melompat dengan kaki belakang", "Memiliki kantong di perut", "Hewan asal Australia"]},
    {"nama": "Panda", "ciri": ["Berbulu hitam putih", "Suka makan bambu", "Asal dari Tiongkok"]},
    {"nama": "Kucing", "ciri": ["Hewan peliharaan", "Suka mengeong", "Suka bermain"]},
    {"nama": "Anjing", "ciri": ["Hewan peliharaan setia", "Suka menggonggong", "Bisa dilatih"]},
    {"nama": "Elang", "ciri": ["Hewan pemangsa", "Memiliki paruh tajam", "Terbang tinggi"]},
    {"nama": "Buaya", "ciri": ["Bertubuh besar", "Memiliki kulit bersisik", "Hidup di air dan darat"]},
    {"nama": "Ular", "ciri": ["Tidak berkaki", "Melata", "Beberapa jenisnya berbisa"]},
    {"nama": "Kelinci", "ciri": ["Bertelinga panjang", "Suka wortel", "Melompat-lompat"]},
    {"nama": "Kuda", "ciri": ["Biasa dikendarai", "Memiliki surai", "Bisa berlari cepat"]},
    {"nama": "Sapi", "ciri": ["Memiliki tanduk", "Bertubuh besar", "Sumber susu dan daging"]},
    {"nama": "Kambing", "ciri": ["Memakan rumput", "Memiliki janggut kecil", "Hidup berkelompok"]},
    {"nama": "Harimau", "ciri": ["Berbulu belang-belang", "Pemangsa daging", "Sering disebut kucing besar"]},
    {"nama": "Zebra", "ciri": ["Berbulu belang hitam putih", "Hidup di padang rumput", "Berkerabat dengan kuda"]},
    {"nama": "Badak", "ciri": ["Memiliki tanduk di hidung", "Bertubuh besar", "Kulitnya tebal"]},
    {"nama": "Koala", "ciri": ["Memakan daun eukaliptus", "Hewan asli Australia", "Menghabiskan waktu di pohon"]},
    {"nama": "Lumba-lumba", "ciri": ["Hidup di laut", "Pintar dan suka bermain", "Dikenal sebagai mamalia laut"]},
    {"nama": "Penguin", "ciri": ["Tidak bisa terbang", "Berjalan tegak", "Hidup di tempat dingin"]},
    {"nama": "Rusa", "ciri": ["Memiliki tanduk bercabang", "Hidup di hutan", "Suka makan rumput"]},
    {"nama": "Beruang", "ciri": ["Bertubuh besar dan kuat", "Pemakan daging dan buah", "Hidup di hutan"]},
    {"nama": "Kuda Nil", "ciri": ["Memiliki mulut besar", "Hidup di air dan darat", "Bertubuh besar"]},
    {"nama": "Burung Hantu", "ciri": ["Aktif di malam hari", "Memiliki penglihatan tajam", "Suaranya khas saat berburu"]},
    {"nama": "Banteng", "ciri": ["Bertanduk kuat", "Sering berwarna coklat tua", "Hidup di padang rumput"]}
]

def game_tebak_hewan():
    while True:
        print("Selamat datang di permainan tebak-tebakan hewan!")
        print("Kamu akan diberikan 5 Soal untuk menjawab dan mendapatkan skor!")
        
        mulai = input("Apakah Kamu ingin Bermain ? (Ya / Tidak) : ").strip().lower()
        
        if mulai == "ya":
            skor = 0
            soal_diberikan = 5 

            soal_hewan = random.sample(hewan, soal_diberikan)

            for nomor, hewan_pilihan in enumerate(soal_hewan, 1):
                nama_hewan = hewan_pilihan["nama"]
                ciri_ciri = hewan_pilihan["ciri"]
                
                print(f"\nSoal nomor {nomor} :")
                print("Tebak hewan berdasarkan ciri-cirinya :")
                for i, ciri in enumerate(ciri_ciri, 1):
                    print(f"Ciri {i} : {ciri}")
                
                tebakan = input("Tebakan kamu : ").strip().capitalize()
                
                if tebakan == nama_hewan:
                    print("Selamat! Tebakan kamu benar.")
                    skor += 1
                else:
                    print(f"Maaf, tebakan kamu salah. Hewan yang dimaksud adalah {nama_hewan}.")

            print(f"\nPermainan selesai! Selamat! Skor kamu : {skor} dari {soal_diberikan}.")

            mainlagi = input("Apakah kamu ingin bermain lagi ? (Ya / Tidak) : ").strip().lower()

            print()

            if mainlagi != "ya":
                print("Terima kasih sudah bermain! Sampai jumpa.")
                break 
        else:
            print("Terima kasih, permainan selesai!")
            break

game_tebak_hewan()
