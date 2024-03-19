import streamlit as st

def main():
    st.title("Age Classifier")

    # Get user input
    name = st.text_input("Enter your name:")
    age = st.number_input("Enter your age:", min_value=0)

    # Determine age category
    if age < 18:
        message = "You are a child."
    elif age == 18:
        message = "You are young."
    elif age > 18 and age < 65:
        message = "You are mature."
    else:
        message = f"{name}, tu mara nae abhy tak."

    # Display message
    if st.button("Submit"):
        st.write(message)

if __name__ == "__main__":
    main()
