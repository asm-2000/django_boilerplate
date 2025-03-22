from rest_framework import status


def service_return(
    message: str = None,
    error: str = None,
    data: dict | list = None,
    status: status = status.HTTP_500_INTERNAL_SERVER_ERROR,
):
    return {"message": message, "data": data, "error": error, "status": status}
