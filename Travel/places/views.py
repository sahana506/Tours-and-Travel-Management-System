from django.shortcuts import render,get_object_or_404,redirect
from .forms import BookForm,MultipleForms,CreateUserForm
from django.forms import formset_factory
from .models import Details,Catalog,Idnum
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

def first(request):
    return render(request,'places/first.html',{})



no =1
#@login_required(login_url='/register/')
def home(request):
    global no
    idnumber = Idnum.objects.get(pk=no)
    no=no+1
    
    multiple_form = MultipleForms()
    if request.method == 'POST':
        filled_form = BookForm(request.POST)
        if filled_form.is_valid():
            created_books=filled_form.save()
            created_books_pk=created_books.id
            note='tqs for booking and have a great journey from %s to %s '  %(filled_form.cleaned_data['source'],filled_form.cleaned_data['dest'])
            filled_form = BookForm() 
        else:
            created_books_pk = None
            note='its not booked try again'
        return render(request,'places/home.html',{'created_books_pk':created_books_pk,'bookform':filled_form,'note':note,'multiple_form':multiple_form,'idnumber':idnumber})

    else:   
        form = BookForm()
        return render(request,'places/home.html',{'bookform':form,'multiple_form' : multiple_form})


def orders(request):
    number_of_people = 2
    filled_multiple_pizza_form = MultipleForms(request.GET)
    if filled_multiple_pizza_form.is_valid():
        number_of_people = filled_multiple_pizza_form.cleaned_data['number']
    
    BookFormSet = formset_factory(BookForm,extra=number_of_people)
    formset = BookFormSet()
    if request.method =='POST':
        filled_formset = BookFormSet(request.POST)
        if filled_formset.is_valid():
            for form in filled_formset:
                form.save()
            #filled_form.save()
            for form in filled_formset:
                print(form.cleaned_data['name'])
            note ='its booked'

        else:
            note ='its not booked'
        return render(request,'places/orders.html',{'note':note,'formset':formset})
    else:
        return render(request,'places/orders.html',{'formset':formset})

def edit_order(request,pk):
    book=Details.objects.get(pk=pk)
    form = BookForm(instance=book)
    if request.method == 'POST':
        filled_form =BookForm(request.POST,instance=book)
        if filled_form.is_valid():
            filled_form.save()
            form=filled_form
            note='order has been updated'
            return render(request,'places/edit_order.html',{'note':note,'bookform':form,'book':book})
    return render(request,'places/edit_order.html',{'bookform':form,'book':book})








def catalog(request):
    catalogs = Catalog.objects
    
    return render(request,'places/catalog.html',{'catalogs':catalogs})



def catdetails(request,cat_id):
    cat_details = get_object_or_404(Catalog,pk=cat_id)
    return render(request,'places/catalog_details.html',{'cata':cat_details})

def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            note = 'User Created'
            user=form.cleaned_data['username']
            messages.success(request,'Account  Created for' + user)
            return redirect('login')
            return render(request,'places/register.html',{'form':form ,'note':note})
    else:
        form = CreateUserForm()
        return render(request,'places/register.html',{'form':form})


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request,'places/login.html',{'form':form})



def history(request):
    history1 = Details.objects.all()
    return render(request,'places/history.html',{'history1':history1})