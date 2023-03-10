import json
from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core.handlers.wsgi import WSGIRequest
import utils
import config


def hiring(request):
    if request.method == 'POST':
        return hiring_submit(request)
    return render(request, 'index.html')


@csrf_exempt  # This is a security risk, but we'll talk about that later
def hiring_submit(request: WSGIRequest):
    if request.method != 'POST':
        print("[handler]", "Failed to handle request: not a POST request.")
        print("[handler]", request)
        return HttpResponse("404 Not Found", status=404)
    data = json.loads(request.body)
    print("[handler]", "Get new data!")
    print("[handler]", data)
    try:
        message = '<b>Свежее мясо!</b>\n\n'
        for key, value in data.items():
            if key == 'chat':
                if 'vk' in value:
                    message += f'<b>VK</b>: vk.com/{value["vk"][1:]}\n'
                if 'tg' in value:
                    message += f'<b>TG</b>: {value["tg"]}\n'
                continue
            message += f'<b>{key}</b>: {value}\n'
        utils.send_tg_message(config.TG_CHAT_ID, message)
    except Exception as exc:
        print("[handler]", "failed to send message")
        print("[handler]", exc)
        return HttpResponse("500 Internal Server Error", status=500)
    return JsonResponse({"success": True}, status=200)
