from django.shortcuts import render, redirect
from .models import Transaction
from .create_transaction import TransactionForm
# Create your views here.

def dashboard(request):
    transactions = Transaction.objects.all().order_by('-islem_tarihi')
    context = {
        'transactions': transactions
    }
    return render(request, 'pages/overview.html', context)

def new_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/new-transaction/')  # Redirect to the dashboard after saving
    else:
        form = TransactionForm()
    return render(request, 'pages/new-transaction.html', {'form': form}) 

def transactions(request):
    transactions = Transaction.objects.all().order_by('-islem_tarihi')
    context = {
        'transactions': transactions
    }
    return render(request, 'pages/transactions.html', context)

def update(request, islem_id):
    transaction = Transaction.objects.get(pk=islem_id)
    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('/transactions/')  # Redirect to the transactions page after updating
    else:
        form = TransactionForm(instance=transaction)
    return render(request, 'pages/update-transaction.html', {'form': form
                                                             , 'transaction': transaction})

def delete(request, islem_id):
    transaction = Transaction.objects.get(pk=islem_id)
    if request.method == 'POST':
        transaction.delete()
        return redirect('/transactions/')  # Redirect to the transactions page after deleting
    return render(request, 'pages/delete-transaction.html', {'transaction': transaction})


def transaction_detail(request, islem_id):
    transaction = Transaction.objects.get(pk=islem_id)
    context = {
        'transaction': transaction
    }
    return render(request, 'pages/transaction-detail.html', context)