
def day1_solution_part1():
    with open('input.txt') as file:
        content = file.read()
        content = content.split('\n')
        value = 0
        for sentence in content:
            first_number = ''
            second_number = ''
            for char in sentence:
                if(char.isnumeric()):
                    if(first_number == ''):
                        first_number = char
                    second_number = char
            sentence_number = int(first_number + second_number)   
            value += sentence_number
        return value
    
               
print(day1_solution_part1())

numbers = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine"
]

def day1_solution_part2():
    with open('input.txt') as file:
        content = file.read()
        content = content.split('\n')
        value = 0
        for sentence in content:
            first_number = ''
            second_number = ''
            char_number= ''
            for char in sentence:
                if(char.isnumeric()):
                    char_number= ''
                    if(first_number == ''):
                        first_number = char
                    second_number = char
                else:
                    char_number += char
                    if(len(char_number) >= 3):
                        for index in range(len(numbers)):
                            _, last_N, _ = char_number.partition(char_number[-len(numbers[index]):])  
                            if(last_N == numbers[index]):
                                number = str(index+1)
                                if(first_number == ''):
                                    first_number = number
                                second_number = number
                                break   
            sentence_number = int(first_number + second_number)   
            value += sentence_number
        return value      
        
print(day1_solution_part2())