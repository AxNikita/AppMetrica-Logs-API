from datetime import date

from pydantic import BaseModel, Field


class ProfilesSchema(BaseModel):
    """
    Профили.
    https://appmetrica.yandex.ru/docs/ru/mobile-api/logs/ref/profiles
    """
    profile_id: str | None = Field(
        description='Идентификатор пользовательского профиля.'
    )
    appmetrica_gender: str | None = Field(
        description='Пол.'
    )
    appmetrica_birth_date: str | None = Field(
        description='Возраст.'
    )
    appmetrica_notifications_enabled: bool | None = Field(
        description='Push разрешены.'
    )
    appmetrica_name: str | None = Field(
        description='Имя.'
    )
    appmetrica_crashes: int | None = Field(
        description='Количество крэшей.'
    )
    appmetrica_errors: int | None = Field(
        description='Количество ошибок.'
    )
    appmetrica_first_session_date: date | None = Field(
        description='Дата начала первой сессии.'
    )
    appmetrica_last_start_date: date | None = Field(
        description='Дата последнего запуска приложения.'
    )
    appmetrica_push_opens: int | None = Field(
        description='Количество открытых push-уведомлений.'
    )
    appmetrica_push_send_count: int | None = Field(
        description='Количество отправленных push-уведомлений.'
    )
    appmetrica_sdk_version: int | None = Field(
        description='Версия AppMetrica SDK.'
    )
    appmetrica_sessions: int | None = Field(
        description='Количество сессий.'
    )
    android_id: str | None = Field(
        description='Идентификатор Android.'
    )
    appmetrica_device_id: str | None = Field(
        description='Уникальный идентификатор устройства, который устанавливает AppMetrica. В Android от AppSetId, в IOS от IFV.'
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
    device_manufacturer: str | None = Field(
        description='Производитель устройства, определяется сервисом AppMetrica (например, Apple или Samsung).'
    )
    device_model: str | None = Field(
        description='Модель устройства, определяется сервисом AppMetrica (например, Galaxy S6).'
    )
    device_type: str | None = Field(
        description='Тип устройства, определяется сервисом AppMetrica. Возможные значения: phone | tablet | unknown.'
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
    os_name: str | None = Field(
        description='Операционная система на устройстве пользователя: ios | android | windows.'
    )
    os_version: str | None = Field(
        description='Версия операционной системы на устройстве пользователя.'
    )
    windows_aid: str | None = Field(
        description='Windows AID устройства в формате, в котором получен от устройства.'
    )
    app_build_number: int | None = Field(
        description='Номер сборки приложения.'
    )
    app_framework: int | None = Field(
        description='Тип фреймворка. Возвращает следующие возможные значения: "0" — Native. "1" — Unity. "2" — Xamarin. "3" — React. "4" — Cordova.'
    )
    app_package_name: str | None = Field(
        description='Имя пакета для Android или Bundle ID для iOS (например, ru.yandex.metro).'
    )
    app_version_name: str | None = Field(
        description='Версия приложения в виде, как указана разработчиком.'
    )
