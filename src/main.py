from dotenv import load_dotenv
import os

print('Hello from repository\\!')
print('Hi')

def print_author():
        load_dotenv('my.env')
        author = os.getenv('AUTHOR')
        print(f'Автор проекта: {author}')

print_author()
