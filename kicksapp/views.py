from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse
from .forms import LoginForm, SignUPForm
from django.contrib.auth import authenticate, login, logout
from .models import Image,Shoes,Jacket,Shirt,JacketCategory,ShirtCategory,DummyUpload,Category,Cart_Items,User,Comment,logo, ChatSpace,Message,location
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from decimal import Decimal
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.urls import reverse_lazy



def usersignup(request):
    if request.method == "POST":
        form = SignUPForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = SignUPForm()

    return render(request, "signup.html", {"form": form})


def userlogin(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect("mainpage")
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})


def userlogout(request):
    logout(request)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    

def mainpage(request):
    lg = logo.objects.get(id = 1)
    lgitem = lg.image.url
    image = Image.objects.get(imagename = 'jordan')
    url = image.img.url
    imagename = image.imagename
    image2 = Image.objects.get(imagename = 'jacket')
    url2 = image2.img.url
    image3 = Image.objects.get(imagename = 'shirt')
    url3 = image3.img.url
    image4 = Image.objects.get(imagename = 'airmax')
    url4 = image4.img.url
    
    context = {
            "image_url": url, 
            "image_url2": url2,
             "image_url3": url3,
              "image_url4": url4,
              "lg":lgitem

        }
    
    return render(request, "mainpage.html", context) 



def Shoe(request):
    try:
        official_category = Category.objects.get(name='official')
        official_shoes = Shoes.objects.filter(category=official_category)
    except Category.DoesNotExist:
        official_shoes = []

    try:
        sneaker_category = Category.objects.get(name='sneaker')
        sneaker_shoes = Shoes.objects.filter(category=sneaker_category)
    except Category.DoesNotExist:
        sneaker_shoes = []

    try:
        boots_category = Category.objects.get(name='boots')
        boots_shoes = Shoes.objects.filter(category=boots_category)
    except Category.DoesNotExist:
        boots_shoes = []

    try:
        sport_category = Category.objects.get(name='sport')
        sport_shoes = Shoes.objects.filter(category=sport_category)
    except Category.DoesNotExist:
        sport_shoes = []
    lg = logo.objects.get(id = 1)
    lgitem = lg.image.url
    
    context = {
        'official': official_shoes,
        'sneaker': sneaker_shoes,
        'boots': boots_shoes,
        'sport': sport_shoes,
        'user':request.user,
        "lg":lgitem

    }
    
    return render(request, 'Shoes.html', context)

 
def Jacko(request):
     try:
       name = JacketCategory.objects.get(name__icontains = 'hoodies')
       hoodie= Jacket.objects.filter(jacketname = name).all()
     except JacketCategory.DoesNotExist:
        name = []

     try:
       name = JacketCategory.objects.get(name__icontains = 'puff')
       puffy= Jacket.objects.filter(jacketname = name).all()
     except JacketCategory.DoesNotExist:
        name = []
     try:
       name = JacketCategory.objects.get(name__icontains = 'trench')
       trench= Jacket.objects.filter(jacketname = name).all()
     except JacketCategory.DoesNotExist:
        name = []
     lg = logo.objects.get(id = 1)
     lgitem = lg.image.url
     context = {"puff":puffy, "trench": trench, "hoodie":hoodie, "user":request.user, "lg":lgitem}


     return render (request, 'jackets.html', context)
   
   




def Shati(request):
    try:
        catategory_official = ShirtCategory.objects.filter(name = 'official').first()
        official= Shirt.objects.filter(shirtname = catategory_official).all()

    except ShirtCategory.DoesNotExist:
        cat1 = []
    try:
        category_longsleeve = ShirtCategory.objects.filter(name = 'Long sleeve').first()
        longsleeve= Shirt.objects.filter(shirtname = category_longsleeve).all()

    except ShirtCategory.DoesNotExist:
        cat1 = []
    lg = logo.objects.get(id = 1)
    lgitem = lg.image.url
    context = {"shirtname":official, "shirt":longsleeve ,"user":request.user,"lg":lgitem}
      
    return render (request, 'shirt.html', context)
  


# def ShirtUpload(request):
#     if request.method == 'POST':
#         cat = request.POST.get('cat')
#         gen = request.POST.get('gender')
#         pric = request.POST.get('price')
#         price = Decimal(pric)   
#         file = request.FILES['imagefile']
#         fs = FileSystemStorage()
#         filename = fs.save(file.name, file)
#         if ShirtCategory.objects.filter( name = cat).exists():
#              shirt = ShirtCategory.objects.filter(name__icontains = cat ).first()
#              shirti = Shirt(shirtname = shirt, price = price, sex = gen, upload = filename)
#              shirti.save()
#         else:
#             category = ShirtCategory.objects.create(name = cat)
#             category.save() 
#             shirt = ShirtCategory.objects.filter(name__icontains = cat ).first()
#             shirti = Shirt(shirtname = shirt, price = price, sex = gen, upload = filename)
#             shirti.save()
#         return redirect('shirt')
#     else:
#         return render(request, "dummy.html")

