from fastapi.routing import APIRouter

from .resources.googleads_dv360 import googleads_router
from .resources.health_check import health_router

router = APIRouter(prefix="/api/v1")
router.include_router(health_router)
router.include_router(googleads_router)
