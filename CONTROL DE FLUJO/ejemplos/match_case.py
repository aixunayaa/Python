# Ejemplo de match-case (Python 3.10+)
dia = "lunes"
match dia:
    case "lunes":
        print("Es lunes, inicio de semana")
    case "viernes":
        print("Es viernes, casi fin de semana")
    case _:
        print("Es otro día")