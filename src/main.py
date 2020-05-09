import re

def descifrar():
    with open('encoded.txt', 'r', encoding='utf-8') as f:
        txt = f.read()
        print(''.join(re.findall("[a-z]+", txt)))
        f.close()

def run():
    descifrar()


if __name__ == '__main__':
    run()
