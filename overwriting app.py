# %%writefile app.py
import streamlit as st

st.title("welcome streamlit")
st.header("this is header")
st.subheader("this is subheader")
formula = ''' a+b '''
st.latex(formula)
python_code = '''
     a = 9
     b=4
     c=78
     v = a+b+c
     print(v)

    '''
st.code(python_code, language='python')
st.header("Python")
st.caption("python is good lang ")

