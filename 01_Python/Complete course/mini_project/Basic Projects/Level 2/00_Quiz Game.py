import random

# 6. Simple Quiz Game
#    - Ask multiple-choice questions.
#    - Keep score of correct answers.


# store the quiz questions in list or dict

score =0
quiz = [
    {
        "question": "What is the capital of France?",
        "a": "Berlin",
        "b": "Madrid",
        "c": "Paris",
        "d": "Rome",
        "answer": "c",
    },
    {
        "question": "Who wrote Romeo and Juliet?",
        "a": "Charles Dickens",
        "b": "William Shakespeare",
        "c": "Jane Austen",
        "d": "Mark Twain",
        "answer": "b",
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "a": "Earth",
        "b": "Mars",
        "c": "Venus",
        "d": "Jupiter",
        "answer": "b",
    },
     {
        "question": "Which planet is known as the Red Planet?",
        "a": "Earth",
        "b": "Mars",
        "c": "Venus",
        "d": "Jupiter",
        "answer": "b"
    },
    {
        "question": "What is the capital of Japan?",
        "a": "Beijing",
        "b": "Seoul",
        "c": "Tokyo",
        "d": "Bangkok",
        "answer": "c"
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "a": "William Shakespeare",
        "b": "Charles Dickens",
        "c": "Jane Austen",
        "d": "Mark Twain",
        "answer": "a"
    },
    {
        "question": "Which gas do plants absorb during photosynthesis?",
        "a": "Oxygen",
        "b": "Carbon Dioxide",
        "c": "Nitrogen",
        "d": "Hydrogen",
        "answer": "b"
    },
    {
        "question": "Which is the largest mammal in the world?",
        "a": "African Elephant",
        "b": "Blue Whale",
        "c": "Giraffe",
        "d": "Hippopotamus",
        "answer": "b"
    },
    {
        "question": "In which year did India gain independence?",
        "a": "1942",
        "b": "1947",
        "c": "1950",
        "d": "1962",
        "answer": "b"
    },
    {
        "question": "Which continent is the Sahara Desert located in?",
        "a": "Asia",
        "b": "Australia",
        "c": "Africa",
        "d": "South America",
        "answer": "c"
    },
    {
        "question": "What is H2O commonly known as?",
        "a": "Salt",
        "b": "Hydrogen",
        "c": "Water",
        "d": "Oxygen",
        "answer": "c"
    },
    {
        "question": "Who is known as the Father of Computers?",
        "a": "Albert Einstein",
        "b": "Isaac Newton",
        "c": "Charles Babbage",
        "d": "Nikola Tesla",
        "answer": "c"
    },
    {
        "question": "Which organ in the human body purifies blood?",
        "a": "Heart",
        "b": "Kidney",
        "c": "Lungs",
        "d": "Liver",
        "answer": "b"
    }
]


# Shuffle questios
random.shuffle(quiz)


# give random questions from the list
answer =0
que =0
for q in quiz:
    que+=1
    if que >= 5:
        
        break
        
# give options
        
    print("\n" + q["question"])
    print("a:", q["a"])
    print("b:", q["b"])
    print("c:", q["c"])
    print("d:", q["d"])
        
# ask for anser

    answer = input("Your answer (a/b/c/d): ").lower()
    
    
    
    if answer == q["answer"]:
        score+=1
        print("Correct answer !!!!")
    else:
        print("Wrong answer")
    
    print("Your Final Score is: ",score)



# if correct > give correct message > increase the score


