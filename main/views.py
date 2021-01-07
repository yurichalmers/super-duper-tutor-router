from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Tutorhelp, Comment
import bcrypt


def index(request):
    
    return render(request, 'index.html')


def register_page(request):

    return render(request, 'register.html')


def create_student(request):
    errors = User.objects.validator(request.POST)

    if len(errors) > 0:
        for key, val in errors.items():
            messages.error(request, val)

        return redirect("/register")

    hashed_pw = bcrypt.hashpw(
        request.POST['password'].encode(),
        bcrypt.gensalt()
    ).decode()

    current_user = User.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        username = request.POST['username'],
        user_type = "Learner",
        email = request.POST['email'],
        level = request.POST['level'],
        password = hashed_pw
    )
    request.session['user_id'] = current_user.id 

    return redirect("/dashboard")

def create_tutor(request):
    errors = User.objects.validator(request.POST)

    if len(errors) > 0:
        for key, val in errors.items():
            messages.error(request, val)

        return redirect("/register")

    hashed_pw = bcrypt.hashpw(
        request.POST['password'].encode(),
        bcrypt.gensalt()
    ).decode()

    current_user = User.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        username = request.POST['username'],
        user_type = "Tutor",
        email = request.POST['email'],
        level = request.POST['level'],
        password = hashed_pw
    )
    request.session['user_id'] = current_user.id 

    return redirect("/dashboard")


def login_user(request):
    user_logging_in = User.objects.filter(email=request.POST['email'])
    if len(user_logging_in) == 0:
        messages.error(request, "Please try again.")

        return redirect ("/")

    if bcrypt.checkpw(
        request.POST['password'].encode(),
        user_logging_in[0].password.encode()
    ):
        request.session['user_id'] = user_logging_in[0].id
        return redirect("/dashboard")

    messages.error(request, "Please check your email and password.")
    return redirect("/")

def dashboard(request):

    context = {
        "this_user" : User.objects.get(id=request.session['user_id']),
        "all_requests": Tutorhelp.objects.all().order_by("-created_at"),
        "all_comments": Comment.objects.all().order_by("-created_at")
    }
    return render(request, 'dashboard.html', context)


def my_account(request, user_id):
    context = {
        "this_user": User.objects.get(id=user_id),
        "num_contrib": len(Comment.objects.filter(poster=user_id)),
        "num_posts": len(Tutorhelp.objects.filter(poster=user_id))


    }

    return render(request, 'my-account.html', context)

def tutor_request_page(request):

    return render(request, 'add.html')

def math_page(request):
    context = {
        "all_math": Tutorhelp.objects.filter(subject="Math").order_by("-created_at"),
        "this_user": User.objects.get(id=request.session['user_id'])
    
    }
    return render(request, 'subjects/math.html', context)

def add_math_request(request):
    Tutorhelp.objects.create(
        subject = "Math",
        course = request.POST['course'],
        topic = request.POST['topic'],
        desc = request.POST['desc'],
        poster = User.objects.get(id=request.session['user_id'])
    )
    return redirect("/dashboard/math")

def science_page(request):
    context = {
        "all_science": Tutorhelp.objects.filter(subject="Science").order_by("-created_at"),
        "this_user": User.objects.get(id=request.session['user_id'])

    }
    return render(request, 'subjects/science.html', context)

def add_science_request(request):
    Tutorhelp.objects.create(
        subject = "Science",
        course = request.POST['course'],
        topic = request.POST['topic'],
        desc = request.POST['desc'],
        poster = User.objects.get(id=request.session['user_id'])    
    )
    return redirect("/dashboard/science")

def english_page(request):
    context = {
        "all_english": Tutorhelp.objects.filter(subject="English").order_by("-created_at"),
        "this_user": User.objects.get(id=request.session['user_id'])
    }

    return render(request, 'subjects/english.html', context)
def add_english_request(request):
    Tutorhelp.objects.create(
        subject = "English",
        course = request.POST['course'],
        topic = request.POST['topic'],
        desc = request.POST['desc'],
        poster = User.objects.get(id=request.session['user_id'])
    )
    return redirect("/dashboard/english")

def history_page(request):
    context = {
        "all_history": Tutorhelp.objects.filter(subject="History").order_by("-created_at"),
        "this_user": User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'subjects/history.html', context)

def add_history_request(request):
    Tutorhelp.objects.create(
        subject = "History",
        course = request.POST['course'],
        topic = request.POST['topic'],
        desc = request.POST['desc'],
        poster = User.objects.get(id=request.session['user_id'])
    )
    return redirect("/dashboard/history")
 
def foreign_language_page(request):
    context = {
        "all_foreign_languages": Tutorhelp.objects.filter(subject="Foreign Language").order_by("-created_at"),
        "this_user": User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'subjects/foreign-language.html', context)

def add_foreign_language_request(request):
    Tutorhelp.objects.create(
        subject = "Foreign Language",
        course = request.POST['course'],
        topic = request.POST['topic'],
        desc = request.POST['desc'],
        poster = User.objects.get(id=request.session['user_id'])
    )
    return redirect("/dashboard/foreign-language")

def misc_page(request):
    context = {
        "all_misc": Tutorhelp.objects.filter(subject="Other").order_by("-created_at"),
        "this_user": User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'subjects/misc.html', context)
def add_misc_request(request):
    Tutorhelp.objects.create(
        subject = "Other",
        course = request.POST['course'],
        topic = request.POST['topic'],
        desc = request.POST['desc'],
        poster = User.objects.get(id=request.session['user_id'])
    )
    return redirect("/dashboard/misc")

def view_topic(request, tutorhelp_id):
    context = {
        "this_topic": Tutorhelp.objects.get(id=tutorhelp_id),
        "this_user": User.objects.get(id=request.session['user_id']),
        "these_comments": Comment.objects.all()
    }

    return render(request, "view-topic.html", context)

def add_comment(request, tutorhelp_id):
    new_comment = Comment.objects.create(
        comment = request.POST['comment'],
        request = Tutorhelp.objects.get(id=tutorhelp_id),
        poster = User.objects.get(id=request.session['user_id'])
    )
    return redirect(f"/tutor-help/{new_comment.request.id}")


def tutor_info_page(request, user_id):
    context = {
        "this_user": User.objects.get(id=request.session['user_id']),
        "this_tutor": User.objects.get(id=user_id),
        "num_posts": len(Tutorhelp.objects.filter(poster=user_id)),
        "num_contrib": len(Comment.objects.filter(poster=user_id))
    }
    return render(request, "tutor-info.html", context)


def logout(request):
    request.session.clear()

    return redirect("/")