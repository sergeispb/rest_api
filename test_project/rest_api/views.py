from rest_framework import generics
from rest_api.models import Product, ProductGroup, Reservation
from rest_api.serializers import ProductsListSerializer, ProductGroupsListSerializer, ReservationsSerializer, ProductSerializer


class ProductsListView(generics.ListAPIView):
    serializer_class = ProductsListSerializer

    def get_queryset(self):
        """
        Метод для фильтрации товаров по категории.
        """
        group_filter = self.request.GET.get('group', None)
        if group_filter:
            return Product.objects.filter(group__name=group_filter)
        return Product.objects.all()


class ProductCreateView(generics.CreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductRUD(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductsListSerializer
    queryset = Product.objects.all()
    lookup_field = 'sku'


class GroupsListView(generics.ListAPIView):
    serializer_class = ProductGroupsListSerializer
    queryset = ProductGroup.objects.all()


class GroupCreateView(generics.CreateAPIView):
    serializer_class = ProductGroupsListSerializer
    queryset = ProductGroup.objects.all()


class GroupRUD(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductGroupsListSerializer
    queryset = ProductGroup.objects.all()


class ReservationsListView(generics.ListAPIView):
    serializer_class = ReservationsSerializer
    queryset = Reservation.objects.all()


class ReservationCreateView(generics.CreateAPIView):
    serializer_class = ReservationsSerializer
    queryset = Reservation.objects.all()


class ReservationRUD(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReservationsSerializer
    queryset = Reservation.objects.all()
