import streamlit as st 



st.title('10 Cool Beginner Python Tricks That Will Make Your Life Easier')
st.subheader('Simple but effective tips for every python lovers')
st.image('imagenes/im.jpeg', caption='Photo by Miesha Maiden from Pexels')

st.markdown('##### The compactness of Python can make a developer’s life a lot easier when writing lines and lines of code. But there are some lesser-known Python tricks that can surprise you with their amazing capabilities.')
st.markdown('##### In today’s article, I will discuss 10 Python tips and tricks that will be really helpful for beginners to write more compact code. Knowing these tips and tricks will definitely save you some valuable time.')

st.header('1. Walrus operator')
st.markdown('##### The Walrus or := operator is one of the latest additions to python 3.8. It is an assignment operator that lets you assign value to a variable within an expression like conditional statements, loops, etc.')

st.subheader('Example')
st.markdown('##### If we want to check and print the length of a list:')

st.code('Mylist = [1,2,3]  print(l)')
st.code('if(l := len(mylist) > 2)')
st.code('print(1)')

st.subheader('Output')
st.code('3') 
###################################################################################
st.header('2. Splitting a string')
st.markdown('##### If you want to split the components of a string into a list you can do that easily using the split() function in python. This will make the string operations a lot easier! ')

st.subheader("Example")
st.code('string = “hello world”')
st.code('string.split()')

st.subheader('Output')
st.code('[‘hello’, ‘world’]')

###################################################################################
st.header('3. Reversing a string')
st.markdown('##### If you want to reverse a given string, you can do that with only one line of code using the negative indexing of the string.')

st.subheader("Example")
st.code('str=”hello world!”')
st.code('a=str[::-1]')
st.code('print(a)')

st.subheader('Output')
st.code('!dlrow olleh')

###################################################################################
st.header('4. Merging two dictionaries')
st.markdown('##### This amazing trick will help you merge two dictionaries with just 1 line of code. We just need to use ** in front of the name of the two dictionaries like below two merge them into a single dictionary: ')

st.subheader("Example")
st.code('d1 = {“a”: 10, “b”:20}')
st.code('d2 = {“c”: 30, “d”:40}')
st.code('d3 = {**d1, **d2}')
st.code('print(d3)')

st.subheader('Output')
st.code('{‘a’: 10, ‘b’: 20, ‘c’: 30, ‘d’: 40}')
###################################################################################
st.header('5. The zip() function')
st.markdown('##### The zip() function in python can make your life a lot easier when working with lists and dictionaries. It is used to combine several lists of the same length.')

st.subheader("Example")
st.code('colour = [“red”, “yellow”, “green”]')
st.code('fruits = [‘apple’, ‘banana’, ‘mango’]')
st.code('for colour, fruits in zip(colour, fruits):')
st.code('print(colour, fruits)')

st.subheader('Output')
st.code('red apple')
st.code('yellow banana')
st.code('green mango')

st.markdown('##### The zip() function can also be used for combining two lists into a dictionary. This method can be really helpful while grouping data from the list.')
###################################################################################
st.header('6. Assigning multiple list values to a variable')
st.markdown('##### If you want to assign some specific values of a list to a variable and all the remaining values to another variable in a list format, you can use the following technique:')

st.subheader("Example")
st.code('mylist = [1,2,3,4,5]')
st.code('a,*b = mylist')
st.code('print(f”a =”,a)')
st.code('print(f”b =”,b)')

st.subheader('Output')
st.code('a = 1')
st.code('b = [2, 3, 4, 5]')
st.markdown('##### This process is also called list unpacking and you can apply this method for more than 2 variables also!')
###################################################################################
st.header('7. Remove duplicate list items')
st.markdown('##### Do you have duplicate items in your list which you want to remove? You can do that with only one line of code using the set() function.')

st.subheader("Example")
st.code('mylist = [1,1,1,2,2,3,3,4,4,5,6,7,7,8,9]')
st.code('newlist = set(mylist)')
st.code('print(newlist)')

st.subheader('Output')
st.code('{1, 2, 3, 4, 5, 6, 7, 8, 9}')
###################################################################################
st.header('8. Lambda function')
st.markdown('##### If you need a function that is not very complicated, it can be done easily in one line using lambda. They are also called anonymous functions and are used heavily in data science and web development.')

st.subheader("Example")
st.markdown('##### Let’s say you want to write a function to multiply two numbers. Instead of writing a conventional function, you can do that in one line using :')
st.code('mul = lambda a,b: a*b')
st.code('mul(5,6)')

st.subheader('Output')
st.code('30')
###################################################################################
st.header('9. Swapping variable value')
st.markdown('##### One of the first programs that we learn while learning about variables is swapping the values of two variables. In python you can achieve that with one line of code:')

st.subheader("Example")
st.code('a = 100')
st.code('b = 200')
st.code('a,b =b,a')
st.code('print(f’a = ‘,a)')
st.code('print(f’b = ‘,b)')

st.subheader('Output')
st.code('a = 200, b = 100')
###################################################################################
st.header('10. Use a password in your code')
st.markdown('##### This python trick is amazing for securing your code with a password. We will use the getpass() function from the library getpass which encodes your input. This will prevent anyone from running the code without a password. Isn’t that cool!')

st.subheader("Example")
st.code('from getpass import getpass')
st.code('password = getpass(“password: “)')
st.code('if password == “abcd”:')
st.code('     print(“welcome strnger!”)')
st.code('else:')
st.code('     print(“wrong password”)')

st.subheader('Output')
st.code('password: **** [abcd]')
st.code('Welcome stranger!')
st.code('Password: **** [abdc]')
st.code('Wrong password')

st.markdown('##### _Here is a book on Python programming that I would definitely recommend for all beginners._')

st.header('Conclusion')
st.markdown('##### These were a few amazing Python tips and tricks which will make your work a lot easier while coding. There are many more shortcuts like these that you can explore from the official documentation or any other website.')
st.markdown('##### _Note: This article contains an affiliate link. This means that if you click on it and choose to buy the resource I linked above, a small portion of your subscription fee will go to me._')
st.markdown('##### _However, the recommended resource is experienced by me and helped me in my data science career journey._')

st.markdown('#### Before you go…')
st.markdown('##### If you liked this article and want to stay tuned with more exciting articles on Python & Data Science — do consider becoming a medium member by clicking here https://pranjalai.medium.com/membership.')
st.markdown('##### Please do consider signing up using my referral link. In this way, the portion of the membership fee goes to me, which motivates me to write more exciting stuff on Python and Data Science.')
st.markdown('##### Also, feel free to subscribe to my free newsletter: Pranjal’s Newsletter.')

st.text('Thanks to Elliot Gunn')

