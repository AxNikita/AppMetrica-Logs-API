from datetime import datetime

from pydantic import BaseModel, Field


class AdRevenueEventsSchema(BaseModel):
    """
    Доходы.
    https://appmetrica.yandex.ru/docs/ru/mobile-api/logs/ref/ad_revenue_events
    """
    ad_revenue_datetime: datetime | None = Field(
        description='Дата и время события в формате yyyy-mm-dd hh:mm:ss.'
    )
    ad_revenue_timestamp: int | None = Field(
        description='Время события в формате UNIX-time.\n\nPost API позволяет загрузить только те события, у которых разница между датой совершения события (event_timestamp) и датой загрузки не больше 7 дней. Ожидается значение в секундах.'
    )
    ad_revenue_receive_datetime: datetime | None = Field(
        description='Дата и время получения сервером события. Может отличаться от ad_revenue_datetime из-за задержек в сети или отсутствия подключения у пользователя на момент события.'
    )
    ad_revenue_receive_timestamp: int | None = Field(
        description='Время получения сервером события в формате UNIX-time. Может отличаться от ad_revenue_timestamp из-за задержек в сети или отсутствия подключения у пользователя на момент события.'
    )
    ad_revenue: float | None = Field(
        description='Сумма денег Ad Revenue.'
    )
    ad_revenue_currency: str | None = Field(
        description='Валюта Ad Revenue.'
    )
    ad_revenue_type: str | None = Field(
        description='Тип Ad Revenue. Возможные значения:\n\nnative\nbanner\nrewarded\ninterstitial\nmrec\nother'
    )
    ad_revenue_data_source: str | None = Field(
        description='Признак автособранного Ad Revenue. Возможные значения:\n\nautocollected\nmanual'
    )
    ad_revenue_network: str | None = Field(
        description='Рекламная сеть.'
    )
    ad_revenue_placement_id: str | None = Field(
        description='ID расположения рекламы.'
    )
    ad_revenue_placement_name: str | None = Field(
        description='Название расположения рекламы.'
    )
    ad_revenue_unit_id: str | None = Field(
        description='ID рекламной единицы.'
    )
    ad_revenue_unit_name: str | None = Field(
        description='Название рекламной единицы.'
    )
    ad_revenue_precision: str | None = Field(
        description='Точность суммы Ad Revenue, как передано в SDK. Например, "publisher_defined" или "estimated".'
    )
    ad_revenue_payload: str | None = Field(
        description='Дополнительные данные, сериализованные в JSON.'
    )
    session_id: int | None = Field(
        description='Идентификатор сессии. Набор из значений installation_id, session_id и платформенного идентификатора устройства (google_aid / ios_ifa) позволяет однозначно идентифицировать сессию пользователя.'
    )
    installation_id: str | None = Field(
        description='Идентификатор установки.'
    )
    android_id: str | None = Field(
        description='Идентификатор Android.'
    )
    appmetrica_device_id: str | None = Field(
        description='Уникальный идентификатор устройства, который устанавливает AppMetrica. В Android от AppSetId, в IOS от IFV.'
    )
    appmetrica_sdk_version: int | None = Field(
        description='Версия AppMetrica SDK.'
    )
    city: str | None = Field(
        description='Название города на английском языке, где был произведен клик.'
    )
    connection_type: str | None = Field(
        description='Тип подключения устройства. Возможные значения: wifi | cell | unknown.'
    )
    country_iso_code: str | None = Field(
        description='ISO-код страны.'
    )
    device_ipv6: str | None = Field(
        description='IP-адрес в момент совершения события в формате IPv6. Например, 2a02:6b8::40c:6676:baff:fea6:53d8, ::ffff:5.255.232.147.'
    )
    device_locale: str | None = Field(
        description='Язык интерфейса устройства.'
    )
    device_manufacturer: str | None = Field(
        description='Производитель устройства, определяется сервисом AppMetrica (например, Apple или Samsung).'
    )
    device_model: str | None = Field(
        description='Модель устройства, определяется сервисом AppMetrica (например, Galaxy S6).'
    )
    google_aid: str | None = Field(
        description='Google AID устройства в формате, в котором получен от устройства.'
    )
    ios_ifa: str | None = Field(
        description='IFA устройства в формате, в котором получен от устройства.'
    )
    ios_ifv: str | None = Field(
        description='IFV для приложения в формате, в котором получен от устройства.'
    )
    mcc: int | None = Field(
        description='Мобильный код страны.'
    )
    mnc: int | None = Field(
        description='Код мобильной сети.'
    )
    operator_name: str | None = Field(
        description='Имя оператора сотовой связи.'
    )
    original_device_model: str | None = Field(
        description='Заводская модель устройства (например, для Galaxy S8 возможны следующие значения: SM-G9550, SM-G9558 и т. д.).'
    )
    os_version: str | None = Field(
        description='Версия операционной системы на устройстве пользователя.'
    )
    profile_id: str | None = Field(
        description='Идентификатор пользовательского профиля.'
    )
    windows_aid: str | None = Field(
        description='Windows AID устройства в формате, в котором получен от устройства.'
    )
    app_build_number: int | None = Field(
        description='Номер сборки приложения.'
    )
    app_package_name: str | None = Field(
        description='Имя пакета для Android или Bundle ID для iOS (например, ru.yandex.metro).'
    )
    app_version_name: str | None = Field(
        description='Версия приложения в виде, как указана разработчиком.'
    )
