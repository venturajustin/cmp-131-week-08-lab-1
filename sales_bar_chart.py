#Jusitn Ventura nov 12 2026 cmp 131 week 8
sales = list(
    float(input(f"Enter today's sales for store {i}: ")) 
    for i in range(1, 6)
)
for i in range(5):
    stars = int(sales[i] // 100)
    print(f"Store {i + 1}: {'*' * stars}")