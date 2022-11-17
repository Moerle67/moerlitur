if request.method == "POST":
    print(request.POST)
    if 'button' in request.POST:
        if request.POST["button"] == "Anmelden":
            username = request.POST['login_name']
            password = request.POST['login_pwd']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                print("loggin")
                login(request, user)
            else:
                print("login failed")
        elif request.POST["button"] == "Abmelden":
            logout(request)
    return redirect("/")         
