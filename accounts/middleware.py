import logging

logger = logging.getLogger(__name__)

class PickleDetectionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Only inspect POST requests going to our API
        if request.method == 'POST' and 'api/' in request.path:
            body_str = str(request.body)
            
            # 'gASV' is the standard base64 signature for Pickle Protocol 4.
            # 'cposix' and 'os.system' are signatures of remote code execution.
            if 'gASV' in body_str or 'cposix' in body_str:
                attacker_ip = request.META.get('REMOTE_ADDR')
                print(f"\n[CRITICAL SECURITY ALERT] Insecure Deserialization signature detected!")
                print(f"[!] Attacker IP: {attacker_ip}")
                print(f"[!] Target URL: {request.path}\n")
                
                logger.critical(f"Deserialization attack detected from {attacker_ip}")

        # Continue processing the request normally
        response = self.get_response(request)
        return response