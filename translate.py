"""
Creamos un diccionario que contenga las traducciones de letras, números y caracteres
especiales a código Morse. He de aclarar que existen funciones/librerías compatibles con
Python para realizar la traducción, pero el punto del proyecto es hacerlo desde 0.
"""
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', 
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', 
    '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..', 
    '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-'
}

# Función que traduce el texto a código Morse.
def translate_to_morse(text): 
    morse_code = [] # Lista para almacenar el código Morse.

    for char in text.upper(): # Convertimos todo el texto a mayúsculas para simplificar el mapeo.
        if char in MORSE_CODE_DICT: # Verificamos si el carácter está en el diccionario.
            morse_code.append(MORSE_CODE_DICT[char]) # Agregamos el código Morse a la lista.
        
        elif char == ' ': # Manejamos los espacios en el texto.
            morse_code.append('/') # Representamos los espacios en el texto como '/'
    
    return ' '.join(morse_code) # Unimos la lista en una cadena separada por espacios y la retornamos.

# Función que traduce el código Morse a texto.
def translate_to_text(morse_code):
    morse_code += ' ' # Agregamos un espacio al final del código Morse para asegurarnos que la última palabra se procese.
    decipher = '' # Cadena para almacenar el texto descifrado.
    citext = '' # Variable temporal para almacenar el código Morse de un solo carácter o número.
    
    for char in morse_code:
        if char != ' ':
            i = 0 # Restablecemos el contador de espacios.
            citext += char # Agregamos el carácter actual a la variable temporal.

        else:
            i += 1 # Incrementamos el contador de espacios.
            if i == 2: # Si hay dos espacios consecutivos, significa un nuevo término en el texto.
                decipher += ' ' # Agregamos un espacio al texto descifrado.

            else:
                if citext in MORSE_CODE_DICT.values():
                    # Convertimos el código Morse temporal en el carácter correspondiente y agregamos al texto descifrado.
                    decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext)]
                citext = '' # Reseteamos la variable temporal para el siguiente código Morse.

    return decipher # Retornamos el texto descifrado.

# Función que verifica si el texto es código Morse.
def is_morse_code(text):
    morse_characters = set('.-/ ')
    return all(char in morse_characters for char in text)