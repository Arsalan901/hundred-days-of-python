import streamlit as st

def main():
    st.title("User Information")

    # Get user input
    name = st.text_input("Enter your name:")
    age = st.number_input("Enter your age:", min_value=0, max_value=150, step=1)
    gender = st.selectbox("Select your gender:", ["Awesome", "Handsome", "Beautiul"])

    # Display message
    if st.button("Submit"):
        st.write(f"Your name is {name}, your age is {age}, and you are {gender}.")

if __name__ == "__main__":
    main()
