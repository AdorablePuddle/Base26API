from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from Base26API.quickstart.app.app import *

# Create your views here.

@api_view(["GET", "POST"])
def base26_post(request):
    if request.method == "GET":
        return Response(status = status.HTTP_200_OK)
    elif request.method == "POST":
        request_data = dict(request.data)
        if ("value" not in request_data.keys()) or ("type" not in request_data.keys()):
            return Response(data = {"error_type" : "Missing key"}, status = status.HTTP_400_BAD_REQUEST)
        else:
            response = ""
            if request_data["type"] == "dto26":
                response = str(base10to26(int(request_data["value"])))
            elif request_data["type"] == "26tod":
                response = str(base26to10(request_data["value"]))
            else:
                return Response(data = {"error_type" : f"Invalid \"type\" key: {request_data["type"]}"}, status = status.HTTP_400_BAD_REQUEST)
            return Response(data = {"result" : response}, status = status.HTTP_200_OK)
    else:
        return Response(status = status.HTTP_400_BAD_REQUEST)