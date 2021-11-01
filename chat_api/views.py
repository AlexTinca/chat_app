from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MessageSerializer, RoomSerializer, ParticipantSerializer

from .models import Message, Participant


@api_view(['POST'])
def messages_post(request):
    serializer = MessageSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
def messages_get(request, room_id):
    messages = Message.objects.filter(roomID=room_id)

    serializer = MessageSerializer(messages, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def room_post(request):
    serializer = RoomSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def participant_post(request, room_id):
    data = {'userID': request.data.get('id'),
            'roomID': room_id}

    serializer = ParticipantSerializer(data=data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def participant_delete(request, room_id, user_id):
    try:
        participant = Participant.objects.get(userID__exact=user_id, roomID__exact=room_id)
    except Participant.DoesNotExist:
        return HttpResponse(status=404)

    participant.delete()

    return Response(status=204)
