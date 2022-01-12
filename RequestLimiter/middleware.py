from django.shortcuts import render, redirect
from django.conf import settings
from .functions import date_time_now, str_to_datetime
import requests

class RequestLimiterMiddleware:
    
    def __init__(self, get_response) -> None:
        self.get_response = get_response
        self.available_views = settings.AVAILABLE_VIEWS or []
        self.min_request_time = settings.MIN_REQUEST_TIME or 1.8
        self.punishment_requests = settings.PUNISHMENT_REQUESTS or 100
    
    def __call__(self, request):
        response = self.get_response(request)
        return response
    
    
    def process_view(self, request, view, *args, **kwargs):
        if request.method == 'POST' and self._view_is_valid(view):
            if not self._session_has_values(request.session):
                session_values = self._get_session_values()
                for k, v in session_values.items():
                    request.session[k] = v
            else:
                last_post_request = str_to_datetime(request.session['last_post_request'])
                now_request = date_time_now()
                request.session['last_post_request'] = now_request.__str__()
                if not self._request_is_valid(last_post_request, now_request, self.min_request_time):
                    request.session['invalid_request_sequence'] += 1
                    if request.session['invalid_request_sequence'] > 3:
                        self._apply_punishment(self.punishment_requests)
                    return redirect('request:invalid_request')
                request.session['invalid_request_sequence'] = 0
        request.session.modified = True
                
                
    def _view_is_valid(self, view) -> bool:
        return view.__name__ not in self.available_views
    
    
    def _get_session_values(self) -> dict:
        return {
            'last_post_request': date_time_now().__str__(),
            'min_request_time': self.min_request_time,
            'punishment_requests': self.punishment_requests,
            'invalid_request_sequence': 0,
        }
        
    
    def _session_has_values(self, session) -> bool:
        for key in self._get_session_values().keys():
            if key not in session.keys():
                return False
        return True
        
        
    def _request_is_valid(self, last, now, min_request_time):
        return (now - last).total_seconds() > min_request_time
    
    
    def _apply_punishment(self, amount_requests):
        return [requests.get('http://www.google.com') for _ in range(amount_requests + 1)]