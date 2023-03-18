""" Добавьте в модуль с загадками функцию, которая хранит словарь списков.
Ключ словаря- загадка, значение- список с отгадками
Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки"""


class Question:
    def __init__(self, text, real_answer):
        self.text = text
        self.real_answer = real_answer
        self.answers = [real_answer]

    def add_false_answer(self, answer):
        self.answers.append(answer)

    def __str__(self):
        return f'Загадка: {self.text}\nВарианты ответов:{list(set(self.answers))}'


class Game:
    def __init__(self):
        self.questions = []
        self.wrong = self.right = 0

    def add(self, question):
        self.questions.append(question)

    def run(self):
        for question in self.questions:
            print(question)
            answer = input('Ответ>>>')
            if answer == question.real_answer:
                print('Верно!')
                self.right += 1
            else:
                print('Неверно!')
                self.wrong += 1
        print(f'Верных ответов {self.right}, неверных {self.wrong}')


if __name__ == '__main__':
    game = Game()
    question1 = Question('Зимой и летом одним цветом', 'елка')
    question1.add_false_answer('дуб')
    question1.add_false_answer('береза')
    question2 = Question('Столица России', 'Москва')
    question2.add_false_answer('Вашингтон?')
    question2.add_false_answer('Токио')
    question3 = Question('Не лает не кусает а в дом не пускает', 'замок')
    question3.add_false_answer('собака')
    question3.add_false_answer('сторож')
    question4 = Question('Висит груша-нельзя скушать', 'лампочка')
    question4.add_false_answer('тетя Груша повесилась')
    question4.add_false_answer('боксерская груша')
    game.add(question1)
    game.add(question2)
    game.add(question3)
    game.add(question4)
    game.run()
