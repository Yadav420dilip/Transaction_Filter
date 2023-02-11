from .models import Transaction
import django_filters


class TransactionFilter(django_filters.FilterSet):
    # date = django_filters.DateFilter(field_name='date', lookup_expr='date')
    start_date = django_filters.DateFilter(field_name='date', lookup_expr='date__gt', label='Start Date')
    end_date = django_filters.DateFilter(field_name='date', lookup_expr='date__lt', label='End Date')

    amt = django_filters.OrderingFilter(
        fields=(
            ('amt', 'Amount'),
        ),

        # labels do not need to retain order
        field_labels={
            'Amount': 'Amount',
        }
    )
    class Meta:
        model = Transaction
        fields = ['date']
