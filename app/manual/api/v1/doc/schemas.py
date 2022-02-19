from drf_yasg import openapi

from src.settings import CUSTOM_RESPONSES
# x = openapi.Schema(
# )
validate_items_response_schema = {
    "200": openapi.Response(
        description="custom 200 response",
        examples={
            "application/json": CUSTOM_RESPONSES[0]
        }
    ),
    "204": openapi.Response(
        description="custom 204 response",
        examples={
            "application/json": CUSTOM_RESPONSES[1],
        }
    ),
    "400": openapi.Response(
        description="custom 400 response",
        examples={
            "application/json": CUSTOM_RESPONSES[2]
        }
    ),
}
