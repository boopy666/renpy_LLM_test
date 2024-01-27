# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define m = Character("Maddy")

label start:
    python:
        while True:
            user_input = renpy.input("What will you say to Maddy")

            # Check if the user input is the break command
            if user_input == "==break==":
                break

            response = send_prompt(user_input)

            if response["success"]:
                ai_response = response["data"]["choices"][0]["message"]["content"]

                # Escape curly braces in the AI response
                ai_response = ai_response.replace("{", "{{").replace("}", "}}")

                renpy.say(m, ai_response)
            else:
                error_message = str(response["error"])  # Convert error to a string
                renpy.say(None, "Error: " + error_message)

    "Conversation ended."

    return
