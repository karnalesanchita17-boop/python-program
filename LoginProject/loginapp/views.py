
import re
from django.shortcuts import render


def login_view(request):
    message = ""

    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")

        username_pattern = r"^[A-Za-z0-9]{3,15}$"
        password_pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d@$!%*?&]{8,}$"

        if not re.fullmatch(username_pattern, username):
            message = "Invalid username! Use 3-15 letters or digits."

        elif not re.fullmatch(password_pattern, password):
            message = "Invalid password! Use at least 8 characters, including uppercase, lowercase, and a digit."

        elif username == "Student123" and password == "Student123":
            message = "Login successful!"

        else:
            message = "Invalid username or password!"

    return render(request, "login.html", {"message": message})
