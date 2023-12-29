n, m = [int(x) for x in input().split()]  # Äá»c sá» trÆ°á»ng há»c vÃ  sá» tiá»m bÃ¡nh
num_students = [int(x) for x in input().split()]  # Äá»c sá» lÆ°á»£ng há»c sinh á» má»i trÆ°á»ng
bakeries = [int(x) for x in input().split()]  # Äá»c vá» trÃ­ cÃ¡c tiá»m bÃ¡nh
schools = [100 * i for i in range(n)]  # Táº¡o danh sÃ¡ch vá» trÃ­ trÆ°á»ng há»c

def find():
    # TÃ¬m khoáº£ng cÃ¡ch giá»¯a trÆ°á»ng há»c vÃ  tiá»m bÃ¡nh
    school_bakery = []
    for i in schools:
        school_bakery.append([abs(i - j) for j in bakeries])
    
    ans = []
    # TÃ¬m tiá»m bÃ¡nh tá»i Æ°u cho tá»«ng trÆ°á»ng há»c
    for i in range(len(schools)):
        d = min(school_bakery[i])
        ans.append([j for j in range(len(school_bakery[i])) if school_bakery[i][j] == d])
  
    return ans

temp_max = 0  # Biáº¿n lÆ°u tá»ng sá» há»c sinh mua bÃ¡nh tá»i Äa
solution = -1  # Vá» trÃ­ tiá»m bÃ¡nh tÆ°Æ¡ng á»©ng

for i in range(1, int(2 * 10e3 + 3)):
    if (i in schools) or (i in bakeries):
        continue

    sold = [0 for i in range(len(bakeries) + 1)]
    bakeries.append(i)  # Thá»­ gÃ¡n vá» trÃ­ tiá»m bÃ¡nh áº£o
    ans = find()
 
    for uni_index in range(len(ans)):
        for bakery_index in ans[uni_index]:
            sold[bakery_index] += num_students[uni_index]

    if sold[-1] > temp_max:
        solution = i
        temp_max = sold[-1]
    bakeries.pop()  # Há»§y gÃ¡n vá» trÃ­ tiá»m bÃ¡nh áº£o

print(temp_max)  # In ra tá»ng sá» há»c sinh mua bÃ¡nh tá»i Äa