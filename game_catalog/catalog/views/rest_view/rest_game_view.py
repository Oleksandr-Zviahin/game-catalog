from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from catalog.models.game import Game, GameSerializer


@api_view(['GET', 'POST'])
def game_list(request):
    if request.method == 'GET':
        data = Game.objects.all()

        serializer = GameSerializer(data, many=True, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = GameSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
