import os

# 1. Define the HTML template with CSS styling
html_head = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DSA Visualizations</title>
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; background-color: #0d1117; color: #c9d1d9; margin: 0; padding: 40px; }
        h1 { text-align: center; color: #58a6ff; margin-bottom: 40px; }
        .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 20px; max-width: 1200px; margin: 0 auto; }
        .card { background: #161b22; border: 1px solid #30363d; border-radius: 8px; padding: 20px; text-decoration: none; color: inherit; transition: border-color 0.2s, transform 0.2s; }
        .card:hover { border-color: #58a6ff; transform: translateY(-2px); }
        .topic { font-size: 0.85em; color: #8b949e; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 8px; }
        .title { font-size: 1.2em; font-weight: 600; color: #c9d1d9; margin: 0; }
    </style>
</head>
<body>
    <h1>Interactive DSA Visualizations</h1>
    <div class="grid">
"""

html_tail = """
    </div>
</body>
</html>
"""

# 2. Scan directories and generate cards
cards = ""
for root, dirs, files in os.walk('.'):
    # Ignore hidden folders like .git
    if '.git' in root:
        continue
        
    for file in files:
        if file.endswith('.html') and file != 'index.html':
            # Extract folder name and file path
            folder_name = os.path.basename(root)
            file_path = os.path.join(root, file).replace('./', '').replace('\\', '/')
            display_name = file.replace('.html', '').replace('-', ' ').title()
            
            # Create a clickable card for the visual
            cards += f"""
            <a href="{file_path}" class="card">
                <div class="topic">{folder_name}</div>
                <h3 class="title">{display_name}</h3>
            </a>
            """

# 3. Write the final index.html
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_head + cards + html_tail)

print("Successfully generated index.html!")