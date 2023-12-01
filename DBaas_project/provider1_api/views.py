from rest_framework import viewsets,status
from .models import Provider
from .serializers import ProviderSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class ProviderViewSet(viewsets.ModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer

    def create(self, request, *args, **kwargs):
        user_id = request.data.get('user')
        provider_name = request.data.get('provider_name')
        Key_name = request.data.get('key_name')
        provider_url = request.data.get('provider_url')
        secret_key = request.data.get('secret_key')
        access_token = request.data.get('access_token')
        
        if Provider.objects.filter(provider_url=provider_url).exists():
            return Response({"Provider_error": "Provider URL already exists"}, status=status.HTTP_400_BAD_REQUEST)
 
        # Error handling for Key_name
        if Provider.objects.filter(Key_name=Key_name).exists():
            return Response({"apiName_error": "Key name already exists"}, status=status.HTTP_400_BAD_REQUEST)

        provider = Provider(
            user_id=user_id,
            provider_name=provider_name,
            Key_name=Key_name,
            provider_url=provider_url,
            secret_key=secret_key,
            access_token=access_token,
            is_connected=True
        )
        provider.save()

        serializer = ProviderSerializer(provider)
        return Response(serializer.data, status=201)

    def get_provider_by_name(self, request, provider_name):
        provider = get_object_or_404(Provider, provider_name=provider_name)
        serializer = ProviderSerializer(provider)
        return Response(serializer.data)

    def get_provider_by_user_id(self, request, user_id):
        providers = Provider.objects.filter(user=user_id)
        serializer = ProviderSerializer(providers, many=True)
        return Response(serializer.data)
