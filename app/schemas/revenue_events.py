from datetime import datetime

from pydantic import BaseModel, Field


class RevenueEventsSchema(BaseModel):
    """
    Доходы.
    https://appmetrica.yandex.ru/docs/ru/mobile-api/logs/ref/revenue_events
    """
    revenue_quantity: int | None = Field(
        description='Количество покупок (купленных товаров).'
    )
    revenue_price: str | None = Field(
        description='Стоимость. Может быть отрицательной (например, для возврата).'
    )
    revenue_currency: str | None = Field(
        description='Код валюты покупки в формате ISO 4217.'
    )
    revenue_product_id: str | None = Field(
        description='Идентификатор товара.'
    )
    revenue_order_id: str | None = Field(
        description='Идентификатор заказа.'
    )
    revenue_order_id_source: str | None = Field(
        description='Источник идентификатора заказа. Возможные значения: autogenerated | user_defined.'
    )
    is_revenue_verified: str | None = Field(
        description='Признак верификации покупки в магазине. Возможные значения:\n\ntrue — проверено;\nfalse — проверено и отбраковано;\nundefined — неизвестно.'
    )
    event_datetime: datetime | None = Field(
        description='Дата и время события в формате yyyy-mm-dd hh:mm:ss.'
    )
    event_name: str | None = Field(
        description='Имя события (как передано в SDK).'
    )
    event_receive_datetime: datetime | None = Field(
        description='Дата и время получения сервером события. Может отличаться от event_datetime из-за задержек в сети или отсутствия подключения у пользователя на момент события.'
    )
    event_receive_timestamp: int | None = Field(
        description='Время получения сервером события в формате UNIX-time. Может отличаться от event_timestamp из-за задержек в сети или отсутствия подключения у пользователя на момент события.'
    )
    event_timestamp: int | None = Field(
        description='Время события в формате UNIX-time.\n\nPost API позволяет загрузить только те события, у которых разница между датой совершения события (event_timestamp) и датой загрузки не больше 7 дней. Ожидается значение в секундах.'
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
        description='Язык интерфейса устр��йства.'
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