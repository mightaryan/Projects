def caesar(text, shift, encrypt=True):
    """
    Performs Caesar cipher encryption or decryption on the given text.
    
    Args:
        text: The string to encrypt or decrypt
        shift: Number of positions to shift each letter (1-25)
        encrypt: True for encryption, False for decryption
    
    Returns:
        The encrypted/decrypted text, or an error message if invalid input
    """
    # Validate that shift is an integer
    if not isinstance(shift, int):
        return 'Shift must be an integer value.'

    # Validate that shift is within valid range (1-25)
    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    # Define the standard alphabet
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    # For decryption, reverse the shift direction
    if not encrypt:
        shift = - shift
    
    # Create the shifted alphabet by rotating the original
    # Example: shift=3 gives 'defghijklmnopqrstuvwxyzabc'
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    
    # Create a translation table that maps each letter to its shifted version
    # Handles both lowercase and uppercase letters
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    
    # Apply the translation to the input text
    encrypted_text = text.translate(translation_table)
    return encrypted_text

def encrypt(text, shift):
    """
    Encrypts text using Caesar cipher.
    
    Args:
        text: The string to encrypt
        shift: Number of positions to shift each letter
    
    Returns:
        The encrypted text
    """
    return caesar(text, shift)
    
def decrypt(text, shift):
    """
    Decrypts text that was encrypted with Caesar cipher.
    
    Args:
        text: The encrypted string to decrypt
        shift: Number of positions that were used for encryption
    
    Returns:
        The decrypted text
    """
    return caesar(text, shift, encrypt=False)

# Example usage: encrypt 'freeCodeCamp' with a shift of 3
encrypted_text = encrypt('freeCodeCamp', 3)
print(encrypted_text)
