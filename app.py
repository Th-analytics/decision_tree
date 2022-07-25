import threading
from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)
global free_status
free_status = True
class Threading:

    def __init__(self):
        thread = threading.Thread(target=self.thread_main(),args=())
        thread.daemon = True
        thread.start()

    def thread_main(self):
        global free_status
        free_status = False
        #thread = threading.Thread(target=,args=)


@app.route('/', methods=['POST','GET'])
def home():
    global free_status
    if request.method == 'POST':

        if free_status is not True:
            return "Website is Busy"
        else:
            free_status = True

        passenger_class  = request.form['p_class']
        age = request.form['age']
        fare = request.form['fare']
        p_c_aboard = request.form['p_c_aboard']
        sibling_aboard = request.form['s_aboard']
        print(f"passenger_class: {passenger_class}, age: {age}, fare: {fare}, p_c_aboard: {p_c_aboard}, sibling_aboard: {sibling_aboard}")
        return redirect(url_for('result'))

    else:
        return render_template('index.html')

@app.route('/result', methods=['GET'])
def result():
    return render_template('result.html')

if __name__ == "__main__":
    app.run(port=8000,debug=True)