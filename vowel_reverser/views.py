from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions, generics

from .helpers import reverse

# Create your views here.
@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def reverse_vowel(request):
    """ Reverse "message" vowel values """
    if request.method == 'POST':
        message = reverse(request.data['message'])
        return JsonResponse({"message": message}, status=200)
    else:
        return JsonResponse({}, status=405)
