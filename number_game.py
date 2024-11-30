import random
import streamlit as st

# Custom CSS to hide the GitHub icon
hide_github_icon = """
<style>
#GithubIcon {
  visibility: hidden;
}
</style>
"""

# Apply the CSS
st.markdown(hide_github_icon, unsafe_allow_html=True)

# Set up the Streamlit app
st.title("Number Guessing Game 🎯")

# Add a GIF or image from a URL
st.image("https://media.giphy.com/media/l0HlHJGHe4BGjJrSo/giphy.gif", caption="Guess the Number Game!", use_column_width=True)

# Range slider for setting the minimum and maximum values
st.header("Set the Range")
min_value, max_value = st.slider(
    "Select the range for the game:",
    min_value=1,
    max_value=500,
    value=(1, 100),
    step=1
)

# Slider for setting lives
lives = st.slider("Select the number of lives:", min_value=1, max_value=10, value=5, step=1)

# Initialize session state variables
if "secret_number" not in st.session_state:
    st.session_state.secret_number = random.randint(min_value, max_value)
    st.session_state.attempts = 0
    st.session_state.lives = lives
    st.session_state.game_over = False

# Display instructions
st.write(f"Guess the number between {min_value} and {max_value}!")
st.write(f"Lives remaining: {st.session_state.lives}")

# Game logic
if st.session_state.game_over:
    if st.session_state.lives == 0:
        st.error(f"Game Over! You've run out of lives. The number was {st.session_state.secret_number}. 😢")
        st.image("https://media.giphy.com/media/3o7aD4WOlffBBQQtdG/giphy.gif", caption="Better Luck Next Time!", use_column_width=True)
    else:
        st.success(f"Congratulations! You guessed the number: {st.session_state.secret_number} 🎉")
        st.image("https://media.giphy.com/media/111ebonMs90YLu/giphy.gif", caption="You Won!", use_column_width=True)

    if st.button("Play Again"):
        st.session_state.secret_number = random.randint(min_value, max_value)
        st.session_state.attempts = 0
        st.session_state.lives = lives
        st.session_state.game_over = False
else:
    guess = st.number_input("Enter your guess:", min_value=min_value, max_value=max_value, step=1, key="guess_input")
    if st.button("Submit Guess"):
        st.session_state.attempts += 1
        if guess < st.session_state.secret_number:
            st.session_state.lives -= 1
            st.warning("Too low! Try again.")
        elif guess > st.session_state.secret_number:
            st.session_state.lives -= 1
            st.warning("Too high! Try again.")
        else:
            st.session_state.game_over = True
            st.success(f"You got it in {st.session_state.attempts} attempts!")

        if st.session_state.lives == 0:
            st.session_state.game_over = True
