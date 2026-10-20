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
class UTest(unittest.TestCase): #юнитест, тесты правильные.неправильные

    def test_simplePair(self):
        self.assertTrue(skobki.balance("()"))

    def test_textWith(self):
        self.assertTrue(skobki.balance("a+(b*c)-[d]"))


    def test_wrongPoriadok(self):
        self.assertFalse(skobki.balance("([)]"))


    def test_withoutOpen(self):
        for text in [")", "]", "}"]:
            with self.subTest(text=text):
                self.assertFalse(skobki.balance(text))

    def test_unclosed(self):
        for text in ["(", "[", "{", "(((", "[({"]:
            with self.subTest(text=text):
                self.assertFalse(skobki.balance(text))

    def test_wrongType(self):
        self.assertFalse(skobki.balance("(]"))
        self.assertFalse(skobki.balance("{)"))

if __name__ == "__main__":
    unittest.main()