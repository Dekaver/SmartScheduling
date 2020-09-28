data = []
total=0
k=0
jadwal=[
    ["08.00-09.00",
     "09.00-10.00",
     "10.00-11.00",
     "11.00-12.00",
     "12.00-13.00",
     "13.00-14.00",
     "14.00-15.00",
     "15.00-16.00"],
    ["-","-","-","-","-","-","-","-"],
    ["-","-","-","-","-","-","-","-"],
    ["-","-","-","-","-","-","-","-"],
    ["-","-","-","-","-","-","-","-"],
    ["-","-","-","-","-","-","-","-"],
    ["-","-","-","-","-","-","-","-"]]
print("Masukkan sesuai format \n{nama jam S S R K J S}(Hari 1 untuk bisa dan 0 untuk tidak bisa) \nContoh\n"
      "Alwi 3 1 0 1 0 1 0")
while (((total != 60) and (total != 61) and (total != 62))):
    a = input().split(" ")
    data.append(a)
    total += int(a[1])
    
def main():
    global k
    while k<48:
        for i in data:
            if int(i[1])==1:
                x=2
                while True: 
                    try:
                        j=i.index("1",x)-1
                        s=sesiEmpty(j)
                        if s>7:
                            x+=1
                        else:
                            join(i[0],j,s)
                            data.remove(i)
                            k+=1
                            break
                    except:
                        if x>7:
                            break
                        x+=1
            if int(i[1])==2:
                x=2
                while True: 
                    try:
                        j=i.index("1",x)-1
                        s=sesiEmpty(j)
                        if s>6:
                            x+=1
                        else:
                            join(i[0],j,s)
                            join(i[0],j,s+1)
                            data.remove(i)
                            k+=2
                            break
                    except:
                        if x>7:
                            break
                        x+=1
            if int(i[1])==3:
                x=2
                while True: 
                    try:
                        j=i.index("1",x)-1
                        s=sesiEmpty(j)
                        if s>5:
                            x+=1
                        else:
                            join(i[0],j,s)
                            join(i[0],j,s+1)
                            join(i[0],j,s+2)
                            data.remove(i)
                            k+=3
                            break
                    except:
                        if x>7:
                            break
                        x+=1
        k+=1
def join(n,h,s):
    jadwal[h][s]=(n)
def sesiEmpty(h):
    c=""
    s=0
    while c!="-" and s!=8:
        c=jadwal[h][s]
        s+=1
    return s-1
def sisajam():
    m=0
    for i in data:
       m+=int(i[1])
    return m

def cetak():
    print("\n|_Jadwal_|_Senin|Selasa|_Rabu_|_Kamis|Jum'at|_Sabtu_|")
    for i in range(8):
        print('|{:^13}|{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|'\
              .format(jadwal[0][i],jadwal[1][i],jadwal[2][i],jadwal[3][i],jadwal[4][i],jadwal[5][i],jadwal[6][i]))
    print("\nTotal =",total-sisajam(),"jam")
    print("Total yang tidak dapat di alokasikan adalah :",sisajam(),"jam")
    print("nama yang baru bisa mengajar minggu berikutnya adalah :")
    u=0
    for i in data:
        if u<len(data)-1:
            print(f'%s(%s)'%(i[0],i[1]),end=",")
        else:
            print(f'dan %s(%s)'%(i[0],i[1]))
        u+=1
main()

for i in jadwal:
    print()
cetak()
"""
contoh Masukan
Adi 3 1 1 1 1 1 1
Beni 1 0 1 0 1 0 1
coki 2 1 1 0 1 0 0
Dena 3 0 1 1 0 1 1
Ema 1 1 0 1 0 1 0
Fifi 2 0 1 1 1 0 1
Gunandi 3 0 0 1 0 1 0
Haryo 3 1 0 1 0 0 0
Ibas 2 0 1 0 0 1 0
Joko 3 0 0 1 1 0 0 
Kartini 3 1 0 0 0 1 1
Linda 2 1 1 1 1 1 1
Mona 1 1 0 1 0 0 0
Neni 2 0 1 0 1 0 1
Omar 3 1 1 1 0 1 0
Parjo 2 1 1 0 1 0 1
Qiqi 3 0 0 1 0 0 1
Robert 3 0 1 0 0 0 0
Santi 3 1 0 1 0 1 0
Titiek 2 0 0 1 1 1 1
Utoyo 2 1 1 1 0 0 0
Vera 3 0 1 1 0 1 0
Wahyu 1 0 0 1 0 1 1
X-men 3 0 0 0 1 1 1
Yongki 2 1 1 1 0 0 0
Zara 3 1 0 1 0 1 0
"""
