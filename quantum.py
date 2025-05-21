import requests
import string
import secrets  # for fallback

class QuantumAPIError(Exception):
    pass

def get_quantum_random_bytes(length):
    try:
        response = requests.get(f'https://qrng.anu.edu.au/API/jsonI.php?length={length}&type=uint8')
        response.raise_for_status()
        data = response.json()
        if data['success']:
            return data['data']
        else:
            raise QuantumAPIError("Failed to fetch quantum random bytes.")
    except requests.RequestException as e:
        # Fallback: Use Python's secrets module to generate random bytes
        print(f"⚠️ Warning: Quantum API failed: {e}. Falling back to pseudo-random bytes.")
        return [secrets.randbelow(256) for _ in range(length)]  # Return list of random bytes

def get_random_password(length, charset):
    random_bytes = get_quantum_random_bytes(length)
    password = ''.join(charset[b % len(charset)] for b in random_bytes)
    return password

def get_password_by_strength(strength):
    if strength == "Weak":
        length = 8
        charset = string.ascii_lowercase + string.digits
    elif strength == "Medium":
        length = 12
        charset = string.ascii_letters + string.digits
    elif strength == "Strong":
        length = 16
        charset = string.ascii_letters + string.digits + string.punctuation
    else:
        raise ValueError("Invalid strength level.")
    
    return get_random_password(length, charset)
