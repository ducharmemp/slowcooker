from flask.views import MethodView

from source.models import connection

class SessionView(MethodView):
    def dispatch_request(self, *args, **kwargs):
        with connection() as session:
            return super().dispatch_request(session, *args, **kwargs)
