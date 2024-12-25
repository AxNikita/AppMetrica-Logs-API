from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class ClicksSchema(BaseModel):
    """
    Трекинговые клики и показы.
    https://appmetrica.yandex.ru/docs/ru/mobile-api/logs/ref/clicks
    """
    application_id: Optional[int] = Field(
        default=None,
        description='Уникальный числовой идентификатор приложения в AppMetrica.'
    )
    touch_type: Optional[str] = Field(
        default=None,
        description='Тип: клик или показ. Возможные значения: click | impression | unknown.'
    )
    click_datetime: Optional[datetime] = Field(
        default=None,
        description='Дата и время клика/показа в формате yyyy-mm-dd hh:mm:ss.'
    )
    click_id: Optional[str] = Field(
        default=None,
        description='Идентификатор клика/показа или \'\' (пустая строка, если недоступен).'
    )
    click_ipv6: Optional[str] = Field(
        default=None,
        description='IP-адрес в момент клика/показа в формате IPv6. Например, 2a02:6b8::40c:6676:baff:fea6:53d8, ::ffff:5.255.232.147.'
    )
    click_timestamp: Optional[int] = Field(
        default=None,
        description='Время клика/показа в формате UNIX-time в секундах.'
    )
    click_url_parameters: Optional[str] = Field(
        default=None,
        description='Параметры, как они представлены в ссылке. При этом специальные символы необходимо экранировать (например, ?param1=1&param2=2... будет выглядеть в запросе как ?param1%3D1%26param2%3D2...).'
    )
    click_user_agent: Optional[str] = Field(
        default=None,
        description='User-agent клика/показа.'
    )
    publisher_id: Optional[int] = Field(
        default=None,
        description='ID партнера в AppMetrica. Может использоваться для определения партнера в отчетах AppMetrica. Если для трекера включены неатрибуцированные постбеки, то значение поля будет равно 0.'
    )
    publisher_name: Optional[str] = Field(
        default=None,
        description='Название партнера AppMetrica. Если для трекера включены неатрибуцированные постбеки, то значение поля будет пустым.'
    )
    tracker_name: Optional[str] = Field(
        default=None,
        description='Название трекера, который добавляется в интерфейсе AppMetrica. Если для трекера включены неатрибуцированные постбеки, то значение поля будет пустым.'
    )
    tracking_id: Optional[int] = Field(
        default=None,
        description='ID трекера в AppMetrica. Может использоваться для определения партнера в отчетах AppMetrica. Если для трекера включены неатрибуцированные постбеки, то значение поля будет равно 0.'
    )
    city: Optional[str] = Field(
        default=None,
        description='Название города на английском языке, где был произведен клик.'
    )
    country_iso_code: Optional[str] = Field(
        default=None,
        description='ISO-код страны.'
    )
    device_manufacturer: Optional[str] = Field(
        default=None,
        description='Производитель устройства, определяется сервисом AppMetrica (например, Apple или Samsung).'
    )
    device_model: Optional[str] = Field(
        default=None,
        description='Модель устройства, определяется сервисом AppMetrica (например, Galaxy S6).'
    )
    device_type: Optional[str] = Field(
        default=None,
        description='Тип устройства, определяется сервисом AppMetrica. Возможные значения: phone | tablet | unknown.'
    )
    google_aid: Optional[str] = Field(
        default=None,
        description='Google AID устройства в формате, в котором получен от устройства.'
    )
    oaid: Optional[str] = Field(
        default=None,
        description='Huawei OAID устройства в формате, в котором получен от устройства.'
    )
    ios_ifa: Optional[str] = Field(
        default=None,
        description='IFA устройства в формате, в котором получен от устройства.'
    )
    ios_ifv: Optional[str] = Field(
        default=None,
        description='IFV для приложения в формате, в котором получен от устройства.'
    )
    os_name: Optional[str] = Field(
        default=None,
        description='Операционная система на устройстве пользователя: ios | android | windows.'
    )
    os_version: Optional[str] = Field(
        default=None,
        description='Версия операционной системы на устройстве пользователя.'
    )
    windows_aid: Optional[str] = Field(
        default=None,
        description='Windows AID устройства в формате, в котором получен от устройства.'
    )
    is_bot: Optional[bool] = Field(
        default=None,
        description='Признак клика, совершённого не из браузера.'
    )
