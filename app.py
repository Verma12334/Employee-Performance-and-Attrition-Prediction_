import pandas as pd
import pickle
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier

from flask import (
    Flask,
    url_for,
    render_template
)
from forms import InputForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret_key"

# Load the model correctly using 'open' and 'with' statement

with open("model.pkl", "rb") as model_file:
    model = pickle.load(model_file)


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title="Home")


@app.route("/predict", methods=["GET", "POST"])
def predict():
    form = InputForm()
    if form.validate_on_submit():
        x_new = pd.DataFrame(dict(
            Age=[form.Age.data],
            BusinessTravel=[form.BusinessTravel.data],
            DailyRate=[form.DailyRate.data],
            Department=[form.Department.data],
            DistanceFromHome=[form.DistanceFromHome.data],
            Education=[form.Education.data],
            EducationField=[form.EducationField.data],
            EmployeeCount=[form.EmployeeCount.data],
            EmployeeNumber=[form.EmployeeNumber.data],
            EnvironmentSatisfaction=[form.EnvironmentSatisfaction.data],
            Gender=[form.Gender.data],
            HourlyRate=[form.HourlyRate.data],
            JobInvolvement=[form.JobInvolvement.data],
            JobLevel=[form.JobLevel.data],
            JobRole=[form.JobRole.data],
            JobSatisfaction=[form.JobSatisfaction.data],
            MaritalStatus=[form.MaritalStatus.data],
            MonthlyIncome=[form.MonthlyIncome.data],
            MonthlyRate=[form.MonthlyRate.data],
            NumCompaniesWorked=[form.NumCompaniesWorked.data],
            Over18=[form.Over18.data],
            OverTime=[form.OverTime.data],
            PercentSalaryHike=[form.PercentSalaryHike.data],
            PerformanceRating=[form.PerformanceRating.data],
            RelationshipSatisfaction=[form.RelationshipSatisfaction.data],
            StandardHours=[form.StandardHours.data],
            StockOptionLevel=[form.StockOptionLevel.data],
            TotalWorkingYears=[form.TotalWorkingYears.data],
            TrainingTimesLastYear=[form.TrainingTimesLastYear.data],
            WorkLifeBalance=[form.WorkLifeBalance.data],
            YearsAtCompany=[form.YearsAtCompany.data],
            YearsInCurrentRole=[form.YearsInCurrentRole.data],
            YearsSinceLastPromotion=[form.YearsSinceLastPromotion.data],
            YearsWithCurrManager=[form.YearsWithCurrManager.data],
        ))
        input_arr = []
        j = 1
        for i in x_new.iloc[0]:
            if isinstance(i, str):
                with open(f"label{j}.pkl", "rb") as label_file:
                    label = pickle.load(label_file)
                try:
                    i = label.transform([i])[0]
                except ValueError:
                    # Handle unseen labels by assigning a special value or skipping
                    i = -1  # Assign a special value for unseen labels
                j += 1
            input_arr.append(i)

        input_array = np.array([input_arr])

        prediction = model.predict(input_array)

        if prediction[0] == 1:
            message = "Employee will not leave the job !"
        else:
            message = "Employee will leave the job !"

       # message = f"The predicted Attrition is {prediction[0]} "
    else:
        message = "Please provide valid input details!"

    return render_template("predict.html", title="Predict", form=form, output=message)



if __name__ == "__main__":
    app.run(debug=True)
