from flask import Flask, render_template, request, redirect, url_for

application = Flask(__name__)
posts = {
    0: {
        'post_id': 0,
        'title': 'Hello, world',
        'content': 'This is my first blog post!'
    }
}


@application.route('/')
def home():
    return render_template('home.jinja2', posts = posts)


@application.route('/post/<int:post_id>')
def post(post_id):
    """
    This function renders a template from the `templates` folder in the directory of app.py.
    It will find the `post.jinja2` template and render it with the data passed in.
    Look at `post.jinja2` for information on how the variable `post` gets used there.
    """
    posted = posts.get(post_id)
    if not posted:  # post will be None if not found; not None => True
        return render_template('404.jinja2', message=f'A post with id {post_id} was not found.')
    return render_template('post.jinja2', post=posted)

'''
Creates a hidden payload. Uses method = "POST"
then the decorator needs the methods = ['POST']
in order to understand it's getting something secert
can only be gotten in a post request. A git requests leads 
'''


@application.route('/post/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form.get('title')# Creates a hidden payload. Uses method= "POST"
        content = request.form.get('content')
        post_id = len(posts)
        posts[post_id] = {'id': post_id, 'title': title, 'content': content}
        return redirect(url_for('post', post_id=post_id))
    return render_template('create.jinja2')



if __name__ == '__main__':
    application.run(debug=True)
