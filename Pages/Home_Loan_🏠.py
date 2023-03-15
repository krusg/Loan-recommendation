import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 
import random
from PIL import Image
import warnings
warnings.filterwarnings('ignore')

#app=Flask(__name__)
#Swagger(app)

pickle_in = open("../Final/models/nb3.pkl","rb")
classifier=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def predict_note_authentication(Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,
LoanAmount,Loan_Amount_Term,Credit_History,Property_Area):
    
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: variance
        in: query
        type: number
        required: true
      - name: skewness
        in: query
        type: number
        required: true
      - name: curtosis
        in: query
        type: number
        required: true
      - name: entropy
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
    test = pd.read_csv("../Final/Data/test.csv")
    
    Gender=str(Gender)
    Married=str(Married)
    Dependents=str(Dependents)
    Education=str(Education)
    Self_Employed=str(Self_Employed)
    ApplicantIncome=int(ApplicantIncome)
    CoapplicantIncome=int(CoapplicantIncome)
    LoanAmount=float(LoanAmount)
    Loan_Amount_Term=float(Loan_Amount_Term)
    Credit_History=float(Credit_History)
    Property_Area=str(Property_Area)

    a = [1,Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome, 
    LoanAmount,Loan_Amount_Term,Credit_History,Property_Area]
    
    test.loc[len(test)-1]= a

    test['Dependents'].replace('3',3,inplace=True)
    test['Dependents'].replace('3+',3,inplace=True)
    test["Gender"].fillna(test["Gender"].mode()[0],inplace=True)
    test['Dependents'].fillna(test["Dependents"].mode()[0],inplace=True)
    test["Self_Employed"].fillna(test["Self_Employed"].mode()[0],inplace=True)
    test["Loan_Amount_Term"].fillna(test["Loan_Amount_Term"].mode()[0],inplace=True)
    test["Credit_History"].fillna(test["Credit_History"].mode()[0],inplace=True)
    test["LoanAmount"].fillna(test["LoanAmount"].median(),inplace=True)
    test["LoanAmount_log"]=np.log(test["LoanAmount"])

    test["TotalIncome"]=test["ApplicantIncome"]+test["CoapplicantIncome"]

    test["TotalIncome_log"] = np.log(test["TotalIncome"])
    test["EMI"]=test["LoanAmount"]/test["Loan_Amount_Term"]
    test["Balance_Income"] = test["TotalIncome"]-test["EMI"]
    test = test.drop(["ApplicantIncome","CoapplicantIncome","LoanAmount","Loan_Amount_Term"],axis=1)
    test=test.drop("Loan_ID",axis=1)

    test = pd.get_dummies(test)
    print(test.iloc[len(test)-1])
    prediction=classifier.predict([test.iloc[len(test)-1]])
    #print(prediction)
    #print(test.iloc[367])
    return prediction



def main():
    st.title("Bank Authenticator")
    html_temp = """
    <div style="background-color:DimGray;padding:10px">
    <h2 style="color:white;text-align:center;">Home Loan 🏠 </h2>
    </div>
    """
    
    st.markdown(html_temp,unsafe_allow_html=True)

    #Gender = st.text_input("Gender","Type Here")
    Gender = st.selectbox('Gender',('Male', 'Female'))
    
    #Married = st.text_input("Married","Type Here")
    Married = st.selectbox('Married',('Yes', 'No'))

    #Dependents = st.text_input("Dependents","Type Here")
    Dependents = st.selectbox('Dependents',('1', '2' , '3', '3+'))

    #Education = st.text_input("Education","Type Here")
    Education = st.selectbox('Education',('Graduate', 'Not Graduate'))
    
    #Self_Employed = st.text_input("Self_Employed","Type Here")
    Self_Employed = st.selectbox('Self_Employed',('Yes', 'No'))

    ApplicantIncome = st.text_input("ApplicantIncome","Type Here")
    CoapplicantIncome = st.text_input("CoapplicantIncome","Type Here")
    LoanAmount = st.text_input("LoanAmount","Type Here")
    Loan_Amount_Term = st.text_input("Loan_Amount_Term","Type Here")

    #Credit_History = st.text_input("Credit_History","Type Here")
    Credit_History = st.selectbox('Credit_History',('Yes', 'No'))
    if (Credit_History=='Yes'):
        Credit_History= '1'
    else:
        Credit_History='0'

    #Property_Area = st.text_input("Property_Area","Type Here")
    Property_Area = st.selectbox('Property_Area',('Rural', 'Semiurban', 'Urban'))

    result=""
    if st.button("Predict"):
        result=predict_note_authentication(Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome, 
        LoanAmount,Loan_Amount_Term,Credit_History,Property_Area)
        if result==1:
            st.success('Congratulations! You Are Eligible For A Home Loan')
        else:
            st.error('Sorry! You Are Not Eligible For A Home Loan')
            list = ['Please Increase Your Credit Score','Please Build A Good Credit History','Please Lower Your Monthly Debt']
            list2 = ['You Have Too Many Bankruptcies','You Have Too Many TaxLiens','Please Increase Your Annual Income']
            
            st.info(random.choice(list))
            st.info(random.choice(list2))
    df= pd.read_csv('../Final/home_loan_table.csv',index_col=0)
    df = df.drop(df.columns[0],axis=1)
    #st.dataframe(df, 100,1000)
    st.table(df)
        

    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()
    