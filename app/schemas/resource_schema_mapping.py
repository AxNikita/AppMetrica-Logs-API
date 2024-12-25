from app.constants import APIResources
from app.schemas.ad_revenue_events import AdRevenueEventsSchema
from app.schemas.clicks import ClicksSchema
from app.schemas.crashes import CrashesSchema
from app.schemas.deeplinks import DeeplinksSchema
from app.schemas.ecommerce_events import ECommerceSchema
from app.schemas.errors import ErrorsSchema
from app.schemas.events import EventsSchema
from app.schemas.installations import InstallationsSchema
from app.schemas.postbacks import PostbacksSchema
from app.schemas.profiles import ProfilesSchema
from app.schemas.push_tokens import PushTokensSchema
from app.schemas.revenue_events import RevenueEventsSchema
from app.schemas.sessions_starts import SessionsStartsSchema

RESOURCES_SCHEMA_MAPPING = {
    APIResources.EVENTS: EventsSchema,
    APIResources.INSTALLATIONS: InstallationsSchema,
    APIResources.PROFILES: ProfilesSchema,
    APIResources.REVENUE_EVENTS: RevenueEventsSchema,
    APIResources.DEEPLINKS: DeeplinksSchema,
    APIResources.CLICKS: ClicksSchema,
    APIResources.POSTBACKS: PostbacksSchema,
    APIResources.SESSIONS_STARTS: SessionsStartsSchema,
    APIResources.ERRORS: ErrorsSchema,
    APIResources.CRASHES: CrashesSchema,
    APIResources.PUSH_TOKENS: PushTokensSchema,
    APIResources.ECOMMERCE_EVENTS: ECommerceSchema,
    APIResources.AD_REVENUE_EVENTS: AdRevenueEventsSchema,
}
