from flask import Flask, render_template, jsonify
app = Flask('web app')


@app.route('/')
def htmlHomePage():
    return render_template('home_two.html')


# @app.route('/home/two')
# def htmlPageTwo():
#     return render_template('home_two.html')


# @app.route('/')
# def homePage():
#     return 'Hello this is my first flask app.'


# @app.route('/two')
# def secondPage():
#     return "this is page two. Hey !"


# @app.route('/three')
# def thirdPage():
#     return 'This is flask third page route'


# @app.route('/link-link')
# def fourthPage():
#     return 'This is forth page'


# @app.route('/<string:username>/details')
# def userDetails(username):
#     di = {
#         'username': username,
#         'location': 'hyd',
#         'mobileNo': '1234567789'
#     }
#     return jsonify(di)

if __name__ == "__main__":
    app.run(debug=True)
