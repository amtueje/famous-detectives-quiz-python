# famous-detectives-quiz-python
Daily challenge from Day 5 of the "100 Days of Code" course on Replit.

# Famous Detectives Python Quiz

This beginner Python problem demonstrates a fun and interactive way to use "if" statements. Users are asked a series of questions to identify which famous detective character they might be, based on their answers.

## Problem Statement

Ask users a series of questions to determine if they resemble one of the famous detective characters in the quiz. Use multiple "if" statements to check the user's responses to each question. If the user doesn't match any of the detective characters, provide a final message indicating that they may need to brush up on their knowledge of famous detectives from literature and TV.

## Implementation

The programme uses the "input()" function to prompt the user for answers to the questions. "If" statements are used to check the user's responses and print a message indicating the detective character they match. If the user doesn't match any of the characters, a final message is displayed.

## Note

The first version of this code contained a logical error in the "if" statement comparisons. The error was corrected by changing the comparisons to the proper format, e.g., `if gotViolin == "Yes" or gotViolin == "Y":` Previously, I had used, `if gotViolin == "Yes" or "Y":`.
