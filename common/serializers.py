from rest_framework import serializers


class GenericSerializer(serializers.ModelSerializer):
    class Meta:
        model = None  # Model will be set dynamically
        fields = '__all__'  # Default to all fields, but can be overridden

    def __init__(self, *args, **kwargs):
        # Dynamically set the model if not set in Meta
        model = kwargs.pop('model', None)
        if model:
            self.Meta.model = model
        super().__init__(*args, **kwargs)
