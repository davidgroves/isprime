import argparse
import re


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--min", type=int, default=1)
    parser.add_argument("--max", type=int, default=100)
    return parser.parse_args()

def is_prime_normal(n: int) -> bool:
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def is_prime_regex(n: int) -> bool:
    if n <= 1:
        return False

    return not re.findall(r"^.?$|^(..+?)\1+$", n * "1")

def main():
    args = parse_args()
    normal_primes = []
    regex_primes = []

    for i in range(args.min, args.max + 1):
        if is_prime_normal(i):
            normal_primes.append(i)
        if is_prime_regex(i):
            regex_primes.append(i)
    
    if normal_primes == regex_primes:
        print("Both methods have determined all primes are the same.")
        print(f"The number of primes found was: {len(normal_primes)}")
        print(f"The primes are: {normal_primes}")
    else:
        print("PRIMES WERE DIFFERENT !")
        print(f"The number of primes found using mathematics was: {len(normal_primes)}")
        print(f"The number of primes found using regex was: {len(regex_primes)}")
        print(f"The primes using mathematics are: {normal_primes}")
        print(f"The primes using regex are: {regex_primes}")

if __name__ == "__main__":
    main()
