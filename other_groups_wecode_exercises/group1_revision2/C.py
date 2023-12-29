# Nháº­p sá» lÆ°á»£ng bá» test
T = int(input())

# Láº·p qua tá»«ng bá» test
for tt in range(T):
    # Nháº­p kÃ­ch thÆ°á»c cá»§a máº£ng
    N = int(input())

    # Nháº­p máº£ng sá» vÃ  sáº¯p xáº¿p theo thá»© tá»± tÄng dáº§n
    arr = list(map(int, input().split()))
    arr.sort()

    # TÃ­nh tá»ng cá»§a máº£ng ÄÃ£ sáº¯p xáº¿p
    total = sum(arr)

    # Khá»i táº¡o cÃ¢u tráº£ lá»i lÃ  ná»­a cá»§a tá»ng lÃ m trÃ²n lÃªn
    result = (total + 1) // 2
    count = result
    additional = 0

    # Láº·p qua máº£ng ÄÃ£ sáº¯p xáº¿p Äá» tÃ¬m cÃ¡c pháº§n tá»­ bá» sung cáº§n thiáº¿t
    for i in range(N):
        count -= arr[i]

        # Náº¿u tá»ng cháº¡y trá» thÃ nh Ã¢m, tÃ­nh toÃ¡n cÃ¡c pháº§n tá»­ bá» sung cáº§n thiáº¿t
        if count < 0:
            additional = N - i
            break

    # In káº¿t quáº£ cuá»i cÃ¹ng, lÃ  tá»ng cá»§a cÃ¢u tráº£ lá»i ban Äáº§u vÃ  cÃ¡c pháº§n tá»­ bá» sung
    print(result + additional)