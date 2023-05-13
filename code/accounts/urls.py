from django.urls import path
from . import views


urlpatterns = [
	# path('login/', views.login, name="login"),  
	# path('logout/', views.logoutUser, name="logout"),
	path('home/', views.home, name="home"),
    # path('loanapp/', views.loanTest, name="loan_url"),
    path('', views.craicLounge, name="craiclounge"),
    path('leaderboard/', views.leaderboard, name='leaderboard'),

    path('profile/', views.profile, name="profile"),

    # path('profile/leaderboard/', views.leaderboard, name='leaderboard'),
    # path('logout', views.logoutUser, name="logout_url"),

    # # path('dashboard/', views.crypto, name="dashboard_url"),

   path('register/', views.register, name="register_url"),



    # path('base/', views.base, name="base-home"),
    # path('products/', views.products, name='products'),
    # path('customer/<str:pk_test>/', views.customer, name="customer"),

    # path('create_order/<str:pk>/', views.createOrder, name="create_order"),
    # path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
    # path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),
	# path('', views.homepage, name="homepage"),

]