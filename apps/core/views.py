from django.db import DatabaseError, connection
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class HealthCheckView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    def get(self, request):
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT 1")

            return Response(
                {
                    "status": "ok",
                    "database": "ok",
                },
                status=200,
            )

        except DatabaseError:
            return Response(
                {
                    "status": "error",
                    "database": "unreachable",
                },
                status=503,
            )
