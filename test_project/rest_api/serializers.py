from rest_framework import serializers

from rest_api.models import Product, ProductGroup, Reservation


class ReservationsSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        """
        Метод проверяет сколько товара можно зарезервировать (кол-во товара на складе минус зарезервированное кол-во).
        Если запрашиваемое кол-во товара больше чем (кол-во товара на складе минус зарезервированное кол-во),
        возбуждается "ValidationError".
        В ином случае происходит резервация товара.
        """
        product = Product.objects.get(sku=attrs['product_sku'])
        if product.balance_including_reservation() < attrs['count']:
            raise serializers.ValidationError({'count': 'There is no such quantity of goods in stock'})
        return super(ReservationsSerializer, self).validate(attrs)

    class Meta:
        model = Reservation
        fields = '__all__'


class ProductsListSerializer(serializers.ModelSerializer):
    sku = serializers.SlugField(read_only=True)
    name = serializers.CharField(read_only=True)
    group = serializers.SlugRelatedField(slug_field='name', read_only=True)
    reservations = ReservationsSerializer(many=True, required=False)

    class Meta:
        model = Product
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductGroupsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductGroup
        fields = '__all__'
