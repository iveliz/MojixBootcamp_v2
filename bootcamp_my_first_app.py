import streamlit as st 



c1, c2, c3 = st.columns([1, 3, 3])
c1.image('imagenes/avatar.jpg', width=45)
c2.markdown('Iveliz A')

#c3.text(['imagenes/github.png']('https://sebastiandres.xyz'))
#c3.text(['imagenes/linkedin.png']('https://www.linkedin.com/in/iveliz-alexandra-ayala-lopez-79b2691b1/)'))
#c3.text(['imagenes/twitter_4.png']('https://sebastiandres.xyz'))

c2.markdown(f"#### @sebastiandres en ![]({repo_path}/github.png) ![]({repo_path}/twitter.png) ![]({repo_path}/linkedin.png)")
st.title('10 Cool Beginner Python Tricks That Will Make Your Life Easier')


 
     


