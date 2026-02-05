def main(): 
    print(f"{'num':<5}{'2':<15}{'3':<15}{'And':<16}")
    for n in range(13, 17): 
        div2 = (n % 2 == 0)
        div3 = (n % 3 == 0)
        And = div2 and div3
        print(f"{n:<5}{str(div2):<15}{str(div3):<15}{str(And):<16}")

if __name__ == "__main__":
    main() 
