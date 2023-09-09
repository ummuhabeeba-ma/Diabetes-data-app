import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image
def home():
    st.title("Welcome to Diabetes data presentation")
    st.write("Diabetes is a condition that happens when your blood sugar (glucose) is too high. It develops when your pancreas doesn’t make enough insulin or any at all, or when your body isn’t responding to the effects of insulin properly. Diabetes affects people of all ages. Most forms of diabetes are chronic (lifelong), and all forms are manageable with medications and/or lifestyle changes.")
    image = Image.open('diabetes.png')
    st.image(image,caption='Diabetes')
df=pd.read_csv("C:/Users/Habeeba/Downloads/diabetes-vid.csv")
df.rename(columns={'DiabetesPedigreeFunction':'Dp',
                   'BloodPressure':'BP'},inplace = True)
def header():
    st.header("Data Header")
    st.write(df.head())
def med():
    tab1,tab2,tab3,tab4,tab5,tab6=st.tabs(["BP","BMI","Glucose","SkinThickness","Insulin","Diabetes Pedigree Function"])
    outcome_level = st.sidebar.multiselect("Select the Outcome:",
                                           options=df["Outcome"].unique(),
                                           default=df["Outcome"].unique(), key="k1")
    df_selection = df.query(
        "Outcome == @outcome_level"
    )
    with tab1:
        st.subheader("Visual Summary")
        bp_selection=st.slider('Blood Pressure:',
                                  min_value=min(df['BP']),
                                  max_value=max(df['BP']),
                                  value=(min(df['BP']), max(df['BP'])))
        mask = (df['BP'].between(*bp_selection))
        fig1= px.histogram(df_selection[mask], x="BP", color="Outcome", title="Diabetes outcome based on Blood Pressure")
        fig1.update_layout(
            font_family="Times new Roman",
            font_color="black",
            title_font_size=20
        )
        st.plotly_chart(fig1)
        st.subheader("Numerical Summary")
        t=df_selection[mask].groupby(['Outcome'])['BP'].aggregate(['sum','mean','median','max','min'])
        st.dataframe(t)
        st.subheader("Observation")
        st.write("1. We can see that there are patients who have died due to diabetes even with less blood pressure")
        st.write("2. Also it can be seen that the count of the patients who have died gradually increases with the increase in blood pressure. But it started to decrease with blood pressure after 74")
        st.write("3. Count of patients who are alive is more compared to the one died.We could also see that there is one patient whose blood pressure is around 120-124 and is still alive")
        st.write("4. Hence it could be said that blood pressure does not affect the patients and it could not be a reason for patients leading to death.")
    with tab2:
        st.subheader("Visual Summary")
        bmi = df['BMI'].unique().tolist()
        bmi_selection = st.slider('BMI:',
                                  min_value=min(bmi),
                                  max_value=max(bmi),
                                  value=(min(bmi), max(bmi)))
        mask = (df['BMI'].between(*bmi_selection))
        fig2= px.box(df_selection[mask], x="Outcome", y="BMI", title="Diabetes outcome based on BMI")
        fig2.update_layout(
            font_family="Times new Roman",
            font_color="black",
            title_font_size=20
        )
        st.plotly_chart(fig2)
        st.subheader("Numerical Summary")
        t1=df_selection[mask].groupby(['Outcome'])['BMI'].aggregate(['sum', 'mean', 'median', 'max', 'min'])
        st.dataframe(t1)
        st.subheader("Observation")
        st.write("1. From the above numeric summary, we could see that the minimum and maximum BMI of the patients who are alive is found to be 0.0 and 57.3 which can also be verified by looking into the above box plot.")
        st.write("2. Also, we could see that the median BMI of the patients who are dead is found to be more compared to the patients who are alive.")
        st.write("3. We can also see that the patients who have died have touched the maximum BMI of 67.1")
        st.write("4. Also the mean value of the patients who died is more than the patients who is alive.")
        st.write("5. 25% of the total patients who are alive have BMI of 25.4 wherease patients who are dead have BMI of 30.8. We could see that BMI is more for patients who are dead.")
        st.write("6. By refering the above numeric summary and the box plot, we could say that patients who are dead had high BMI.")
    with tab3:
        st.subheader("Visual Summary")
        glucose_selection = st.slider('Glucose level:',
                                 min_value=min(df['Glucose']),
                                 max_value=max(df['Glucose']),
                                 value=(min(df['Glucose']), max(df['Glucose'])))
        mask = (df['Glucose'].between(*glucose_selection))
        fig5 = px.histogram(df_selection[mask], x="Glucose", color="Outcome", title="Diabetes Outcome based on Glucose level")
        fig5.update_layout(
            font_family="Times new Roman",
            font_color="black",
            title_font_size=20
        )
        st.plotly_chart(fig5)
        st.subheader("Numerical Summary")
        t2 = df_selection[mask].groupby(['Outcome'])['Glucose'].aggregate(['sum', 'mean', 'median', 'max', 'min'])
        st.dataframe(t2)
        st.subheader("Observation")
        st.write("1. From the above plot, we can see that the majority of the patients who have died had glucose level greater than 100.")
        st.write("2. Also there are few patients who have died with zero glucose level.")
        st.write("3. We can find that few number of patients who are alive had less level of glucose and the count of the patients gradually increased who had glucose level greater than 80.")
        st.write("4. We can also view from the above graph that there are more number of patients who died had very high glucose level, but there are few patients who is still alive with high glucose level.")
        st.write("5. Median of glucose is higher for patients who died.")
        st.write("6. Hence we could say by seeing the above graph that high glucose might be a reason for patients to die since there are more number of patients who died at higher glucose level.")
    with tab4:
        st.subheader("Visual Summary")
        st_selection = st.slider('Skin Thickness level:',
                                      min_value=min(df['SkinThickness']),
                                      max_value=max(df['SkinThickness']),
                                      value=(min(df['SkinThickness']), max(df['SkinThickness'])))
        mask = (df['SkinThickness'].between(*st_selection))
        fig6 = px.box(df_selection[mask], x="Outcome", y="SkinThickness",
                            title="Diabetes outcome based on the thickness of skin")
        fig6.update_layout(
            font_family="Times new Roman",
            font_color="black",
            title_font_size=20
        )
        st.plotly_chart(fig6)
        st.subheader("Numerical Summary")
        t3 = df_selection[mask].groupby(['Outcome'])['SkinThickness'].aggregate(['sum', 'mean', 'median', 'max', 'min'])
        st.dataframe(t3)
        st.subheader("Observation")
        st.write("1. Maximum thickness level of skin is found to be for the patients who died.")
        st.write("2. Comparing both the box plots, we could find that maximum value, median, third quartile of skin thickness are all higher for patients who died.")
        st.write("3. Hence we could conclude that skin thickness level may be reason for the patients to die.")
    with tab5:
        st.subheader("Visual Summary")
        insulin_selection = st.slider('Insulin level:',
                                      min_value=min(df['Insulin']),
                                      max_value=max(df['Insulin']),
                                      value=(min(df['Insulin']), max(df['Insulin'])))
        mask = (df['Insulin'].between(*insulin_selection))
        fig7 = px.box(df_selection[mask], y="Insulin", x="Outcome", title="Diabetes outcome based on Insulin")
        fig7.update_layout(
            font_family="Times new Roman",
            font_color="black",
            title_font_size=20
        )
        st.plotly_chart(fig7)
        st.subheader("Numerical Summary")
        t4 = df_selection[mask].groupby(['Outcome'])['Insulin'].aggregate(['sum', 'mean', 'median', 'max', 'min'])
        st.dataframe(t4)
        st.subheader("Observation")
        st.write("1. Insulin level is consistent for patients who are alive compared to the patients who died.")
        st.write("2. Also we could see that patients who died had relatively greater insulin level than patients who are alive.")
        st.write("3. Hence we may say that greater insulin can also affect the person leading to death.")
    with tab6:
        st.subheader("Visual Summary")
        dp_selection = st.slider('Diabetes Pedigree Function:',
                                      min_value=min(df['Dp']),
                                      max_value=max(df['Dp']),
                                      value=(min(df['Dp']), max(df['Dp'])))
        mask = (df['Dp'].between(*dp_selection))
        fig8 = px.histogram(df_selection[mask], x="Dp", color="Outcome", title="Diabetes outcome based on the Pedigree function")
        st.plotly_chart(fig8)
        st.subheader("Numerical Summary")
        t5 = df_selection[mask].groupby(['Outcome'])['Dp'].aggregate(['sum', 'mean', 'median', 'max', 'min'])
        st.dataframe(t5)
        st.subheader("Observation")
        st.write("1. We can see from the above graph that patients who are alive is more than the patients who died.")
        st.write("2. Also we can find that the number of patients who died started to increase gradually and is at maximum with diabetes pedigree function ranging between 0.25 to 0.299. But we could also see that with the same range there are more number of patients who are alive.")
        st.write("3. The count of patients decreases after that and found in less propotions with diabetes pedigree function greater than 1. We could also see that few patients are alive with diabetes pedigree function greater than 1.4.")
        st.write("4. Very few patients have died with greater diabetes pedigree function.")
        st.write("5. By seeing the above graph, we can conclude that diabetes pedigree function does not affect patients and may not be a reason for the patients to die.")
