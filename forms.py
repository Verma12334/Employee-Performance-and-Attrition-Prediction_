import pandas as pd
from flask_wtf import FlaskForm
from wtforms import (
    SelectField,
    IntegerField,
    SubmitField, 
    StringField
)
from wtforms.validators import DataRequired


# getting the data
df = pd.read_csv("dataset/IBM_HR_Employee_Attrition.csv")
X_data = df.drop('Attrition', axis=1)

class InputForm(FlaskForm):
    Age = IntegerField("Age", validators=[DataRequired()])
    BusinessTravel = SelectField("Business Travel", choices=[('Travel_Rarely', 'Travel_Rarely'), ('Travel_Frequently', 'Travel_Frequently'), ('Non-Travel', 'Non-Travel')], validators=[DataRequired()])
    DailyRate = IntegerField("Daily Rate", validators=[DataRequired()])
    Department = SelectField("Department", choices=[('Sales', 'Sales'), ('Research & Development', 'Research & Development'), ('Human Resources', 'Human Resources')], validators=[DataRequired()])
    DistanceFromHome = IntegerField("Distance From Home", validators=[DataRequired()])
    Education = IntegerField("Education", validators=[DataRequired()])
    EducationField = SelectField("Education Field", choices=[('Life Sciences', 'Life Sciences'), ('Medical', 'Medical'), ('Marketing', 'Marketing'), ('Technical Degree', 'Technical Degree'), ('Other', 'Other')], validators=[DataRequired()])
    EmployeeCount = IntegerField("Employee Count", validators=[DataRequired()])
    EmployeeNumber = IntegerField("Employee Number", validators=[DataRequired()])
    EnvironmentSatisfaction = IntegerField("Environment Satisfaction", validators=[DataRequired()])
    Gender = SelectField("Gender", choices=[('Male', 'Male'), ('Female', 'Female')], validators=[DataRequired()])
    HourlyRate = IntegerField("Hourly Rate", validators=[DataRequired()])
    JobInvolvement = IntegerField("Job Involvement", validators=[DataRequired()])
    JobLevel = IntegerField("Job Level", validators=[DataRequired()])
    JobRole = SelectField("Job Role", choices=[('Manager', 'Manager'), ('Research Scientist', 'Research Scientist'), ('Sales Executive', 'Sales Executive'), ('Lab Technician', 'Lab Technician'), ('Manufacturing Director', 'Manufacturing Director')], validators=[DataRequired()])
    JobSatisfaction = IntegerField("Job Satisfaction", validators=[DataRequired()])
    MaritalStatus = SelectField("Marital Status", choices=[('Single', 'Single'), ('Married', 'Married'), ('Divorced', 'Divorced')], validators=[DataRequired()])
    MonthlyIncome = IntegerField("Monthly Income", validators=[DataRequired()])
    MonthlyRate = IntegerField("Monthly Rate", validators=[DataRequired()])
    NumCompaniesWorked = IntegerField("Num Companies Worked", validators=[DataRequired()])
    Over18 = StringField("Over 18", validators=[DataRequired()])
    OverTime = SelectField("Over Time", choices=[('Yes', 'Yes'), ('No', 'No')], validators=[DataRequired()])
    PercentSalaryHike = IntegerField("Percent Salary Hike", validators=[DataRequired()])
    PerformanceRating = IntegerField("Performance Rating", validators=[DataRequired()])
    RelationshipSatisfaction = IntegerField("Relationship Satisfaction", validators=[DataRequired()])
    StandardHours = IntegerField("Standard Hours", validators=[DataRequired()])
    StockOptionLevel = IntegerField("Stock Option Level", validators=[DataRequired()])
    TotalWorkingYears = IntegerField("Total Working Years", validators=[DataRequired()])
    TrainingTimesLastYear = IntegerField("Training Times Last Year", validators=[DataRequired()])
    WorkLifeBalance = IntegerField("Work Life Balance", validators=[DataRequired()])
    YearsAtCompany = IntegerField("Years At Company", validators=[DataRequired()])
    YearsInCurrentRole = IntegerField("Years In Current Role", validators=[DataRequired()])
    YearsSinceLastPromotion = IntegerField("Years Since Last Promotion", validators=[DataRequired()])
    YearsWithCurrManager = IntegerField("Years With Current Manager", validators=[DataRequired()])
    submit = SubmitField("Submit")