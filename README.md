# ACI Performance Evaluation Dashboard

### Evaluating Ambient Clinical Intelligence Implementation Through Healthcare Performance Analytics

An interactive healthcare analytics project designed to evaluate the implementation of an **Ambient Clinical Intelligence (ACI)** system in outpatient clinical settings.

The project uses Python-generated synthetic healthcare data and Microsoft Power BI to examine how AI-powered clinical documentation systems influence operational efficiency, system reliability, clinician performance, and technology adoption.

The dashboard is developed as part of the **DH5750: Leading Interprofessional Teams in Health Initiatives** course at Iowa State University.

---

## 1. Project Overview

Healthcare professionals spend considerable time completing electronic health record (EHR) documentation, contributing to administrative burden, reduced clinical efficiency, and physician burnout.

Ambient Clinical Intelligence (ACI) systems use technologies such as automatic speech recognition and natural language processing to generate clinical documentation from patient-provider conversations.

Although these systems have the potential to reduce documentation burden, successful implementation requires more than technical functionality. Healthcare organizations must also evaluate clinician adoption, documentation quality, workflow integration, and employee satisfaction.

This project demonstrates how healthcare leaders can use an interactive performance dashboard to evaluate both technical and human factors during an ACI implementation.

### Project Objectives

1. Evaluate ACI system reliability and EHR integration performance.
2. Measure changes in clinical documentation efficiency.
3. Monitor clinician adoption, training, and satisfaction.
4. Examine relationships between system-level and employee-level performance.
5. Demonstrate how healthcare leaders can use performance analytics to identify implementation challenges and support decision-making.

---

## 2. Healthcare Use Case

### Scenario

A healthcare organization is conducting a **90-day pilot implementation** of an ACI system across three outpatient departments:

- Primary Care
- Cardiology
- Internal Medicine

The pilot includes 30 clinicians and approximately 6,000 patient encounters.

The system generates AI-assisted clinical notes that clinicians review and approve before transferring them into the EHR.

The project evaluates whether ACI improves documentation efficiency while maintaining clinical accuracy, system reliability, and clinician satisfaction.

### Simulated EHR Integration Outage

During week 6, the ACI system experiences a three-day EHR integration disruption.

The simulated incident results in:

- Reduced system availability.
- Increased EHR integration failures.
- Longer documentation completion times.
- Reduced clinician adoption.
- Increased administrative workload.
- Lower clinician satisfaction.

This scenario demonstrates how technical failures can influence employee performance and why healthcare leaders should evaluate system and clinician metrics together.

---

## 3. Synthetic Dataset

All datasets are generated using Python.

**Important:** The data is entirely synthetic and does not contain real patient records, protected health information (PHI), or actual clinician performance evaluations.

The simulated relationships are based on assumptions developed for educational purposes and should not be interpreted as validated clinical findings.

### Dataset Overview

| Dataset | Records | Description |
|---|---:|---|
| clinicians.csv | 30 | Clinician characteristics, departments, and training information |
| encounters.csv | 6,000 | Encounter-level documentation, ACI adoption, and EHR integration metrics |
| system_performance.csv | 90 | Daily system reliability, downtime, and technical incidents |
| clinician_feedback.csv | 390 | Weekly clinician satisfaction, workload, and usability measurements |

### Data Dictionary

#### clinicians.csv

| Variable | Description |
|---|---|
| clinician_id | Unique synthetic clinician identifier |
| department | Clinical department |
| role | Clinical professional role |
| years_experience | Years of clinical experience |
| training_completed | ACI training completion indicator |
| training_date | Date training was completed |
| training_score | Simulated training assessment score |
| adoption_preference | Synthetic parameter representing individual adoption tendencies |

#### encounters.csv

