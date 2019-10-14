
# Printing functions

def count_games(file_name):
    with open(file_name, "r") as file:
        x=file.readlines()
        count=0
        for lines in x:
            count+=1
        return count

print(count_games('game_stat.txt'))

def decide(file_name, year):
    with open(file_name, "r") as file:
        x=file.read()
        if str(year) in x:
            return True
        else:
            return False

print(decide('game_stat.txt',2005))

def get_latest(file_name):
    with open(file_name, "r") as file:
        x=file.readlines()
        years=[]
        for line in x:
            line_t=line.split('\t')
            years.append(line_t[2])
        maximum=max(years)
        for line in x:
            line_t=line.split('\t')
            if line_t[2]==maximum:
                return line_t[0]

print(get_latest('game_stat.txt'))

def count_by_genre(file_name, genre):
    with open(file_name,"r") as file:
        x=file.readlines()
        count=0
        for line in x:
            line_t=line.split('\t')
            if line_t[3]==genre:
                count+=1
        return count

print(count_by_genre('game_stat.txt',"Real-time strategy"))

def get_line_number_by_title(file_name, title):
    with open(file_name, "r") as file:
        x=file.readlines()
        line_number=0
        for line in x:
            line_t=line.split('\t')
            line_number+=1
            if line_t[0]==title:
                return line_number

print(get_line_number_by_title('game_stat.txt',"StarCraft"))       
