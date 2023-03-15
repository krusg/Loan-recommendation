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

pickle_in = open("../Final/models/nb1.pkl","rb")
classifier=pickle.load(pickle_in) 
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
    LoanAmount = st.text_input("Loan Amount","Type Here")
    
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

    Profession_count = st.selectbox("Profession",('Mechanical_engineer', 'Software_Developer', 'Technical_writer',
       'Civil_servant', 'Librarian', 'Economist', 'Flight_attendant',
       'Architect', 'Designer', 'Physician', 'Financial_Analyst',
       'Air_traffic_controller', 'Politician', 'Police_officer', 'Artist',
       'Surveyor', 'Design_Engineer', 'Chemical_engineer',
       'Hotel_Manager', 'Dentist', 'Comedian', 'Biomedical_Engineer',
       'Graphic_Designer', 'Computer_hardware_engineer',
       'Petroleum_Engineer', 'Secretary', 'Computer_operator',
       'Chartered_Accountant', 'Technician', 'Microbiologist',
       'Fashion_Designer', 'Aviator', 'Psychologist', 'Magistrate',
       'Lawyer', 'Firefighter', 'Engineer', 'Official', 'Analyst',
       'Geologist', 'Drafter', 'Statistician', 'Web_designer',
       'Consultant', 'Chef', 'Army_officer', 'Surgeon', 'Scientist',
       'Civil_engineer', 'Industrial_Engineer', 'Technology_specialist'))
    e = ['Mechanical_engineer', 'Software_Developer', 'Technical_writer',
       'Civil_servant', 'Librarian', 'Economist', 'Flight_attendant',
       'Architect', 'Designer', 'Physician', 'Financial_Analyst',
       'Air_traffic_controller', 'Politician', 'Police_officer', 'Artist',
       'Surveyor', 'Design_Engineer', 'Chemical_engineer',
       'Hotel_Manager', 'Dentist', 'Comedian', 'Biomedical_Engineer',
       'Graphic_Designer', 'Computer_hardware_engineer',
       'Petroleum_Engineer', 'Secretary', 'Computer_operator',
       'Chartered_Accountant', 'Technician', 'Microbiologist',
       'Fashion_Designer', 'Aviator', 'Psychologist', 'Magistrate',
       'Lawyer', 'Firefighter', 'Engineer', 'Official', 'Analyst',
       'Geologist', 'Drafter', 'Statistician', 'Web_designer',
       'Consultant', 'Chef', 'Army_officer', 'Surgeon', 'Scientist',
       'Civil_engineer', 'Industrial_Engineer', 'Technology_specialist']
    Profession_count = e.index(Profession_count)
    f = [ 5217, 5053, 5195, 4413, 4628, 4573, 5128, 4657, 4598, 5957, 5167,
       5281, 4944, 5035, 4861, 4714, 4729, 5205, 5178, 4782, 5259, 5127,
       5166, 5372, 5041, 5061, 4990, 4493, 4864, 4881, 5304, 4758, 5390,
       5357, 4818, 4507, 4048, 4087, 4668, 4672, 5359, 5806, 5397, 4808,
       4635, 4661, 4772, 4781, 4616, 5250, 4737]
    Profession_count = f[Profession_count]

    CITY_count = st.selectbox("CITY",('Rewa', 'Parbhani', 'Alappuzha', 'Bhubaneswar',
       'Tiruchirappalli[10]', 'Jalgaon', 'Tiruppur', 'Jamnagar',
       'Kota[6]', 'Karimnagar', 'Hajipur[31]', 'Adoni', 'Erode[17]',
       'Kollam', 'Madurai', 'Anantapuram[24]', 'Kamarhati', 'Bhusawal',
       'Sirsa', 'Amaravati', 'Secunderabad', 'Ahmedabad', 'Ajmer',
       'Ongole', 'Miryalaguda', 'Ambattur', 'Indore', 'Pondicherry',
       'Shimoga', 'Chennai', 'Gulbarga', 'Khammam', 'Saharanpur',
       'Gopalpur', 'Amravati', 'Udupi', 'Howrah', 'Aurangabad[39]',
       'Hospet', 'Shimla', 'Khandwa', 'Bidhannagar', 'Bellary', 'Danapur',
       'Purnia[26]', 'Bijapur', 'Patiala', 'Malda', 'Sagar', 'Durgapur',
       'Junagadh', 'Singrauli', 'Agartala', 'Thanjavur', 'Hindupur',
       'Naihati', 'North_Dumdum', 'Panchkula', 'Anantapur', 'Serampore',
       'Bathinda', 'Nadiad', 'Kanpur', 'Haridwar', 'Berhampur',
       'Jamshedpur', 'Hyderabad', 'Bidar', 'Kottayam', 'Solapur',
       'Suryapet', 'Aizawl', 'Asansol', 'Deoghar', 'Eluru[25]',
       'Ulhasnagar', 'Aligarh', 'South_Dumdum', 'Berhampore',
       'Gandhinagar', 'Sonipat', 'Muzaffarpur', 'Raichur',
       'Rajpur_Sonarpur', 'Ambarnath', 'Katihar', 'Kozhikode', 'Vellore',
       'Malegaon', 'Kochi', 'Nagaon', 'Nagpur', 'Srinagar', 'Davanagere',
       'Bhagalpur', 'Siwan[32]', 'Meerut', 'Dindigul', 'Bhatpara',
       'Ghaziabad', 'Kulti', 'Chapra', 'Dibrugarh', 'Panihati',
       'Bhiwandi', 'Morbi', 'Kalyan-Dombivli', 'Gorakhpur', 'Panvel',
       'Siliguri', 'Bongaigaon', 'Patna', 'Ramgarh', 'Ozhukarai',
       'Mirzapur', 'Akola', 'Satna', 'Motihari[34]', 'Jalna', 'Jalandhar',
       'Unnao', 'Karnal', 'Cuttack', 'Proddatur', 'Ichalkaranji',
       'Warangal[11][12]', 'Jhansi', 'Bulandshahr', 'Narasaraopet',
       'Chinsurah', 'Jehanabad[38]', 'Dhanbad', 'Gudivada', 'Gandhidham',
       'Raiganj', 'Kishanganj[35]', 'Varanasi', 'Belgaum',
       'Tirupati[21][22]', 'Tumkur', 'Coimbatore', 'Kurnool[18]',
       'Gurgaon', 'Muzaffarnagar', 'Aurangabad', 'Bhavnagar', 'Arrah',
       'Munger', 'Tirunelveli', 'Mumbai', 'Mango', 'Nashik', 'Kadapa[23]',
       'Amritsar', 'Khora,_Ghaziabad', 'Ambala', 'Agra', 'Ratlam',
       'Surendranagar_Dudhrej', 'Delhi_city', 'Bhopal', 'Hapur', 'Rohtak',
       'Durg', 'Korba', 'Bangalore', 'Shivpuri', 'Thrissur',
       'Vijayanagaram', 'Farrukhabad', 'Nangloi_Jat', 'Madanapalle',
       'Thoothukudi', 'Nagercoil', 'Gaya', 'Chandigarh_city', 'Jammu[16]',
       'Kakinada', 'Dewas', 'Bhalswa_Jahangir_Pur', 'Baranagar',
       'Firozabad', 'Phusro', 'Allahabad', 'Guna', 'Thane', 'Etawah',
       'Vasai-Virar', 'Pallavaram', 'Morena', 'Ballia', 'Surat',
       'Burhanpur', 'Phagwara', 'Mau', 'Mangalore', 'Alwar',
       'Mahbubnagar', 'Maheshtala', 'Hazaribagh', 'Bihar_Sharif',
       'Faridabad', 'Lucknow', 'Tenali', 'Barasat', 'Amroha', 'Giridih',
       'Begusarai', 'Medininagar', 'Rajahmundry[19][20]', 'Saharsa[29]',
       'New_Delhi', 'Bhilai', 'Moradabad', 'Machilipatnam',
       'Mira-Bhayandar', 'Pali', 'Navi_Mumbai', 'Mehsana', 'Imphal',
       'Kolkata', 'Sambalpur', 'Ujjain', 'Madhyamgram', 'Jabalpur',
       'Jamalpur[36]', 'Ludhiana', 'Bareilly', 'Gangtok', 'Anand',
       'Dehradun', 'Pune', 'Satara', 'Srikakulam', 'Raipur', 'Jodhpur',
       'Darbhanga', 'Nizamabad', 'Nandyal', 'Dehri[30]', 'Jorhat',
       'Ranchi', 'Kumbakonam', 'Guntakal', 'Haldia', 'Loni',
       'Pimpri-Chinchwad', 'Rajkot', 'Nanded', 'Noida',
       'Kirari_Suleman_Nagar', 'Jaunpur', 'Bilaspur', 'Sambhal', 'Dhule',
       'Rourkela', 'Thiruvananthapuram', 'Dharmavaram', 'Nellore[14][15]',
       'Visakhapatnam[4]', 'Karawal_Nagar', 'Jaipur', 'Avadi',
       'Bhimavaram', 'Bardhaman', 'Silchar', 'Buxar[37]', 'Kavali',
       'Tezpur', 'Ramagundam[27]', 'Yamunanagar', 'Sri_Ganganagar',
       'Sasaram[30]', 'Sikar', 'Bally', 'Bhiwani', 'Rampur', 'Uluberia',
       'Sangli-Miraj_&_Kupwad', 'Hosur', 'Bikaner', 'Shahjahanpur',
       'Sultan_Pur_Majra', 'Vijayawada', 'Bharatpur', 'Tadepalligudem',
       'Tinsukia', 'Salem', 'Mathura', 'Guntur[13]', 'Hubliâ€“Dharwad',
       'Guwahati', 'Chittoor[28]', 'Tiruvottiyur', 'Vadodara',
       'Ahmednagar', 'Fatehpur', 'Bhilwara', 'Kharagpur', 'Bettiah[33]',
       'Bhind', 'Bokaro', 'Karaikudi', 'Raebareli', 'Pudukkottai',
       'Udaipur', 'Mysore[7][8][9]', 'Panipat', 'Latur', 'Tadipatri',
       'Bahraich', 'Orai', 'Raurkela_Industrial_Township', 'Gwalior',
       'Katni', 'Chandrapur', 'Kolhapur'))
    a = ['Rewa', 'Parbhani', 'Alappuzha', 'Bhubaneswar',
       'Tiruchirappalli[10]', 'Jalgaon', 'Tiruppur', 'Jamnagar',
       'Kota[6]', 'Karimnagar', 'Hajipur[31]', 'Adoni', 'Erode[17]',
       'Kollam', 'Madurai', 'Anantapuram[24]', 'Kamarhati', 'Bhusawal',
       'Sirsa', 'Amaravati', 'Secunderabad', 'Ahmedabad', 'Ajmer',
       'Ongole', 'Miryalaguda', 'Ambattur', 'Indore', 'Pondicherry',
       'Shimoga', 'Chennai', 'Gulbarga', 'Khammam', 'Saharanpur',
       'Gopalpur', 'Amravati', 'Udupi', 'Howrah', 'Aurangabad[39]',
       'Hospet', 'Shimla', 'Khandwa', 'Bidhannagar', 'Bellary', 'Danapur',
       'Purnia[26]', 'Bijapur', 'Patiala', 'Malda', 'Sagar', 'Durgapur',
       'Junagadh', 'Singrauli', 'Agartala', 'Thanjavur', 'Hindupur',
       'Naihati', 'North_Dumdum', 'Panchkula', 'Anantapur', 'Serampore',
       'Bathinda', 'Nadiad', 'Kanpur', 'Haridwar', 'Berhampur',
       'Jamshedpur', 'Hyderabad', 'Bidar', 'Kottayam', 'Solapur',
       'Suryapet', 'Aizawl', 'Asansol', 'Deoghar', 'Eluru[25]',
       'Ulhasnagar', 'Aligarh', 'South_Dumdum', 'Berhampore',
       'Gandhinagar', 'Sonipat', 'Muzaffarpur', 'Raichur',
       'Rajpur_Sonarpur', 'Ambarnath', 'Katihar', 'Kozhikode', 'Vellore',
       'Malegaon', 'Kochi', 'Nagaon', 'Nagpur', 'Srinagar', 'Davanagere',
       'Bhagalpur', 'Siwan[32]', 'Meerut', 'Dindigul', 'Bhatpara',
       'Ghaziabad', 'Kulti', 'Chapra', 'Dibrugarh', 'Panihati',
       'Bhiwandi', 'Morbi', 'Kalyan-Dombivli', 'Gorakhpur', 'Panvel',
       'Siliguri', 'Bongaigaon', 'Patna', 'Ramgarh', 'Ozhukarai',
       'Mirzapur', 'Akola', 'Satna', 'Motihari[34]', 'Jalna', 'Jalandhar',
       'Unnao', 'Karnal', 'Cuttack', 'Proddatur', 'Ichalkaranji',
       'Warangal[11][12]', 'Jhansi', 'Bulandshahr', 'Narasaraopet',
       'Chinsurah', 'Jehanabad[38]', 'Dhanbad', 'Gudivada', 'Gandhidham',
       'Raiganj', 'Kishanganj[35]', 'Varanasi', 'Belgaum',
       'Tirupati[21][22]', 'Tumkur', 'Coimbatore', 'Kurnool[18]',
       'Gurgaon', 'Muzaffarnagar', 'Aurangabad', 'Bhavnagar', 'Arrah',
       'Munger', 'Tirunelveli', 'Mumbai', 'Mango', 'Nashik', 'Kadapa[23]',
       'Amritsar', 'Khora,_Ghaziabad', 'Ambala', 'Agra', 'Ratlam',
       'Surendranagar_Dudhrej', 'Delhi_city', 'Bhopal', 'Hapur', 'Rohtak',
       'Durg', 'Korba', 'Bangalore', 'Shivpuri', 'Thrissur',
       'Vijayanagaram', 'Farrukhabad', 'Nangloi_Jat', 'Madanapalle',
       'Thoothukudi', 'Nagercoil', 'Gaya', 'Chandigarh_city', 'Jammu[16]',
       'Kakinada', 'Dewas', 'Bhalswa_Jahangir_Pur', 'Baranagar',
       'Firozabad', 'Phusro', 'Allahabad', 'Guna', 'Thane', 'Etawah',
       'Vasai-Virar', 'Pallavaram', 'Morena', 'Ballia', 'Surat',
       'Burhanpur', 'Phagwara', 'Mau', 'Mangalore', 'Alwar',
       'Mahbubnagar', 'Maheshtala', 'Hazaribagh', 'Bihar_Sharif',
       'Faridabad', 'Lucknow', 'Tenali', 'Barasat', 'Amroha', 'Giridih',
       'Begusarai', 'Medininagar', 'Rajahmundry[19][20]', 'Saharsa[29]',
       'New_Delhi', 'Bhilai', 'Moradabad', 'Machilipatnam',
       'Mira-Bhayandar', 'Pali', 'Navi_Mumbai', 'Mehsana', 'Imphal',
       'Kolkata', 'Sambalpur', 'Ujjain', 'Madhyamgram', 'Jabalpur',
       'Jamalpur[36]', 'Ludhiana', 'Bareilly', 'Gangtok', 'Anand',
       'Dehradun', 'Pune', 'Satara', 'Srikakulam', 'Raipur', 'Jodhpur',
       'Darbhanga', 'Nizamabad', 'Nandyal', 'Dehri[30]', 'Jorhat',
       'Ranchi', 'Kumbakonam', 'Guntakal', 'Haldia', 'Loni',
       'Pimpri-Chinchwad', 'Rajkot', 'Nanded', 'Noida',
       'Kirari_Suleman_Nagar', 'Jaunpur', 'Bilaspur', 'Sambhal', 'Dhule',
       'Rourkela', 'Thiruvananthapuram', 'Dharmavaram', 'Nellore[14][15]',
       'Visakhapatnam[4]', 'Karawal_Nagar', 'Jaipur', 'Avadi',
       'Bhimavaram', 'Bardhaman', 'Silchar', 'Buxar[37]', 'Kavali',
       'Tezpur', 'Ramagundam[27]', 'Yamunanagar', 'Sri_Ganganagar',
       'Sasaram[30]', 'Sikar', 'Bally', 'Bhiwani', 'Rampur', 'Uluberia',
       'Sangli-Miraj_&_Kupwad', 'Hosur', 'Bikaner', 'Shahjahanpur',
       'Sultan_Pur_Majra', 'Vijayawada', 'Bharatpur', 'Tadepalligudem',
       'Tinsukia', 'Salem', 'Mathura', 'Guntur[13]', 'Hubliâ€“Dharwad',
       'Guwahati', 'Chittoor[28]', 'Tiruvottiyur', 'Vadodara',
       'Ahmednagar', 'Fatehpur', 'Bhilwara', 'Kharagpur', 'Bettiah[33]',
       'Bhind', 'Bokaro', 'Karaikudi', 'Raebareli', 'Pudukkottai',
       'Udaipur', 'Mysore[7][8][9]', 'Panipat', 'Latur', 'Tadipatri',
       'Bahraich', 'Orai', 'Raurkela_Industrial_Township', 'Gwalior',
       'Katni', 'Chandrapur', 'Kolhapur']
    CITY_count = a.index(CITY_count)
    b = [ 798,  849,  688,  607,  809,  857,  834,  862,  660,  740, 1098,
        953, 1064,  741,  757,  994,  775,  706,  885,  840,  612,  649,
        829, 1067,  931, 1130,  897,  773,  608,  810, 1051,  794,  725,
        760,  687, 1016,  708, 1058,  833,  614, 1033, 1065, 1037,  494,
        572,  540,  866,  769,  684, 1003,  683,  768,  624,  579,  738,
        844,  896,  913, 1001,  613,  679,  861,  812,  940,  657,  985,
        933,  977,  858,  868,  790,  651,  956,  781,  778,  883,  893,
        730,  916,  854,  961,  826,  731, 1136,  899,  838,  865,  658,
        860,  939,  963,  971,  880,  655,  965,  751,  926,  743,  510,
        536,  723,  767, 1028,  641,  793,  821,  903,  618,  870,  752,
        459,  948, 1185,  529,  805,  719,  625,  753,  718,  663,  792,
        772,  704,  702,  685,  668,  835,  976,  786,  661,  841,  807,
        905,  776, 1012,  736,  596, 1208,  546,  797,  634,  727,  973,
       1259,  673,  935,  656,  644,  682,  646,  951,  713,  785,  877,
        615,  930,  984,  803,  830,  845,  763,  791,  919,  715,  501,
        665,  645,  666,  863,  915,  745,  889,  598, 1180,  631,  832,
        699,  653, 1084,  486,  874, 1036,  906,  873,  942, 1096,  629,
        820, 1056,  550,  891,  823, 1079,  782,  588,  509,  907,  756,
        729,  761,  774,  686,  802,  900,  674,  945,  667,  606,  689,
        958,  822,  734,  659,  801,  681,  770,  648,  777,  639,  630,
        590,  601,  528, 1172,  800,  533,  735,  695,  749,  960,  711,
        457,  733,  654,  431,  739,  580,  523,  970,  894,  616,  448,
        499]
    CITY_count = b[CITY_count]
    

    
    STATE_count = st.selectbox("STATE",('Madhya_Pradesh', 'Maharashtra', 'Kerala', 'Odisha', 'Tamil_Nadu',
'Gujarat', 'Rajasthan', 'Telangana', 'Bihar', 'Andhra_Pradesh',
'West_Bengal', 'Haryana', 'Puducherry', 'Karnataka',
'Uttar_Pradesh', 'Himachal_Pradesh', 'Punjab', 'Tripura',
'Uttarakhand', 'Jharkhand', 'Mizoram', 'Assam',
'Jammu_and_Kashmir', 'Delhi', 'Chhattisgarh', 'Chandigarh',
'Uttar_Pradesh[5]', 'Manipur', 'Sikkim'))
    c = ['Madhya_Pradesh', 'Maharashtra', 'Kerala', 'Odisha', 'Tamil_Nadu',
    'Gujarat', 'Rajasthan', 'Telangana', 'Bihar', 'Andhra_Pradesh',
    'West_Bengal', 'Haryana', 'Puducherry', 'Karnataka',
    'Uttar_Pradesh', 'Himachal_Pradesh', 'Punjab', 'Tripura',
    'Uttarakhand', 'Jharkhand', 'Mizoram', 'Assam',
    'Jammu_and_Kashmir', 'Delhi', 'Chhattisgarh', 'Chandigarh',
    'Uttar_Pradesh[5]', 'Manipur', 'Sikkim']
    STATE_count = c.index(STATE_count)
    d = [ 14122, 25562,  5805,  4658, 16537, 11408,  9174,  7524, 19780,
    25297, 23483,  7890,  1433, 11855, 28400,   833,  4720,   809,
     1874,  8965,   849,  7062,  1780,  5490,  3834,   656,   743,
      608]
    STATE_count = d[STATE_count]
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(Income, Age, Experience, Married_Single, House_Ownership,
       Car_Ownership, CURRENT_JOB_YRS, CURRENT_HOUSE_YRS, Profession_count,
       CITY_count,STATE_count)
        if result==1:
            st.success('Congratulations! You Are Eligible For A Personal Loan')
        else:
            st.error('Sorry! You Are Not Eligible For A Personal Loan')

            if (((int(LoanAmount))*0.3)>(int(Income))):
                st.info("Please Increase Your Income As It Is Less Than 30%% Of The Loan Amount")
            if(int(Experience)<10):
                st.info("Please Increase Your Experience")


                
            # list = ['Please Increase Your Credit Score','Please Build A Good Credit History','Please Lower Your Monthly Debt']
            # list2 = ['You Have Too Many Bankruptcies','You Have Too Many TaxLiens','Please Increase Your Annual Income']
            
            # st.info(random.choice(list))
            # st.info(random.choice(list2))
 
    #st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Hello")
        
            
            
    df= pd.read_csv('../Final/personal_loan_table.csv',index_col=0)
    df = df.drop(df.columns[0],axis=1)
    #st.dataframe(df, 100,1000)
    st.table(df)
    

if __name__=='__main__':
    main()
    