| Variable | Description |
|---|---|
| encounter_id | Unique synthetic encounter identifier |
| date | Encounter date |
| pilot_day | Day of the implementation pilot |
| pilot_week | Week of the implementation pilot |
| clinician_id | Identifier linking the encounter to a clinician |
| department | Clinical department |
| aci_used | Whether ACI was used during the encounter |
| baseline_documentation_time_min | Estimated documentation time without ACI |
| documentation_time_min | Simulated actual documentation time |
| note_accuracy_score | Simulated AI-generated note accuracy |
| note_review_time_min | Time spent reviewing AI-generated documentation |
| ehr_integration_success | Whether the ACI note was successfully transferred |
| documentation_completed_on_time | Whether documentation met the required completion timeframe |
| after_hours_documentation_min | Estimated after-hours documentation time |
| outage_flag | Whether the encounter occurred during the simulated outage |

#### system_performance.csv

| Variable | Description |
|---|---|
| date | Monitoring date |
| pilot_day | Pilot day |
| pilot_week | Pilot week |
| system_uptime_pct | Daily system availability percentage |
| downtime_minutes | Estimated system downtime |
| technical_incidents | Number of simulated technical incidents |
| integration_success_probability | Probability parameter used to simulate integration success |
| outage_flag | Indicator for the simulated outage period |

#### clinician_feedback.csv

| Variable | Description |
|---|---|
| clinician_id | Unique clinician identifier |
| department | Clinical department |
| pilot_week | Pilot week |
| aci_adoption_rate | Weekly clinician-level ACI adoption rate |
| average_documentation_time_min | Weekly average documentation time |
| satisfaction_score | Simulated clinician satisfaction (1–5) |
| perceived_workload_score | Simulated perceived workload (1–5) |
| usability_score | Simulated system usability rating (1–5) |
| outage_exposure | Proportion of the clinician's encounters affected by the outage |

---

## 4. Key Performance Indicators

The dashboard evaluates two categories of performance.

### System-Level KPIs

| KPI | Measurement |
|---|---|
| Documentation Efficiency | Average documentation time per encounter |
| EHR Integration Success | Percentage of attempted ACI note transfers completed successfully |
| Documentation Accuracy | Percentage of audited AI-generated notes meeting accuracy requirements |
| System Availability | Percentage of monitored time the system is operational |
| After-Hours Documentation | Average after-hours documentation time per encounter |

### Employee-Level KPIs

| KPI | Measurement |
|---|---|
| ACI Adoption Rate | Percentage of eligible encounters using ACI |
| Training Completion | Percentage of clinicians completing ACI training |
| Documentation Completion | Percentage of encounters documented within the required timeframe |
| Clinician Satisfaction | Average clinician satisfaction score |
| Note Review Time | Average time spent reviewing AI-generated notes |

### KPI Relationships

The project examines relationships between technical and employee performance.

Examples include:

- EHR integration failures and delayed documentation completion.
- System downtime and reduced clinician adoption.
- Documentation accuracy and clinician note review time.
- ACI adoption and documentation efficiency.
- Technical incidents and clinician satisfaction.

These relationships are simulated to demonstrate performance evaluation methods, not to establish clinical causality.

---

## 5. Dashboard Design

The Power BI dashboard is organized into three pages.

### Page 1: Executive Overview

**Audience:** Hospital administrators and department leaders.

Provides a high-level overview of ACI implementation performance.

Visualizations include:

- Documentation efficiency KPI cards.
- ACI adoption rate.
- EHR integration success rate.
- Clinician satisfaction score.
- Weekly documentation time trends.
- Department-level performance comparisons.

### Page 2: System Performance

**Audience:** IT teams, clinical informatics specialists, and technology vendors.

Focuses on technical reliability and operational performance.

Visualizations include:

- Daily system availability.
- EHR integration success and failure rates.
- Documentation accuracy trends.
- Technical incidents over time.
- System downtime.
- Week 6 outage analysis.

### Page 3: Employee Performance

**Audience:** Clinical managers and department leaders.

Evaluates clinician engagement and documentation workflows.

Visualizations include:

- ACI adoption by department.
- Training completion rates.
- Documentation completion rates.
- Clinician satisfaction trends.
- Average note review time.
- Perceived workload.

The dashboard supports interactive filtering by department, clinician role, and pilot period.

