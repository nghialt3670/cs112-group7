import math

def kiemtra(p): 
    tongtiento = 0
    
    for j in range(n):
        if (p[j]==0):
            if(DayNgoac[j]=='('): # náº¿u ngoáº·c má» tÄng tá»ng tiá»n tá» lÃªn 1
                tongtiento+=1
            else:
                tongtiento-=1 # náº¿u ngoáº·c ÄÃ³ng giáº£m tá»ng tiá»n tá» xuá»ng 1
        if(tongtiento<0): # náº¿u ngoáº·c ÄÃ³ng > ngoáº·c má», dÃ£y khÃ´ng há»£p lá»
            return False
    if(tongtiento==0): # náº¿u ngoáº·c ÄÃ³ng = ngoáº·c má», dÃ£y há»£p lá»
        return True
    else:
        return False

def TimXau(p): # lÆ°u láº¡i xÃ¢u
    Xau=""
    for j in range(n):
        if (p[j]==0):
            Xau = Xau + DayNgoac[j]
    return Xau
    
DayNgoac = input()
n = len(DayNgoac)
p = [0] * 200 # máº£ng p lÃ  máº£ng ÄÃ¡nh dáº¥u xem thá»­ ÄÃ£ xÃ³a dáº¥u ngoáº·c táº¡i vá» trÃ­ i hay chÆ°a
              # p[i]=1 tá»©c lÃ  ÄÃ£ xÃ³a, p[i]=0 tá»©c lÃ  chÆ°a xÃ³a
KetQua = 0    # biáº¿n lÆ°u káº¿t quáº£ cá»§a bÃ i toÃ¡n
XauKetQua = "" # biáº¿n lÆ°u xÃ¢u káº¿t quáº£ ÄÃºng cá»§a bÃ i toÃ¡n
for i in range(pow(2,n)): # xÃ¢u cÃ³ n kÃ­ tá»± thÃ¬ sáº½ cÃ³ 2^n cÃ¡ch xÃ³a
    dem = 0
    for j in range(n): 
        
        if ((i>>j)&1): # xem thá»­ vá»i cÃ¡ch thá»© i thÃ¬ kÃ­ tá»± thá»© j cÃ³ bá» xÃ³a hay khÃ´ng
            p[j] = 1   # ÄÃ¡nh dáº¥u xÃ³a
            dem += 1   # tÄng sá» lÆ°á»£ng kÃ­ tá»± xÃ³a lÃªn 1
    if(kiemtra(p)): # kiá»m tra xem xÃ¢u vá»i cÃ¡ch xÃ³a thá»© i cÃ³ thá»a mÃ£n hay khÃ´ng
        XauThoaMan = TimXau(p) # lÆ°u xÃ¢u vá»i cÃ¡ch xÃ³a thá»© i
        if(KetQua < n-dem): # náº¿u cÃ¡ch xÃ³a thá»© i cÃ³ káº¿t quáº£ tá»t hÆ¡n biáº¿n káº¿t quáº£ hiá»n táº¡i cá»§a mÃ¬nh
            KetQua = n - dem # gÃ¡n láº¡i káº¿t quáº£
            XauKetQua = XauThoaMan 
        elif (KetQua == n-dem) and (XauKetQua > XauThoaMan): # Æ°u tiÃªn xÃ¢u cÃ³ thá»© tá»± tá»« Äiá»n bÃ© hÆ¡n
            XauKetQua = XauThoaMan
            
    for j in range(n): # ÄÃ¡nh dáº¥u láº¡i chÆ°a xÃ³a
        p[j] = 0
    
print(KetQua)         
print(XauKetQua)