from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Profile

# Create your views here.
@login_required(login_url='signin')
def index(request):
    return render(request, 'index.html')


@login_required(login_url='signin')
def settings(request):
    user_profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        
        if request.FILES.get('image') == None:
            image = user_profile.profileimg
            firstname = request.POST['firstname']
            lastname = request.POST['lastname']
            bio = request.POST['bio']
            gradset = request.POST['gradset']
            house = request.POST['house']
            location = request.POST['location']
            occupation = request.POST['occupation']
            relationship = request.POST['relationship']

            user_profile.profileimg = image
            user_profile.firstname = firstname
            user_profile.lastname = lastname
            user_profile.bio = bio
            user_profile.gradset = gradset
            user_profile.house = house
            user_profile.location = location
            user_profile.occupation = occupation
            user_profile.relationship = relationship


            user_profile.save()
        if request.FILES.get('image') != None:
            image = request.FILES.get('image')
            firstname = request.POST['firstname']
            lastname = request.POST['lastname']
            bio = request.POST['bio']
            gradset = request.POST['gradset']
            house = request.POST['house']
            location = request.POST['location']
            occupation = request.POST['occupation']
            relationship = request.POST['relationship']

            user_profile.profileimg = image
            user_profile.firstname = firstname
            user_profile.lastname = lastname
            user_profile.bio = bio
            user_profile.gradset = gradset
            user_profile.house = house
            user_profile.location = location
            user_profile.occupation = occupation
            user_profile.relationship = relationship
            user_profile.save()
        
        return redirect('settings')
    return render(request, 'settings.html', {'user_profile': user_profile})


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


def signin(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'credentials does not correspond to a registered member.')
            return redirect('signin')

    else:
        return render(request, 'signin.html')


@login_required(login_url='signin')
def logout(request):
    auth.logout(request)
    return redirect('signin')



# Additional contents
def faq(request):
    return render(request, 'faq.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def pay(request):
    return render(request, 'pay.html')