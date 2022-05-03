from pydantic import Field

from src.schemas import CustomBaseModel


class ThirdPartyOnlyConfigSchema(CustomBaseModel):
    pixel_order_id_reporting_enabled: bool = Field(alias="pixelOrderIdReportingEnabled")


class AdServerConfigSchema(CustomBaseModel):
    third_party_only_config: ThirdPartyOnlyConfigSchema = Field(
        alias="thirdPartyOnlyConfig"
    )


class GeneralConfigSchema(CustomBaseModel):
    domain_url: str = Field(alias="domainUrl")
    currency_code: str = Field(alias="currencyCode")


class CreateAdvertiserSchema(CustomBaseModel):
    partner_id: int = Field(alias="partnerId")
    display_name: str = Field(alias="displayName")
    entity_status: str = Field(alias="entityStatus")
    general_config: GeneralConfigSchema = Field(alias="generalConfig")
    ad_server_config: AdServerConfigSchema = Field(alias="thirdPartyOnlyConfig")
