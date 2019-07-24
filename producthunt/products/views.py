from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product, Mobile
from django.db.models import Q
from django.utils import timezone
from django_tables2 import RequestConfig
from .tables import ProductTable
from .forms import MyForm
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def home(request):
    products = Product.objects
    query = request.GET.get("q")
    if query:
        products = products.filter(
        Q(title=query)|
        Q(prize=query)
        ).distinct()
    return render(request, 'products/home.html',{'products': products})


@login_required(login_url="/accounts/signup")
def create(request):
    if request.method=='POST':
        if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['icon'] and request.FILES['image'] and request.FILES['video']:
            product = Product()
            product.title = request.POST['title']
            product.body = request.POST['body']
            if request.POST['url'].startswith('http//') or request.POST['url'].startswith('http://'):
                product.url = request.POST['url']
            else:
                product.url = 'http://' + request.POST['url']

            product.icon = request.FILES['icon']
            product.image = request.FILES['image']
            product.pub_date = timezone.datetime.now()
            product.hunter = request.user
            product.hunter = request.FILES['video']
            product.save()
            return redirect('/products/' + str(product.id))
        else:
            return render(request,'products/create.html',{'error':'please fill all the fields'})
    else:
        return render(request, 'products/create.html')

def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'products/detail.html', {'product':product})

@login_required(login_url="/accounts/signup")
def upvote(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=product_id)
        print(product)
        product.votes_total += 1
        product.save()
        return redirect('/products/success.html' + str(product.id))

def about(request):
    return render(request, 'products/about.html',{'about': about})

def contact(request):
    return render(request, 'products/contact.html',{'contact': contact})


def mobile(request):
    mobiles = Mobile.objects.all()
    context ={
       'mobiles':mobiles
    }
    return render(request, 'products/mobile.html', context)

def people(request):
    table = ProductTable(Product.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'products/people.html', {'table': table})

def detail_view(request,mob_id):
    mobiledetail = get_object_or_404(Mobile, pk=mob_id)
    return render(request, 'products/detail_view.html',{'mobile': mobiledetail})

def sucess(request):
    return render(request, 'products/success.html',{'sucess': sucess})

def admit_card(request):
    if request.method == 'POST':
        myForm = MyForm(request.POST)

        if myForm.is_valid():
            name = myForm.cleaned_data['name']
            email = myForm.cleaned_data['email']
            feedback = myForm.cleaned_data['feedback']
            Card_Number = myForm.cleaned_data['feedback']

            context = {
            'name': name,
            'email': email,
            'feedback': feedback,
            'Card_Number':Card_Number

            }

            template = loader.get_template('products/thankyou.html')

            return HttpResponse(template.render(context, request))
    else:
          form = MyForm()
    return render(request, 'products/admit_card.html', {'form':form});

def thankyou(request):
    return render(request, 'products/thankyou.html',{'thankyou': thankyou})
