import math

say = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

for i in range(0,16): say[i] = 0

while 1:

    op = input(
        "\n1_TOPLAMA(+) \n2_ÇIKARMA(-) \n3_ÇARPMA() \n4_BÖLME(/) \n5_KARESİNİ ALMA(x*y) \n6_KAREKÖK HESAPLAMA(√)"
        "\n7_SİNÜS HESAPLAMA(sin) \n8_COSİNÜS HESAPLAMA(cos) \n9_TANJANT HESAPLAMA(tan) \n10_ln TABANINDA LOGARİTMASI(ln) \n11_LOGARİTMASINI ALMA(log)"
        "\n12_MUTLAK DEĞER \n13_MODUNU ALMA(%) \n14_ÜST ALMA \n15_FAKTORİYEL HESAPLAMA(!) \n0_ÇIKIŞ  \n\nYAPMAK İSTEDİĞİNİZ İŞLEMİ SEÇİNİZ:   ")

    if op == "1" or op == "toplama" or op == "TOPLAMA" or op == "Toplama" or op == "+":
        t1 = float(int(input("1. sayıyı giriniz: ")))
        t2 = float(int(input("2. sayıyı giriniz: ")))
        print(t1 + t2)

        say[0] = say[0] + 1
        say[1] += 1
        if (say[1] >= 3):
            print("Yapılan toplama işlemi sayısı {}".format(say[1]))

    elif op == "2" or op == "ÇIKARMA" or op == "Çıkarma" or op == "çıkarma" or op == "-":
        c1 = float(int(input("1. Sayıyı Giriniz: ")))
        c2 = float(int(input("2. Sayıyı Giriniz: ")))
        print(c1 - c2)

        say[0] += 1
        say[2] += 1
        if (say[2] >= 3):
            print("Yapılan çıkartma işlemi sayısı {}".format(say[2]))

    elif op == "3" or op == "çarpma" or op == "Çıkarma" or op == "ÇARPMA" or op == "*":
        a1 = float(int(input("1. Sayıyı Giriniz: ")))
        a2 = float(int(input("2. Sayıyı Giriniz: ")))
        print(a1 * a2)

        say[0] = say[0] + 1
        say[3] += 1
        if (say[3] >= 3):
            print("Yapılan çarpma işlemi sayısı {}".format(say[3]))

    elif op == "4" or op == "Bölme" or op == "BÖLME" or op == "bölme" or op == "/":
        b1 = float(int(input("1. Sayıyı Giriniz: ")))
        b2 = float(int(input("2. Sayıyı Giriniz: ")))
        print(b1 / b2)

        say[0] = say[0] + 1
        say[4] += 1
        if (say[4] >= 3):
            print("Yapılan bölme işlemi sayısı {}".format(say[4]))

    else:

        if op == "5" or op == "karesini al" or op == "KARESİNİ AL" or op == "Karesini al":
            a = float(int(input("bir sayı giriniz: ")))
            print(a ** 2)

            say[0] = say[0] + 1
            say[5] += 1
            if (say[5] >= 3):
                print("Yapılan karesini alma işleminin sayısı {}".format(say[5]))

        elif op == "6" or op == "KAREKÖKÜ" or op == "karekökü" or op == "Karekökü" or op == "√":
            b = float(int(input("bir sayı giriniz: ")))
            print(math.sqrt(b))

            say[0] = say[0] + 1
            say[6] += 1
            if (say[6] >= 3):
                print("Yapılan karakök işleminin sayısı {}".format(say[6]))

        elif op == "7" or op == "Sinüs" or op == "SİNÜS" or op == "sinüs" or op == "sin":
            c = int(input("bir sayı giriniz: "))
            print(math.sin(c))

            say[0] = say[0] + 1
            say[7] += 1
            if (say[7] >= 3):
                print("Yapılan sinüs hesaplama işleminin sayısı {}".format(say[7]))

        elif op == "8" or op == "cos" or op == "Cos" or op == "COS":
            x = int(input("Bir sayı giriniz: "))
            print(math.cos(x))

            say[0] = say[0] + 1
            say[8] += 1
            if (say[8] >= 3):
                print("Yapılan cosünüs hesaplama işleminin sayısı {}".format(say[8]))

        elif op == "9" or op == "tan" or op == "Tan" or op == "TAN":
            t = int(input("Bir sayı giriniz: "))
            print(math.tan(t))

            say[0] = say[0] + 1
            say[9] += 1
            if (say[9] >= 3):
                print("Yapılan tanjant işleminin sayısı {}".format(say[9]))

        elif op == "10" or op == "ln" or op == "LN" or op == "Ln":
            ln1 = int(input("Bir Sayı Giriniz: "))
            print(math.log1p(ln1))

            say[0] = say[0] + 1
            say[10] += 1
            if (say[10] >= 3):
                print("Yapılan ln tabanında logaritma işleminin sayısı {}".format(say[10]))

        elif op == "11" or op == "log" or op == "LOG" or op == "Log":
            l1 = int(input("1. Sayıyı Giriniz: "))
            l2 = int(input("2. Sayıyı Giriniz: "))
            print(math.log(l1, l2))

            say[0] = say[0] + 1
            say[11] += 1
            if (say[11] >= 3):
                print("Yapılan logaritmasını alma işleminin sayısı {}".format(say[11]))

        elif op == "12":
            md = int(input("Bir Sayı Giriniz: "))
            print(math.fabs(md))

            say[0] = say[0] + 1
            say[12] += 1
            if (say[12] >= 3):
                print("Yapılan Mutlak Değer işleminin sayısı {}".format(say[12]))

        elif op == "13" or op == "Modunu al" or op == "MODUNU AL" or op == "%":
            m1 = int(input("1. Sayıyı Gir: "))
            m2 = int(input("2. Sayıyı Gir: "))
            print(math.fmod(m1, m2))

            say[0] = say[0] + 1
            say[13] += 1
            if (say[13] >= 3):
                print("Yapılan Modunu alma işleminin sayısı {}".format(say[13]))

        elif op == "14":
            n1 = float(int(input("birinci sayıyı gir: ")))
            n2 = float(int(input("ikinci sayıyı gir: ")))
            print(math.pow(n1, n2))

            say[0] = say[0] + 1
            say[14] += 1
            if (say[14] >= 3):
                print("Yapılan Üst alma işleminin sayısı {}".format(say[14]))

        elif op == "15" or op == "!":
            f = int(input("Bir sayı giriniz: "))
            print(math.factorial(f))

            say[0] = say[0] + 1
            say[15] += 1
            if (say[15] >= 3):
                print("Yapılan faktöriyel alma işleminin sayısı {}".format(say[15]))

        elif op=="0" or op=="ÇIKIS" or op=="çıkış":
            print("çıkış yapılıyor...")
            break
    print("Yapılan tüm işlemler toplamı {}".format(say[0]))
    input()



