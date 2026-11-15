from __future__ import annotations

import enum
from dataclasses import dataclass
from datetime import date


class DeviceType(enum.StrEnum):
    MOBILE = "mobile"
    DESKTOP = "desktop"
    TABLET = "tablet"
    SMARTWATCH = "smartwatch"


class SubscriptionType(enum.StrEnum):
    FREE = "free"
    TRIAL = "trial"
    PREMIUM = "premium"
    FAMILY = "family"
    STUDENT = "student"


@dataclass(frozen=True, slots=True)
class DateDimension:
    date_id: int
    date: date
    year: int
    month: int
    day: int
    day_of_week: int
    iso_week: int
    is_weekend: bool

    def __post_init__(self) -> None:
        if not 1 <= self.day_of_week <= 7:
            raise ValueError("1")
        if not 1 <= self.iso_week <= 53:
            raise ValueError("2")


@dataclass(frozen=True, slots=True)
class TimeDimension:
    time_id: int
    hour: int
    minute: int
    is_day_time: bool

    def __post_init__(self) -> None:
        if not 0 <= self.time_id <= 1439:
            raise ValueError("1")
        if not 0 <= self.hour <= 23:
            raise ValueError("2")
        if not 0 <= self.minute <= 59:
            raise ValueError("3")
        if self.time_id != self.hour * 60 + self.minute:
            raise ValueError("4")


@dataclass(frozen=True, slots=True)
class User:
    user_id: int
    age:int
    username: str
    country_id: int
    subscription_type: SubscriptionType


@dataclass(frozen=True, slots=True)
class Track:
    track_id: int
    title: str
    artist_id: int
    genre_id: int


@dataclass(frozen=True, slots=True)
class Genre:
    genre_id: int
    name: str


@dataclass(frozen=True, slots=True)
class Artist:
    artist_id: int
    name: str
    country_id: int
    label: str


@dataclass(frozen=True, slots=True)
class Country:
    country_id: int
    name: str


@dataclass(frozen=True, slots=True)
class Device:
    device_id: int
    device_type: DeviceType


@dataclass(frozen=True, slots=True)
class MusicReading:
    reading_id: int
    track_id: int
    user_id: int
    device_id: int
    date_id: int
    time_id: int
    genre_id: int
    listen_seconds: int
    skip_flag: bool


@dataclass(frozen=True, slots=True)
class HourlyTracks:
    hour_key: int
    date_id: int
    time_id: int
    hour: int
    track_id: int
    artist_id: int
    genre_id: int
    listens_count: int
    unique_users: int
    avg_listen_seconds: float
    skips_count: int


@dataclass(frozen=True, slots=True)
class DailyTracks:
    day_key: int
    date_id: int
    track_id: int
    artist_id: int
    genre_id: int
    listens_count: int
    unique_users: int
    avg_listen_seconds: float
    skips_count: int


@dataclass(frozen=True, slots=True)
class DailyTrackMV:
    date_id: int
    track_id: int
    listens_count: int
    unique_users: int
    avg_listen_seconds: float
    skips_count: int


@dataclass(frozen=True, slots=True)
class DailyGenreMV:
    date_id: int
    genre_id: int
    listens_count: int
    unique_users: int
    skips_count: int


@dataclass(frozen=True, slots=True)
class HourlyArtistMV:
    date_id: int
    time_id: int
    hour: int
    artist_id: int
    listens_count: int
    unique_users: int
    skips_count: int
