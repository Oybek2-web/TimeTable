import datetime

from django.http import HttpResponse


class LogIPMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = request.META.get('REMOTE_ADDR', 'Noma\'lum IP')
        now = datetime.datetime.now()
        print(f"[{now}] So'rov IP: {ip}")


        response = self.get_response(request)


        print(f"Status: {response.status_code}")

        return response


class TimeLimitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        hours = datetime.datetime.now().hour

        if not (8 <= float(hours) < 18):
            return HttpResponse('Ish vaqtida emas')
        response = self.get_response(request)
        return response