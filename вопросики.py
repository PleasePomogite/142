import random

questions = []

count = 0

def vapros_dai():
    with open("vap.txt", 'r', encoding='utf-8') as f:
        lines = f.readlines()
        q = []
        for i in range(len(lines)):
            if lines[i] == '\n': 
                questions.append(vap)
                q = []
                continue
            q.append(lines[i][:-1])

vapros_dai()

for i in range(len(questions)):
    j = random.randint(0, len(vaprosi) - 1)
    vapros = vaprosi[j]
    print(f'{i+1}) ' + vapros[0])
    variants = vapros[1].split('/')
    for j, variant in enumerate(variants):
        print(f'{j+1}. ' + variant)
    print()
    ans = input("Ответ: ")
    if vapros[2] == variants[int(ans)-1]:
        print("\nОтвет правильный! +1 балл")
        count += 1
    else:
        print("\nНу ответ нулёвый кнш... Вот правильный: " + vapros[2] + ". -1 балл")
    vaprosi.remove(vapros)

print(f"\nРезультат: {count}")
