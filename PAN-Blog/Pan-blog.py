from flask import Flask,request,render_template
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def hello_world():
    if request.method=='GET':
        return render_template('index.html')
    elif request.method=='POST':
        print(request.args.to_dict())
        return 'POST'
    

# @app.route('/login',methods=['GET','POST'])
# def login():
#     if request.method=='POST':
#         print('aaa')
#     else:
#         return render_template('test.html')
#     return 'OK'

if __name__ == '__main__':
    app.run(debug=True)