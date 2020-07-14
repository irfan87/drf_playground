from django.shortcuts import render
from django.http import JsonResponse

# drf package
from rest_framework.views import APIView
from rest_framework.response import Response   

class TestView(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            'name': 'irfan',
            'age': 33,
        }

        return Response(data)

# def test_view(request):
#     data = {
#         'name': 'irfan',
#         'age': 33,
#     }

#     return JsonResponse(data)
