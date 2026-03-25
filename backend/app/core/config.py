from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # API 기본 정보
    PROJECT_NAME: str = "AIOps Auto-Healing API"
    API_V1_STR: str = "/api/v1"

    # Database
    DATABASE_URL: str

    # AI (OpenAI Function Calling을 위한 키)
    OPENAI_API_KEY: str

    # Slack (Human-in-the-loop 관리자 승인용)
    SLACK_BOT_TOKEN: str
    SLACK_CHANNEL_ID: str

    # .env 파일에서 변수들을 자동으로 읽어오도록 설정
    model_config = SettingsConfigDict(env_file="../.env", env_file_encoding="utf-8")

# 앱 전체에서 싱글톤처럼 사용할 수 있게 인스턴스화
settings = Settings()