import threading
from flask import Flask, request, render_template, redirect, url_for
from prediction import Prediction
app = Flask(__name__)
global free_status
free_status = True
result_ = "Wait for The Result"

class Threading:

    def __init__(self,object,passenger_class,gender,age,fare,p_c_aboard, sibling_aboard):
        self.object = object
        self.passenger_class = passenger_class
        self.age = age
        self.gender = gender
        self.fare = fare
        self.p_c_aboard = p_c_aboard
        self.sibling_aboard = sibling_aboard
        thread = threading.Thread(target=self.thread_main(),args=())
        thread.daemon = True
        thread.start()

    def thread_main(self):
        global free_status
        free_status = False
        threading.Thread(target=self.object.run(passenger_class=self.passenger_class,gender=self.gender,age_p = self.age,siblings_a=self.sibling_aboard,parents_a=self.p_c_aboard,fare_p=self.fare)).start()
        free_status = True

@app.route('/', methods=['POST','GET'])
def home():
    global free_status, obj_pre
    if request.method == 'POST':

        if free_status is not True:
            return "Website is Busy"
        else:
            free_status = True

        passenger_class_  = request.form['p_class']
        gender_ = request.form['gender']
        age_ = request.form['age']
        fare_ = request.form['fare']
        p_c_aboard_ = request.form['p_c_aboard']
        sibling_aboard_ = request.form['s_aboard']
        print(f"passenger_class: {passenger_class_},Gender: {gender_}, age: {age_}, fare: {fare_}, p_c_aboard: {p_c_aboard_}, sibling_aboard: {sibling_aboard_}")
        Threading(object=obj_pre,passenger_class=int(passenger_class_),gender=int(gender_),age=int(age_),fare=int(fare_),p_c_aboard=int(p_c_aboard_), sibling_aboard=int(sibling_aboard_))
        return redirect(url_for('result'))

    else:
        return render_template('index.html')

@app.route('/result', methods=['GET'])
def result():
    global result_
    result_ = obj_pre.result_value
    print(result_)
    if result_ is None:
        return render_template('result.html',result = result_)
    else:
        return render_template('result.html', result=obj_pre.result_value)

if __name__ == "__main__":
    obj_pre = Prediction()
    app.run(port=8000,debug=True)