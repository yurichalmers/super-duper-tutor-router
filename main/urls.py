from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register_page),
    path('create-student', views.create_student),
    path('create-tutor', views.create_tutor),
    path('login-user', views.login_user),
    path('dashboard', views.dashboard),
    path('user/<int:user_id>', views.my_account),
    path('tutor-request/add', views.tutor_request_page),
    path('dashboard/math', views.math_page),
    path('add-math-request', views.add_math_request),
    path('add-science-request', views.add_science_request),
    path('add-english-request', views.add_english_request),
    path('add-history-request', views.add_history_request),
    path('add-foreign-language-request', views.add_foreign_language_request),
    path('add-misc-request', views.add_misc_request),
    path('dashboard/science', views.science_page),
    path('dashboard/english', views.english_page),
    path('dashboard/history', views.history_page),
    path('dashboard/foreign-language', views.foreign_language_page),
    path('dashboard/misc', views.misc_page),
    path('tutor-help/<int:tutorhelp_id>', views.view_topic),
    path('tutor-help/<int:tutorhelp_id>/add-comment', views.add_comment),
    path('tutor/<int:user_id>', views.tutor_info_page),
    path('logout', views.logout)

]