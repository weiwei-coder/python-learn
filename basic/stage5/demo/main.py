from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 简易数据库 (实际项目中应使用真实数据库)
posts = []

@app.route('/')
def home():
    return render_template('home.html', posts=posts)

@app.route('/post', methods=['GET', 'POST'])
def create_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        posts.append({'title': title, 'content': content})
        return redirect(url_for('home'))
    return render_template('create_post.html')

if __name__ == '__main__':
    app.run(debug=True)