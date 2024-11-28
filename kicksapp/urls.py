from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth import views as auth_views
urlpatterns = [
   path('', views.mainpage, name='mainpage'),
    path('login/', views.userlogin, name='login'),
    path('signup/', views.usersignup, name='signup'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reset_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(success_url='mainapp/login/'), name='password_reset_confirm'),
    path('reset/done', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('logout/', views.userlogout, name='logout'),
    path('Shoes', views.Shoe, name='Shoes'),
    path('jackets', views.Jacko, name='jackets'),
    path('shirt', views.Shati, name='shirt'),
    # path('shirtsupload', views.ShirtUpload, name='dummy'),
    # path('shoesupload', views.ShoeUpload, name= 'shoesupload'),
    # path('jacketsupload', views.JacketUpload, name= 'Jacketsupload'),
    path('add_to_cart/<str:pk>/<int:itemid>', views.CartItems, name = "add_to_cart"),
    path('viewcart/<str:pk>', views.ViewCart, name='viewcart'),
    path('removeitem/<int:itemid>', views.RemoveCart , name = 'removeitem'),
    path('adminjamo', views.AdminJamo, name='Admin'),
    path('search', views.search, name='search'),
    path('submit-comment/', views.comment_view, name='comment_view'),
    path('clear', views.clear, name="clear"),
    path('shirtsearch/<str:gen>', views.ShirtSearch, name='shirtsearch'),
    path('shoesearch/<str:gen>', views.ShoeSearch, name="shoesearch"), 
    path('jacketsearch/<str:gen>', views.JacketSearch, name="shoesearch"),
    path('details/<str:name>/<int:id>', views.Details, name='details' ),
    path('aboutus', views.AboutUs, name= 'aboutus'),
    path('chatspace', views.Chatspace, name='chatspace'),
    path('chatroom/<str:spacename>', views.ChatRoom, name = 'chatroom'),
    path('adminroom>', views.Admin, name = 'adminroom'),
    path('location/', views.Locate, name="Locate"),




  

]
