# isi titik - titik di bawah ini
benefit_membership = {"Platinum":[15/100, 
                  "Benefit Silver + Gold + "
                  "Voucher Liburan + Cashback max. 30%"
                 ],
                      "Gold" : [10/100,
                    "Benefit Silver + Voucher Ojek Online"
                 ],
                      "Silver" : [8/100,
                  "Voucher Makanan"
                 ]
    }

membership_requirements = {"Platinum":{'expense': 8, 'income': 15
                            },
                      "Gold" : {'expense' : 6, 'income': 10
                            },
                      "Silver" : {'expense' : 5, 'income' : 7
                            }

    }

user_database = {'Sumbul': 'Platinum',
                 'Ana': 'Gold',
                 'Cahya': 'Platinum',
                 'Shandy': 'Platinum'
    }

database_prediksi = []

tiers = list(benefit_membership.keys())

    # method untuk menampilkan benefit membership

def show_benefit():
    print(f'Terdapat banyak keuntungan bagi kamu yang terdaftar '
            f'sebagai member pada PacCommerce \n'
    )
    print(f"{'Tier' :<10}{'Platinum':<63}{'Gold':<40}{'Silver'} \n")
    print(f"{'Diskon(%)' :<10}{benefit_membership['Platinum'][0]*100:<63}"\
            f"{benefit_membership['Gold'][0]*100:<40}{benefit_membership['Silver'][0]*100}\n"
        f"{'Benefit' :<10}{benefit_membership['Platinum'][1]:<63}"\
            f"{benefit_membership['Gold'][1]:<40}{benefit_membership['Silver'][1]}"
    )

class Membership():
    
    # inisialisasi data

    def __init__ (self, username):
    
        # inisialisasi attribute
        self.username = username
        

    # method untuk menampilkan requirements membership

    def membership_req(self):
        print(f'\n \n-------------------------- \nKetentuan bagi calon member PacCommerce \n')
        print(f"{'Tier' :<24}{'Platinum':<24}{'Gold':<24}{'Silver'} \n")
        print(f"{'Monthly Expense (juta)' :<24}{membership_requirements['Platinum']['expense']:<24}"\
                f"{membership_requirements['Gold']['expense']:<24}{membership_requirements['Silver']['expense']}\n"
            f"{'Monthly Income (juta)' :<24}{membership_requirements['Platinum']['income']:<24}"\
                f"{membership_requirements['Gold']['income']:<24}{membership_requirements['Silver']['income']}")


    # method untuk melakukan prediksi membership
    # menggunakan euclidean distance

    def prediksi_member(self):
        import numpy as np
        pendapatan_bulanan = int(input("Berapa pendapatan bulanan anda: Rp"))
        pengeluaran_bulanan = int(input("Berapa pengeluaran bulanan anda: Rp"))
        r_platinum = np.sqrt(np.square(pendapatan_bulanan-(membership_requirements['Platinum']['income']*1000_000))
                            + np.square(pengeluaran_bulanan-(membership_requirements['Platinum']['expense']*1000_000))
        )
        r_gold = np.sqrt(np.square(pendapatan_bulanan-(membership_requirements['Gold']['income']*1000_000))
                            + np.square(pengeluaran_bulanan-(membership_requirements['Gold']['expense']*1000_000))
        )
        r_silver = np.sqrt(np.square(pendapatan_bulanan-(membership_requirements['Silver']['income']*1000_000))
                            + np.square(pengeluaran_bulanan-(membership_requirements['Silver']['expense']*1000_000))
        )
        member_value = min(r_platinum, r_gold, r_silver) # mencari nilai paling dekat dengan ketentuan
        if member_value == r_platinum : # mengembalikann nilai Platinum, Gold, Silver
            member = "Platinum"
        elif member_value == r_gold :
            member = "Gold"
        else :
            member = "Silver"
        
        database_prediksi.append({"username": self.username, "membership": member})
        print(f"Anda dekat dengan tier membership {member} \nSegera daftarkan diri anda sekarang!")
            
    
    # method untuk menampilkan membership yang dimiliki
    # dari database yang dimiliki
    def benefit_user(self):
        tier_user = user_database[self.username]
        diskon = benefit_membership[tier_user][0] * 100
        benefit_lainnya = benefit_membership[tier_user][1]
        print(f'Anda adalah user dengan tier {tier_user} memiliki benefit diskon {diskon} % setiap belanja dan benefit lainnya berupa {benefit_lainnya}')
    

