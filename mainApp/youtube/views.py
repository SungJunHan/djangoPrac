
import json
from django.http import JsonResponse, HttpResponse
from django.views import View
from .models import VideosName
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.core.serializers import serialize
from django.views.decorators.csrf import csrf_exempt


class GetVideo(View):
    def get(self, request):
        videos = VideosName.objects.all().order_by('id')
        data=json.loads(serialize('json', videos))

        return JsonResponse({'data':data}, status=200)

    @csrf_exempt
    def post(self, request):
        if request.META['CONTENT_TYPE'] == "application/json":
            request = json.loads(request.body)

            video = VideosName(title = request['title'],
                               body = request['body'],
                               uploadDate=timezone.localtime()
                               )

        else:
            video = VideosName(title=request.POST['title'],
                               body=request.POST['body'],
                               uploadDate=timezone.localtime()
                               )

        video.save()
        return JsonResponse({'message': 'success'}, status=201)

    @csrf_exempt
    def put(self, request):
        request = json.loads(request.body)
        id = request['id']
        title = request['title']

        video = get_object_or_404(VideosName, pk=id)
        video.title = title

        video.save()
        return JsonResponse({'message':'put success'}, status=200)

    @csrf_exempt
    def delete(self, request):
        request = json.loads(request.body)
        id = request['id']
        video = get_object_or_404(VideosName, pk=id)
        video.delete()

        return JsonResponse({'message': 'delete success'}, status=200)

# @csrf_exempt
#     def put(self, request):
#         if request.META['CONTENT_TYPE'] == "application/json":
#             request = json.loads(request.body)
#             id = request['id']
#             title = request['title']
#             body = request['body']
#         else:
#             id = request.PUT['id']
#             title = request.PUT['title']
#             body = request.PUT['body']
#         video = get_object_or_404(VideosName, pk=id)
#         video.title = title
#         video.body = body
#         video.save()
#         return JsonResponse({"message": "put success"}, status=200)
#
#     @csrf_exempt
#     def delete(self, request):
#         if request.META['CONTENT_TYPE'] == "application/json":
#             request = json.loads(request.body)
#             id = request['id']
#         else:
#             id = request.DELETE['id']
#         video = get_object_or_404(VideosName, pk=id)
#         video.delete()
#         return JsonResponse({"message": "delete success"}, status=200)