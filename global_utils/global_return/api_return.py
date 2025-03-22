from rest_framework.response import Response
from rest_framework import status


def api_response(
    message: str = None,
    error: str = None,
    data: dict | list = None,
    status: status = status.HTTP_500_INTERNAL_SERVER_ERROR,
):
    return Response(
        {"message": message, "data": data, "status": status, "error": error}
    )
