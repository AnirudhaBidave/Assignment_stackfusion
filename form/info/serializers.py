from rest_framework import serializers
# from django.contrib.auth.models import submit_info
from info.models import submit_info


class SubmitSerializer(serializers.ModelSerializer):
    class Meta:
        model = submit_info
        fields = ('name', 'dob', 'email', 'mob')
