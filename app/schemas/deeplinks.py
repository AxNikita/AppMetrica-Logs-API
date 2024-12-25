from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class DeeplinksSchema(BaseModel):
    """
    Открытия приложения через deeplink.
    https://appmetrica.yandex.ru/docs/ru/mobile-api/logs/ref/deeplinks
    """
    deeplink_url_host: Optional[str] = Field(
        default=None,
        description='Доменное имя deeplink. Например, для ссылки вида [scheme]:[//host][/path][?parameters] возвращает host.'
    )
    deeplink_url_parameters: Optional[str] = Field(
        default=None,
        description='Параметры, которые передаются в deeplink. Подробнее о передаче параметров в р��зделе Параметры tracking URL.'
    )
    deeplink_url_path: Optional[str] = Field(
        default=None,
        description='URL-путь deeplink. Например, для ссылки вида [scheme]:[//host][/path][?parameters] возвращает path.'
    )
    deeplink_url_scheme: Optional[str] = Field(
        default=None,
        description='URL-схема deeplink. Например, для ссылки вида [scheme]:[//host][/path][?parameters] возвращает scheme.'
    )
    event_datetime: Optional[datetime] = Field(
        default=None,
        description='Дата и время события в формате yyyy-mm-dd hh:mm:ss.'
    )
    event_receive_datetime: Optional[datetime] = Field(
        default=None,
        description='Дата и время получения сервером события. Может отличаться от event_datetime из-за задержек в сети или отсутствия подключения у пользователя на момент события.'
    )
    event_receive_timestamp: Optional[int] = Field(
        default=None,
        description='Время получения сервером события в формате UNIX-time. Может отличаться от event_timestamp из-за задержек в сети или отсутствия подключения у пользователя на момент события.'
    )
    event_timestamp: Optional[int] = Field(
        default=None,
        description='Время события в формате UNIX-time. Post API позволяет загрузить только те события, у которых разница между датой совершения события (event_timestamp) и датой загрузки не больше 7 дней. Ожидается значение в секундах.'
    )
    is_reengagement: Optional[bool] = Field(
        default=None,
        description='Признак, который определяет, что трекер создан для ремаркетинг-кампании.'
    )
    profile_id: Optional[str] = Field(
        default=None,
        description='Идентификатор пользовательского профиля.'
    )
    publisher_id: Optional[int] = Field(
        default=None,
        description='ID партнера в AppMetrica. Может использоваться для определения партнера в отчетах AppMetrica. Если для трекера включены неатрибуцированные постбеки, то значение поля будет равно 0.'
    )
    publisher_name: Optional[str] = Field(
        default=None,
        description='Название партнера AppMetrica. Если для трекера включены неатрибуцированные постбеки, то значение поля будет пустым.'
    )
    session_id: Optional[int] = Field(
        default=None,
        description='Идентификатор сессии. Набор из значений installation_id, session_id и платформенного идентификатора устройства (google_aid / ios_ifa) позволяет однозначно идентифицировать сессию пользователя.'
    )
    tracker_name: Optional[str] = Field(
        default=None,
        description='Название трекера, который добавляется в интерфейсе AppMetrica. Если для трекера включены неатрибуцированные постбеки, то значение поля будет пустым.'
    )
    tracking_id: Optional[int] = Field(
        default=None,
        description='ID трекера в AppMetrica. Может использоваться для определения партнера в отчетах AppMetrica. Если для трекера включены неатрибуцированные постбеки, то значение поля будет равно 0.'
    )
    android_id: Optional[str] = Field(
        default=None,
        description='Идентификатор Android.'
    )
    appmetrica_device_id: Optional[str] = Field(
        default=None,
        description='Уникальный идентификатор устройства, который устанавливает AppMetrica. В Android от AppSetId, в IOS от IFV.'
    )
    appmetrica_sdk_version: Optional[int] = Field(
        default=None,
        description='Версия AppMetrica SDK.'
    )
    city: Optional[str] = Field(
        default=None,
        description='Название города на английском языке, где был произведен клик.'
    )
    connection_type: Optional[str] = Field(
        default=None,
        description='Тип подключения устройства. Возможные значения: wifi | cell | unknown.'
    )
    country_iso_code: Optional[str] = Field(
        default=None,
        description='ISO-код страны.'
    )
    device_ipv6: Optional[str] = Field(
        default=None,
        description='IP-адрес в момент совершения события в формате IPv6. Например, 2a02:6b8::40c:6676:baff:fea6:53d8, ::ffff:5.255.232.147.'
    )
    device_locale: Optional[str] = Field(
        default=None,
        description='Язык интерфейса устройства.'
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
    ios_ifa: Optional[str] = Field(
        default=None,
        description='IFA устройства в формате, в котором получен от устройства.'
    )
    ios_ifv: Optional[str] = Field(
        default=None,
        description='IFV для приложения в формате, в котором получен от устройства.'
    )
    mcc: Optional[int] = Field(
        default=None,
        description='Мобильный код страны.'
    )
    mnc: Optional[int] = Field(
        default=None,
        description='Код мобильной сети.'
    )
    original_device_model: Optional[str] = Field(
        default=None,
        description='Заводская модель устройства (например, для Galaxy S8 возможны следующие значения: SM-G9550, SM-G9558 и т. д.).'
    )
    os_version: Optional[str] = Field(
        default=None,
        description='Версия операционной системы на устройстве пользователя.'
    )
    windows_aid: Optional[str] = Field(
        default=None,
        description='Windows AID устройства в формате, в котором получен от устройства.'
    )
    app_build_number: Optional[int] = Field(
        default=None,
        description='Номер сборки приложения.'
    )
    app_package_name: Optional[str] = Field(
        default=None,
        description='Имя пакета для Android или Bundle ID для iOS (например, ru.yandex.metro).'
    )
    app_version_name: Optional[str] = Field(
        default=None,
        description='Версия приложения в виде, как указана разработчиком.'
    )
