import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image
def home():
    st.title("Welcome to Diabetes data presentation")
    st.write("Diabetes is a condition that happens when your blood sugar (glucose) is too high. It develops when your pancreas doesn’t make enough insulin or any at all, or when your body isn’t responding to the effects of insulin properly. Diabetes affects people of all ages. Most forms of diabetes are chronic (lifelong), and all forms are manageable with medications and/or lifestyle changes.")
    image = Image.open('diabetes.png')
    st.image(image,caption='Diabetes')
df=pd.read_csv("diabetes-vid.csv")
df.rename(columns={'DiabetesPedigreeFunction':'Dp',
                   'BloodPressure':'BP'},inplace = True)
def header():
    st.header("Data Header")
    st.write(df.head())
def med():
    tab1,tab2,tab3,tab4,tab5,tab6=st.tabs(["BP","BMI","Glucose","SkinThickness","Insulin","Diabetes Pedigree Function"])
    with tab1:
        st.subheader("Visual Summary")
        bp_selection=st.slider('Blood Pressure:',
                                  min_value=min(df['BP']),
                                  max_value=max(df['BP']),
                                  value=(min(df['BP']), max(df['BP'])))
        mask=(df['BP'].between(*bp_selection))
        fig1= px.histogram(df[mask], x="BP", color="Outcome", title="Diabetes outcome based on Blood Pressure")
        fig1.update_layout(
            font_family="Times new Roman",
            font_color="black",
            title_font_size=20
        )
        st.plotly_chart(fig1)
        st.subheader("Numerical Summary")
        t=df[mask].groupby(['Outcome'])['BP'].aggregate(['sum','mean','median','max','min'])
        st.dataframe(t)
    with tab2:
        st.subheader("Visual Summary")
        Outcome = df['Outcome'].unique().tolist()
        bmi = df['BMI'].unique().tolist()

        bmi_selection = st.slider('BMI:',
                                  min_value=min(bmi),
                                  max_value=max(bmi),
                                  value=(min(bmi), max(bmi)))

        df_selection = st.multiselect('Outcome:',
                                      Outcome,
                                      default=Outcome)

        # --- FILTER DATAFRAME BASED ON SELECTION
        mask = (df['BMI'].between(*bmi_selection)) & (df['Outcome'].isin(df_selection))
        fig2= px.box(df[mask], x="Outcome", y="BMI", title="Diabetes outcome based on BMI")
        fig2.update_layout(
            font_family="Times new Roman",
            font_color="black",
            title_font_size=20
        )
        st.plotly_chart(fig2)
        st.subheader("Numerical Summary")
        t1=df.groupby(['Outcome'])['BMI'].aggregate(['sum', 'mean', 'median', 'max', 'min'])
        st.dataframe(t1)
    with tab3:
        st.subheader("Visual Summary")
        glucose_selection = st.slider('Glucose level:',
                                 min_value=min(df['Glucose']),
                                 max_value=max(df['Glucose']),
                                 value=(min(df['Glucose']), max(df['Glucose'])))
        mask = (df['Glucose'].between(*glucose_selection))
        fig5 = px.histogram(df[mask], x="Glucose", color="Outcome", title="Diabetes Outcome based on Glucose level")
        fig5.update_layout(
            font_family="Times new Roman",
            font_color="black",
            title_font_size=20
        )
        st.plotly_chart(fig5)
        st.subheader("Numerical Summary")
        t2 = df[mask].groupby(['Outcome'])['Glucose'].aggregate(['sum', 'mean', 'median', 'max', 'min'])
        st.dataframe(t2)
    with tab4:
        st.subheader("Visual Summary")
        fig6 = px.histogram(df, x="Outcome", y="SkinThickness",
                            title="Diabetes outcome based on the thickness of skin")
        fig6.update_layout(
            font_family="Times new Roman",
            font_color="black",
            title_font_size=20
        )
        st.plotly_chart(fig6)
        st.subheader("Numerical Summary")
        t3 = df.groupby(['Outcome'])['SkinThickness'].aggregate(['sum', 'mean', 'median', 'max', 'min'])
        st.dataframe(t3)
    with tab5:
        st.subheader("Visual Summary")
        fig7 = px.box(df, y="Insulin", x="Outcome", title="Diabetes outcome based on Insulin")
        fig7.update_layout(
            font_family="Times new Roman",
            font_color="black",
            title_font_size=20
        )
        st.plotly_chart(fig7)
        st.subheader("Numerical Summary")
        t4 = df.groupby(['Outcome'])['Insulin'].aggregate(['sum', 'mean', 'median', 'max', 'min'])
        st.dataframe(t4)
    with tab6:
        st.subheader("Visual Summary")
        fig8 = px.histogram(df, x="Dp", color="Outcome", title="Diabetes outcome based on the Pedigree function")
        st.plotly_chart(fig8)
        st.subheader("Numerical Summary")
        t5 = df.groupby(['Outcome'])['Dp'].aggregate(['sum', 'mean', 'median', 'max', 'min'])
        st.dataframe(t5)
