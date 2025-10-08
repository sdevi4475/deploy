st.title("welcome streamlit")
st.header("this is header")
st.subheader("this is subheader")
formula1 = ''' a+b '''
st.latex(formula1)
formula = ''' (a+b)2 =  a2+b2+2ab '''
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
