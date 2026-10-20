class skobki: #основной класс
    def __init__(self, data):
        self.data = data
        self.next = None
        
    def balance(text):
        top = None
        
        for char in text:   #Проходим по символам строки
            #открывающие скобки
            if char == "(" or char == "[" or char == "{":
                new_n= skobki(char)
                new_n.next=top
                top=new_n
            #закрывающие скобки
            elif char == ")" or char == "]" or char == "}": 
                if top is None:
                    return False
            #Взятие символа из топа    
            last=top.data
            top=top.next
            #Проверка пары
            if (char == ")" and last !="(") or \
                (char == "]" and last !="[") or \
                (char == "}" and last !="{"):
                    return False
        return top is None