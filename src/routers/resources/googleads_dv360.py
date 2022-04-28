import logging
from fastapi import APIRouter, HTTPException, status
from googleapiclient.errors import HttpError
from src.schemas.googleads_dv360 import CreateAdvertiserSchema

logger = logging.getLogger(__name__)

googleads_router = APIRouter(prefix="/googleads", tags=["Google DV-360"])


@googleads_router.post("/")
def create_advertiser(data: CreateAdvertiserSchema):
    try:
        return data
    except Exception as error:
        logger.exception(f"Error: {error}")
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail={
                "message": "Erro ao realizar cadastro. Tente novamente em alguns minutos"
            },
        ) from error
    except HttpError as error:
        logger.info("[Register Error] - Occurred error in register of the advertiser")
        logger.exception(f"Error: {error}")
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail={f"message": {error}
                    },
        ) from error
