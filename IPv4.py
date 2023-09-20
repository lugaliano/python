def verificar_grupos(dir):
    bandera = True
    if len(dir)>16:
        bandera=False
        exit
    else:
        grupos = dir.split(".")
        if len (grupos)!=4:
            bandera = False
        for i in dir:
            for caracter in i:
                if i not in "0123456789.":
                    bandera = False
                    break
        for i in grupos:
            i = int(i)
            if i <0 or i >255:
                bandera = False
                break
    return bandera
    

direccion_ipv= input("ingrese direccion ipv4: ")


if verificar_grupos(direccion_ipv)== True:
    print("la direccion es correcta")
    
else:
    print("La direccion NO es correcta")