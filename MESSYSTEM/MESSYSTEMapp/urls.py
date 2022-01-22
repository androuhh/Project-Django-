from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('login2.html', views.login, name='login'),
    path('register.html', views.register, name='register'),
    path('Admin(F.A Distribution).html', views.adminFAD, name='Admin(F.A Distribution)'),
    path('Admin(Financial Assistance).html', views.adminFA, name='Admin(Financial Assistance)'),
    path('adminhomepage.html', views.adminhomepage, name='adminhomepage'),
    path('student-history-transaction.html', views.student_history_transaction, name='student-history-transaction'),
    path('student-transaction.html', views.student_transaction, name='student-transaction'),
    path('teacher-transaction.html', views.teacher_transaction, name='teacher-transaction'),
    path('distribution-and-retrieval.html', views.distribution_and_retrieval, name='distribution-and-retrieval'),
]