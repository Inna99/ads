from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from .serializers import AdSerializer
from .models import Ad


class ListAdAPIView(ListAPIView):
    """This endpoint list all of the available todos from the database"""

    queryset = Ad.objects.all()
    serializer_class = AdSerializer


class CreateAdAPIView(CreateAPIView):
    """This endpoint allows for creation of a todo"""

    queryset = Ad.objects.all()
    serializer_class = AdSerializer


class UpdateAdAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific todo by passing in the id of the todo to update"""

    queryset = Ad.objects.all()
    serializer_class = AdSerializer


class DeleteAdAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific Todo from the database"""

    queryset = Ad.objects.all()
    serializer_class = AdSerializer
