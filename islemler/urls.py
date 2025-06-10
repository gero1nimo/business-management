from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('new-transaction/', views.new_transaction, name='new-transaction'),
    path('delete-transaction/<int:islem_id>/', views.delete, name='delete-transaction'),
    path('update-transaction/<int:islem_id>/', views.update, name='update-transaction'),
    path('transactions/', views.transactions, name='transactions'),
    path('transaction/<int:islem_id>/', views.transaction_detail, name='transaction-detail'),
]

