# password_gen.py
import secrets
import string
import math

AMBIGUOUS = set("O0oIl1|S5B8Z2")
DEFAULT_WORDS = [
    "orbit","pixel","mango","tiger","quantum","neon","river","echo","kite","ember",
    "cobalt","nova","panda","vortex","maple","ninja","raven","citrus","solar","zen",
    "glacier","pepper","pluto","delta","matrix","salsa","saber","ultra","violet","whale",
    "laser","cocoa","canyon","cosmic","jelly","lotus","meteor","onyx","peppermint","bamboo",
    "falcon","hazel","comet","sigma","turbo","arctic","ember","omega","ripple","zephyr"
]

def bits_of_entropy(pool_size: int, length: int) -> float:
    return length * math.log2(pool_size) if pool_size > 0 else 0.0

def strong_password(length=16, use_lower=True, use_upper=True, use_digits=True,
                    use_symbols=True, avoid_ambiguous=False):
    pools = []
    if use_lower: pools.append(string.ascii_lowercase)
    if use_upper: pools.append(string.ascii_uppercase)
    if use_digits: pools.append(string.digits)
    if use_symbols: pools.append("!@#$%^&*()-_=+[]{};:,.?/")

    if not pools:
        raise ValueError("Select at least one character set.")

    # Merge pool
    pool = "".join(pools)
    if avoid_ambiguous:
        pool = "".join(ch for ch in pool if ch not in AMBIGUOUS)
        if not pool:
            raise ValueError("All characters filtered as ambiguous—relax filters.")

    # Guarantee at least one from each chosen set
    password_chars = []
    for subset in pools:
        subset_filtered = subset if not avoid_ambiguous else "".join(ch for ch in subset if ch not in AMBIGUOUS)
        if not subset_filtered:
            continue
        password_chars.append(secrets.choice(subset_filtered))

    # Fill remaining with full pool
    while len(password_chars) < length:
        password_chars.append(secrets.choice(pool))

    # Shuffle securely
    for i in range(len(password_chars)-1, 0, -1):
        j = secrets.randbelow(i+1)
        password_chars[i], password_chars[j] = password_chars[j], password_chars[i]

    pwd = "".join(password_chars[:length])
    entropy = bits_of_entropy(len(pool), length)
    return pwd, entropy

def passphrase(num_words=4, separator="-", capitalize=False, add_number=True):
    if num_words < 2: num_words = 2
    words = [secrets.choice(DEFAULT_WORDS) for _ in range(num_words)]
    if capitalize:
        words = [w.capitalize() for w in words]
    phrase = separator.join(words)
    if add_number:
        phrase += separator + str(secrets.randbelow(100))
    # Entropy ≈ log2(wordlist_size^num_words) + log2(100 if add_number else 1)
    entropy = num_words * math.log2(len(DEFAULT_WORDS)) + (math.log2(100) if add_number else 0)
    return phrase, entropy

def strength_label(bits):
    if bits < 40: return "Weak"
    if bits < 64: return "OK"
    if bits < 80: return "Good"
    if bits < 100: return "Strong"
    return "Excellent"

def demo():
    print("=== Strong Password ===")
    pwd, e = strong_password(length=16, avoid_ambiguous=True)
    print(pwd)
    print(f"Entropy: {e:.1f} bits ({strength_label(e)})\n")

    print("=== Memorable Passphrase ===")
    phrase, e2 = passphrase(num_words=4, separator="-", capitalize=True, add_number=True)
    print(phrase)
    print(f"Entropy: {e2:.1f} bits ({strength_label(e2)})\n")

if __name__ == "__main__":
    print("Password Generator 🔐")
    print("1) Strong random password")
    print("2) Memorable passphrase")
    choice = input("Choose 1 or 2: ").strip()

    if choice == "1":
        try:
            L = int(input("Length (e.g., 16-24): ").strip() or "16")
        except ValueError:
            L = 16
        avoid = input("Avoid ambiguous characters (y/N)? ").strip().lower() == "y"
        pwd, e = strong_password(length=L, avoid_ambiguous=avoid)
        print("\nYour password:\n", pwd)
        print(f"Entropy: {e:.1f} bits ({strength_label(e)})")
        print("Tip: Store it in a password manager.")
    else:
        try:
            N = int(input("How many words (4–6 recommended): ").strip() or "4")
        except ValueError:
            N = 4
        sep = input("Separator (default '-'): ").strip() or "-"
        cap = input("Capitalize words (y/N)? ").strip().lower() == "y"
        addnum = input("Append a number (Y/n)? ").strip().lower()
        addnum = False if addnum == "n" else True
        phrase, e2 = passphrase(num_words=N, separator=sep, capitalize=cap, add_number=addnum)
        print("\nYour passphrase:\n", phrase)
        print(f"Entropy: {e2:.1f} bits ({strength_label(e2)})")
        print("Tip: Longer passphrases are easier to remember and very strong.")
