def Try(pos,sototien,tongtien):
    global SoToTienMax
    if(tongtien > m or sototien + len(Tien) - pos < SoToTienMax):
        return 
    if (pos==len(Tien)):
        if(tongtien==m):
            if(sototien>=SoToTienMax):
                global CachChonToiUu
                CachChon = ""
                for i in range(len(Tien),-1,-1):
                    if (check[i]==True):
                        CachChon = CachChon + str(Tien[i]) + " "
                if(sototien>SoToTienMax):
                    SoToTienMax = sototien
                    CachChonToiUu=CachChon
                elif (sototien==SoToTienMax and CachChonToiUu > CachChon):
                    CachChonToiUu = CachChon       
        return 
    for j in range(0,2):
        if (j==1):
            check[pos]=True
        Try(pos+1,sototien+j,tongtien+Tien[pos]*j)
        check[pos]=False
        
n,m = input().split()
n = int(n)
m = int(m)
Tien = []
check = [False] * 30
SoToTienMax = 0
CachChonToiUu = ""
for i in range(n):
    a,b = input().split()
    a = int(a)
    b = int(b)
    while (b>0):
        Tien.append(a)
        b -= 1
Tien.sort(reverse=True)
Try(0,0,0)
print(SoToTienMax)
print(CachChonToiUu)
# for i in range(len(Tien)):
#     print(Tien[i],end= " ")