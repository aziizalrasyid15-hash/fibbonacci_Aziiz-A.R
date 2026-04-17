def fibonacci_rekursif(n):
    if n <= 0:
        return []
    elif n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    else:
        fib = fibonacci_rekursif(n -1)
        fib.append(fib[-1] + fib[-2])
        return fib
    
def m_kali_n_rekursif(m, n):
    if n == 0:
        return 0
    return m + m_kali_n_rekursif(m, n -1)

def main():
    while True:
        print("menu pilihan")
        print("1. Barisan Fibonacci")
        print("2. M kali N")
        print("0. keluar")

        pilih = input("pilih menu : ")
        print()

        if pilih == "1":
            n = int(input("Masukkan Jumlah Suku : "))
            hasil = fibonacci_rekursif(n)
            print(f"\nbarisan fibonacci sebanyak {n} suku :")
            print(", ". join(map(str, hasil)))
            print()

        elif pilih =="2":
            m = int(input("Masukan Suatu Bilangan Bulat : "))
            n = int(input("Masukan Suatu Bilangan Pengali: "))
            hasil = m_kali_n_rekursif(m, n)
            print(f"\n{m} x {n} = {hasil}\n")
            
        elif pilih =="0":
            print("keluar dari program.")
            break
        else :
            print("Menu tidak valid, coba lagi.\n")

main()
