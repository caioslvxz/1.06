def celsius_para_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_para_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Exemplo de uso:
temperatura_celsius = 30
temperatura_fahrenheit = celsius_para_fahrenheit(temperatura_celsius)
print(f"{temperatura_celsius}°C equivalem a {temperatura_fahrenheit}°F")

temperatura_fahrenheit = 86
temperatura_celsius = fahrenheit_para_celsius(temperatura_fahrenheit)
print(f"{temperatura_fahrenheit}°F equivalem a {temperatura_celsius}°C")
