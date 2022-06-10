import re

def read_template(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        raise FileNotFoundError

def parse_template(text):
    reg = '\{(.*?)\}'
    prompts = re.findall(reg, text)
    text = re.sub(reg, '{}', text)
    return text, tuple(prompts)

def get_user_responses(prompts):
    inputs = []
    for i in prompts:
        inputs.append(input(f'Enter a {i.lower()}: '))
    return inputs

def merge(text, inputs):
    return text.format(*inputs)

def print_formatted_text(text):
    print(text)

def write_to_file(filename, text):
    with open(filename, 'w') as out_file:
        out_file.write(text)

def run():
    filename = '../assets/madlib.txt'
    text = read_template(filename)
    text, prompts = parse_template(text)
    inputs = get_user_responses(prompts)
    text = merge(text, inputs)
    print_formatted_text(text)
    out_filename = '../assets/solved_template.txt'
    write_to_file(out_filename, text)

if __name__ == '__main__':
    print("Welcome to Madlib game you will enter a few words and you will have fun with us.")
    run()

