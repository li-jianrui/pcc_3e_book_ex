survey_results = {
    "John": "Python",
    "Alice": "JavaScript",
    "Bob": "",
    "Charlie": "",
    "David": "Java",
    "Eve": "C++",
    "Frank": "",
}

for name, language in survey_results.items():
    if language:
        print(f"Thank you, {name.title()}! You prefer {language}.")
    else:
        print(f"Hi {name.title()}, would you like to take the survey and share your favorite programming language?")
