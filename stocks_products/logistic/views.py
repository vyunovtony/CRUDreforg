from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters
from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer
from django_filters import rest_framework as rest_framework_filters


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ['title', 'description']


class StockFilter(rest_framework_filters.FilterSet):
    products = rest_framework_filters.ModelChoiceFilter(queryset=Product.objects.all())

    class Meta:
        model = Stock
        fields = ['products']


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = (rest_framework_filters.DjangoFilterBackend, filters.OrderingFilter)
    filterset_class = StockFilter 
    ordering_fields = ['address']
