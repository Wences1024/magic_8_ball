# Magic 8 Ball Simulation

This project implements a simulation of the classic Magic 8 Ball toy. Users can ask questions, and the program responds with a randomly generated answer, categorized into affirmative, non-committal, and negative responses. The program continues until the user types `exit`.

## Features
- Provides responses categorized into:
  - Affirmative answers
  - Non-committal answers
  - Negative answers
- Interactive console-based experience.

## How to Run
1. Save the code in a file named, for example, `magic_8_ball.py`.
2. Run the script using Python:
   ```bash
   python magic_8_ball.py
   ```
3. Follow the on-screen instructions:
   - Type your question to get an answer.
   - Type `exit` to end the program.

## Prerequisites
Ensure you have Python installed on your system. No additional libraries are required as the program only uses built-in modules.

## Code Overview
The script contains the following components:

### `MagicBall` Class
- **Attributes:**
  - `answ`: A dictionary containing categorized responses:
    - Affirmative (10 responses)
    - Non-committal (5 responses)
    - Negative (5 responses)
- **Methods:**
  - `Answer()`: Generates a random answer from one of the three categories and returns it.

### Main Functionality
- Creates an instance of the `MagicBall` class.
- Greets the user and provides instructions.
- Enters a loop where:
  - The user inputs a question.
  - The program responds with a random answer.
  - Exits when the user types `exit`.

## Example Output
```
Welcome to magic 8 Ball!
Ask any question, and I'll answer it for you!
Type exit when you are done

Ask your question: Will I pass my exam?
It is decidedly so

Ask your question: Should I go on a trip?
Reply hazy, try again

Ask your question: exit
```

## Notes
- The program uses `os.system("cls")` to clear the console on Windows systems. If you're using Linux or macOS, you can replace it with `os.system("clear")`.
- The answers are pre-defined and categorized into 3 types to mimic the behavior of a real Magic 8 Ball.

## License
This project is open-source and available under the MIT License.