def Preg_plot():
    st.subheader("Visual Summary")
    Outcome = df['Outcome'].unique().tolist()
    pgs = df['Pregnancies'].unique().tolist()
    pgs_selection = st.slider('Pregnancies',
                              min_value=min(pgs),
                              max_value=max(pgs),
                              value=(min(pgs), max(pgs)))
    df_selection = st.multiselect('Outcome:',
                                  Outcome,
                                  default=Outcome)
    # --- FILTER DATAFRAME BASED ON SELECTION
    mask = (df['Pregnancies'].between(*pgs_selection)) & (df['Outcome'].isin(df_selection))
    fig4 = px.box(df[mask], x="Outcome", y="Pregnancies", title="Diabetes outcome based on pregnancies")
    fig4.update_layout(
        font_family="Times new Roman",
        font_color="black",
        title_font_size=20
    )
    st.plotly_chart(fig4)
    st.subheader("Numerical Summary")
    t6=df[mask].groupby(['Outcome'])['Pregnancies'].aggregate(['mean', 'median', 'max', 'min'])
    st.dataframe(t6)
    st.subheader("Observation")
    st.write("1. From the above plot, we can see that the patient who have died due to diabetes have undergone maximum number of pregnancies than patients who is alive.")
    st.write("2. Also we could see that the minimum number of pregnancies is same for both patients who are alive and the patients who have died.")
    st.write("3. We can see that only few patients have pregnancy count greater than 11 for the patients who are alive.")
    st.write("4. By seeing the above plot, we could conclude that more number of pregnancies might be a reason for patients to die due to diabetes.")
