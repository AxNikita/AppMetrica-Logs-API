class APIResources(object):
    """
    Ресурсы API AppMetrica.
    Подробнее: https://appmetrica.yandex.ru/docs/ru/mobile-api/logs/ref/index.html
    """
    # Возвращает данные о трекинговых кликах и показах за определенный интервал дат.
    CLICKS = 'clicks'

    # Возвращает данные об установках за определенный интервал дат.
    INSTALLATIONS = 'installations'

    # Возвращает данные о постбеках за определенный интервал дат.
    POSTBACKS = 'postbacks'

    # Возвращает данные о событиях за определенный интервал дат.
    EVENTS = 'events'

    # Возвращает информацию о профилях, обновленных за определенный интервал дат.
    PROFILES = 'profiles_v2'

    # Возвращает данные о покупках за определенный интервал дат.
    REVENUE_EVENTS = 'revenue_events'

    # Возвращает данные об открытиях приложения через deeplink за определенный интервал дат.
    DEEPLINKS = 'deeplinks'

    # Возвращает данные об аварийных остановках за определенный интервал дат.
    CRASHES = 'crashes'

    # Возвращает данные об ошибках за определенный интервал дат.
    ERRORS = 'errors'

    # Возвращает данные о push-токенах.
    PUSH_TOKENS = 'push_tokens'

    # Возвращает данные о сессиях за определенный интервал дат.
    SESSIONS_STARTS = 'sessions_starts'

    # Возвращает данные о доходах за показ рекламы (Ad Revenue) за определенный интервал дат.
    AD_REVENUE_EVENTS = 'ad_revenue_events'

    # Возвращает данные о покупках за определенный интервал дат.
    ECOMMERCE_EVENTS = 'ecommerce_events'


class ExportFormat(object):
    """
    Формат экспорта данных: csv или json.
    """
    CSV = 'csv'
    JSON = 'json'


class DateDimension(object):
    """
    Определяет, относительно какого события считается дата:
    default — относительно момента, когда событие произошло на устройстве пользователя;
    receive — относительно момента, когда информация о событии была получена сервером.
    """
    DEFAULT = 'default'
    RECEIVE = 'receive'
