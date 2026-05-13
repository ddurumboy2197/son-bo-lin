def ikkita_sonni_bolish(a, b):
    return a / b

son1 = float(input("Birinchi sonni kiriting: "))
son2 = float(input("Ikkinchi sonni kiriting: "))

natija = ikkita_sonni_bolish(son1, son2)
print(f"{son1} / {son2} = {natija:.2f}")
