



def hemm():
    b='0000000 0001111 0010110 0011001 0100101 0101010 0110011 0111100 1000011 1001100'
    hem=b.split()
    code = "0101010"
    def Distance(first_code, second_code):
        dinstance = 7
        for i in range(len(first_code)):
            if first_code[i] == second_code[i]: dinstance -= 1
        return dinstance
    print(code)
    min_ = Distance(code, hem[0])
    i_min = 0
    for i in range(1, 10):
        d = Distance(code, hem[i])
        if min_ > d: 
            min_ = d
            i_min = i
    if min_ == 0: print("Код верный")
    elif min_ == 1: print(f"Код исправлен: {hem[i]} = {i_min}")
    else: print("CODE IS PLOHO")

def morze():
    a="абвгдеёжзийк"
    alf=list(a)
    print (alf)
    mors=".- -... .-- --. -.. . .... ...- --.. .. .--- -.-"
    alfm=mors.split()
    print (alfm)
    morze=input("текст")
    for i in range(len(morze)):
        print (morze[i])

def sus():
    число = int(input("Число10 = "))
    п = int(input("п = "))

    к = 1
    числоп = 0

    while (число != 0):
        числоп = числоп + (число % п) * к

        к *= 10
        число = число // п

    print(числоп)

fu = [hemm, morze, sus]

while True:
    a= input("Выберите программу. 1 - Хемминг, 2 - Азбука Морзе, 3 - Код морзе\n")
    if a.isnumeric:
        if int(a) in [1, 2, 3, 4]:
            print("\n"*10)
            fu[int(a)-1]()
            print("")