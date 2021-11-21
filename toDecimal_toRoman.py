# Autor: Paulo Henrique Diniz de Lima Alencar

decimal = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
roman = ['I','IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']


# Funcao: reponsavel pela conversao de numero romano para decimal.
def toDecimal(roman_number=""):
    if roman_number == "":
        return None
    
    digits = []
    
    i = 0 
    while (i < len(roman_number)):

        if roman_number[i:i+2] in roman:
            digits.append(decimal[roman.index(roman_number[i:i+2])])
            i = i + 2
        elif roman_number[i] in roman:
            digits.append(decimal[roman.index(roman_number[i])])
            i = i + 1
        else:    
            i = i + 1

    return f'{roman_number}: {sum(digits)}'


# Funcao: reponsavel pela conversao de numero decimal para romano.
def toRoman(decimal_number):
    
    if not (decimal_number >= 1 and decimal_number <= 3999):
        return "Invalid number!"

    root_number = decimal_number
    
    roman_number = ""
    new_decimal = decimal[:]
    new_decimal.reverse()
   
    for base_value in new_decimal:
        
        if base_value <= decimal_number:
            while True:
                repetitions = decimal_number // base_value
                decimal_number = decimal_number % base_value
                
                if repetitions == 0:
                    break

                while repetitions:
                    roman_number +=  roman[decimal.index(base_value)]
                    repetitions -= 1
                
                if decimal_number == 0:
                    return f'{root_number}: {roman_number}'
    

print(toDecimal("IV"))
print(toDecimal("VII"))
print(toDecimal("CIX"))

print(toRoman(199))
print(toRoman(200))
print(toRoman(1000))
print(toRoman(4))
print(toRoman(109))
print(toRoman(3549))
print(toRoman(45))
print(toRoman(4000))
print(toRoman(2923))
