from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from contactUs.models import contactMessage
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def item_api(request):
    if request.method == 'GET':
        data = {
            'id':1,
            'username':'mahmut'
        }
        return JsonResponse(data,status=200)
    
    if request.method == 'POST':
        try:
            body = json.loads(request.body)
            name = body.get('name')
            email = body.get('email')
            subject = body.get('subject')
            message = body.get('message')
            try:
                a = contactMessage(name=name,email=email,subject=subject,message=message)
                a.save()
                return JsonResponse({'message':'contact message has been saved'},status=200)
            except contatMessage.DoesNotExist:
                return JsonResponse({'error':'contact message could not be saved'},status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error':'invalid request'},status=400)
    
    if request.method == 'PUT':
        try:
            body = json.loads(request.body)
            id = body.get('id')
            if id is not None and isinstance(id,int):
                try:
                    item = contactMessage.objects.get(id=id)
                    if body.get('name') is None and body.get('subject') is None and body.get('email') is None and body.get('message') is  None:
                        return JsonResponse({'error':'message, subject, email or message need to be provided'},status=400)
                    if body.get('name') is not None:
                        item.name = body.get('name')            
                    if body.get('subject') is not None:
                        item.subject = body.get('subject')                   
                    if body.get('email') is not None:
                        item.email = body.get('email')
                    if body.get('message') is not None:
                        item.message = body.get('message')
                    item.save()
                    return JsonResponse({'message':'The item has been updated'}, status= 200)
                except contactMessage.DoesNotExist:
                    return JsonResponse({'error':'id could not be found'}, status=204)
            else:
                return JsonResponse({'error':'an integer id is required'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error':'invalid request'}, status=400)
    
    if request.method == 'DELETE':
        try:
            body = json.loads(request.body)
            id = body.get('id')
            if id is not None and isinstance(id,int):
                try:
                    item = contactMessage.objects.get(id=id)
                    item.delete()
                    return JsonResponse({'message':'The item has been deleted'}, status= 200)
                except contactMessage.DoesNotExist:
                    return JsonResponse({'error':'id could not be found'}, status=204)
            else:
                return JsonResponse({'error':'an integer id is required'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error':'invalid request'}, status=400)

    else:
        return HttpResponse(status=405)