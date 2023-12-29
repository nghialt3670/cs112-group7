def Try(id,tong,CachRutTien):
    if(tong==S):
        global SoTruongHop
        SoTruongHop = SoTruongHop + 1
        Ketqua[SoTruongHop] = CachRutTien
        return
    for i in range(id,n): # for tá»« id Äáº¿n n Äá» Äáº£m báº£o cÃ¡c má»nh giÃ¡ tiá»n khÃ´ng ÄÆ°á»£c chá»n xen káº½
        if (tong+Tien[i]<=S): # náº¿u tá»ng hiá»n táº¡i + má»nh giÃ¡ tiá»n i chÆ°a vÆ°á»£t quÃ¡ tá»ng thÃ¬ sáº½ sá»­ dá»¥ng
            Try(i,tong+Tien[i],CachRutTien + str(Tien[i]) + " ")
        
        
n,S = input().split()
n = int(n)
S = int(S)
Tien = []
Tien = [int(i) for i in input().split()]
Tien.sort()
SoTruongHop = 0 # lÆ°u sá» trÆ°á»ng há»£p xáº£y ra khi rÃºt tiá»n S
Ketqua = [""] * 100000 # máº£ng lÆ°u láº¡i cÃ¡ch táº¡o ra káº¿t quáº£
Try(0,0,"")
print(SoTruongHop)
for TruongHop in range(1,SoTruongHop+1):
    print(Ketqua[TruongHop])