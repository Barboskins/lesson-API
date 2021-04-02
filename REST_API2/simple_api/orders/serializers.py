from rest_framework import serializers

from orders.models import Order, ProductOrders


class ProductOrdersSerializer(serializers.ModelSerializer):

    product_id = serializers.IntegerField()

    class Meta:
        model = ProductOrders

        fields = ('id','quantity','product_id')

class OrderSerializer(serializers.ModelSerializer):

    positions = ProductOrdersSerializer(many=True, source='order_positions')

    class Meta:
        model = Order

        fields = ('id', 'name', 'positions', 'created_at')
    def create(self, validated_data):
        positions = validated_data.pop("order_positions")
        order = super().create(validated_data)
        if positions:
            to_save = []
            for position in positions:
                to_save.append(ProductOrders(
                    product_id=position["product_id"],
                    order_id=order.id,
                    quantity=position["quantity"]
                ))
            ProductOrders.objects.bulk_create(to_save)
        return order

