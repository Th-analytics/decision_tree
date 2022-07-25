import pickle
import sklearn

class Prediction:

    def __init__(self):
        self.result_value = None
        self.model_file = None

    def get_model(self):
        """
        Method to get Model File for the prediction task
        :return:
        """
        """
        In order to rebuild a similar model with future versions of scikit-learn, additional metadata should be saved along the pickled model:

The training data, e.g. a reference to an immutable snapshot

The python source code used to generate the model

The versions of scikit-learn and its dependencies

The cross validation score obtained on the training data
        """

        try:
            with open('model/decision_tree_model.pickle','rb') as file_read:
                self.model_file = pickle.load(file_read)
        except Exception as e:
            print("Error in get_model of Prediction: ",e)

    def predict(self,p_class,sex,age,sib_Aboard,pc_aboard,fare):
        # Pclass	Sex	Age	SiblingsAboard	Parn/chldrnAboard	Fare
        """

        :param p_class: Passenger Class Variable
        :param sex: Gender of the Passenger 0- Female, 1- Male
        :param age: Age of the passenger
        :param sib_Aboard: Sibling on board
        :param pc_aboard: Parents or children Onboard
        :param fare: Fare
        :return: chances of Survival 0- No chance 1- High Chance of Survival.
        """
        try:
            self.get_model()
            prediction_class = self.model_file.predict([[p_class,sex,age,sib_Aboard,pc_aboard,fare]])
            return prediction_class[0]
        except Exception as e:
            print("Error in Predict Method of Prediction Class: ",e)
            return None

    def run(self,passenger_class,gender,age_p,siblings_a,parents_a,fare_p):
        """
        This Method is used to call the predict method of Prediction Class .
        :return: Predicted Outcome
        """
        try:
            print(passenger_class,gender,age_p,siblings_a,parents_a,fare_p)
            value = self.predict(p_class=passenger_class,sex=gender,age=age_p,sib_Aboard=siblings_a,pc_aboard=parents_a,fare=fare_p)
            if value == 0:
                self.result_value = "No Survival Chance"
            elif value == 1:
                self.result_value = "Survived "
            else:
                self.result_value = None
        except Exception as e:
            print("Error in run of Prediction class:",e)
"""
if __name__=="__main__":
    obj = Prediction()
    print(obj.run(passenger_class=3,gender=1,age_p=22,siblings_a=1,parents_a=0,fare_p=7.25))


"""