# def ShoeUpload(request):
#         if request.method == 'POST':
#          shoe_category = request.POST.get('cat')
#          sex = request.POST.get('gender')
#          shoe_name = request.POST.get('name')
#          shoe_price= request.POST.get('price')
#          price = Decimal(shoe_price)   
#          file = request.FILES['imagefile']
#          filesever = FileSystemStorage()
#          shoe_filename = filesever.save(file.name, file)
#          if Category.objects.filter( name = shoe_category).exists():
#              shoe = Category.objects.filter(name__icontains = shoe_category).first()
#              shoesdb= Shoes(category = shoe, name = shoe_name, price = price, sex = sex, upload = shoe_filename)
#              shoesdb.save()
#              return redirect('Shoes')
#          else:
#             category = Category.objects.create(name = shoe_category)
#             category.save() 
#             shoe = Category.objects.filter(name__icontains = shoe_category ).first()
#             shoedb = Shoes(category = shoe, name = shoe_name, price = price, sex = sex, upload = shoe_filename)
#             shoedb.save()
#             return redirect('Shoes')
#         else:
#             return render(request, "shoeupload.html")
        
# def JacketUpload(request):
#         if request.method == 'POST':
#          cat = request.POST.get('cat')
#          gen = request.POST.get('gender')
#          pric = request.POST.get('price')
#          price = Decimal(pric)   
#          file = request.FILES['imagefile']
#          fs = FileSystemStorage()
#          filename = fs.save(file.name, file)
#          if JacketCategory.objects.filter( name = cat).exists():
#              shirt = JacketCategory.objects.filter(name__icontains = cat ).first()
#              shirti = Jacket(jacketname= shirt,price = price, sex = gen, upload = filename)
#              shirti.save()
#              return redirect('jackets')
#          else:
#             category = JacketCategory.objects.create(name = cat)
#             category.save() 
#             shirt = JacketCategory.objects.filter(name__icontains = cat ).first()
#             shirti = Jacket(jacketname = shirt,price = price, sex = gen, upload = filename)
#             shirti.save()
#             return redirect('jackets')
#         else:
#             return render(request, "jacketsupload.html")



@login_required
def CartItems(request, pk, itemid):


    try:
        content_type = get_object_or_404(ContentType, model=pk)

        model_class = content_type.model_class()

        product = get_object_or_404(model_class, id=itemid)

       
        cartitems, created = Cart_Items.objects.get_or_create(
            content_type=content_type,
            object_id=product.id,
            user=request.user
        )
        
    
        cartitems.quantity += 1
        cartitems.save()

        return redirect('viewcart',pk)

    except ContentType.DoesNotExist:
        return HttpResponse('Error: Invalid model type!')
    except TypeError:
        return HttpResponse('Error: Something went wrong!')


def ViewCart(request, pk):   
     if request.user.is_staff or request.user.is_superuser:
        return redirect('mainpage') 
     cart_view = Cart_Items.objects.filter(user=request.user).all() 
     total = sum(item.quantity * item.cart_product.price for item in cart_view)
     lg = logo.objects.get(id = 2)
     lgitem = lg.image.url

   
        
   

     context = {
        "user": request.user,
        "cartitems": cart_view,
        "total": total,
        "pk":pk,
        "logo":lgitem
    }
     return render(request, 'addtocart.html', context)


def RemoveCart(request, itemid):
    cartitem = Cart_Items.objects.filter(id = itemid)
    cartitem.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))



def AdminJamo(request):
    user_with_cart = User.objects.filter(cart_items__isnull=False).distinct()

    cart_view = []

    for user in user_with_cart:
        cart_products = Cart_Items.objects.filter(user=user)
        total = 0
        
        for item in cart_products:
           
            if item.cart_product and hasattr(item.cart_product, 'price'):
                total += item.quantity * item.cart_product.price
            else:
                print(f"Invalid cart product: {item.cart_product}")

        cart_view.append({
            'user': user,
            'cart_products': cart_products,
            'total': total,
        })

    return render(request, 'adminjamo.html', {'cart': cart_view})



