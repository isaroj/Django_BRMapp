from BRMapp import views
from django.urls import path
urlpatterns=[
              path('view-books',views.viewBook),
              path('edit-book',views.editBook),
              path('delete-book',views.deleteBook),
              path('search-book',views.searchBook),
              path('new-book',views.newBook),
              path('add',views.add),
              path('edit',views.edit),
              path('search',views.search),
              path('login',views.userLogin),
              path('logout',views.userLogout),
              path('signup',views.userSignup),
              path('valid',views.valid),


]
