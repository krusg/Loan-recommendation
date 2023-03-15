import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 
from sklearn.preprocessing import MinMaxScaler
from PIL import Image
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode
import random
import warnings
warnings.filterwarnings('ignore')

#app=Flask(__name__)
#Swagger(app)

pickle_in = open("./Final/models/nb2.pkl","rb")
classifier=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def predict_note_authentication(CarLoanAmount,Term,CreditScore,AnnualIncome,MonthlyDebt,YearsofCreditHistory,Monthssincelastdelinquent,
NumberofOpenAccounts,NumberofCreditProblems,
CurrentCreditBalance,MaximumOpenCredit,Bankruptcies,TaxLiens):
    
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
    dataframe = pd.read_csv("./Final/Data/CarLoan_Dataset.csv")
    
    CarLoanAmount=int(CarLoanAmount)
    Term=str(Term)
    CreditScore=float(CreditScore)
    AnnualIncome=float(AnnualIncome)
    MonthlyDebt=float(MonthlyDebt)
    YearsofCreditHistory=float(YearsofCreditHistory)

    Monthssincelastdelinquent=float(Monthssincelastdelinquent)
    NumberofOpenAccounts=int(NumberofOpenAccounts)
    NumberofCreditProblems=int(NumberofCreditProblems)
    CurrentCreditBalance=int(CurrentCreditBalance)
    MaximumOpenCredit=int(MaximumOpenCredit)
    Bankruptcies=float(Bankruptcies)
    TaxLiens=float(TaxLiens)
    

    a = ["14dd8831","981165ec","Fully Paid",CarLoanAmount,Term,CreditScore,AnnualIncome,MonthlyDebt,YearsofCreditHistory,Monthssincelastdelinquent,
    NumberofOpenAccounts,NumberofCreditProblems,
     CurrentCreditBalance,MaximumOpenCredit,Bankruptcies,TaxLiens]
     
    dataframe.loc[len(dataframe)-1]= a
    
    dataframe['Tax Liens'] = dataframe['Tax Liens'].fillna(0)
    dataframe['Bankruptcies'] = dataframe['Bankruptcies'].fillna(0)
    dataframe.loc[dataframe['Months since last delinquent'].isnull(),'Months since last delinquent'] = 240
    dataframe['Months since last delinquent'] = dataframe['Months since last delinquent'] - 240
    dataframe.loc[dataframe['Credit Score'].isnull(),'Credit Score'] = 0
    dataframe.loc[dataframe['Annual Income'].isnull(),'Annual Income'] = 0
    dataframe = dataframe.dropna()
    dataframe.loc[dataframe['Credit Score']>850, ['Credit Score']] = (dataframe.loc[dataframe['Credit Score']>850, ['Credit Score']])/10
    dataframe = dataframe.loc[dataframe['Car Loan Amount']!=99999999]
    Continuous = ['CarLoan Status', 'Car Loan Amount', 'Credit Score', 'Annual Income', 'Monthly Debt', 'Years of Credit History', 'Months since last delinquent', 'Number of Open Accounts', 'Number of Credit Problems', 'Current Credit Balance', 'Maximum Open Credit', 'Bankruptcies', 'Tax Liens']
    Category = ['CarLoan Status', 'Term']
    Continuous.remove('CarLoan Status')
    Category.remove('CarLoan Status')
    scale = MinMaxScaler().fit(dataframe[Continuous])
    scaled_dataframe = pd.DataFrame(scale.transform(dataframe[Continuous]), columns= Continuous, index= dataframe.index)
    df_dummies = pd.get_dummies(dataframe[Category], drop_first= True)
    findataframe = pd.concat([scaled_dataframe, df_dummies], axis= 1)
    target = dataframe['CarLoan Status']
    target = target.replace('Fully Paid', 1)
    target = target.replace('Charged Off', 0)
    
    prediction=classifier.predict([findataframe.iloc[len(findataframe)-1]])
    print(prediction)
    
    return prediction



