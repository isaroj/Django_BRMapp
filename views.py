from django.shortcuts import render
from BRMapp.forms import NewBookForm, SearchForm
from django.http import HttpResponse, HttpResponseRedirect
from BRMapp.models import Book, BRMuser
from BRMapp import models
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
def userSignup(request):
    res=render(request,'BRMapp/signup.html')
    return res
def valid(request):
        flag=0
        s=""
        name=request.POST['name']
        username=request.POST['username']
        password=request.POST['password']
        repassword=request.POST['repassword']
        phone=request.POST['phone']
        phone='+91'+phone
        if password!=repassword:
            s="<h1 style='background-color:black; color:white;text-align:center'>Password and re-password is not matching</h1><br><center><a href='signup' style='text-decoration:none;color:red;background:black;font-size:32px'>GoTo SignUp Page</a></center>"
            return HttpResponse(s)
        user=BRMuser.objects.all()
        for u in user:
            if u.username==username:
                s="<h1 style='background-color:black; color:white;text-align:center'>Username already exists!</h1><br><center><a href='signup' style='text-decoration:none;color:red;background:black;font-size:32px'>GoTo SignUp Page</a></center>"
                return HttpResponse(s)
            if u.phone==phone:
                s="<h1 style='background-color:black; color:white;text-align:center'>Phone number already registered!</h1><br><center><a href='signup' style='text-decoration:none;color:red;background:black;font-size:32px'>GoTo SignUp Page</a></center>"
                return HttpResponse(s)
        user=models.BRMuser()
        user.name=name
        user.username=username
        user.password=password
        user.phone=phone
        user.save()
        return HttpResponseRedirect('/BRMapp/login')
def userLogin(request):
    data={}
    if request.method=='POST':
        unm=request.POST['username']
        pwd=request.POST['password']
        user=BRMuser.objects.all()
        for u in user:
            if u.username==unm and u.password==pwd:
               flag=1
               #match=request.session['username']
               break
        else:
            flag=0
        if flag:
            request.session['username']=unm
            return HttpResponseRedirect('/BRMapp/view-books')
        else:
            data['error']="username or password is incorrect!"
            res=render(request,'BRMapp/user_login.html',data)
            return res
    else:
        return render(request,'BRMapp/user_login.html',data)
def userLogout(request):
    logout(request)
    return HttpResponseRedirect('/BRMapp/login')
#@login_required(login_url='/BRMapp/login')
def searchBook(request):
    try:
         username=request.session['username']
    except:
         return HttpResponseRedirect('login')
    else:
        form=SearchForm()
        res=render(request,'BRMapp/search_book.html',{'form':form,'username':username})
        return res
#@login_required(login_url='/BRMapp/login')
def search(request):
    try:
         username=request.session['username']
    except:
         return HttpResponseRedirect('login')
    else:
        x=0
        form=SearchForm(request.POST)
        books=models.Book.objects.filter(title=form.data['title'])
        if len(books)==0:
            x=1
        res=render(request,'BRMapp/search_book.html',{"books":books,"form":form,"x":x,'username':username})
        return res
#@login_required(login_url='/BRMapp/login')
def deleteBook(request):
    try:
         username=request.session['username']
    except:
         return HttpResponseRedirect('login')
    else:
        bookid=request.GET['bookid']
        book=models.Book.objects.filter(id=bookid)
        book.delete()
        return HttpResponseRedirect('view-books')
#@login_required(login_url='/BRMapp/login')
def editBook(request):
    try:
         username=request.session['username']
    except:
         return HttpResponseRedirect('login')
    else:
        book=models.Book.objects.get(id=request.GET['bookid'])
        fields={"title":book.title,"price":book.price,"author":book.author,"publisher":book.publisher}
        form=NewBookForm(initial=fields)
        res=render(request,'BRMapp/edit_book.html',{"form":form,"book":book,'username':username})
        return res
#@login_required(login_url='/BRMapp/login')
def edit(request):
    try:
         username=request.session['username']
    except:
         return HttpResponseRedirect('login')
    if request.method=='POST':
        form=NewBookForm(request.POST)
        book=models.Book()
        book.id=request.POST['bookid']
        book.title=form.data['title']
        book.price=form.data['price']
        book.author=form.data['author']
        book.publisher=form.data['publisher']
        book.save()
    return HttpResponseRedirect('view-books')
#@login_required(login_url='/BRMapp/login')
def viewBook(request):
   try:
        username=request.session['username']
   except:
        return HttpResponseRedirect('login')
   else:
        books=models.Book.objects.all()
        res=render(request,'BRMapp/view_book.html',{'books':books,'username':username})
        return res
#@login_required(login_url='/BRMapp/login')
def newBook(request):
    try:
         username=request.session['username']
    except:
         return HttpResponseRedirect('login')
    else:
        form=NewBookForm()
        res=render(request,'BRMapp/new_book.html',{'form':form,'username':username})
        return res
#@login_required(login_url='/BRMapp/login')
def add(request):
    try:
         username=request.session['username']
    except:
         return HttpResponseRedirect('login')
    else:
         if request.method=='POST':
            form=NewBookForm(request.POST)
            book=models.Book()
            book.title=form.data['title']
            book.price=form.data['price']
            book.author=form.data['author']
            book.publisher=form.data['publisher']
            book.save()
            s="<h1 style='color:white;text-align:center;background:black'>Book details stored successfully</h1><br><center><a style='color:white;text-align:center;background:green;text-decoration:none;font-size:30px' href='view-books'>Click to view Books</a></center>"
            return HttpResponse(s)
