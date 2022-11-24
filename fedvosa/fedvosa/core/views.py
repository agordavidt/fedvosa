from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def signup(request):
    pin_lists = ['111a', '222b', '333c', '444d', '555e', '666f']

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']        
        pin = request.POST['pin']
        # pin = request.POST['pin']

        if pin in pin_lists:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('signup')
            # elif pin not in pin_lists:
            #     messages.info(request, 'Incorrect Pin')
            #     return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

                #log user in and redirect to settings page
                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)

                #create a Profile object for the new user
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
                new_profile.save()
                return redirect('settings')
                #remove the entered pin from the pin_lists
                pin_lists.remove(pin)
        else:
            messages.info(request, 'Invalid PIN')
            return redirect('signup')
        
    else:
        return render(request, 'signup.html')


# Additional contents
def faq(request):
    return render(request, 'faq.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def pay(request):
    return render(request, 'pay.html')