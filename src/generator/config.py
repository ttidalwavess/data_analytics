from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class ClickHouseSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="CLICKHOUSE_",
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=False,
    )
    host: str = Field(default="localhost")
    port: int = Field(default=8123, ge=1, le=65535)
    database: str = Field(default="music")
    user: str = Field(default="default")
    password: str = Field(default="")


class GeneratorSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="GENERATOR_",
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=False,
    )

    batch_size: int = Field(
        default=100,
        ge=1,
        description="Количество событий в одном батче",
    )

    interval_seconds: float = Field(
        default=1.0,
        ge=0.0,
        description="Пауза между батчами в секундах",
    )

    seed: int = Field(
        default=42,
        description="Seed для воспроизводимости генерации",
    )

    users_count: int = Field(
        default=1000,
        ge=1,
        description="Количество пользователей",
    )

    artists_count: int = Field(
        default=100,
        ge=1,
        description="Количество исполнителей",
    )

    tracks_count: int = Field(
        default=500,
        ge=1,
        description="Количество музыкальных треков",
    )

    genres_count: int = Field(
        default=10,
        ge=1,
        description="Количество музыкальных жанров",
    )

    devices_count: int = Field(
        default=4,
        ge=1,
        description="Количество типов устройств",
    )

    history_days: int = Field(
        default=30,
        ge=1,
        description="Количество дней истории для генерации",
    )

    skip_probability: float = Field(
        default=0.15,
        ge=0.0,
        le=1.0,
        description="Вероятность пропуска трека",
    )

    min_listen_seconds: int = Field(
        default=5,
        ge=0,
        description="Минимальная длительность прослушивания",
    )

    max_listen_seconds: int = Field(
        default=300,
        ge=1,
        description="Максимальная длительность прослушивания",
    )

    log_level: str = Field(
        default="INFO",
        description="Уровень логирования",
    )

    retry_max_attempts: int = Field(default=5, ge=1)

    retry_base_delay_seconds: float = Field(
        default=0.5,
        ge=0.0,
    )

    retry_max_delay_seconds: float = Field(
        default=30.0,
        ge=0.0,
    )

    retry_backoff_factor: float = Field(
        default=2.0,
        ge=1.0,
    )



@dataclass(frozen=True, slots=True)
class Settings:
    generator: GeneratorSettings
    clickhouse: ClickHouseSettings

@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings(
        generator=GeneratorSettings(),
        clickhouse=ClickHouseSettings(),
    )