def Age_plot():
     st.subheader("Visual Summary")
     Outcome = df['Outcome'].unique().tolist()
     ages = df['Age'].unique().tolist()
     age_selection = st.slider('Age:',
                               min_value=min(ages),
                               max_value=max(ages),
                               value=(min(ages), max(ages)))

     df_selection = st.multiselect('Outcome:',
                                           Outcome,
                                           default=Outcome)
     mask = (df['Age'].between(*age_selection)) & (df['Outcome'].isin(df_selection))
     fig3 = px.box(df[mask], x="Outcome", y="Age", title="Diabetes outcome based on Age")
     fig3.update_layout(
         font_family="Times new Roman",
         font_color="black",
         title_font_size=20
     )
     st.plotly_chart(fig3)
     st.subheader("Numerical Summary")
     t7 = df[mask].groupby(['Outcome'])['Age'].aggregate(['mean', 'median', 'max', 'min'])
     st.dataframe(t7)
     st.subheader("Observation")
     st.write("1. Maximum and minimum age of the patient who died is 70 and 21 respectively.")
     st.write("2. Also we could find the median age of the patient who died is more (i.e 36) compared to the patient who is alive (i.e 27).")
     st.write("3. We can also see that there are more number of patients who are alive and the maximum age is found to be 81.")
     st.write("4. Hence it could be concluded that age may not be reason for the patients to die due to diabetes.")
