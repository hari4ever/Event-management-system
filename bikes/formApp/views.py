from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import *
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

# def fst(request) :
#     return render(request , 'base.html')

# def home(request) :
#     return render(request , 'index.html')

# def second(request) :
#     return HttpResponse("second......")

# def register(request) :
#     v = {
#         'form' : Registrationforms
#     }
#     return render(request , 'navbar.html',v)

# def adduser(request) :
#     form = Registrationforms(request.POST)
#     if form.is_valid() :
#         myregister = Registion(
#             username = form.cleaned_data['username'],
#             password = form.cleaned_data['password'],
#             )
#         myregister.save()
        
#     return redirect('home')



    # print('\nnot found\n')
    # data = list(data)
    # for d in data :
    #     print(d)
    # if request.method == 'POST' :
    #     u = request.POST['username']
    #     p = request.POST['pass']
        
    #     dataset = Registion(
    #         username = u, password = p
    #     )
    #     dataset.save()
    

def home(request) :
    return render(request, 'index.html')


def loginpage(request) :
    inf = {
        'mistake' : '',
        'username' : '',
        'password' : '',
        }
    if request.method == 'POST' :
        u = request.POST['username']
        p = request.POST['pass']
        data = list(Mydata.objects.filter(username = u).values())
        if len(data) !=0 :
            data = data[0]
            if data['password'] == p :
                global logindetails 
                logindetails = data
                return redirect('final')
            else :
                inf['mistake'] = 'p'
        else :
            inf['mistake'] = 'u'
        inf['username'], inf['password'] = u, p
    return render(request, 'login.html',{'data' : inf})




def signuppage(request) :
        inf = {
            'mistake' : '',
            'email' : '',
            'username' : '',
            'password' : '',
        }
        if request.method == 'POST' :
            u = request.POST['username']
            p = request.POST['pass']
            e :str = request.POST['email']
            ph :str = request.POST['phno']
            a = request.POST['Again']
            data = list(Mydata.objects.filter(username = u).values())
            if len(data) != 0 :
                inf['mistake'] += 'u'
            if not p == a :
                inf['mistake'] += 'p'
            if e.endswith('@gmail.com') == False :
                inf['mistake'] += 'e'
            if not ph.isdigit() :
                inf['mistake'] += 'z'
            if len(inf['mistake']) == 0 :
                dataset = Mydata(
            username = u, password = p , email = e)
                dataset.save()
                return redirect('home')
            inf['email'],inf['username'],inf['password'] = e , u , p
        return render(request, 'signup.html', {'data' : inf})
    
    
def final(request) :
    return render(request , 'final.html', {'data' : logindetails})

def data(request) :
    if request.method == 'POST' :
        n = request.POST['name']
        ph = request.POST['phno']
        e = request.POST['email']
        ad = request.POST['address']
        
        data1 = registerdata(
            username = n , ph_no = ph, email = e , address = ad
        )
        data1.save()
        return redirect('home')
        
    return render(request,'data.html')

# def sendemail() :
#     sub = 'this email'
#     mess = 'hi this is ram '
#     from_em = settings.EMAIL_HOST_USER
#     R = ['ramsurampudi77@gmail.com']
#     send_mail(sub,mess,from_em,R)
    
# def shome(request) :
#     sendemail()
#     return redirect('home')