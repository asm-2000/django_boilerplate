from rest_framework import status
from typing import Dict, Any, List


def service_return(
    message: str = None,
    error: str = None,
    data: Dict[str, Any] | List[Any] = None,
    status: status = status.HTTP_500_INTERNAL_SERVER_ERROR,
):
    return {"message": message, "data": data, "error": error, "status": status}
