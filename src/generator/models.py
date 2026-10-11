from __future__ import annotations

import enum
from dataclasses import dataclass
from datetime import datetime

class DeviceType(enum.StrEnum):
    MOBILE = "mobile"
    DESKTOP = "desktop"
    TABLET = "tablet"
    WATCHES = "watches"

class SubscriptionType(enum.Enum):
    FREE = "free"
    TRIAL = "trial"
    PREMIUM = "premium"
    FAMILY = "family"
    STUDENT = "student"

@dataclass(frozen=True, slots=True)
class Device:
    device_id: int
    device_type: DeviceType

@dataclass(frozen=True, slots=True)
class Artist:
    artist_id: int
    name: str
    country_id: int
    label: str

@dataclass(frozen=True, slots=True)
class Track:
    track_id: int
    title: str
    artist_id: int

@dataclass(frozen=True, slots=True)
class Genre:
    genre_id: int
    name: str

@dataclass(frozen=True, slots=True)
class Country:
    country_id: int
    country_name: str


@dataclass(frozen=True, slots=True)
class User:
    user_id: int
    ## age_group я хз какого типа

    ## username: str
    ## first_name: str
    ## last_name: str этого у нас нет но как будто надо

    country: Country
    subscription_type: SubscriptionType
    ## device_type: DeviceType - может добавить тоже или только в факт ридинге я пока хз


@dataclass(frozen=True, slots=True)
class DateDimension:
    date_id: int
    date: datetime
    year: int
    month: int
    day: int
    day_of_week: int
    week: int
    is_weekend: bool


@dataclass(frozen=True, slots=True)
class TimeDimension:
    time_id: int
    hour: int
    minute: int
    second: int
    is_daytime: bool


## fact_reading table
@dataclass(frozen=True, slots=True)
class MusicReading:
    reading_id: int
    track_id: int
    user_id: int
    device_id: int
    date_id: int
    genre_id: int
    listen_seconds: int
    skip_flag: bool


@dataclass(frozen=True, slots=True)
class HourlyTracks:
    hour_key: int
    track_id: int
    date_id: int
    time_id: int
    listens_count: int
    unique_users: int
    avg_listen_seconds: int
    skips_count: int

@dataclass(frozen=True, slots=True)
class DailyTracks:
    day_key: int
    track_id: int
    date_id: int
    listens_count: int
    unique_users: int
    avg_listen_seconds: int
    skips_count: int