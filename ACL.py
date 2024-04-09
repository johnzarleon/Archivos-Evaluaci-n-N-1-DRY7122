#tipo de ACL
def tipo_acl(numero_acl):
    if 1 <= numero_acl <= 99:
        return "ACL Estándar"
    elif 100 <= numero_acl <= 199:
        return "ACL Extendida"
    else:
        return "El número no corresponde a una lista de acceso"

numero_acl = int(input("Ingrese el número de ACL IPv4: "))

print("Tipo de ACL:", tipo_acl(numero_acl))
