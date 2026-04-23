import os
from flask import Flask, render_template
import markdown

template_dir = os.path.abspath('template')

app = Flask(__name__, template_folder=template_dir)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
POSTS_FOLDER = os.path.join(BASE_DIR, 'posts')

@app.route('/')
def home():
    posts_list = []
    
    if not os.path.exists(POSTS_FOLDER):
        os.makedirs(POSTS_FOLDER)
        return "Pasta 'posts' criada. Adicione um arquivo .md lá e atualize a página."

    filenames = [f for f in os.listdir(POSTS_FOLDER) if f.endswith('.md')]
    if not filenames:
        return "Nenhum arquivo .md encontrado na pasta 'posts'."

    for filename in filenames:
        file_path = os.path.join(POSTS_FOLDER, filename)
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            html_content = markdown.markdown(content)
            posts_list.append(html_content)
    
    return render_template('index.html', posts=posts_list)

if __name__ == '__main__':
    app.run(debug=True)