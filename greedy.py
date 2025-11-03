amount = int(input("Masukkan jumlah uang: "))

coins = list(map(int, input("Masukkan daftar nilai koin (misal: 1000 500 200 100 50): ").split()))

coins.sort(reverse=True)

print("\nKombinasi koin yang digunakan:")
total_coins = 0
remaining = amount

for coin in coins:
    count = remaining // coin
    if count > 0:
        print(f"{coin} x {count}")
        total_coins += count
        remaining %= coin

print(f"\nJumlah total koin: {total_coins}")