---

## 6. Technology Stack

| Technology | Purpose |
|---|---|
| Python | Synthetic data generation |
| NumPy | Random sampling and simulation |
| pandas | Data manipulation and CSV export |
| Microsoft Power BI | Data modeling and interactive dashboard development |
| DAX | KPI calculations and performance measures |
| GitHub | Version control and project documentation |

---

## 7. Repository Structure

```text
aci-performance-dashboard/
│
├── data/
│   ├── clinicians.csv
│   ├── encounters.csv
│   ├── system_performance.csv
│   └── clinician_feedback.csv
│
├── src/
│   └── generate_data.py
│
├── dashboards/
│   └── aci_performance_dashboard.pbix
│
├── requirements.txt
├── README.md
└── .gitignore
```

The Power BI dashboard file will be added after development.

---

## 8. Installation and Usage

### Prerequisites

- Python 3.10 or later
- pip
- Microsoft Power BI Desktop or an appropriate Power BI environment

### Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/aci-performance-dashboard.git

cd aci-performance-dashboard
```

Replace `YOUR_USERNAME` with your GitHub username.

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Generate Synthetic Data

```bash
python src/generate_data.py
```

The script generates four CSV files in the `data/` directory.

A fixed random seed is used to support reproducibility.

### Import Data into Power BI

1. Open Power BI Desktop.
2. Select **Home → Get Data → Text/CSV**.
3. Import the four generated CSV files.
4. Verify column data types.
5. Create the required table relationships.
6. Define KPI measures using DAX.
7. Build the interactive dashboard visualizations.

### Suggested Data Relationships

| Table | Related Table | Key |
|---|---|---|
| clinicians | encounters | clinician_id |
| clinicians | clinician_feedback | clinician_id |
| system_performance | encounters | date |

A dedicated calendar or pilot-week dimension may be added to support consistent filtering across daily and weekly datasets.

---

## 9. Limitations

This project uses synthetic data and has several important limitations.

**Synthetic assumptions:** The simulation parameters are illustrative and are not estimated from real-world clinical data.

**Documentation baseline:** Baseline documentation time is an estimated counterfactual rather than an observed preimplementation measurement.

**Clinician behavior:** Adoption probabilities and satisfaction scores are simulated using simplified assumptions.

**Clinical accuracy:** The note accuracy score is simulated and does not represent a validated clinical documentation quality assessment.

**Generalizability:** Results cannot be generalized to actual healthcare organizations or ACI implementations.

The dashboard is intended to demonstrate healthcare performance analytics and leadership decision-making rather than evaluate the effectiveness of a commercial ACI product.

---

## 10. Future Improvements

Potential future developments include:

- Incorporating real-world, de-identified implementation data where authorized.
- Adding preimplementation and postimplementation comparisons.
- Developing validated documentation quality measures.
- Including patient satisfaction and safety indicators.
- Expanding the simulation to additional departments.
- Incorporating more detailed training and workflow metrics.
- Developing predictive models for identifying implementation risks.

---

## 11. References

Microsoft. (n.d.). *Power BI documentation*. Microsoft Learn. https://learn.microsoft.com/en-us/power-bi/

NumPy Developers. (n.d.). *NumPy documentation*. https://numpy.org/doc/stable/

pandas development team. (n.d.). *pandas documentation*. https://pandas.pydata.org/docs/

Tierney, A. A., Gayre, G., Hoberman, B., Mattern, B., Ballesca, M., Kipnis, P., Liu, V., & Lee, K. (2024). Ambient artificial intelligence scribes to alleviate the burden of clinical documentation. *NEJM Catalyst Innovations in Care Delivery, 5*(3). https://doi.org/10.1056/CAT.23.0404

---

## 12. Author

**Sarra Hanish**

Master of Digital Health  
Iowa State University

Biomedical Engineering | Digital Health | Healthcare AI | Product Management

---

## License

This project is intended for educational and research demonstration purposes.

All generated datasets are synthetic and do not contain real patient or clinician information.
