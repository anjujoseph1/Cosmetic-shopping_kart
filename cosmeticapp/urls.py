from django.urls import path
from.import views
urlpatterns = [
    path('cart_details/',views.cartdetails,name='cart_details'),
    path('add/<int:product_id>/',views.add_cart,name='addcart'),
    path('min/<int:product_id>/',views.min_cart, name='mincart'),
    path('remove/<int:product_id>/',views.remove, name='remove'),
    path('',views.home,name='home'),
    path('<slug:c_slug>',views.home,name='homee'),
    path('<slug:c_slug>/<slug:product_slug>',views.productdetails,name='details'),
    path('login/',views.loginform,name='login'),
    path('register/',views.registerform,name='register'),
]


