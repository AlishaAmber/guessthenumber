import random
import streamlit as st

# Streamlit UI setup
st.title("🎉 Ultimate Number Guessing Game 🔢🎯")
st.write("I'm thinking of a number between 1 and 100. Can you guess it? 🤔🔢")

# Initialize session state variables
if 'number' not in st.session_state:
    st.session_state.number = random.randint(1, 100)  # Secret number
    st.session_state.guesses_left = 7

guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)

if st.button("Submit Guess"):
    if st.session_state.guesses_left > 0:
        if guess < st.session_state.number:
            st.warning("Too low! Try another number. 📉🔢")
        elif guess > st.session_state.number:
            st.warning("Too high! Try another number. 📈🔢")
        else:
            st.success(f"🎉 Congratulations! You guessed the correct number in {7 - st.session_state.guesses_left + 1} tries.")
            st.session_state.number = random.randint(1, 100)  # Reset game
            st.session_state.guesses_left = 7
            st.stop()

        st.session_state.guesses_left -= 1

    if st.session_state.guesses_left == 0:
        st.error(f"😢 You've used all your guesses! The correct number was {st.session_state.number}.")
        st.session_state.number = random.randint(1, 100)  # Reset game
        st.session_state.guesses_left = 7
