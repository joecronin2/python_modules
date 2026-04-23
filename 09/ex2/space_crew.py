from enum import Enum
from datetime import datetime
from typing import List
from pydantic import BaseModel, Field, ValidationError, model_validator


class Rank(str, Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: List[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def validate_mission_safety(self) -> "SpaceMission":
        if not self.mission_id.startswith("M"):
            raise ValueError('Mission ID must start with "M"')

        lead_ranks = {Rank.CAPTAIN, Rank.COMMANDER}
        has_leader = any(member.rank in lead_ranks for member in self.crew)
        if not has_leader:
            raise ValueError(
                "Mission must have at least one Commander or Captain")

        if self.duration_days > 365:
            experienced_count = sum(
                1 for m in self.crew if m.years_experience >= 5)
            if experienced_count < (len(self.crew) / 2):
                raise ValueError(
                    "Long missions (> 365 days) need at least 50% "
                    "experienced crew (5+ years)"
                )

        if not all(member.is_active for member in self.crew):
            raise ValueError("All crew members must be active")
        return self


def main() -> None:
    print("Space Mission Crew Validation")
    print("=" * 41)
    try:
        valid_crew = [
            CrewMember(
                member_id="C01",
                name="Sarah Connor",
                rank=Rank.COMMANDER,
                age=45,
                specialization="Mission Command",
                years_experience=20,
            ),
            CrewMember(
                member_id="C02",
                name="John Smith",
                rank=Rank.LIEUTENANT,
                age=30,
                specialization="Navigation",
                years_experience=6,
            ),
            CrewMember(
                member_id="C03",
                name="Alice Johnson",
                rank=Rank.OFFICER,
                age=28,
                specialization="Engineering",
                years_experience=5,
            ),
        ]

        mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime(2024, 11, 1),
            duration_days=900,
            crew=valid_crew,
            budget_millions=2500.0,
        )

        print("Valid mission created:")
        print(f"Mission: {mission.mission_name}")
        print(f"ID: {mission.mission_id}")
        print(f"Destination: {mission.destination}")
        print(f"Duration: {mission.duration_days} days")
        print(f"Budget: ${mission.budget_millions}M")
        print(f"Crew size: {len(mission.crew)}")
        print("Crew members:")
        for m in mission.crew:
            print(f"- {m.name} ({m.rank.value}) - {m.specialization}")

    except ValidationError as e:
        print(f"Unexpected error: {e}")
    print("=" * 41)
    print("Expected validation error:")
    try:
        invalid_crew = [
            CrewMember(
                member_id="C04",
                name="Newbie Cadet",
                rank=Rank.CADET,
                age=19,
                specialization="Cleaning",
                years_experience=0,
            )
        ]
        SpaceMission(
            mission_id="M_FAIL_01",
            mission_name="Test Mission",
            destination="Moon",
            launch_date=datetime.now(),
            duration_days=10,
            crew=invalid_crew,
            budget_millions=10.0,
        )
    except ValidationError as e:
        print(e.errors()[0]["msg"].split(", ")[-1])


if __name__ == "__main__":
    main()
