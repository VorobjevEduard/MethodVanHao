class sentence:
    """ Хранит исходное состояние и целевое, выводимость которого требуется выяснить"""

    def __init__(self, source_state, target_state):

        self.source_state = source_state
        self.target_state = target_state
        self.__and_2_comma()
        self.__or_2_comma()

    def compare(self):

        temp_source = self.source_state.split(" , ")
        temp_target = self.target_state.split(" , ")
        temp_source.sort()
        temp_target.sort()

        if temp_source == temp_target:
            return True
        else:
            return False

    def print(self):

        print(self.source_state + " --> " + self.target_state)

    def __and_2_comma(self):

        self.source_state = self.source_state.replace("and", ",")

    def __or_2_comma(self):

        self.target_state = self.target_state.replace("or", ",")

    def proc_not(self):

        split_source = self.source_state.split(" , ")
        i = 0
        while i < len(split_source):
            if "!" in split_source[i] and len(split_source[i]) == 2:
                self.target_state += (" , " + split_source[i][1:])
                del split_source[i]
                continue
            i = i + 1

        temp_source = ""
        for i in split_source:
            temp_source += (i + " , ")
        self.source_state = temp_source[:-3]

        split_target = self.target_state.split(" , ")
        i = 0
        while i < len(split_target):
            if "!" in split_target[i] and len(split_target[i]) == 2:
                self.source_state += (" , " + split_target[i][1:])
                del split_target[i]
                continue
            i = i + 1

        temp_target = ""
        for i in split_target:
            temp_target += (i + " , ")
        self.target_state = temp_target[:-3]

    def proc_brackets(self):
         
        if self.source_state.find("(") != -1:
            open = self.source_state.find("(")
            close = self.source_state.find(")")
            part1 = self.source_state[0: open]
            part1 += self.source_state[open + 1: close].split(" ")[0]
            part1 += self.source_state[close + 1:]

            part2 = self.source_state[0: open]
            part2 += self.source_state[open + 1: close].split(" ")[2]
            part2 += self.source_state[close + 1:]
        
            return sentence(part1, self.target_state), \
                sentence(part2, self.target_state)

        elif self.target_state.find("(") != -1:
            open = self.target_state.find("(")
            close = self.target_state.find(")")
            part1 = self.target_state[0: open]
            part1 += self.target_state[open + 1: close].split(" ")[0]
            part1 += self.target_state[close + 1:]

            part2 = self.target_state[0: open]
            part2 += self.target_state[open + 1: close].split(" ")[2]
            part2 += self.target_state[close + 1:]
        
            return sentence(self.source_state, part1), \
                sentence(self.source_state, part2)

        else:
            return 0, 0

state = [sentence("a and (b or y)", "(!b and y) or (a and (!y or b))")]   # справедливо

while True:
    i = 0
    if len(state) == 0:
        print("Выражение несправедливо!")
        exit()
    while i < len(state):
        for j in state:
            j.print()
        print("************************************")
        if "(" not in state[i].source_state and \
            ")" not in state[i].source_state and \
            "!" not in state[i].source_state and \
            "(" not in state[i].target_state and \
            ")" not in state[i].target_state and \
            "!" not in state[i].target_state:
            del state[i]
            continue
        temp1, temp2 = state[i].proc_brackets()
        if temp1 != 0:
            del state[i]
            state.append(temp1)
            state.append(temp2)
        state[i].proc_not()
        if state[i].compare():
            state[i].print()
            print("Выражение справедливо!")
            exit()
        i = i + 1






















# TODO:
# 1) импликация в source_state и target_state
# 2) поддержка !(expression)