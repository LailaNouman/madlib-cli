def read_template(path):
    try:
        with open(path, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError as err:
        return err

def parse_template(path):
    with open(path, 'r') as file:
        content = file.read()
        x = content.replace("{Noun}", "{}")
        y = x.replace("{Adjective}", "{}")
        z = ("Adjective", "Adjective", "Noun")
        return y,z
# print(parse_template("../assets/dark_and_stormy_night_template.txt"))
def merge(string1, values):
    with open("../assets/solved_game.txt", 'w') as file:
        file.write(string1.format(*values))
    return string1.format("dark", "stormy", "night")

if __name__ == '__main__':
    print("Welcome to Madlib game you will enter a few words and you will have fun with us.")
    inputs = []
    adj = input("Enter an Adjective ")
    inputs.append(adj)
    adj2 = input("Enter an Adjective ")
    inputs.append(adj2)
    first = input("Enter your First Name ")
    inputs.append(first)
    past = input("Enter a Past tense verb ")
    inputs.append(past)
    first2 = input("Enter a Name ")
    inputs.append(first2)
    adj3 = input("Enter an Adjective ")
    inputs.append(adj3)
    adj4 = input("Enter an Adjective ")
    inputs.append(adj4)
    plural = input("Enter a Plural noun ")
    inputs.append(plural)
    large = input("Enter a Large animal ")
    inputs.append(large)
    small = input("Enter a Small animal ")
    inputs.append(small)
    girl = input("Enter a Girls Name ")
    inputs.append(girl)
    adj5 = input("Enter an Adjective ")
    inputs.append(adj5)
    plural2 = input("Enter a Plural noun ")
    inputs.append(plural2)
    adj6 = input("Enter an Adjective ")
    inputs.append(adj6)
    plural3 = input("Enter a Plural noun ")
    inputs.append(plural3)
    numb = input("Enter a Number between 1-50 ")
    inputs.append(numb)
    first3 = input("Enter a Name ")
    inputs.append(first3)
    numb2 = input("Enter a Number ")
    inputs.append(numb2)
    plural4 = input("Enter a Plural noun ")
    inputs.append(plural4)
    numb3 = input("Enter a Number ")
    inputs.append(numb3)
    plural5 = input("Enter a Plural noun ")
    inputs.append(plural5)

