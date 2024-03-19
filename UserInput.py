import streamlit as st

def main():
    st.title("Age Classifier")

    # Get user input
    name = st.text_input("Enter your name:")
    age = st.number_input("Enter your age:", min_value=0)

    # Determine age category
    if age < 18:
        message = f"{name}, you are a child."
    elif age == 18:
        message = f"{name}, you are an adult."
    elif age > 18:
        message = f"{name}, you are young."
    else:
        message = f"{name}, please enter a valid age."

    # Display message
    if st.button("Submit"):
        st.write(message)

if __name__ == "__main__":
    main()
