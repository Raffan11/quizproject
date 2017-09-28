from quiz.models import Quiz
from django.shortcuts import render

# quizzes = [
# 	{
# 		"quiz_number": 1,
# 		"name": "GÖTEBORG",
# 		"description": "Är du expert på GBG?"
# 	},
# 	{
# 		"quiz_number": 2,
# 		"name": "Största fotbollslagen",
# 		"description": "Kan du dina lag?"
# 	},
# 	{
# 		"quiz_number": 3,
# 		"name": "Världens mest kända hackare",
# 		"description": "Kan du din hackerhistoria?"
# 	},
# ]



def start(request):
	context = {
		"quizzes": Quiz.objects.all(),
	}
	return render(request, "start.html", context)


def quiz(request, quiz_number):
	context = {
		"quiz": quizzes [quiz_number -1],
		"quiz_number": quiz_number,
	}
	return render(request, "quiz.html", context)


def question(request, quiz_number, question_number):
	context = {
		"question_number": question_number,
	    "question": "Vilken Göteborgare har skrivit låten: in kommer ting",
		"answer1": "Håkan Hellström",
	   	"answer2": "Kapten Röd",
	    "answer3": "Joel Alme",
	    "quiz_number": quiz_number,
	}
	return render(request, "question.html", context)


def results(request, quiz_number):
	context = {
	    "correct": 12,
	    "total": 20,
		"quiz_number": quiz_number,
	}
	return render(request, "results.html", context)




















