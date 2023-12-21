import random

# Beispiel for Dictionary Comprehension.
# new_dict = {new_key : new_value for item in list}
# new_dict = {new_key : new_valeu for  (key, value) in dict.items()}
# new_dict = {new_key : new_valeu for  (key, value) in dict.items() if test}

names = ['Alex', 'Beth', 'Caroline', 'Dave',  'Eleanor', 'Freddie']
# new_dict = {new_key : new_value for item in list}
students_scores = {student: random.randint(1, 100) for student in names}
print(students_scores)
# passed_students = {new_key: new_value for (key, value) in dictionary.items()}
passed_students = {student: score for (student, score)
                   in students_scores.items() if score >= 60}
print(passed_students)

# CHALLENGE
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word: len(word) for word in sentence.split()}
print(result)

# Convert Celsius aus einem Dictionary in Fahrenheit
weather_c= {
    'Monday': 12,
    'Tuesday': 14,
    'Wednesday': 15,
    'Thursday': 14,
    'Friday': 21,
    'Saturday': 22,
    'Sunday': 24
}
weather_f = {day: (temp_c*9/5) for (day, temp_c) in weather_c.items()}
print(weather_f)






