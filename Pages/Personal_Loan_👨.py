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

pickle_in = open("C:/Users/krushan/Desktop/rohan/Final/models/nb1.pkl","rb")
classifier=pickle.load(pickle_in)
print(classifier.feature_names_in_) 
#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def predict_note_authentication(Income, Age, Experience, Married_Single, House_Ownership,
       Car_Ownership, CURRENT_JOB_YRS, CURRENT_HOUSE_YRS, Profession_count,
       CITY_count,STATE_count):
    
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
   
    prediction=classifier.predict([[Income, Age, Experience, Married_Single, House_Ownership,
       Car_Ownership, CURRENT_JOB_YRS, CURRENT_HOUSE_YRS, Profession_count,
       CITY_count,STATE_count]])
    return prediction



def main():
    
    html_t = """
    <div style="background-color:DimGray;padding:10px">
    <h2 style="color:white;text-align:center;">How You Can Increase Your Chances Of Getting A Personal Loan 👨</h2>
    </div>
    <div>
    <p>Personal loans are availed by
individuals and used for various
purposes such as home renovation, from
renovating your house, going on an
international vacation, to debt
consolidation. They are usually
unsecured, meaning you do not have to
provide collateral, making them an
attractive financing option for
customers. However, the risk for
lenders is higher, and therefore
personal loan interest
rates also tend to be high.
Moreover, getting approval for personal
loans may be difficult.</p>
<p>Here are a few steps you can take to
increase your chances of getting a
personal loan.</p>
<h2>1. Check your credit score before
you apply</h2>
<p>Your credit score is a measure of
your ability to repay the loan.
Therefore, the higher your credit
score, the better your chances of
approval. Ideally, it would help if you
had a credit score of above 750 to get
approved easily. If you have a lower
score, it is better to wait and improve
before you approach any bank or NBFC
with a personal loan application.
You can improve your credit by paying
off your existing debt, paying all your
bills on time, not maxing out your
credit cards, etc.</p>
<h2>2. Do not make multiple loan
applications</h2>
<p>Avoid making multiple loan
applications to different lenders,
hoping to get approved by at least one
of them. This makes you seem desperate
for credit, which gives the wrong
impression that you need more than one
loan to meet your expenses.
Additionally, if you do not get
approved for these loans, your credit
score reduces, making it very hard to
get approved for any credit.</p>
<h2>3. Have a gap of a minimum of 6
months between loan applications</h2>
<p>It is better to have a gap of at
least 6 months between your loan
applications. Your lender will
otherwise doubt your ability to repay
the loan. If your reason to avail the
personal loan is non-urgent, wait a few
months before you apply to have a
better chance of being approved.</p>
<h2>4. Choose your lender
carefully</h2>
<p>It is essential that you do your
homework and compares loans before you
choose your lender. Even if you must
select a lender that specializes in
high-risk borrowers due to your poor
credit score, you need to be careful.
Avoid payday and title loans at all
costs. These loans are designed to keep
you in permanent debt with their
ridiculously high fees. Avoid any offer
that seems too good to be true.</p>
<h2>5. Be careful of your
debt-to-income ratio</h2>
<p>Ideally, you should not be spending
more than 40% of your income toward
EMIs. So, if you earn Rs. 25,000 a
month, you should not be paying more
than Rs. 10,000 for your EMIs. Your
monthly debt divided by your gross
monthly income is your debt-to-income
ratio. It would be best to keep this as
low as possible, meaning do not borrow
money unless necessary. Lenders won’t
approve loans that you cannot afford
anyway.</p>
<p>Lastly, searching and applying
online for a personal loan may ease the
application process and speed up the
approval.<br>
&nbsp;</p>
    </div>
    """
    st.markdown(html_t,unsafe_allow_html=True)
    st.title("Bank Authenticator")
    html_temp = """
    <div style="background-color:DimGray;padding:10px">
    <h2 style="color:white;text-align:center;">Personal Loan 👨</h2>
    
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    #ID = st.text_input("ID","Type Here")
    
    Income = st.text_input("Income","Type Here")
    Age = st.text_input("Age","Type Here")
    Experience = st.text_input("Experience","Type Here")
    
    #Married_Single = st.text_input("Married_Single","Type Here")
    Married_Single = st.selectbox('Married',('Yes', 'No'))
    if (Married_Single=='Yes'):
        Married_Single= '1'
    else:
        Married_Single='0'

    
    #House_Ownership = st.text_input("House_Ownership","Type Here")
    House_Ownership = st.selectbox('Do you own a House?',('Yes', 'No'))
    if (House_Ownership=='Yes'):
        House_Ownership= '1'
    else:
        House_Ownership='0'

    #Car_Ownership = st.text_input("Car_Ownership","Type Here")
    Car_Ownership = st.selectbox('Do you own a Car?',('Yes', 'No'))
    if (Car_Ownership=='Yes'):
        Car_Ownership= '1'
    else:
        Car_Ownership='0'
    


    CURRENT_JOB_YRS = st.text_input("CURRENT_JOB_YRS","Type Here")
    CURRENT_HOUSE_YRS = st.text_input("CURRENT_HOUSE_YRS","Type Here")
    Profession_count = st.text_input("Profession_count","Type Here")
    CITY_count = st.text_input("CITY_count","Type Here")
    STATE_count = st.text_input("STATE_count","Type Here")
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(Income, Age, Experience, Married_Single, House_Ownership,
       Car_Ownership, CURRENT_JOB_YRS, CURRENT_HOUSE_YRS, Profession_count,
       CITY_count,STATE_count)
        if result==1:
            st.success('Congratulations! You Are Eligible For A Personal Loan')
        else:
            st.error('Sorry! You Are Not Eligible For A Personal Loan')
            list = ['Please Increase Your Credit Score','Please Build A Good Credit History','Please Lower Your Monthly Debt']
            list2 = ['You Have Too Many Bankruptcies','You Have Too Many TaxLiens','Please Increase Your Annual Income']
            
            st.info(random.choice(list))
            st.info(random.choice(list2))
 
    #st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        if result==1:
            st.success('Congratulations! You Are Eligible For A Personal Loan')
        else:
            st.success('Sorry! You Are Not Eligible For A Personal Loan')
    df= pd.read_csv('C:/Users/krushan/Desktop/rohan/Final/personal_loan_table.csv',index_col=0)
    df = df.drop(df.columns[0],axis=1)
    #st.dataframe(df, 100,1000)
    st.table(df)
    

if __name__=='__main__':
    main()
    


