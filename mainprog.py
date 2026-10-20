import unittest

class skobki:  # основной класс 
    def __init__(self, data):
        self.data = data
        self.next = None

    @staticmethod
    def balance(text): #Проходим по символам строки
        top = None

        for char in text: 
            #Открывающие скобки
            if char in '([{':
                new_n = skobki(char)
                new_n.next = top
                top = new_n

            #Закрывающие скобки
            elif char in ')]}':
                # Если стек пустой
                if top is None:
                    return False

                #Взятие символа из топа 
                last = top.data
                top = top.next

                # Проверка пары
                if (char == ')' and last != '(') or \
                   (char == ']' and last != '[') or \
                   (char == '}' and last != '{'):
                    return False

        return top is None
    

print("Проверка строки [[()]]:", skobki.balance("[[()]]"))
print("Проверка строки ([]):", skobki.balance("([])"))
print("Проверка строки ([)] :", skobki.balance("([)]"))
print("Проверка строки ((()):", skobki.balance("((())"))
