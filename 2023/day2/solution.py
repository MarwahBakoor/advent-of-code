

BAG_MAX = {
    "red": 12,
    "green":13,
    "blue": 14
}

def day2_solution_part1():
    with open('input.txt') as file:
        content = file.read()
        games = content.split('\n')
        id_sum=0
        for game in games:
            is_possible = True
            game_info = game.split(':')
            game_id= int(game_info[0].split(' ')[1])
            sets_array = game_info[1].split(';')
            for each_set in sets_array:
                rounds = each_set.split(",")
                for each_round in rounds:
                    each_round= each_round.strip()
                    each_round = each_round.split(" ")
                    number = int(each_round[0].replace(" ",""))
                    cube = each_round[1].replace(" ","")
                    if(number > BAG_MAX[cube]):
                        is_possible = False
                        break
            if is_possible:
                id_sum += game_id
        return id_sum                         
        
print(day2_solution_part1())


BAG_MAX = {
    "red": 12,
    "green":13,
    "blue": 14
}

def day2_solution_part2():
    with open('input.txt') as file:
        content = file.read()
        games = content.split('\n')
        power_sum=0
        for game in games:
            fewest_bag_values = {
                "red": 0,
                "green": 0,
                "blue": 0
            }
            game_info = game.split(':')
            game_id= int(game_info[0].split(' ')[1])
            sets_array = game_info[1].split(';')
            for each_set in sets_array:
                rounds = each_set.split(",")
                for each_round in rounds:
                    each_round= each_round.strip()
                    each_round = each_round.split(" ")
                    number = int(each_round[0].replace(" ",""))
                    cube = each_round[1].replace(" ","")
                    if(fewest_bag_values[cube] < number):
                        fewest_bag_values[cube] = number
            fewest_power =1
            for _,value in fewest_bag_values.items():
                fewest_power *= value
            power_sum +=fewest_power
        return power_sum      
    
    
print(day2_solution_part2())
