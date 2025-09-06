import streamlit as st
import cv2        
import numpy as np
import os
import base64   

st.set_page_config(page_title="Dart To Done", page_icon="🎉", layout="wide")

st.title("Dart To Done 🎇🎉")

def Image(path=None, caption=""):
    if path is None:
        st.warning("⚠️ No image path provided")
        return                       
    
    if isinstance(path, str):  
        if not os.path.exists(path):
            st.error(f"File not found: {path}")
            return
        image = cv2.imread(path)
    else:  
        image = path.read()
        np_imgage = np.frombuffer(image, np.uint8)
        image = cv2.imdecode(np_imgage, cv2.IMREAD_COLOR)

    result_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    _, buffer = cv2.imencode(".png", result_image)
    encoded_image = base64.b64encode(buffer).decode("utf-8")

    st.markdown(
        f"""
        <div style='text-align: center; margin:20px 0;'>
            <img src='data:image/png;base64,{encoded_image}'
                 style='max-width:80%; height:auto; border-radius:10px; box-shadow: 0px 4px 10px rgba(0,0,0,0.2);'/>
            <p style="font-size:16px; font-weight:bold; color:#444;">{caption}</p>
        </div>
        """,
        unsafe_allow_html=True
    )


def description_box(text, color):
    st.markdown(
        f"""
        <div style='
            background-color: var(--background-color-secondary);
            color: var(--text-color);
            padding:15px;
            border-radius:12px;
            border: 2px solid {color};
            margin-top:10px;
            margin-bottom:10px;
            line-height:1.6;
            font-size:16px;
            text-align:justify;'>
            {text}
        </div>
        """,
        unsafe_allow_html=True
    )


st.subheader("Part_1")
Image("images/Screenshot 2025-09-03 163021.png", "Code Example")

if st.button("click here to see the description of the code", key="des_1", type="primary"):
    description_box(
        "In the first line we use <code>void main (){.......}</code> and this is the main function of the application; all codes execute in it.<br><br>"
        "In the second line you can see <code>//</code>. When we start the code with this sign it means this is a <b>comment</b> to describe what the code does.<br><br>"
        "In the third line we want to apply a <b>variable</b>. To create one, we start by the type {String, Integer, Bool, etc.}, then set the variable name.<br><br>"
        "In the fourth line you can see <b>print</b>. We use <code>print(......);</code> to print anything inside the brackets.<br><br>"
        "If you want to write a string you should use <code>\"\"</code> or <code>''</code>. Numbers and floats don’t need quotes.<br><br>"
        "For example: <code>('4+5')</code> will print '4+5', but <code>(4+5)</code> will print 9.<br><br>"
        "In the sixth line you can see a new variable of type <b>int</b>.<br><br>"
        "💡 Hint: If you declare a variable as <b>String</b> you cannot change its type, but if you set it as <b>dynamic</b> you can change it.",
        "#1E90FF"
    )

if st.button("Click to see the result of the code", key="button_1"):
    Image("images/re_1.png", "Result Example")


st.subheader("Part_2")
Image("images/Screenshot 2025-09-03 170447.png", "Code Example")

if st.button("click here to see the description of the code", key="des_2", type="primary"):
    description_box(
        "I will skip some lines from now and so on because they have already been explained.<br><br>"
        "Third line has <code>String?</code> and this means the variable could be <b>null</b> or <b>String</b>, but <code>String</code> alone can only be String.<br><br>"
        "Fifth line says if the variable is still null then print the value (salem).<br><br>"
        "The last line indicates that if the value equals null, no error is set but the function is not applied.",
        "#32CD32"
    )

if st.button("Click to see the result of the code", key="button_2"):
    Image("images/re_2.png", "Result Example")


st.subheader("Part_3_If_Statement")
Image("images/3.png", "If Statement Example")

if st.button("click here to see the description of the code", key="des_3", type="primary"):
    description_box(
        "If Statement is used when we want to execute code according to some condition.<br><br>"
        "For example, if we want a program to determine if a student is failed or not, we can use an If Statement.<br><br>"
        "We write: <code>if (condition){ print('failed'); }</code><br><br>"
        "If you want to write more than one condition, you will use <code>else if (condition){ ... }</code>.<br><br>"
        "And <code>else</code> is written without condition, it runs if no other conditions are true.",
        "#FFA500"
    )

if st.button("Click to see the result of the code", key="button_3"):
    Image("images/re3.png", "Result Example")


st.subheader("Part_4")
Image("images/4.png", "Loop Example")

if st.button("click here to see the description of the code", key="des_4", type="primary"):
    description_box(
        "<b>For loop:</b> we use it if we want to do something multiple times.<br><br>"
        "For example, if I want to write 'Hello' 10 times, you write:<br>"
        "<code>for (int i = 0; i &lt; 10; i++)</code><br><br>"
        "<b>While loop:</b> works according to a condition. If the condition is true, it continues; if false, it stops immediately.",
        "#FF4500"
    )

if st.button("Click to see the result of the code", key="button_4"):
    Image("images/re4.png", "Result Example")


st.subheader("Part_5_Function")
Image("images/5.png", "Function Example")
Image("images/5_.png", "Function Call Example")

if st.button("click here to see the description of the code", key="des_5", type="primary"):
    description_box(
        "Now the description of the function:<br><br>"
        "We use functions to avoid writing the same code many times.<br><br>"
        "For example, if you have a greeting message for customers, instead of writing it each time, create a function and call it when needed.<br><br>"
        "Code:<br>"
        "• In the first line you can see <code>void</code>, this means the function will not return anything.<br>"
        "• In the second function you see <code>String</code>, this means it will return a String.<br>"
        "• In the third function there is nothing before the function name, meaning it can return anything (not specifically declared).<br><br>"
        "By this knowledge you can understand the following functions.<br><br>"
        "In the second image, you see the <b>calling</b> of the function: write the function name + <code>()</code>, and if there are arguments, pass them inside.",
        "#8A2BE2"
    )

if st.button("Click to see the result of the code", key="button_5"):
    Image("images/re5.png", "Result Example")


st.subheader("Last_Part")
Image("images/6.png", "Arrow Function Example")

if st.button("click here to see the description of the code", key="des_6", type="primary"):
    description_box(
        "In this stage I will describe the new structure for functions called <b>arrow function</b>.<br><br>"
        "We use it if we want to return something directly without any additional operations.",
        "#FF1493"
    )

if st.button("Click to see the result of the code", key="button_6"):
    Image("images/re_la.png", "Result Example")
