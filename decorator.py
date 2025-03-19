def parametre_decorator(fonksiyon_adi):
    def wrapper(*args, **kwargs):
        print("Parametreler:", args, kwargs)
        for arg in args:
            if type(arg) !=  int:
                return False
        return fonksiyon_adi(*args, **kwargs)
    return wrapper

@parametre_decorator
def topla(a, b):
    return a + b

sonuc = topla(2, 3)
print("Sonuç:", sonuc)