def Preg_plot():
    st.subheader("Visual Summary")
    fig4 = px.box(df, x="Outcome", y="Pregnancies", title="Diabetes outcome based on pregnancies")
    fig4.update_layout(
        font_family="Times new Roman",
        font_color="black",
        title_font_size=20
    )
    st.plotly_chart(fig4)
    st.subheader("Numerical Summary")
    t6=df.groupby(['Outcome'])['Pregnancies'].aggregate(['mean', 'median', 'max', 'min'])
    st.dataframe(t6)
def Age_plot():
     st.subheader("Visual Summary")
     Outcome = df['Outcome'].unique().tolist()
     ages = df['Age'].unique().tolist()

     age_selection = st.slider('Age:',
                            min_value= min(ages),
                            max_value= max(ages),
                            value=(min(ages),max(ages)))

     df_selection = st.multiselect('Outcome:',
                                        Outcome,
                                        default=Outcome)

    # --- FILTER DATAFRAME BASED ON SELECTION
     mask = (df['Age'].between(*age_selection)) & (df['Outcome'].isin(df_selection))
     fig3 = px.box(df[mask], x="Outcome", y="Age", title="Diabetes outcome based on Age")
     fig3.update_layout(
         font_family="Times new Roman",
         font_color="black",
         title_font_size=20
     )
     st.plotly_chart(fig3)
     st.subheader("Numerical Summary")
     t7 = df.groupby(['Outcome'])['Age'].aggregate(['mean', 'median', 'max', 'min'])
     st.dataframe(t7)

def per():
    options = st.selectbox('Select the variable of your choice',["Pregnancies","Age"])
    if options=='Pregnancies':
        Preg_plot()
    elif options=='Age':
        Age_plot()

def rep():
    st.header("REPORT")
def data():
    st.header("ABOUT THE DATASET")
    st.write("Anonymized factors of diabetes")
    st.write("Response variable of the dataset is found to be Outcome attribute which is a categorical variable and has 2 levels (dichotomous). The dataset contains 9 attributes and 768 rows in which all other attributes except Outcome are numerical. Also the dataset doesnt contain any null values in it")
    st.write("Attributes and their description:")
    st.write("1. Pregnancies - Number of pregnancies")
    st.write("2. Glucose - Glucose level: The expected values for normal fasting blood glucose concentration are between 70 mg/dL and 100 mg/dL")
    st.write("3. Blood Pressure - Blood Pressure: A normal blood pressure level is less than 120/80 mmHg")
    st.write("4. Skin Thickness - Thickness of the skin")
    st.write("5. Insulin - Insulin level")
    st.write("6. BMI - Body Mass Index")
    st.write("7. Diabetes Pedigree Function - Calculates diabetes likelihood depending on the subject's age and his/her diabetic family history.")
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

