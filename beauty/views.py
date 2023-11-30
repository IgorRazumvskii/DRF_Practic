from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from .models import Beauty
from .serializers import BeautySerializer, BeautyGetSerializer, MailSerializer


class BeautyView(generics.ListAPIView):
    queryset = Beauty.objects.all()
    serializer_class = BeautySerializer


class Mail(generics.ListAPIView):
    queryset = Beauty.objects.all()
    #  lookup_field = 'user__email'
    serializer_class = MailSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user__email=self.kwargs['email'])


class BeautyCreate(generics.CreateAPIView):
    queryset = Beauty.objects.all()
    serializer_class = BeautySerializer

    def post(self, request, *args, **kwargs):
        serializer = BeautySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            obj = serializer.save()
            return Response({'status': 200, 'message': 'null', 'id': obj.id})
        else:
            return Response(serializer.errors.as_data())

    def get_queryset(self):
        return


class Beauty(generics.RetrieveUpdateAPIView):
    queryset = Beauty.objects.all()
    serializer_class = BeautyGetSerializer
    http_method_names = ['get', 'patch']

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.status == 'new':
            serializer = BeautyGetSerializer(data=request.data, instance=instance)
            if serializer.is_valid():
                serializer.save()
                return Response({'state': 1})
            else:
                return Response({'state': 0,
                          'message': serializer.errors})

        else:
            return Response({'state': 0,
                      'message': 'Status not new'})