# method untuk menghitung final price berdasarkan membership

class PlatinumUser(Membership):
    def __init__ (self, username):
        super().__init__ (username)
        self.diskon = benefit_membership["Platinum"][0]
        
        
    def hitung_belanja(self):
        harga = int(input("Besaran belanja: "))
        harga_final = harga - (harga * self.diskon)
        return harga_final


class GoldUser(Membership):
    def __init__ (self, username):
        super().__init__ (username)
        self.diskon = benefit_membership["Gold"][0]
        
        
    def hitung_belanja(self):
        harga = int(input("Besaran belanja: "))
        harga_final = harga - (harga * self.diskon)
        return harga_final


class SilverUser(Membership):
    def __init__ (self, username):
        super().__init__ (username)
        self.diskon = benefit_membership["Silver"][0]
        
        
    def hitung_belanja(self):
        harga = int(input("Besaran belanja: "))
        harga_final = harga - (harga * self.diskon)
        return harga_final



def klasifikasiUser(username):
    username = username.strip().capitalize()
    user = Membership(username)
    if username in user_database:
        user.benefit_user()
        if user_database[username]=="Platinum":
            user = PlatinumUser(username)
        elif user_database[username]=="Gold":
            user = GoldUser(username)
        elif user_database[username]=="Silver":
            user = SilverUser(username)
        print(f'\nAnda habis berbelanja.')
        harga_final = user.hitung_belanja()
        print (f'Harga final untuk belanja anda adalah Rp{harga_final}')
    else:
        user.membership_req()
        print(f'username tidak ditemukan. sistem akan melakukan prediksi membership untuk anda.')
        prediksi_member = Membership(username).prediksi_member()
        user_database[username] = prediksi_member
    


def interface():
    print(f'    selamat datang di \n'
          f' ----- PacCommerce ----- \n')
    
    show_benefit()
    print(f"  \n")
    username = input("Masukkan username anda: ")

    klasifikasiUser(username)


interface()

'''
def show_benefit():
    print(f'Terdapat banyak keuntungan bagi kamu yang terdaftar '
            f'sebagai member pada PacCommerce \n')
    print(f"{'Tier' :<10}{'Platinum':<63}{'Gold':<40}{'Silver'} \n")
    print(f"{'Diskon(%)' :<10}{benefit_membership['Platinum'][0]*100:<63}"\
            f"{benefit_membership['Gold'][0]*100:<40}{benefit_membership['Silver'][0]*100}\n"
          f"{'Benefit' :<10}{benefit_membership['Platinum'][1]:<63}"\
            f"{benefit_membership['Gold'][1]:<40}{benefit_membership['Silver'][1]}"
            )
            
def membership_req():
    print(f'\n \n-------------------------- \nKetentuan bagi calon member PacCommerce \n')
    print(f"{'Tier' :<24}{'Platinum':<24}{'Gold':<24}{'Silver'} \n")
    print(f"{'Monthly Expense (juta)' :<24}{membership_requirements['Platinum']['expense']:<24}"\
            f"{membership_requirements['Gold']['expense']:<24}{membership_requirements['Silver']['expense']}\n"
          f"{'Monthly Income (juta)' :<24}{membership_requirements['Platinum']['income']:<24}"\
            f"{membership_requirements['Gold']['income']:<24}{membership_requirements['Silver']['income']}")
            
            '''