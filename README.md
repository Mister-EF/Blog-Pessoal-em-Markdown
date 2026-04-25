# Personal Markdown Blog

A full-stack bridge using a Python backend (Flask) to process local `.md` files and serve them through styled HTML/CSS templates for a seamless reading experience. Write posts in Markdown, run the server, and your blog renders automatically — no CMS, no database, no overhead.

---

## How It Works

Flask reads every `.md` file from the `posts/` directory, converts each one to HTML using the `markdown` library, and passes the rendered content to a Jinja2 template. The template loops through the posts and displays them as styled cards. If the `posts/` folder doesn't exist, the app creates it on first run.

---

## Built With

| Technology | Role |
|------------|------|
| Python | Core backend language |
| Flask | Web server and template rendering |
| `markdown` | `.md` to HTML conversion |
| Jinja2 | Template engine for dynamic post rendering |
| HTML/CSS | Blog layout and post card styling |

---

## Project Structure

```
/
├── app.py                # Flask app, file reader, and markdown converter
├── posts/
│   └── post1.md          # Your blog posts go here
└── template/
    └── index.html        # Jinja2 template with post loop and styling
```

---

## Getting Started

**1. Install dependencies**

```bash
pip install flask markdown
```

**2. Add your posts**

Drop any `.md` files into the `posts/` folder. If it doesn't exist, the app will create it on first run.

**3. Start the server**

```bash
python app.py
```

**4. Open your blog**

Navigate to `http://127.0.0.1:5000` in your browser.

---

## Writing Posts

Posts are written in standard Markdown and converted to HTML automatically on each request. No restart needed — just save your `.md` file and refresh the page.

```markdown
# My Post Title
Some **bold** content and a code block:

```python
print("Hello, World!")
```
```

---

## Features

- Automatic `.md` discovery — drop files in `posts/` and they appear instantly
- Full Markdown support including headers, lists, bold, italics, and code blocks
- Auto-creates the `posts/` folder on first run with a setup prompt
- Clean card-based layout with inline CSS — no external stylesheets needed
- Zero frontend dependencies — pure Flask, Jinja2, and standard Markdown

Thank you for your attention!