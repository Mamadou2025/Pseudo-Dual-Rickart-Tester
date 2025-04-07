from itertools import product

def gcd(x, y):
    """Calculates the GCD of x and y, with gcd(0,0) = 0"""
    while y != 0:
        x, y = y, x % y
    return abs(x) if x != 0 else 0

def is_endomorphism(f, M):
    """Checks if f preserves the GCD operation"""
    return all(f[gcd(x, y)] == gcd(f[x], f[y]) for x, y in product(M, repeat=2))

def is_idempotent(f, M):
    """Checks if f ∘ f = f"""
    return all(f[f[x]] == f[x] for x in M)

def direct_image(f, M):
    """Calculates the direct image of f"""
    return {f[x] for x in M}

def extended_image(f, M):
    """Calculates the extended image closed under GCD"""
    im_f = direct_image(f, M)
    return {y for y in M if any(gcd(y, f[x]) in im_f for x in M)}

def generate_valid_functions(M):
    """Generates all valid endomorphisms"""
    functions = []
    for f_vals in product(M, repeat=len(M)):
        f = dict(enumerate(f_vals))
        if f[0] == 0 and is_endomorphism(f, M):
            functions.append(f)
    return functions

def analyze_functions(M):
    """Displays a complete analysis with 'i-regular'"""
    print("\nFunction".ljust(15), "Idempotent".ljust(12), "Image".ljust(15), "Extended Image".ljust(18), "i-regular")
    print("-" * 65)
    
    for f in generate_valid_functions(M):
        f_tuple = tuple(f[i] for i in sorted(M))
        im = direct_image(f, M)
        im_ext = extended_image(f, M)
        
        row = f"{str(f_tuple).ljust(15)} | "
        row += f"{'Yes' if is_idempotent(f, M) else 'No'.ljust(10)} | "
        row += f"{str(im).ljust(13)} | "
        row += f"{str(im_ext).ljust(16)} | "
        
        # Determine i-regularity
        if im == im_ext:
            row += "Yes"
        else:
            row += "No"
        
        print(row)

# Define n directly here (no input())
n = 2  # Change this value as needed
M = list(range(n + 1))
analyze_functions(M)