# Rock Paper Scissors Game

This is a simple web-based Rock Paper Scissors game developed using Flask. The game allows a user to play against the computer, which randomly selects its move.

## Prerequisites

- Python 3.x
- Flask

## Installation

1. **Clone the repository** (or download the files):
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Create a virtual environment** (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Flask**:
    ```bash
    pip install flask
    ```

## Running the Application

1. **Navigate to the project directory**.
2. **Run the Flask application**:
    ```bash
    python app.py
    ```
3. **Open your web browser** and go to `http://127.0.0.1:5000` to play the game.

## Application Structure

- `app.py`: Main application file containing the Flask routes and game logic.
- `templates/`: Directory containing HTML templates for the homepage and result page.

## Game Logic

The game consists of the following logic:

- The user selects their choice (Rock, Paper, or Scissors) via a form.
- The computer randomly selects its choice.
- The winner is determined based on traditional Rock Paper Scissors rules:
  - Rock beats Scissors
  - Scissors beat Paper
  - Paper beats Rock
  - If both choices are the same, it is a tie.

## Flask Routes

- **`/`** (GET and POST): 
  - **GET**: Renders the homepage where the user can select their choice.
  - **POST**: Processes the user's choice, computes the result, and renders the result page with the outcome.

## HTML Templates

- `home.html`: The homepage where the user can choose Rock, Paper, or Scissors.
- `result.html`: The result page that displays whether the user won, lost, or tied the round, along with appropriate styling based on the outcome.


## Conclusion

This simple Rock Paper Scissors game demonstrates the basics of using Flask to handle user input, process game logic, and render HTML templates based on the game's outcome. Enjoy playing and tweaking the game to add more features or improve the design!