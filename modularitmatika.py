import aritmatika


def main():
    a=int(input("masukan nilai A: "))
    b= int(input("masukan nilai B: "))

    print('a\t : %d' % a)
    print('a\t : %d' % b)

    print('a+b\t : %d' % aritmatika.tambah(a,b))
    print('a-b\t : %d' % aritmatika.kurang(a,b))
    print('a*b\t : %d' % aritmatika.kali(a,b))
    print('a/b\t : %d' % aritmatika.bagi(a,b))

if __name__=="__main__":
    main()