def search(request):
    que = request.GET.get('search')
    query = str(que).lower()
    sh = request.GET.get('searchshoe')
    shoe = str(sh).lower()
    shir = request.GET.get('searchshirt')
    shirt = str(shir).lower()
    lg = logo.objects.get(id = 1)
    lgitem = lg.image.url

    if shoe:
            shoe_results = Shoes.objects.filter(
            Q(shoename__icontains=shoe) |
            Q(color__icontains=shoe) |
            Q(sex=shoe)
        )
            return render(request, 'search.html', {"shoeresult": shoe_results, "shoeid": shoe, "logo":lgitem})

    elif query:
            jacket_results = Jacket.objects.filter(
            Q(name__icontains=query) |
            Q(color__icontains=query) |
            Q(sex=query)
        )
            return render(request, 'search.html', {"jacketresult": jacket_results, "query": query,"logo":lgitem})  
    elif shirt:
            shirt_results = Shirt.objects.filter(
            Q(name__icontains=query) |
            Q(color__icontains=query) |
            Q(sex=query)
        )
            return render(request, 'search.html', {"shirtresult":shirt_results, "shirt":shirt, "logo":lgitem}) 
    else:  
        return HttpResponse('Item of search Not Found')
    

def ShirtSearch(request, gen):
    gen = str(gen).lower()
    results = Shirt.objects.filter(sex = gen)
    lg = logo.objects.get(id = 1)
    lgitem = lg.image.url
    return render(request, "shirtsearch.html", {"results":results, "gen": gen, "logo":lgitem})



def ShoeSearch(request, gen):
    gen = str(gen).lower()
    results = Shoes.objects.filter(sex = gen)
    lg = logo.objects.get(id = 1)
    lgitem = lg.image.url
    return render(request, "shoesearch.html", {"results":results, "gen": gen,"logo":lgitem})


def JacketSearch(request, gen):
    gen = str(gen).lower()
    results = Jacket.objects.filter(sex = gen)
    lg = logo.objects.get(id = 1)
    lgitem = lg.image.url
    return render(request, "jacketsearch.html", {"results":results, "gen": gen,"logo":lgitem})

@csrf_exempt  
def comment_view(request):
    if request.method == 'POST':
        data = json.loads(request.body) 
        comment_text = data.get('comment')

        if comment_text:
            
            comment = Comment.objects.create(comment=comment_text)

            
            return JsonResponse({'message': 'Thanks for Your feedback!'}, status=200)

    
    comments = Comment.objects.all().values() 
    return render(request, "comment.html", {"comment":comments})

def clear(request):
    clear = Comment.objects.all()
    clear.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def Details(request, name,  id):
    if name == 'shoes':
        shoedetails = Shoes.objects.filter(id = id)
        return render(request, "details.html", {"details":shoedetails, "name":name})

    elif name == 'jacket':
        jacketdetails = Jacket.objects.filter(id = id)
        return render(request, "details.html", {"details":jacketdetails, "name":name})
    elif name == 'shirt':
         shirtdetails = Shirt.objects.filter(id = id)
         return render(request, "details.html", {"details":shirtdetails,"name":name})

def AboutUs(request):
    return render(request, 'aboutus.html')
@login_required
def Chatspace(request):
    try:
        # Check if the user already has a chat space
        chat_space = ChatSpace.objects.filter(user=request.user).first()

        if chat_space:
            # If the user has a chat space, redirect to it
            return redirect('chatroom', spacename=chat_space.space)
    except ChatSpace.DoesNotExist:
        pass  # Continue to the next part to create a new space

    if request.method == 'POST':
        # Get the space name from the form submission
        spacename = request.POST.get('spacename')
        
        # Create a new ChatSpace if none exists for this user
        chat_space = ChatSpace.objects.create(space=spacename, user=request.user)
        
        # Redirect to the newly created chatroom
        return redirect('chatroom', spacename=chat_space.space)
    
    # Render the form to create a new chat space if not a POST request
    return render(request, 'chatspace.html')
    

def ChatRoom(request, spacename):
    if request.method == 'POST':
         messge = request.POST.get('textname')
         usr = request.user
         chat_space = ChatSpace.objects.get(space = spacename)
         create = Message.objects.create(space = chat_space, user = usr, message = messge)
         msg = Message.objects.filter(space = chat_space ).all()
         return render(request, 'chatroom.html', {"message":msg, "user":usr, "spacename":spacename} )
    else:
         return render(request, 'chatroom.html', {"spacename":spacename})
def Admin(request):
    return render(request, 'adminroom.html')


def Locate(request):
    if request.method == "get":
        locatin = request.POST.get('location')
        locate = location.get_or_create(location__icontains = locatin)
        return redirect('mainpage')
        
    