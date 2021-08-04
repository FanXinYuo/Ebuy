import random


class RandomString:
    string1 = ''

    def digit(self, number):  # 生成number位的纯数字
        self.string1 = ''
        for i in range(number):
            self.string1 += str(random.randint(1, 9))
        return self.string1

    def units(self):    # 单位
        self.string1 = ''
        list1 = ['箱', '瓶', '根', '条', '本', '件', '套']
        self.string1 = random.choice(list1)
        return self.string1

    def character(self, number):
        self.string1 = ''
        list1 = ['这', '是', '垃', '圾', '玩', '意', '千', '万', '值', '得', '购', '很', '可', '安']
        for i in range(number):
            self.string1 += str(random.choice(list1))
        return self.string1

    def sex(self):
        self.string1 = ''
        list1 = ['男', '女']
        return random.choice(list1)

    def hybrid(self, letter, number):   # 生成数字、字母的复合形式
        self.string1 = ''
        list1 = ['a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F', 'g', 'G', 'h', 'H', 'i', 'I', 'j', 'J', 'k', 'K', 'l', 'L']
        while letter > 0:
            self.string1 += random.choice(list1)
            letter -= 1
        while number > 0:
            self.string1 += str(random.randint(0, 9))
            number -= 1
        return self.string1




