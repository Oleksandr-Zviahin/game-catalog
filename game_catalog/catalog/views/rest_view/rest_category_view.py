from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from catalog.models.category import Category, CategorySerializer


@api_view(['GET', 'POST'])
def category_list(request):
    if request.method == 'GET':
        data = Category.objects.all()

        serializer = CategorySerializer(data, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
