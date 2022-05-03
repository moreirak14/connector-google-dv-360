import logging

from fastapi import APIRouter, HTTPException, status
from googleapiclient.errors import HttpError

from src.schemas.googleads_dv360 import CreateAdvertiserSchema
from src.utils.samples_util import get_service

logger = logging.getLogger(__name__)

google_router = APIRouter(prefix="/google-dv360", tags=["Google DV-360"])


@google_router.get("/")
def list_advertiser():
    service = get_service(version="v1")
    request = service.advertisers().list(partnerId="1359235", pageSize="5")
    return request.execute()


# TODO: ENDPOINT PARA PEGAR INFORMAÇÕES DO ADVERTISER
# https://developers.google.com/display-video/api/reference/rest/v1/advertisers#Advertiser
@google_router.get("/advertiser")
def get_advertiser(advertiser_id: str):
    service = get_service(version="v1")
    request = service.advertisers().advertiser.get(partnedId="1359235", advertiserId=advertiser_id)
    return request

# TODO: ENDPOINT PARA LISTAR AS CAMPANHAS
# https://developers.google.com/display-video/api/reference/rest/v1/advertisers.campaigns/list

# TODO: ENDPOINT PARA PEGAR INFORMAÇÕES DA CAMPANHA
# https://developers.google.com/display-video/api/reference/rest/v1/advertisers.campaigns/get


@google_router.post("/")
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
        )
    except HttpError as error:
        logger.info("[Register Error] - Occurred error in register of the advertiser")
        logger.exception(f"Error: {error}")
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail={"message": error},
        )
