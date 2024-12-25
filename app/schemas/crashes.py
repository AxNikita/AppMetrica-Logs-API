from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class CrashesSchema(BaseModel):
    """
    Крэши.
    https://appmetrica.yandex.ru/docs/ru/mobile-api/logs/ref/crashes
    """
    # Информация об аварийной остановке приложения
    crash: Optional[str] = Field(
        default=None,
        description='Отслеживание стека.'
    )
    crash_datetime: Optional[datetime] = Field(
        default=None,
        description='Дата и время аварийной остановки приложения в формате yyyy-mm-dd hh:mm:ss.'
    )
    crash_group_id: Optional[int] = Field(
        default=None,
        description='Идентификатор группы схожих аварийных остановок.'
    )
    crash_id: Optional[int] = Field(
        default=None,
        description='Идентификатор аварийной остановки.'
    )
    crash_name: Optional[str] = Field(
        default=None,
        description='Имя аварийной остановки.'
    )
    crash_receive_datetime: Optional[datetime] = Field(
        default=None,
        description='Дата и время получения сервером сообщения об аварийной остановке в формате yyyy-mm-dd hh:mm:ss. Может отличаться от crash_datetime из-за задержек в сети или отсутствия подключения у пользователя.'
    )
    crash_receive_timestamp: Optional[int] = Field(
        default=None,
        description='Время получения сервером сообщения об аварийной остановке в формате UNIX-time. Может отличаться от crash_timestamp из-за задержек в сети или отсутствия подключения у пользователя.'
    )
    crash_timestamp: Optional[int] = Field(
        default=None,
        description='Время аварийной остановки приложения в формате UNIX-time.'
    )
    # Информация об устройстве и ОС
    appmetrica_device_id: Optional[str] = Field(
        default=None,
        description='Уникальный идентификатор устройства, который устанавливает AppMetrica. В Android от AppSetId, в IOS от IFV.'
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
    # Информация о приложении
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