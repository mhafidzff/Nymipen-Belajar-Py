# -*- coding: utf-8 -*-

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


# fungsi menunjukkan melihat opsi plan
def cek_benefit():
    print('Plan berlangganan yang tersedia')
    for plan, detil in plan_berlangganan.items():
        print(f'     {plan}')
        print(f' 🎞️ Kualitas Mengunduh {detil["download"]} \n'
              f' 📱 Jumlah Devices {detil["jumlah devices"]} \n'
              f' 🏂 Konten {detil["konten"]}')
        print("-" * 32) # pembatas antara plan
        print(" " * 32)

''' cek_benefit() #coba menampilkan opsi plan''' # nyimpen ae


# database user
user_database = {'mhafidzff' :{'langganan_sekarang' : 'Standard Plan', 
        'durasi_langganan_bulan' : '13'
        },
       'shandy' :{'langganan_sekarang' : 'Basic Plan', 
        'durasi_langganan_bulan' : '10'
        }
}


# fungsi untuk melihat status langganan kita
username = input("Username: ")
def cek_langganan_user():
    for key, status in user_database.items():
        if username == key:
            print(f'Pengguna dengan username {key} memiliki '\
                  f'status berlangganan : {status["langganan_sekarang"]}')
            for plan, detil in plan_berlangganan.items():
                if status["langganan_sekarang"] == plan:
                    print(f' Pengguna memiliki benefit: \n'
                    f' Kualitas Mengunduh: {detil["download"]} \n'
                    f' Jumlah Devices : {detil["jumlah devices"]} \n'
                    f' Konten : {detil["konten"]}'
                    )
            next_step = input("Apakah anda akan ingin meningkatkan plan? (Ans: Ya/Keluar)")
            next_step = next_step.lower()
            if next_step == "ya": # meneruskan opsi upgrade plan
                meningkatkan_plan()
            elif next_step == "keluar":
                pass 
            else:
                print("jawaban anda tidak sesuai")
            return
    raise NameError("Username belum terdaftar")
     

# fungsi mengecek durasi langganan
def cek_durasi_langganan(username):
    for key, status in user_database.items():
        if username == key:
             durasi_langganan = status["durasi_langganan_bulan"]
             if int(durasi_langganan) >= 12:
                    diskon = 5/100
             else:
                    diskon = 0
             return diskon
        

# fungsi untuk meningkatkan plan saat ini
def meningkatkan_plan():
    for key, status in user_database.items(): # ngecek username yang dimasukkan dengan database
        if username == key: # jika username yang masuk sama dengan database maka
            if status["langganan_sekarang"] == "Basic Plan": # jika status berlangganan di database adalah basic plan
                print(f'Anda bisa meningkatkan plan berlangganan anda '\
                    f'menjadi Standard Plan atau Premium Plan')
                pilihan_peningkatan = input("Upgrade ke Standard atau Premium Plan? (Ans: Standard/ Premium) ") # pengguna diminta memasukkan pilihan upgrade jika
                pilihan_peningkatan = pilihan_peningkatan.lower()
                diskon = cek_durasi_langganan(username) 
                if pilihan_peningkatan == "standard":
                    biaya_langganan = int(plan_berlangganan["Standard Plan"]["biaya"])
                elif pilihan_peningkatan == "premium":
                    biaya_langganan = int(plan_berlangganan["Premium Plan"]["biaya"])
                else:
                    print("pilihan tidak Valid")
                
                biaya_langganan_disc = biaya_langganan - (biaya_langganan*diskon)
                print(f' Upgrade status berlanggananmu ke {pilihan_peningkatan.capitalize()} dengan Rp {biaya_langganan_disc}')
                return
                    
            if status["langganan_sekarang"] == "Standard Plan": # jika status berlangganan di database adalah standard plan
                print(f'Anda bisa meningkatkan plan berlangganan anda '\
                    f'menjadi Premium Plan')
                pilihan_peningkatan = input("Upgrade ke Premium? (Ans: Premium) ")
                pilihan_peningkatan = pilihan_peningkatan.lower()
                diskon = cek_durasi_langganan(username)
                if pilihan_peningkatan == "premium":
                    biaya_langganan = int(plan_berlangganan["Premium Plan"]["biaya"])
                else:
                    print("Pilihan tidak Valid")
                
                biaya_langganan_disc = biaya_langganan - (biaya_langganan*diskon)
                print(f'Upgrade status berlanggananmu ke premium dengan Rp {biaya_langganan_disc}')



cek_langganan_user() # nyimpen ae