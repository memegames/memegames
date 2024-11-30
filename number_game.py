import random
import streamlit as st

st.title("Meme Games 🎮")

# Dropdown menu to select the game
game_choice = st.selectbox("Choose a Game:", options=["","Number Guessing Game", "Rock, Paper, Scissors"])

if game_choice == "Rock, Paper, Scissors":
    st.header("Rock, Paper, Scissors ✊✋✌️")

    # Define the choices
    choices = ["Rock", "Paper", "Scissors"]

    # Player's choice
    player_choice = st.selectbox("Make your choice:", choices)

    if st.button("Play!"):
        # Computer's choice
        computer_choice = random.choice(choices)

        # Show choices
        st.write(f"**You chose:** {player_choice}")
        st.write(f"**Computer chose:** {computer_choice}")

        # Determine the winner
        if player_choice == computer_choice:
            st.info("It's a tie! 🤝")
        elif (player_choice == "Rock" and computer_choice == "Scissors") or \
             (player_choice == "Paper" and computer_choice == "Rock") or \
             (player_choice == "Scissors" and computer_choice == "Paper"):
            st.success("You win! 🎉")
        else:
            st.error("You lose! 😢")

elif game_choice == "Number Guessing Game":
    st.header("Number Guessing Game 🎯")

    # Restart button at the top
    if st.button("Restart Game 🔄"):
        # Reset session state variables
        st.session_state.secret_number = None
        st.session_state.attempts = 0
        st.session_state.lives = 0
        st.session_state.game_over = False
        st.experimental_rerun()

    # Range slider for min and max values
    min_value, max_value = st.slider(
        "Select the number range:",
        min_value=1,
        max_value=500,
        value=(1, 100),
        step=1
    )

    # Slider for selecting lives
    lives = st.slider("Select the number of guesses:", min_value=1, max_value=10, value=5, step=1)

    # Initialize session state variables
    if "secret_number" not in st.session_state:
        st.session_state.secret_number = random.randint(min_value, max_value)
        st.session_state.attempts = 0
        st.session_state.lives = lives
        st.session_state.game_over = False

    # Game instructions
    st.write(f"Guess the number between {min_value} and {max_value}!")
    st.write(f"Lives remaining: {st.session_state.lives}")

    if st.session_state.game_over:
        if st.session_state.lives == 0:
            st.error(f"Game Over! You've run out of lives. The number was {st.session_state.secret_number}. 😢")
        else:
            st.success(f"Congratulations! You guessed the number: {st.session_state.secret_number} 🎉")

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
                # Display the image for a wrong guess
                st.image(
                    "https://raw.githubusercontent.com/memegames/memegames/main/guess.png", 
                    caption="Wrong guess! Try again!", 
                    use_column_width=True
                )
            elif guess > st.session_state.secret_number:
                st.session_state.lives -= 1
                st.warning("Too high! Try again.")
                # Display the image for a wrong guess
                st.image(
                    "https://raw.githubusercontent.com/memegames/memegames/main/guess.png", 
                    caption="Wrong guess! Try again!", 
                    use_column_width=True
                )
            else:
                st.session_state.game_over = True
                st.success(f"You got it in {st.session_state.attempts} attempts!")
            if st.session_state.lives == 0:
                st.session_state.game_over = True
