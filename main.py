# buraya istediğiniz fonksiyonu yazın.
def f(x):
    func = (x**3)-(7*(x**2))+(14*x)-6
    return func


def bisection(a, b, e, max):
    step = 1

    condition = True
    while condition:
        # ortanca değeri bulma.
        m = (a + b)/2

        # Bu ifade doğruysa kök a ile ortanca değer arasında.
        if f(a) * f(m) < 0:
            b = m
        else:
            a = m

        step = step + 1
        condition = abs((b-a)/2) >= e
        if step >= max and abs((b-a)/2) >= e:
            condition = False
            print("Maksimum tekrarda yankınsama sağlanamadı.")

    print('\nYaklaşık kök: %0.4f ' % m)
    print('\nTekrar sayısı: %d ' % step)


a = float(input('Aralığın ilk değeri: '))
b = float(input('Aralığın ikinci değeri: '))
e = float(input('Tolerans: '))
max = float(input('Maksimum tekrar sayısı: '))


# Ara değer yöntemi ile girilen aralıkta kök olup olmadığını kontrol edelim.
if f(a) * f(b) > 0.0:
    print('Verilen aralıkta kök bulunamadı.')
else:
    bisection(a, b, e, max)
