from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)

# !!! IMPORTANT !!! 
# A secret key is required to use Flask Sessions. 
# In a real-world app, use a strong, random key and set it via an environment variable.
app.secret_key = 'your_very_secret_key_here' # <-- CHANGE THIS

# Set the range for the guessing game
MIN_NUM = 1
MAX_NUM = 100

def generate_secret_number():
    """Generates a new random number and stores it in the session."""
    session['secret_number'] = random.randint(MIN_NUM, MAX_NUM)
    session['guess_count'] = 0

@app.route('/')
def index():
    # If a new session starts or the game needs to be reset, generate a new number
    if 'secret_number' not in session:
        generate_secret_number()
        
    # Provide hints and welcome message
    message = f"Guess a number between {MIN_NUM} and {MAX_NUM}."
    
    return render_template('index.html', 
                           message=message, 
                           guess_count=session.get('guess_count', 0))

@app.route('/guess', methods=['POST'])
def guess():
    try:
        # Get the user's guess and convert it to an integer
        user_guess = int(request.form.get('guess'))
    except (ValueError, TypeError):
        # Handle invalid input gracefully
        message = "Invalid input! Please enter a whole number."
        return render_template('index.html', 
                               message=message, 
                               guess_count=session.get('guess_count', 0))

    # Check if the secret number exists in the session (it should)
    if 'secret_number' not in session:
        return redirect(url_for('index'))

    # Increment the guess count
    session['guess_count'] += 1
    secret_number = session['secret_number']
    
    if user_guess == secret_number:
        # Correct Guess
        message = f"🥳 **Congratulations!** You guessed the number {secret_number} in {session['guess_count']} guesses."
        # Clear session to allow a new game
        session.pop('secret_number', None)
        return render_template('result.html', message=message)

    elif user_guess < secret_number:
        # Too Low
        message = f"Too **Low**! Try again. (Guess #{session['guess_count']})"
    else: # user_guess > secret_number
        # Too High
        message = f"Too **High**! Try again. (Guess #{session['guess_count']})"

    return render_template('index.html', 
                           message=message, 
                           guess_count=session['guess_count'])

@app.route('/reset')
def reset():
    # Clear the session variables and redirect to start a new game
    session.pop('secret_number', None)
    session.pop('guess_count', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    # Flask application runs on all interfaces (0.0.0.0) and port 5000
    app.run(host = "0.0.0.0", port=5000)