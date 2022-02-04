"""
    Zainstaluj bibliotekę inflection
    >> pip install inflection
    Korzystaj z niesamowitych funkcji do przetwarzania napisów!
"""

import inflection

# ----------------------------------------------------------------------------------
# Konwersja napisu do postaci CamelCase

# km_programs => KmPrograms
print(inflection.camelize('km_programs'))
# km_programs => kmPrograms
print(inflection.camelize('km_programs', False))

# Konwersja napisu do postaci snake_case
# KmPrograms => km_programs
print(inflection.underscore('KmPrograms'))

# -----------------------------------------------------------------------------------
# Wyznaczanie liczby mnogiej dla podanego wyrazu
# z uwzględnieniem zasad gramatyki

# post => posts
print(inflection.pluralize('post'))

# posts => posts
print(inflection.pluralize('posts'))

# octopus => octopi
print(inflection.pluralize('octopus'))

# CamelOctopus => CamelOctopi
print(inflection.pluralize('CamelOctopus'))

# -------------------------------------------------------------------------------------
# Wyznaczanie nazwy tabeli np dla bazy danych

# BestPlayer => best_players
print(inflection.tableize('BestPlayer'))

# CustomerOrder => customer_orders
print(inflection.tableize('CustomerOrder'))

# Biblioteka posiada jeszcze kilka innych ciekawych funkcji.
# KONIECZNIE SPRAWDŹ W DOKUMENTACJI! => Link w opisie ;)