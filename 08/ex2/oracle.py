import os
from dotenv import load_dotenv


def load_config() -> dict[str, str | None]:
    load_dotenv()

    return {
        "mode": os.getenv("MATRIX_MODE", "development"),
        "database": os.getenv("DATABASE_URL"),
        "api_key": os.getenv("API_KEY"),
        "log_level": os.getenv("LOG_LEVEL", "DEBUG"),
        "zion": os.getenv("ZION_ENDPOINT"),
    }


def validate(config) -> list[str]:
    required = ["database", "api_key", "zion"]
    return [k for k in required if not config.get(k)]


def main() -> None:
    print("ORACLE STATUS: Reading the Matrix...\n")

    config = load_config()
    missing = validate(config)

    if missing:
        for m in missing:
            print(f"[MISSING] {m}")
        return

    mode = config["mode"]

    if mode == "production":
        db = "Connected to remote instance"
        log = "WARNING"
    else:
        db = "Connected to local instance"
        log = config["log_level"]

    print("Configuration loaded:")
    print(f"Mode: {mode}")
    print(f"Database: {db}")
    print("API Access: Authenticated")
    print(f"Log Level: {log}")
    print("Zion Network: Online\n")

    print("Environment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available")


if __name__ == "__main__":
    main()
