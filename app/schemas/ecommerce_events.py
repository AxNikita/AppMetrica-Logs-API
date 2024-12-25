from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class ECommerceSchema(BaseModel):
    """
    E-commerce
    https://appmetrica.yandex.ru/docs/ru/mobile-api/logs/ref/ecommerce_events
    """
    ecom_type: Optional[str] = Field(
        default=None,
        description='Тип события покупки. Возможные значения: show_screen, show_product_card, show_product_details, add_cart_item, remove_cart_item, begin_checkout, purchase.'
    )
    ecom_screen_name: Optional[str] = Field(
        default=None,
        description='Название экрана.'
    )
    ecom_screen_search_query: Optional[str] = Field(
        default=None,
        description='Поисковый запрос.'
    )
    ecom_screen_payload: Optional[str] = Field(
        default=None,
        description='Параметры экрана, как передали в SDK. Имеет формат объекта JSON “строковые ключ-значение”, например: {"configuration": "landscape", "fullscreen": "true"}.'
    )
    ecom_screen_category_path_1: Optional[str] = Field(
        default=None,
        description='Категория экрана. Уровень 1.'
    )
    ecom_screen_category_path_2: Optional[str] = Field(
        default=None,
        description='Категория экрана. Уровень 2.'
    )
    ecom_screen_category_path_3: Optional[str] = Field(
        default=None,
        description='Категория экрана. Уровень 3.'
    )
    ecom_screen_category_path_4: Optional[str] = Field(
        default=None,
        description='Категория экрана. Уровень 4.'
    )
    ecom_screen_category_path_5: Optional[str] = Field(
        default=None,
        description='Категория экрана. Уровень 5.'
    )
    ecom_screen_category_path_6: Optional[str] = Field(
        default=None,
        description='Категория экрана. Уровень 6.'
    )
    ecom_screen_category_path_7: Optional[str] = Field(
        default=None,
        description='Категория экрана. Уровень 7.'
    )
    ecom_screen_category_path_8: Optional[str] = Field(
        default=None,
        description='Категория экрана. Уровень 8.'
    )
    ecom_screen_category_path_9: Optional[str] = Field(
        default=None,
        description='Категория экрана. Уровень 9.'
    )
    ecom_screen_category_path_10: Optional[str] = Field(
        default=None,
        description='Категория экрана. Уровень 10.'
    )
    ecom_product_name: Optional[str] = Field(
        default=None,
        description='Название товара.'
    )
    ecom_product_sku: Optional[str] = Field(
        default=None,
        description='ID товара.'
    )
    ecom_product_promocodes: Optional[str] = Field(
        default=None,
        description='Промокоды товара. Имеет формат списка строк JSON, например: ["BT79IYX", "UT5412EP"].'
    )
    ecom_product_payload: Optional[str] = Field(
        default=None,
        description='Параметры товара, как передали в SDK. Имеет формат объекта JSON “строковые ключ-значение”, например: {"configuration": "landscape", "fullscreen": "true"}.'
    )
    ecom_product_category_path_1: Optional[str] = Field(
        default=None,
        description='Категория товара. Уровень 1.'
    )
    ecom_product_category_path_2: Optional[str] = Field(
        default=None,
        description='Категория товара. Уровень 2.'
    )
    ecom_product_category_path_3: Optional[str] = Field(
        default=None,
        description='Категория товара. Уровень 3.'
    )
    ecom_product_category_path_4: Optional[str] = Field(
        default=None,
        description='Категория товара. Уровень 4.'
    )
    ecom_product_category_path_5: Optional[str] = Field(
        default=None,
        description='Категория товара. Уровень 5.'
    )
    ecom_product_category_path_6: Optional[str] = Field(
        default=None,
        description='Категория товара. Уровень 6.'
    )
    ecom_product_category_path_7: Optional[str] = Field(
        default=None,
        description='Категория товара. Уровень 7.'
    )
    ecom_product_category_path_8: Optional[str] = Field(
        default=None,
        description='Категория товара. Уровень 8.'
    )
    ecom_product_category_path_9: Optional[str] = Field(
        default=None,
        description='Категория товара. Уровень 9.'
    )
    ecom_product_category_path_10: Optional[str] = Field(
        default=None,
        description='Категория товара. Уровень 10.'
    )
    ecom_product_actual_price_fiat_unit_type: Optional[str] = Field(
        default=None,
        description='Валюта актуальной стоимости товара.'
    )
    ecom_product_actual_price_fiat_value: Optional[float] = Field(
        default=None,
        description='Актуальная стоимость товара.'
    )
    ecom_product_actual_price_internal_components: Optional[str] = Field(
        default=None,
        description='Составляющие актуальной стоимости товара. Имеет формат списка JSON-объектов-пар “ключ-значение”, например: [{"wood": 25.01}, {"iron": 10}].'
    )
    ecom_product_original_price_fiat_unit_type: Optional[str] = Field(
        default=None,
        description='Валюта базовой стоимости товара.'
    )
    ecom_product_original_price_fiat_value: Optional[float] = Field(
        default=None,
        description='Базовая стоимость товара.'
    )
    ecom_product_original_price_internal_components: Optional[str] = Field(
        default=None,
        description='Составляющие базовой стоимости товара. Имеет формат списка JSON-объектов-пар “ключ-значение”, например: [{"wood": 25.01}, {"iron": 10}].'
    )
    ecom_cart_item_price_fiat_unit_type: Optional[str] = Field(
        default=None,
        description='Валюта стоимости товара в корзине.'
    )
    ecom_cart_item_price_fiat_value: Optional[float] = Field(
        default=None,
        description='Стоимость товара в корзине.'
    )
    ecom_cart_item_quantity: Optional[int] = Field(
        default=None,
        description='Количество товара в корзине.'
    )
    ecom_cart_item_internal_components: Optional[str] = Field(
        default=None,
        description='Составляющие стоимости товара в корзине. Имеет формат списка JSON-объектов-пар “ключ-значение”, например: [{"wood": 25.01}, {"iron": 10}].'
    )
    ecom_referrer_type: Optional[str] = Field(
        default=None,
        description='Тип источника перехода.'
    )
    ecom_referrer_id: Optional[str] = Field(
        default=None,
        description='ID источника перехода.'
    )
    ecom_order_id: Optional[str] = Field(
        default=None,
        description='ID покупки.'
    )
    ecom_order_payload: Optional[str] = Field(
        default=None,
        description='Параметры покупки, как передали в SDK. Имеет формат объекта JSON “строковые ключ-значение”, например: {"configuration": "landscape", "fullscreen": "true"}.'
    )
    event_datetime: Optional[datetime] = Field(
        default=None,
        description='Дата и время события в формате yyyy-mm-dd hh:mm:ss.'
    )
    event_name: Optional[str] = Field(
        default=None,
        description='Имя события (как передано в SDK).'
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
    session_id: Optional[str] = Field(
        default=None,
        description='Идентификатор сессии. Набор из значений installation_id, session_id и платформенного идентификатора устройства (google_aid / ios_ifa) позволяет однозначно идентифицировать сессию пользователя.'
    )
    installation_id: Optional[str] = Field(
        default=None,
        description='Идентификатор установки.'
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
    operator_name: Optional[str] = Field(
        default=None,
        description='Имя оператора сотовой связи.'
    )
    original_device_model: Optional[str] = Field(
        default=None,
        description='Заводская модель устройства (например, для Galaxy S8 возможны следующие значения: SM-G9550, SM-G9558 и т. д.).'
    )
    os_name: Optional[str] = Field(
        default=None,
        description='Операционная система на устройстве пользователя: ios | android | windows.'
    )
    os_version: Optional[str] = Field(
        default=None,
        description='Версия операционной системы на устройстве пользователя.'
    )
    profile_id: Optional[str] = Field(
        default=None,
        description='Идентификатор пользовательского профиля.'
    )
    windows_aid: Optional[str] = Field(
        default=None,
        description='Windows AID устройства в формате, в котором получен от устройства.'
    )
    app_build_number: Optional[str] = Field(
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
    application_id: Optional[int] = Field(
        default=None,
        description='Уникальный числовой идентификатор приложения в AppMetrica.'
    )