def per():
    options = st.selectbox('Select the variable of your choice',["Pregnancies","Age"])
    if options=='Pregnancies':
        Preg_plot()
    elif options=='Age':
        Age_plot()

def rep():
    st.header("REPORT")
    st.write("1. Count of patients who died is maximum with blood pressure ranging between 70-74, in which range we could see there are more number of patients who are alive. Hence it could be said that blood pressure does not affect the patients and it could not be a reason for patients leading to death.")
    st.write("2.  We could see that patients who have died had high BMI. Hence it can be concluded that high BMI can affect the patients leading to death.")
    st.write("3.  High glucose might be a reason for patients to die since there are more number of patients who died at higher glucose level.")
    st.write("4. Insulin level is consistent for patients who are alive compared to the patients who died. But greater insulin level is found to be for patients who died.")
    st.write("5.  Comparing the skin thickness level of patients who are alive and of the patients who died, it is found that patients who died had the higher skin thickness level.")
    st.write("6. The number of patients who died increased and is at maximum with diabetes pedigree function ranging between 0.25 to 0.299. But we could also see that with the same range there are more number of patients who are alive. Hence  we can conclude that diabetes pedigree function does not affect patients and may not be a reason for the patients to die.")
    st.write("7. Outcome of diabetes doesnt depend on age, diabetes pedigree function and blood pressure.")
    st.write("8.  Factors which affects outcome and can lead to death include BMI, glucos level, skin thickness, insulin level and pregnancies.")
def data():
    st.header("ABOUT THE DATASET")
    st.subheader("Anonymized factors of diabetes")
    st.write("Response variable of the dataset is found to be Outcome attribute which is a categorical variable and has 2 levels (dichotomous). The dataset contains 9 attributes and 768 rows in which all other attributes except Outcome are numerical. Also the dataset doesnt contain any null values in it")
    st.write("Attributes and their description:")
    st.write("1. Pregnancies - Number of pregnancies")
    st.write("2. Glucose - Tells about one's glucose level. A blood glucose test measures the level of glucose (sugar) in your blood. The expected values for normal fasting blood glucose concentration are between 70 mg/dL and 100 mg/dL")
    st.write("3. BloodPressure - Tells about the individual's blood pressure. A normal blood pressure level is less than 120/80 mmHg")
    st.write("4. SkinThickness - Tells about the thickness level of the skin")
    st.write("5. Insulin - Tells about the insulin level in the body. Insulin controls blood sugar levels. However, in people with certain medical conditions, such as diabetes, there can be abnormalities in insulin production or function, leading to high or low insulin levels, which can have significant health implications.")
    st.write("6. BMI - Body Mass Index (BMI) is a person’s weight in kilograms (or pounds) divided by the square of height in meters (or feet)")
    st.write("7. DiabetesPedigreeFunction - Calculates diabetes likelihood depending on the subject's age and his/her diabetic family history.")
    st.write("8. Age - Age of the patients")
    st.write("9. Outcome - Outcome of the diabetes (whether the patient is alive or dead)")
st.sidebar.title('Choose anyone')
side=st.sidebar.radio('Select what you want to display:', ["Home","About Dataset","Header Info","Medical Info","Personal Info","Report"])
if side=="Medical Info":
    med()
elif side=="Report":
    rep()
elif side=="Home":
    home()
elif side=="Header Info":
    header()
elif side=="Personal Info":
    per()
elif side=="About Dataset":
    data()