def main():
    html_t = """
    <div style="background-color:DimGray;padding:10px">
    <h2 style="color:white;text-align:center;">How To Improve Chances Of Getting Car Loan 🚗?</h2>
    </div>
    <p>Applying for a Car Loan can be an overwhelming experience, especially if you are buying your first car. Follow these seven simple steps and improve your chance of getting the Car Loan you want.&nbsp;<br>
    <br><h2>1: Pay your debts on time&nbsp;</h2><br>
    <br>All banks like customers who pay their dues on time. If you already have a loan, such as a Home Loan or Personal Loan, make sure you pay your EMIs on time. Same goes for your Credit Card bill.&nbsp;<br>
    <br>Not only will you avoid high penalties, but this clean record will also help convince your bank that you are credit-worthy and likely to pay your instalments on schedule.&nbsp;<br>
    <br><h2>2: Improve your credit score&nbsp;</h2><br><br>If you have a low credit score (such as the CIBIL score), you can fix it by ensuring you have closed previous loans and by addressing any errors in the report.&nbsp;<br>
    <br>Meanwhile, use the credit limit on your Credit Card prudently. In fact, a good practice would be to ask your Credit Card company to increase your credit limit. This may have a positive impact on your score.&nbsp;&nbsp;<br>
    <br><h2>3: Research eligibility criteria&nbsp;</h2><br>
    <br>Each bank has its own eligibility criteria for Car Loans, such as minimum income requirements and maximum loan amount.<br><br>Study the criteria of various banks and ensure you are the right match for the type of applicant they want.&nbsp;<br>
    <br><br><h2>4: Arrange down payment and documents</h2><br><br>Some banks expect you to pay around 15 to 20 percent of your car’s value, while they finance the rest.&nbsp;<br><br>Make sure you have the funds in place before you apply. CredCare Bank Car Loan comes with 100% finance on new cars, so you don’t have to worry about down payment.<br><br>Refer to the bank’s website for the list of required documents and keep them ready. This will decrease chances of your application being rejected. &nbsp;<br><br>Check Documentation for a Car Loan from CredCare Bank<br><br>If you want to prepay your Car Loan, you can read more here.<br><br><h2>5: Buy a car from a reputed dealer</h2><br><br>Many dealers have tie-ups with banks and getting an auto loan will be easier if you buy from an outlet that has a tie-up with your bank.&nbsp;<br><br><h2>6: Apply to your existing bank</h2><br><br>If you already hold an account, it is much easier to convince the bank to give you a loan, because they are already familiar with your credit-worthiness. CredCare Bank offers select pre - approved customers instant loans with minimal documentation.<br><br>To research and compare cars and seamlessly apply for a hassle-free loan, visit the car portal of CredCare Bank.<br><br>Apply for an CredCare Bank Car Loan here now!<br><br><em>* Terms &amp; conditions apply. Car Loan disbursal at sole discretion of CredCare Bank Ltd.</em>&nbsp;<em>The information provided in this article is generic in nature and for informational purposes only. It is not a substitute for specific advice in your own circumstances.</em></p>
    """
    st.markdown(html_t,unsafe_allow_html=True)
    st.title("Bank Authenticator")
    html_temp = """
    <div style="background-color:DimGray;padding:10px">
    <h2 style="color:white;text-align:center;">Car Loan 🚗</h2>
    </div>
    """
    
    st.markdown(html_temp,unsafe_allow_html=True)
    CarLoanAmount = st.text_input("Car Loan Amount","Type Here")

    #Term = st.text_input("Term","Type Here")
    Term = st.selectbox('Term',('Short Term', 'Long Term'))


    CreditScore = st.text_input("Credit Score","Type Here")
    AnnualIncome = st.text_input("Annual Income","Type Here")
    MonthlyDebt = st.text_input("Monthly Debt","Type Here")
    YearsofCreditHistory = st.text_input("Years of Credit History","Type Here")
    Monthssincelastdelinquent = st.text_input("Months since last delinquent","Type Here")
    NumberofOpenAccounts = st.text_input("Number of Open Accounts","Type Here")

    #NumberofCreditProblems = st.text_input("Number of Credit Problems","Type Here")
    NumberofCreditProblems = st.selectbox('Number of Credit Problems',('0', '1','2','3','4','5','6','7'))

    CurrentCreditBalance = st.text_input("Current Credit Balance","Type Here")
    MaximumOpenCredit = st.text_input("Maximum Open Credit","Type Here")

    #Bankruptcies = st.text_input("Bankruptcies","Type Here")
    Bankruptcies = st.selectbox('Bankruptcies',('0', '1','2','3','4','5'))

    #TaxLiens = st.text_input("TaxLiens","Type Here")
    TaxLiens = st.selectbox('TaxLiens',('0', '1','2','3','4','5','6'))
    
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(CarLoanAmount,Term,CreditScore,AnnualIncome,MonthlyDebt,YearsofCreditHistory,Monthssincelastdelinquent,
        NumberofOpenAccounts,NumberofCreditProblems,
        CurrentCreditBalance,MaximumOpenCredit,Bankruptcies,TaxLiens)
        #st.success('The output is {}'.format(result))
        if result==1:
            st.success('Congratulations! You Are Eligible For A Car Loan')
        else:
            list = ['Please Increase Your Credit Score','Please Build A Good Credit History','Please Lower Your Monthly Debt']
            list2 = ['You Have Too Many Bankruptcies','You Have Too Many TaxLiens','Please Increase Your Annual Income']
            st.error('Sorry! You Are Not Eligible For A Car Loan')
            st.info(random.choice(list))
            st.info(random.choice(list2))
            
    if st.button("About"):
        st.text("Lets LEarn")
        
    df= pd.read_csv('./Final/car_loan_table.csv',index_col=0)
    df = df.drop(df.columns[0],axis=1)
    #st.dataframe(df, 100,1000)
    st.table(df)
    #AgGrid(df,fit_columns_on_grid_load=True,width = '100%')



if __name__=='__main__':
    main()
    