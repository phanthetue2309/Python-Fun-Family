
class sinhVien:
    def __init__(sv,ma,ten):
        sv.msv = ma
        sv.name = ten
    def inthongtin(sv):
        print("Ma sinh vien: " + sv.msv)
        print("Ten sinh vien: " + sv.name)


sinhviena = sinhVien('1000000','Tue' )
sinhviena.inthongtin()
