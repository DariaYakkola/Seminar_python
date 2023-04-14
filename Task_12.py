# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных
# числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя
# делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.
sum = int(input('Введите сумму чисел: '))
multiplication = int(input('Введите произведение чисел: '))
x = y = 0
while x <= 1000:
    while y <= 1000:
        if x * y == multiplication and x + y == sum:
            print(f'{x} + {y} = {sum} и {x} * {y} = {multiplication}')
            exit()
        else:
            y += 1
    y = 0
    x += 1
print('Таких чисел не существует! ')
