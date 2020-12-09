# Local application imports
from kentik_api.api_calls.api_call_decorators import get
from kentik_api.api_calls.api_call import APICall


@get
def get_plans() -> APICall:
    """Returns an array of plans objects that each contain information about an individual plan."""
    return APICall("/plans")
