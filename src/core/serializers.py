from rest_framework import serializers


class ItemSerializer(serializers.Serializer):
    items = serializers.ListField(
        min_length=1,
        allow_empty=False,
        allow_null=False,
        child=serializers.IntegerField(),
    )
