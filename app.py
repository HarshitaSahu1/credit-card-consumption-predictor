import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import joblib


import streamlit as st

st.markdown("""
    <style>
    /* ===================================================
        1️⃣ MAIN BACKGROUND & CONTAINER
    =================================================== */
    /* Naye Streamlit versions ke liye background target */
    .stAppViewContainer, .stMainBlockContainer, .main {
        background-color: #F5F9FF !important;
    }

    .block-container {
        background-color: #F5F9FF !important;
        padding-top: 2rem !important;
        padding-left: 2rem !important;
        padding-right: 2rem !important;
    }

    /* ===================================================
        2️⃣ KPI CARDS (METRICS)
    =================================================== */
    [data-testid="stMetric"], [data-testid="metric-container"] {
        background-color: #E6F0FF !important;
        border: 2px solid #1E3A8A !important;
        border-radius: 14px !important;
        padding: 10px !important;
        box-shadow: 0px 4px 6px rgba(30, 58, 138, 0.1) !important;
    }

    /* KPI LABEL */
    [data-testid="stMetricLabel"] p {
        color: #1E3A8A !important;
        font-weight: 700 !important;
        font-size: 14px !important;
    }

    /* KPI VALUE */
    [data-testid="stMetricValue"] div {
        color: #0F172A !important;
        font-weight: 800 !important;
        font-size: 24px !important;
    }

    /* ===================================================
        3️⃣ HEADINGS & TEXT
    =================================================== */
    h1, [data-testid="stHeader"] h1 {
        color: #0F172A !important;
        font-weight: 900 !important;
        font-size: 28px !important;
    }

    h2, [data-testid="stHeader"] h2 {
        color: #1E3A8A !important;
        font-weight: 800 !important;
    }

    h3, h4 {
        color: #1D4ED8 !important;
        font-weight: 700 !important;
    }

    /* ===================================================
        4️⃣ PLOTLY CHARTS WRAPPER
    =================================================== */
    .stPlotlyChart, .stPyplot {
        background-color: #FFFFFF !important;
        border-radius: 12px !important;
        padding: 6px !important;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.05) !important;
    }

    /* ===================================================
        5️⃣ SIDEBAR NAV & BACKGROUND
    =================================================== */
    [data-testid="stSidebar"], section[data-testid="stSidebar"] {
        background-color: #1E3A8A !important;
    }

    /* Sidebar ke andar ka saara text white karne ke liye */
    [data-testid="stSidebar"] *, [data-testid="stSidebarNavigation"] * {
        color: #FFFFFF !important;
        font-weight: 600 !important;
    }

    /* Active/Selected page highlight color in sidebar navigation */
    [data-testid="stSidebarNavLink"][aria-current="page"] {
        background-color: rgba(255, 255, 255, 0.15) !important;
    }

    /* ===================================================
        6️⃣ INPUT FIELDS & SELECT BOX
    =================================================== */
    div[data-baseweb="select"] > div {
        background-color: #FFFFFF !important;
        border: 2px solid #1E3A8A !important;
        border-radius: 10px !important;
    }

    div[data-baseweb="select"] * {
        color: #0F172A !important; /* TAki dropdown text readable rahe */
    }

    /* ===================================================
        7️⃣ BUTTONS
    =================================================== */
    .stButton > button {
        background-color: #1E3A8A !important;
        color: white !important;
        border: none !important;
        font-weight: 700 !important;
        border-radius: 10px !important;
        padding: 8px 16px !important;
    }

    .stButton > button:hover {
        background-color: #0F172A !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.set_page_config(
    page_title="Credit Card Consumption Dashboard",
    page_icon="💳",
    layout="wide"
)

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ---------------- LOGIN PAGE ---------------- #

if not st.session_state.logged_in:

    left, right = st.columns([1.5, 1])

    with left:
        st.image("Credit Consumption_image.png", use_container_width=True)

    with right:

        st.title("🔐 Login")

        st.markdown(
            "Welcome to the **Credit Card Consumption Analytics Dashboard**."
        )

        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login", use_container_width=True):

            if username == "admin" and password == "123":

                st.session_state.logged_in = True
                st.rerun()

            else:
                st.error("Invalid Username or Password")

        st.divider()

        st.info("""
### 🧪 Demo Credentials

**Username:** admin

**Password:** admin123
""")

# ---------------- DASHBOARD ---------------- #

else:

    st.title("📊 Credit Card Consumption Dashboard")

    st.success("Successfully Logged In!")

    
    if st.button("Logout"):

        st.session_state.logged_in = False
        st.rerun()


    

    st.set_page_config(
        page_title="Credit Card Consumption Dashboard",
        page_icon="💳",
        layout="wide"
    )

    st.header("Credit Card Consumption Dashboard")

    st.markdown("""
    Gain actionable insights into customer spending patterns,
    financial profiles, and credit card consumption through
    interactive analytics and predictive modeling.
    """)



    tab1, tab2 = st.tabs([
        "📊 Analytics Dashboard",
        "🤖 Credit Consumption Prediction"
    ])

    with tab1:
        final_dataset = pd.read_csv(r'C:\Users\Harshita Sahu\OneDrive\Documents\ML_1_CREDIT_CARD\11. Capstone Case Study - Predict Cred Card Consumption\final_dataset.csv')
        final_dataset.head()

        with st.expander("📄 View Sample Dataset"):
            st.dataframe(final_dataset.head())

        


        st.markdown(" ")
        st.markdown(" ")
        st.markdown(" ")

        Total_Customer_Ids = final_dataset['ID'].nunique()
        Avg_Customer_Retention = final_dataset['Tenure_with_Bank'].mean()
        Top_Income_Type = final_dataset.groupby('Income')['ID'].nunique().sort_values(ascending = False).reset_index(name = 'value_counts')
        Top_Income_Type = Top_Income_Type['Income'][0]
        Avg_Days_btw_Transactions = final_dataset[['Avg_days_between_transaction']].mean()


        col1,col2,col3,col4 = st.columns(4)

        with col1:
            st.metric("Total_Customers",Total_Customer_Ids)

        with col2:
            st.metric("Avg_Customer_Retention",Avg_Customer_Retention)

        with col3:
            st.metric("Top_Income_Type",Top_Income_Type)

        with col4:
            st.metric("Avg_Days_btw_Transactions",Avg_Days_btw_Transactions)
            


        col5,col6,col7,col8 = st.columns(4)

        bin_edges = [18,35, 60, 100]
        bin_labels = [ 'Young Adult', 'Middle Aged', 'Senior']

        # Segment the data
        final_dataset['age_bin']  = pd.cut(final_dataset['age'], bins=bin_edges, labels=bin_labels)

        Top_Customer_Type = final_dataset.groupby('age_bin')['ID'].count().sort_values(ascending= False).reset_index(name = 'Cust_id_counts').head()
        Top_Customer_Type = Top_Customer_Type['age_bin'][0]

        with col5:
            st.metric('Most Common Age Group',Top_Customer_Type)


        final_dataset['Credit_Card_Utilization_Limit'] = pd.qcut(final_dataset['card_lim'],q = 3, labels= ['Low','Medium','High'])
        Most_Type_Customer_Utlization = final_dataset.groupby('Credit_Card_Utilization_Limit')['ID'].nunique().sort_values(ascending= False).reset_index(name = 'Cust_id_counts')
        Most_Type_Customer_Utlization = Most_Type_Customer_Utlization['Cust_id_counts'][0]

        with col6:
            st.metric('Most Common Credit Limit Tier',Most_Type_Customer_Utlization)


        s = final_dataset.groupby('ID')[['investment_1','investment_2','investment_3','investment_4']].sum()
        final_dataset['Total_Investements'] = s['investment_1'] + s['investment_2'] +s['investment_3'] + s['investment_4']
        final_dataset['Investment_Type'] = pd.qcut(final_dataset['Total_Investements'],q= 3,labels = ['Low_Investor','Moderate_Investor','High_Investor'])

        final_dataset.rename(columns = {'Investment_Type':'User_Investment_Type'},inplace = True)

        Avg_investment_prcnt = (final_dataset['Total_Investements'].sum()/ final_dataset['ID'].nunique())


        with col7:
            st.metric('Average Investment',f'{round((Avg_investment_prcnt/100000),2)}L')

        loanss = final_dataset.groupby('ID')[['personal_loan_active','vehicle_loan_active']].sum()
        final_dataset['Total_Active_Loans'] = (loanss['personal_loan_active'] + loanss['vehicle_loan_active'])

        Avg_Active_Loan_prcnt = (final_dataset['Total_Active_Loans'].sum()/final_dataset['ID'].nunique())

        with col8:
            st.metric('Average Active Loans',f'{Avg_Active_Loan_prcnt}')
            


        #sns.heatmap(final_dataset[['age','Total_Investements']].corr(),annot = True)
        #plt.show()





        credit_consumption = []
        debit_consumption = []
        credit_consumption_count = []
        debit_consumption_count = []
        for col in final_dataset.columns:
            if col.startswith('cc_cons'):
                credit_consumption.append(col)
            elif col.startswith('dc_cons'):
                debit_consumption.append(col)
            elif col.startswith('cc_count'):
                credit_consumption_count.append(col)
            elif col.startswith('dc_count'):
                debit_consumption_count.append(col)


        credit_consumption_cols = [c for c in credit_consumption if c != 'cc_cons']




        ### Credit Card Consumptions 

        cc_consumptions = final_dataset[credit_consumption_cols].rename(columns ={'cc_cons_apr':'April_Credit_Card_Usage','cc_cons_may':'May_Credit_Card_Usage','cc_cons_jun':'June_Credit_Card_Usage'})


        #dc_consumptions = final_dataset[debit_consumption].rename(columns ={'dc_cons_apr':'April_Credit_Card_Usage','dc_cons_may':'May_Credit_Card_Usage','dc_cons_jun':'June_Credit_Card_Usage'})
        #dc_consumptions

        cc_counts = final_dataset[credit_consumption_count].rename(columns ={'cc_count_apr':'April_Credit_Card_Count','cc_count_may':'May_Credit_Card_Count','cc_count_jun':'June_Credit_Card_Count'})



        cc_consumptions = cc_consumptions.rename(columns = {'April_Credit_Card_Usage':'April','May_Credit_Card_Usage':'May','June_Credit_Card_Usage':'June'})
        cc_counts = cc_counts.rename(columns = {'April_Credit_Card_Count':'April','May_Credit_Card_Count':'May','June_Credit_Card_Count':'June'})



        monthly_consumption = cc_consumptions.sum()


        monthly_consumption_counts = cc_counts.sum()


        monthly_credit_consumption_prct = monthly_consumption*100/monthly_consumption_counts
        st.divider()

        st.subheader("💳 Credit & Debit Card Trends")
        st.divider()

        col1,col2 = st.columns(2)

        with col1:
            fig,axes = plt.subplots(figsize =  (5,5))
            axes.bar(monthly_consumption.index , monthly_consumption.values,label = 'Consumptions')
            axes2 = axes.twinx()
            axes2.plot(monthly_consumption_counts.index,monthly_consumption_counts.values,marker = 'o',label = 'Transaction_Count',color = 'red')
            plt.xticks(rotation = 90)
            plt.xlabel('Months')
            axes.set_ylabel('Total_Consumptions')
            axes2.set_ylabel('Transaction_Counts')
            plt.title('Monthly Credit Card Consuptions ')
            axes.legend(loc='upper left')
            axes2.legend(loc='upper right')
            st.pyplot(fig,use_container_width = False)
            plt.close(fig)

            with st.expander('💡Chart Interpretation'):
                st.markdown('The Credit Consumption is Highest In Month of April followed by Month Of May and then June . ' \
                'here Transaction counts are relatively high in month April & June & in June the amount of credit consumption is low and in may it is very low')




        ##### Debit Card Consumptions 
        debit_consumption = final_dataset[debit_consumption]
        debit_consumption_count = final_dataset[debit_consumption_count]

        debit_consumption = debit_consumption.rename(columns = {'dc_cons_apr':'April','dc_cons_may':'May','dc_cons_jun':'June'})
        dc_counts = debit_consumption_count.rename(columns = {'dc_count_apr':'April','dc_count_may':'May','dc_count_jun':'June'})


        monthly_consumption_debit = debit_consumption.sum()


        monthly_consumption_counts_debit = dc_counts.sum()


        monthly_debit_consumption_prct = (monthly_consumption_debit*100/monthly_consumption_counts_debit)

        with col2:
            fig,axes = plt.subplots(figsize = (5,5))
            axes.bar(monthly_consumption_debit.index , monthly_consumption_debit.values,label = 'Consumptions')
            axes2 = axes.twinx()
            axes2.plot(monthly_consumption_counts_debit.index,monthly_consumption_counts_debit.values,marker = 'o',label = 'Transaction_Count',color = 'red')
            plt.xticks(rotation = 90)
            plt.xlabel('Months')
            axes.set_ylabel('Total_Consumptions')
            axes2.set_ylabel('Transaction_Counts')
            axes.set_title('Monthly Debit Card Consuptions ')
            axes.legend(loc='upper left')
            axes2.legend(loc='upper right')
            st.pyplot(fig,use_container_width = False)
            plt.close(fig)
        
            with st.expander('💡Chart Interpretation'):
                st.markdown('The Debit Consumption is Highest In Month of April followed by Month Of May and then June . ' \
                'here Transaction counts are relatively high in month of June & lowest in month of May but the amout of debit consumption is higher in monh june')


        final_dataset['gender'] = np.where(final_dataset['gender'] == '0','Unkown',final_dataset['gender'])
        k = final_dataset.groupby('gender')['ID'].nunique().reset_index(name = 'users_count')
        st.divider()

        st.subheader("👥 Customer Demographics")
        st.divider()


        col3,col4 = st.columns(2)


        with col3:
            fig,axes = plt.subplots(figsize = (3,3))
            axes.pie(x = k['users_count'],labels= k['gender'],autopct='%1.1f%%')
            axes.set_title('Distribution Customer Based On Gender')
            st.pyplot(fig,use_container_width = False)
            plt.close(fig)

            with st.expander('💡Chart Interpretation'):
                st.markdown("Male customers represent the majority of the customer base." \
                "Female customers contribute a comparatively smaller share." \
                "This indicates that the current customer population is predominantly male.")

        with col4:
            fig,axes = plt.subplots(figsize = (3,3))
            age_dist = final_dataset.groupby('age_bin')['ID'].nunique().reset_index(name = 'user_counts')
            sns.barplot(y = age_dist['user_counts'],x = age_dist['age_bin'])
            axes.set_title('Distribution Of Users Based On Age')
            axes.tick_params(axis = 'x',rotation = 45)
            st.pyplot(fig,use_container_width = False)
            plt.close(fig)

            with st.expander('💡Chart Interpretation'):
                st.markdown("Middle Age Customers are highest who's age is between 35 to 60 then Young adult")


        invts = final_dataset[['investment_1','investment_2','investment_3','investment_4']].sum(axis= 0).reset_index(name = 'total_invt')
        st.divider()
        st.subheader('💰 Investment Insights')
        st.divider()

        col4,col5 = st.columns(2)

        with col4:
            fig,axes = plt.subplots(figsize = (5,5))
            axes.hlines(y = invts['index'],label = invts.index,xmin = 0,xmax = invts['total_invt'] )
            axes.scatter(x = invts['total_invt'] , y = invts['index'])
            axes.set_xlabel('Investments_Counts')
            axes.set_ylabel('Investments_Type')
            axes.set_title('Investments Distribution')
            axes.grid(axis='x', alpha=0.3)
            st.pyplot(fig,use_container_width = False)

            with st.expander('💡Chart Interpretation'):
                st.markdown("Investment 1 is the highest which is of demat which only depicts customer getting aware about investments " \
                "now they are not only going only for accounts in bank but also for demat account for investing." \
                "then investing 2 which is of fixed deposits and least for general insuarance")



        Top_User_Investment_Type = final_dataset.groupby('User_Investment_Type')['ID'].nunique().sort_values(ascending= False).reset_index(name = 'Cust_counts')

        with col5:
            fig,ax = plt.subplots(figsize = (4.5,3))
            s = plt.bar(Top_User_Investment_Type['User_Investment_Type'],Top_User_Investment_Type['Cust_counts'])
            for i,val in enumerate(s):
                plt.text(val.get_x()+val.get_width()/2,val.get_height(),str(int(val.get_height())),ha = 'center',va = 'bottom',fontsize= 8)
            ax.set_xlabel('User_Investment_Types')
            ax.set_ylabel('Customer_Counts')
            ax.set_title('Investor Type Distribution')
            ax.tick_params(axis='x', rotation=45)
            st.pyplot(fig,use_container_width = False)
            
            plt.close(fig)

            with st.expander('💡Chart Interpretation'):
                st.markdown("Here the Investors of all types are in same range there is no much difference in one and another in contribution")


        



    with tab2:
        import joblib
        st.markdown("Upload a customer dataset to predict credit card consumption using the trained machine learning model. The application validates the uploaded data before generating predictions.")
        st.info("""
    ### 🤖 Model Information

    - **Algorithm:** Bagging Regressor
    - **Base Estimator:** Decision Tree Regressor
    - **Target Variable:** Credit Card Consumption
    - **Input:** Customer CSV File
    - **Output:** Predicted Credit Card Consumption
    """)
        
        st.subheader('📂 Upload Customer Dataset')
        uploaded_file = st.file_uploader("Choose a CSV file containing customer information",type = ['csv'])

        if uploaded_file is not None :
            prediction_data = pd.read_csv(uploaded_file)
            st.success("✅ File uploaded successfully!")
            st.dataframe(prediction_data.head())
            st.subheader('Quick_Summary Before Prediction')

            col1,col2,col3,col4 = st.columns(4)

            with col1:
                Rows = prediction_data.shape[0]
                st.metric('Rows',Rows)
            
            with col2:
                Columns = prediction_data.shape[1]
                st.metric('Columns',Columns)
            
            with col3:
                Total_Customer = prediction_data['ID'].nunique()
                st.metric('Total_Customer',Total_Customer)

            with col4:
                Total_Missings = prediction_data.isna().sum().sum()
                st.metric('Total_Missings',Total_Missings)
            
            st.subheader('Validating Data')

            cols = ['ID', 'account_type', 'gender', 'age', 'Income', 'Emp_Tenure_Years', 'Tenure_with_Bank', 'region_code', 'NetBanking_Flag', 'Avg_days_between_transaction', 'cc_cons_apr', 'dc_cons_apr', 'cc_cons_may', 'dc_cons_may', 'cc_cons_jun', 'dc_cons_jun', 'cc_count_apr', 'cc_count_may', 'cc_count_jun', 'dc_count_apr', 'dc_count_may', 'dc_count_jun', 'card_lim', 'personal_loan_active', 'vehicle_loan_active', 'personal_loan_closed', 'vehicle_loan_closed', 'investment_1', 'investment_2', 'investment_3', 'investment_4', 'debit_amount_apr', 'credit_amount_apr', 'debit_count_apr', 'credit_count_apr', 'max_credit_amount_apr', 'debit_amount_may', 'credit_amount_may', 'credit_count_may', 'debit_count_may', 'max_credit_amount_may', 'debit_amount_jun', 'credit_amount_jun', 'credit_count_jun', 'debit_count_jun', 'max_credit_amount_jun', 'loan_enq', 'emi_active', 'cc_cons']

            is_valid = True
            if prediction_data.shape[0] == 0:
                st.success('Invalid Data With No Rows')
                is_valid = False
            elif not all(col in prediction_data.columns for col in cols):
                st.error('Wrong Columns')
                #st.info("✅ Validation Successful Dataset is ready for prediction.")
                is_valid = False
            elif 'cc_cons' not in prediction_data.columns:
                
                st.error('Prediction column is not Present')
                is_valid = False
            else:
                st.success("✅ Dataset validation successful.")

        

            
            if is_valid:
                if st.button("🔮 Predict Credit Card Consumption"):

                    prediction_rows = prediction_data[prediction_data['cc_cons'].isna()]
                    if prediction_rows.empty:
                        st.warning("No rows found where cc_cons is missing.")

                    X_pred = prediction_rows.drop(columns=['ID', 'cc_cons'])

                    model = joblib.load("model_pipeline.pkl")
                    predictions = model.predict(X_pred)
                    
                    prediction_data.loc[prediction_data['cc_cons'].isna(),'cc_cons'] = predictions
                    st.success("🎉 Predictions generated successfully!")

                    st.subheader('Summary After Predictions')
                    col1,col2,col3 = st.columns(3)

                    with col1:
                        st.metric('Total Credit_Consumptions',f"{round((prediction_data['cc_cons'].sum()/1000000),2)}M")

                    with col2:
                        st.metric('Total_Customers',prediction_data['ID'].nunique())

                    with col3:
                        st.metric('Total Predictions Generated',prediction_rows.shape[0])
                    
                    col1,col2 = st.columns(2)
                    with col1:
                        fig,axes = plt.subplots(figsize = (2,2))
                        sns.histplot(prediction_data['cc_cons'],bins = 20,kde = True,ax = axes)
                        axes.set_xlabel('Predicted_Credit_Consumption',fontsize = 7)
                        axes.set_ylabel('Customers',fontsize = 7)
                        ax.set_title("Distribution of Predicted Credit Consumption")
                        st.pyplot(fig,use_container_width = True)
                        
                    
                    csv = prediction_data.to_csv(index = False)
                    st.download_button("📥 Download Predictions",csv,file_name='Prediction_Cosumption_Data.csv',mime = 'text/csv')



                



                    

                

                
                
                
