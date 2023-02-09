from django.shortcuts import render
from .models import Transaction
from .filter import TransactionFilter


def transaction_details(request):
    transaction_list = Transaction.objects.all().values()
    transaction_filter = TransactionFilter(request.GET, queryset=transaction_list)
    return render(request, 'transaction_template.html', context={'filter': transaction_filter})
