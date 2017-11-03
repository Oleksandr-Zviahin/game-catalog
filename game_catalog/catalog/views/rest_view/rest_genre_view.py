from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from catalog.models.genre import Genre, GenreSerializer


@api_view(['GET', 'POST'])
def genre_list(request):
    if request.method == 'GET':
        data = Genre.objects.all()

        serializer = GenreSerializer(data, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
