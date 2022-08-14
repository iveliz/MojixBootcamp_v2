import streamlit as st 



st.title('10 Cool Beginner Python Tricks That Will Make Your Life Easier')
st.subheader('Simple but effective tips for every python lovers')
st.image('imagenes/im.jpeg', caption='Photo by Miesha Maiden from Pexels')

st.markdown('#### The compactness of Python can make a developer’s life a lot easier when writing lines and lines of code. But there are some lesser-known Python tricks that can surprise you with their amazing capabilities.')
st.markdown('#### In today’s article, I will discuss 10 Python tips and tricks that will be really helpful for beginners to write more compact code. Knowing these tips and tricks will definitely save you some valuable time.')

st.header('1. Walrus operator')
st.markdown('##### The Walrus or := operator is one of the latest additions to python 3.8. It is an assignment operator that lets you assign value to a variable within an expression like conditional statements, loops, etc.')

st.subheader('Example')
st.markdown('##### If we want to check and print the length of a list:')

st.code('Mylist = [1,2,3]  print(l)')
st.code('if(l := len(mylist) > 2)')
st.code('print(1)')

st.subheader('Output')
st.code('3') 



