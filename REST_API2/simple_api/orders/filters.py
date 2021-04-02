from django_filters import rest_framework as filters

from orders.models import Order


class OrderFilterSet(filters.FilterSet):
    id = filters.ModelMultipleChoiceFilter(field_name='id', to_field_name='id', queryset=Order.objects.all())
    name = filters.CharFilter(lookup_expr='icontains')
    created_at = filters.DateFromToRangeFilter()
