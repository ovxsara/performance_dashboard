from os import system
from pathlib import Path
import pandas as pd
import numpy as np

RANDOM_SEED = 42
rng = np.random.default_rng(RANDOM_SEED)

PROJECT_ROOT = Path(__file__).parent.parent
OUTPUT_DIR = PROJECT_ROOT / "data"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

PILOT_START = pd.Timestamp("2026-10-01")
PILOT_DAYS = 90
dates = pd.date_range(start=PILOT_START, periods=PILOT_DAYS, freq="D")

n_clinicians = 30
n_encounters = 6000

department_choices = ["Cardiology", "Neurology", "Oncology", "Pediatrics", "General Medicine"]

outage_start_day = 30  # outage starts 30 days into the pilot
outage_end_day = outage_start_day + 2  # outage lasts for 2 days

# helper functions
def clamp(value, minimum, maximum):
    """Keep a numerical value within specified limits."""
    return max(minimum, min(maximum, value))


def is_outage_day(day_number):
    """Identify days affected by the simulated EHR outage."""
    return outage_start_day <= day_number <= outage_end_day


def get_week_number(day_number):
    """Convert pilot day to week number."""
    return ((day_number - 1) // 7) + 1


def get_adoption_probability(day_number, clinician):
    """
    Model gradual ACI adoption.

    Adoption increases as clinicians become more comfortable
    with the system, but decreases during technical outages.
    """

    progress = day_number / PILOT_DAYS

    probability = (
        0.55
        + 0.35 * progress
        + clinician["adoption_preference"]
    )

    if is_outage_day(day_number):
        probability -= 0.35

    return clamp(probability, 0.05, 0.98)

# generate clinician data
def generate_clinicians():
    records = []

    roles = ["Attending Physician", "Nurse Practitioner", "Resident Physician", "Physician Assistant"]

    for clinician_id in range(1, n_clinicians + 1):

        department = department_choices[(clinician_id - 1) // 10]

        role = rng.choice(roles, p=[0.5, 0.25, 0.15, 0.10])

        years_experience = int(rng.integers(1, 26))

        training_day = int(rng.integers(1, 15))

        training_date = (PILOT_START + pd.Timedelta(days=training_day - 1))

        training_score = round(float(rng.uniform(75,100)), 1) 
        
        adoption_preference = float(rng.normal(0.0, 0.08))  # random adoption preference between 0 and 1, rounded to 2 decimal places

        records.append({
            "clinician_id": clinician_id,
            "department": department,
            "role": role,
            "years_experience": years_experience,
            "training_day": training_day,
            "training_date": training_date,
            "training_score": training_score,
            "adoption_preference": adoption_preference
        })

    clinicians = pd.DataFrame(records)
    return clinicians


# generate system performance data

def generate_system_performance():
    records = []
    for day_number, date in enumerate(dates, start=1):

        outage = is_outage_day(day_number)

        if outage:
            uptime = float(rng.uniform(87, 94))
            incidents = int(rng.integers(3, 8))  # low uptime during outage
            integration_rate = float(rng.uniform(0.78, 0.88))  # low integration rate during outage

        else:
            uptime = float(rng.uniform(99.2, 99.99))
            incidents = int(rng.poisson(0.3))  # low number of incidents when system is performing well
            integration_rate = float(rng.uniform(0.985, 0.999))  # high integration rate when system is performing well

        downtime_minutes = round ( 1440 * (1 - uptime / 100), 2)


        records.append({
            "date": date,
            "pilot_day": day_number,
            "pilot_week": get_week_number(day_number),
            "system_uptime_pct": round(uptime, 2),
            "downtime_minutes": downtime_minutes,
            "technical_incidents": incidents,
            "integration_success_probability": integration_rate,
            "outage_flag": int(outage)
        })

    system = pd.DataFrame(records)
    return system

# generate patient encounter data
def generate_encounters(clinicians, system):

    records = []

    # Encounters occur on weekdays.
    weekdays = pd.DatetimeIndex(
        [
            date for date in dates
            if date.weekday() < 5
        ]
    )

    encounter_dates = rng.choice(
        weekdays,
        size=n_encounters,
        replace=True
    )

    encounter_dates = sorted(
        pd.Timestamp(date)
        for date in encounter_dates
    )

    clinician_lookup = clinicians.set_index(
        "clinician_id"
    ).to_dict("index")

    system_lookup = system.set_index(
        "date"
    ).to_dict("index")

    for encounter_id, encounter_date in enumerate(
        encounter_dates,
        start=1
    ):

        day_number = (
            encounter_date - PILOT_START
        ).days + 1

        clinician_id = int(
            rng.integers(1, n_clinicians + 1)
        )

        clinician = clinician_lookup[clinician_id]
        daily_system = system_lookup[encounter_date]

        outage = bool(daily_system["outage_flag"])

        adoption_probability = get_adoption_probability(
            day_number,
            clinician
        )

        aci_used = int(
            rng.random() < adoption_probability
        )

        # Documentation time
        baseline_documentation_time = float(
            rng.normal(14, 3)
        )

        baseline_documentation_time = clamp(
            baseline_documentation_time,
            5,
            30
        )

        if aci_used:

            learning_progress = day_number / PILOT_DAYS

            efficiency_gain = (
                0.15 + 0.20 * learning_progress
            )

            documentation_time = (
                baseline_documentation_time
                * (1 - efficiency_gain)
            )

            documentation_time += rng.normal(0, 1.2)

        else:
            documentation_time = (
                baseline_documentation_time
                + rng.normal(0, 0.8)
            )

        if outage and aci_used:
            documentation_time += rng.uniform(4, 9)

        documentation_time = round(
            clamp(documentation_time, 2, 40),
            2
        )

        # AI note accuracy
        if aci_used:
            note_accuracy = float(
                rng.normal(0.96, 0.025)
            )

            note_accuracy = round(
                clamp(note_accuracy, 0.75, 1),
                3
            )
        else:
            note_accuracy = np.nan

        # EHR integration
        if aci_used:

            integration_success = int(
                rng.random()
                < daily_system[
                    "integration_success_probability"
                ]
            )

        else:
            integration_success = np.nan

        # Note review time
        if aci_used:

            note_review_time = float(
                rng.normal(3.5, 1)
            )

            if note_accuracy < 0.93:
                note_review_time += rng.uniform(1, 3)

            if outage:
                note_review_time += rng.uniform(1, 3)

            note_review_time = round(
                clamp(note_review_time, 0.5, 15),
                2
            )

        else:
            note_review_time = np.nan

        # Documentation completion
        completion_probability = 0.97

        if documentation_time > 18:
            completion_probability -= 0.08

        if outage and aci_used:
            completion_probability -= 0.18

        if aci_used and integration_success == 0:
            completion_probability -= 0.25

        documentation_completed_on_time = int(
            rng.random() < clamp(
                completion_probability,
                0.10,
                0.99
            )
        )

        # After-hours documentation
        after_hours_minutes = float(
            rng.normal(7, 2)
        )

        if aci_used:
            after_hours_minutes *= 0.65

        if outage and aci_used:
            after_hours_minutes += rng.uniform(4, 8)

        after_hours_minutes = round(
            clamp(after_hours_minutes, 0, 25),
            2
        )

        records.append({
            "encounter_id": encounter_id,
            "date": encounter_date,
            "pilot_day": day_number,
            "pilot_week": get_week_number(day_number),
            "clinician_id": clinician_id,
            "department": clinician["department"],
            "aci_used": aci_used,
            "baseline_documentation_time_min": round(
                baseline_documentation_time, 2
            ),
            "documentation_time_min": documentation_time,
            "note_accuracy_score": note_accuracy,
            "note_review_time_min": note_review_time,
            "ehr_integration_success": integration_success,
            "documentation_completed_on_time":
                documentation_completed_on_time,
            "after_hours_documentation_min":
                after_hours_minutes,
            "outage_flag": int(outage)
        })

    encounters = pd.DataFrame(records)

    return encounters

# generate clinician feedback data
def generate_clinician_feedback(clinicians, encounters):

    records = []

    total_weeks = get_week_number(PILOT_DAYS)

    for week in range(1, total_weeks + 1):

        week_encounters = encounters[
            encounters["pilot_week"] == week
        ]

        for _, clinician in clinicians.iterrows():

            clinician_id = clinician["clinician_id"]

            clinician_encounters = week_encounters[
                week_encounters["clinician_id"]
                == clinician_id
            ]

            if len(clinician_encounters) == 0:
                continue

            adoption_rate = (
                clinician_encounters["aci_used"].mean()
            )

            average_documentation_time = (
                clinician_encounters[
                    "documentation_time_min"
                ].mean()
            )

            outage_exposure = (
                clinician_encounters["outage_flag"].mean()
            )

            # Satisfaction score (1-5)
            satisfaction = (
                3.2
                + 1.2 * adoption_rate
                - 0.8 * outage_exposure
                + rng.normal(0, 0.35)
            )

            satisfaction = round(
                clamp(satisfaction, 1, 5),
                2
            )

            # Perceived workload (1-5)
            # Higher score = greater workload
            workload = (
                3.8
                - 0.8 * adoption_rate
                + 0.8 * outage_exposure
                + rng.normal(0, 0.35)
            )

            workload = round(
                clamp(workload, 1, 5),
                2
            )

            # Usability score (1-5)
            usability = (
                3.3
                + 0.9 * adoption_rate
                - 0.7 * outage_exposure
                + rng.normal(0, 0.3)
            )

            usability = round(
                clamp(usability, 1, 5),
                2
            )

            records.append({
                "clinician_id": clinician_id,
                "department": clinician["department"],
                "pilot_week": week,
                "aci_adoption_rate": round(
                    adoption_rate, 3
                ),
                "average_documentation_time_min": round(
                    average_documentation_time, 2
                ),
                "satisfaction_score": satisfaction,
                "perceived_workload_score": workload,
                "usability_score": usability,
                "outage_exposure": round(
                    outage_exposure, 3
                )
            })

    feedback = pd.DataFrame(records)

    return feedback

# DATA VALIDATION
def validate_data(
    clinicians,
    encounters,
    system,
    feedback
):

    print("VALIDATING GENERATED DATA...")

    assert len(clinicians) == n_clinicians
    assert len(encounters) == n_encounters
    assert len(system) == PILOT_DAYS, (
    f"System dataset has {len(system)} records, "
    f"but expected {PILOT_DAYS}."
)
    assert clinicians["clinician_id"].is_unique
    assert encounters["encounter_id"].is_unique
    assert system["date"].is_unique

    assert encounters["clinician_id"].isin(
        clinicians["clinician_id"]
    ).all()

    assert feedback["clinician_id"].isin(
        clinicians["clinician_id"]
    ).all()

    assert encounters["date"].isin(
        system["date"]
    ).all()

    assert encounters["documentation_time_min"].ge(
        0
    ).all()

    assert encounters["aci_used"].isin(
        [0, 1]
    ).all()

    assert encounters["documentation_completed_on_time"].isin(
        [0, 1]
    ).all()

    assert encounters.loc[
        encounters["aci_used"] == 0,
        "note_accuracy_score"
    ].isna().all()

    assert encounters.loc[
        encounters["aci_used"] == 0,
        "ehr_integration_success"
    ].isna().all()

    assert system["system_uptime_pct"].between(
        0, 100
    ).all()

    assert feedback["satisfaction_score"].between(
        1, 5
    ).all()

    print("ALL VALIDATION CHECKS PASSED.")

# EXPORT CSV file
def export_datasets(
    clinicians,
    encounters,
    system,
    feedback
):

    datasets = {
        "clinicians.csv": clinicians,
        "encounters.csv": encounters,
        "system_performance.csv": system,
        "clinician_feedback.csv": feedback
    }

    for filename, dataframe in datasets.items():

        output_path = OUTPUT_DIR / filename

        dataframe.to_csv(
            output_path,
            index=False,
            date_format="%Y-%m-%d"
        )

        print(
            f"Exported {filename}: "
            f"{len(dataframe):,} rows"
        )

# execution
def main():

    print("\nStarting ACI synthetic data generation...\n")

    clinicians = generate_clinicians()

    system = generate_system_performance()

    encounters = generate_encounters(
        clinicians,
        system
    )

    feedback = generate_clinician_feedback(
        clinicians,
        encounters
    )

    validate_data(
        clinicians,
        encounters,
        system,
        feedback
    )

    export_datasets(
        clinicians,
        encounters,
        system,
        feedback
    )

    print("\nData generation completed successfully!")


if __name__ == "__main__":
    main()