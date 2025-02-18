# -*- coding: utf-8 -*-

# database user
user_database = {'mhafidzff' :{'langganan_sekarang' : 'Standard Plan', 
        'durasi_langganan_bulan' : '13'
        },
       'shandy' :{'langganan_sekarang' : 'Basic Plan', 
        'durasi_langganan_bulan' : '10'
        },
        'ana': {'langganan_sekarang' : 'Basic Plan',
        'durasi_langganan_bulan' : '14'
        },
}

# database referral code
referral_database = ['R3ferral', 'D4riTeman']


# dictionary dari plan berlangganan
plan_berlangganan = {
    "Basic Plan":{
            "download" : "Dalam SD",
            "jumlah devices" : "1",
            "konten" : "Hanya 3rd party film",
            "biaya" : "120000"
            },
    "Standard Plan":{
            "download" : "Dalam HD",
            "jumlah devices" : "2",
            "konten" : "3rd party film + Sports(F1, Sepakbola, Basket)",
            "biaya" : "160000"
            },
    "Premium Plan":{
            "download" : "Dalam Ultra HD",
            "jumlah devices" : "4",
            "konten" : "3rd party film + Sports(F1, Sepakbola, Basket) +"\
                 " Pacflix original series and movies",
            "biaya" : "200000"
            }
}

# Membuat Object Oriented Program
# User Basic
class User():
    def __init__ (self, username):
        self.username = username
        print("Hai {self.username}, Selamat datang!")


# OOP User Berlangganan
class UserBerlangganan(User):
    def __init__(self, username, status):
        super().__init__(username)
        self.plan = status['langganan_sekarang']
        self.durasi = int(status['durasi_langganan_bulan'])

    def cek_langganan_user(self):
        status = user_database[username]
        plan_name = status["langganan_sekarang"]
        plan = plan_berlangganan.get(plan_name,{})
        print(f'Pengguna dengan username {self.username} memiliki '\
            f'status berlangganan : {self.plan}')
        print(f' Pengguna memiliki benefit: \n'
            f' 🎞️  Kualitas Mengunduh: {plan.get('download', 'tidak tersedia')} \n'
            f' 📱 Jumlah Devices : {plan.get('jumlah devices','tidak tersedia')} \n'
            f' 🏂 Konten : {plan.get('konten', 'tidak tersedia')} \n'
            f' Sudah berlangganan selama {status['durasi_langganan_bulan']} bulan'
            )
    
    def cek_diskon(self):
        if self.durasi >= 12:
            diskon = 5/100
        else:
            diskon = 0
        return diskon 

    def meningkatkan_plan(self):
        if self.plan == "Basic Plan": # jika status berlangganan di database adalah basic plan
            print(f'Anda bisa meningkatkan plan berlangganan anda '\
                    f'menjadi Standard Plan atau Premium Plan')
            pilihan_peningkatan = input("Upgrade ke Standard atau Premium Plan? (Ans: Standard/ Premium) ") # pengguna diminta memasukkan pilihan upgrade jika
            pilihan_peningkatan = pilihan_peningkatan.lower()
            diskon = self.cek_diskon() 
            if pilihan_peningkatan == "standard":
                biaya_langganan = int(plan_berlangganan["Standard Plan"]["biaya"])
            elif pilihan_peningkatan == "premium":
                biaya_langganan = int(plan_berlangganan["Premium Plan"]["biaya"])
            else:
                print("pilihan tidak Valid")
            
            biaya_langganan_disc = biaya_langganan - (biaya_langganan*diskon)
            print(f' Upgrade status berlanggananmu ke {pilihan_peningkatan.capitalize()} dengan Rp {biaya_langganan_disc}')
            return
                    
        elif self.plan == "Standard Plan" : # jika status berlangganan di database adalah standard plan
            print(f'Anda bisa meningkatkan plan berlangganan anda '\
                f'menjadi Premium Plan')
            pilihan_peningkatan = input("Upgrade ke Premium? (Ans: Premium) ")
            pilihan_peningkatan = pilihan_peningkatan.lower()
            diskon = self.cek_diskon()
            if pilihan_peningkatan == "premium":
                biaya_langganan = int(plan_berlangganan["Premium Plan"]["biaya"])
            else:
                raise Exception ("Pilihan tidak Valid")
            
            biaya_langganan_disc = biaya_langganan - (biaya_langganan*diskon)
            print(f'Upgrade status berlanggananmu ke premium dengan Rp {biaya_langganan_disc}')
            
        
        else :
            print(f' Subskripsi anda sudah maksimal')


# OOP User Baru
class UserBaru(User):
    def __init__ (self, username):
        self.username = username

    def cek_benefit(self):
        print('Plan berlangganan yang tersedia')
        for plan, detil in plan_berlangganan.items():
            print(f'     {plan}')
            print(f' 🎞️ Kualitas Mengunduh {detil["download"]} \n'
                f' 📱 Jumlah Devices {detil["jumlah devices"]} \n'
                f' 🏂 Konten {detil["konten"]}')
            print("-" * 32) # pembatas antara plan
            print(" " * 32)

    def berlangganan(self):
        print("Apakah anda tertarik dengan paket berlangganan yang ada?")
        tertarik = input("(Ya/ Tidak)")
        tertarik = tertarik.capitalize()    
        
        if tertarik == "Ya":
            while True:
                opsi_langganan = input("Basic/ Standard/ Premium?")
                opsi_langganan = opsi_langganan.capitalize()
                opsi_langganan = opsi_langganan + " Plan"

                if opsi_langganan in plan_berlangganan:
                    diskon = self.cek_referral()
                    biaya_langganan = int(plan_berlangganan[opsi_langganan]["biaya"])
                    biaya_langganan_disc = biaya_langganan - (biaya_langganan * diskon)
                    print(f"Anda dapat berlangganan {opsi_langganan} dengan biaya Rp{biaya_langganan_disc}")
                    break

                else:
                    print("Opsi plan yang anda masukkan tidak valid")
                
        elif tertarik == "Tidak":
            print("Noted, Terimakasih!")

        else:
            print("opsi langganan tidak valid")


    def cek_referral(self): #belum dibikin
        referral = input("input kode referral anda: ")
        if referral in referral_database:
            diskon = 4/100
        else:
            diskon = 0
        return diskon
        


# mengkelaskan user baru dan user berlangganan

def klasifikasi_user(username):
    
    if username in user_database:
        user = UserBerlangganan(username, user_database[username])
        user.cek_langganan_user()
        while True:
            next_step = input("Apakah anda berminat meningkatkan " \
                            f"plan berlangganan anda? (Ya/ Tidak) ")
            next_step = next_step.lower()
            if next_step == "ya":
                user.meningkatkan_plan()
                return
            elif next_step == "tidak":
                print(f'Oke. terimakasih!')
                break
            else:
                print(f'Plan yang anda tulis tidak valid')
    else:
        user = UserBaru(username)
        user.cek_benefit()
        user.berlangganan()



# menjalankan program awal
username = input("Username: ")
klasifikasi_user(username)