
import re


# ejrcicio 1
print (re.findall (r"\d{3}-\d{3}", "IDs: 123-456, 999-000, 42-999, 888-777"))

# ejercicio 2
print (re.findall (r"[a-z0-9]+@[a-z]+\.com", "Contactos: admin@test.com, bad@mail, user123@site.com, x@x.com"))

# ejercicio 3
print (re.findall (r"\d{2}/\d{2}/\d{4}", "Hoy es 19/01/2026 y mañana 20/1/2026 y ayer 05/12/2025"))

# ejercicio 4
print (re.findall (r"\b(?=[A-Za-z0-9]{6,}\b)(?=.*[A-Za-z])(?=.*\d)[A-Za-z0-9]+\b", "Claves: abc123, 123456, password, A1b2C3, test12, admin"))

# ejercicios 5
print (re.findall (r"[A-Z]{3}-\d{4}-[A-Z]{3}", "Tokens: ABC-1234-XYZ, BAD-12-ZZZ, API-9999-KEY, HELLO-0000-WORLD"))