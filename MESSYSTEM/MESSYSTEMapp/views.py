from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    return render(request, 'files/homepage.html')

def login(request):
    return render(request, 'files/login2.html')

def adminFAD(request):
    return render(request, 'files/Admin(F.A Distribution).html')

def adminFA(request):
    return render(request, 'files/Admin(Financial Assistance).html')

def adminhomepage(request):
    return render(request, 'files/adminhomepage.html')

def distribution_and_retrieval(request):
    return render(request, 'files/distribution-and-retrieval.html')

def register(request):
    return render(request, 'files/register.html')

def student_history_transaction(request):
    return render(request, 'files/student-history-transaction.html')

def student_transaction(request):
    return render(request, 'files/student-transaction.html')

def teacher_transaction(request):
    return render(request, 'files/teacher-transaction.html')