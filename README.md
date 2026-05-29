# CO₂ Emissions & Energy Transition: Who's Decoupling?

**Module 1 Capstone — Data Wrangling & Retrieval | Ironhack Data Analytics Bootcamp**  
**Team:** Diana Yule · Irene Fafian  
**Week:** 4 | **Status:** 📊 EDA Complete (H1, H2 & H3)

---

## Project Overview

Can countries grow their economies without growing their carbon footprint?

This project investigates whether countries are successfully **decoupling GDP growth from CO₂ emissions** — one of the defining questions of the post-Paris Agreement era. Using global emissions, energy production and consumption, GDP, and electricity access data spanning 2014–2024, we clean, build, and analyse a unified dataset to test this question across world regions.

The analysis uses the **post-Paris Agreement window (2014–2020)** as the evaluation frame — a period where climate policy momentum should, in theory, be visible in the data. The three hypotheses below move from diagnosis (is decoupling happening?) to mechanism (what explains it?) to consequence (who actually bears the cost?).

---

## Research Questions & Hypotheses

### Hypothesis 1 — CO₂ Intensity Decline
> **Has the CO₂ intensity of GDP declined across regions between 2014 and 2020, and does the answer change depending on how we measure emissions?**

Metric: `co2_int = co2 / GDP` (Scenario A — fossil + industrial only, optimistic view)  
Metric: `co2_luc_int = co2_luc / GDP` (Scenario B — full footprint including land-use change, honest view)

> If decoupling holds in Scenario A but weakens in Scenario B → high-income countries shifted emissions, not eliminated them.

### Hypothesis 2 — Renewable Penetration as the Mechanism
> **Which regions show evidence that renewable penetration explains CO₂ intensity decline — and where is the gap largest?**

Following Hypothesis 1, is renewable adoption the driver?  
Metrics: `co2_int`vs `renew_share` (prct_renew_prod &. prct_renw_cons).

### Hypothesis 3 — Electricity Access & CO₂
> **Do high CO₂ emissions always reflect development and improved living standards, or can they coexist with energy poverty?**

Metrics:
- `gdp_per_cap` vs `prct_access_elec` — does richer = better electricity access?
- `gdp_group` (quartiles) vs `prct_access_elec`, `co2`, `co2_per_cap` — comparing wealth groups on access, total emissions, and personal carbon footprint
- `co2` (total, above median) vs `prct_access_elec` (below median) — identifies countries with high total emissions but limited electricity access
- `co2_per_cap` as a control — distinguishes individual consumption from population/industrial scale
- `welfare_ratio = co2_per_cap / (prct_access_elec / 100)` — CO₂ cost per unit of electricity benefit received

> If countries with low/middle GDP per capita and below-median electricity access still show significant total CO₂, then emissions are not translating into universal energy access — the carbon burden is spread across a population that isn't receiving proportional welfare benefits.

---

## Data Sources

| Dataset | Description | Source | Method |
|---------|-------------|--------|--------|
| `energy_co2_data.csv` | Annual CO₂ emissions, energy mix, GDP, LUC emissions per country (1750–2024) | [Our World in Data — CO₂ & GHG Emissions](https://github.com/owid/co2-data) | Direct download (API/CSV) |
| `wregion_mapping.csv` | Country-to-world-region mapping | [Our World in Data — Region Definitions](https://ourworldindata.org/world-region-map-definitions) | Direct download |
| `world_bank_energy.csv` | Access to electricity (%), renewable energy production (%), renewable energy consumption (%), renewable production (kWh) — World Bank | [World Bank Open Data](https://data.worldbank.org/) | Web scraping / API |
| `UN_GDP.csv` | GDP at current prices (US$) per country 2014–2020 | [UN Stats — National Accounts Main Aggregates](https://unstats.un.org/unsd/snaama/Basic) | Direct download |
| `UN_Population.csv` | Population per country 2014–2024 | [UN Stats — National Accounts Main Aggregates](https://unstats.un.org/unsd/snaama/Basic) | Direct download |
| `world_bank_car.csv` | GDP, GDP per capita and population for Central African Republic (gap-fill) | [World Bank DataBank — World Development Indicators](https://databank.worldbank.org/reports.aspx?source=2&series=SP.POP.TOTL&country=CAF) | Direct download |

---

## Project Management

📋 **Kanban Board:** [Trello — Data Wrangling Project Week 4](https://trello.com/invite/b/6a140a85c4baf8ce1b4b4c33/ATTI34b2ec4474650fcb84d88b3223c983ce1D21A984/my-trello-board)

**Presentation slides:** (https://docs.google.com/presentation/d/1aJ232in5u8-AgMorOHoGvTn6O2CPokLlSJ3kl4j82EU/edit?usp=drive_link)

---

## Repository Structure

```
first_project/
├── README.md
├── cfg.yaml                          # Paths and project-wide parameters
├── pyproject.toml                    # Production dependencies
├── uv.lock                           # Pinned dependency lock file
├── .gitignore
├── data/
│   ├── raw/                          # Original unmodified source files
│   └── clean/                        # Processed outputs (merged_final.csv etc.)
├── notebooks/
│   ├── raw_eCO2data_cleaning_Diana.ipynb      # OWID CO₂ data cleaning + region mapping
│   ├── wrangle_clean_irene.ipynb              # GDP, population, renewables cleaning
│   ├── final_clean_merge.ipynb                # final merge + country name harmonisation
│   ├── eda_hypothesis_testing_Diana.ipynb     # EDA, CO₂ intensity, H1 & H2
│   ├── eda_hypothesis_testing_irene.ipynb     # EDA, electricity access, H3
│   └── functions.py                           # Shared reusable helper functions
├── figures/                          # Generated plots and visualisations
├── slides/
│   └── project_presentation slides    # presentation
└── sql_scripts/
    ├── ERD_Miro.png                  # Entity-Relationship Diagram (Miro)
    └── MiniProject_GDP_CO2_schema.sql # SQL schema (drawDB export)
```

---

## Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/YourUsername/repository_name.git
```

### 2. Install UV

**macOS / Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows (Anaconda Powershell Prompt):**
```bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 3. Create and activate the virtual environment

```bash
uv venv
```

**macOS / Linux:**
```bash
source .venv/bin/activate
```

**Windows:**
```bash
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
uv pip install -r pyproject.toml
```

### 5. Register the Jupyter kernel

```bash
python -m ipykernel install --user --name=venv
```

### 6. Launch Jupyter

```bash
jupyter notebook
```

---

## Data Pipeline — How to Run

Run notebooks **in this order** to reproduce the full pipeline:

| Step | Notebook | Owner | Output |
|------|----------|-------|--------|
| 1 | `raw_eCO2data_cleaning_Diana.ipynb` | Diana | `data/clean/co2_clean.csv` |
| 2 | `wrangle_clean_irene.ipynb` | Irene | `data/clean/gdp_pop_clean.csv` |
| 3 | `final_clean_merge.ipynb` | Team | `data/clean/merged_final.csv` |
| 4 | `eda_hypothesis_testing_Diana.ipynb` | Diana | Figures + H1 & H2 findings |
| 5 | `eda_hypothesis_testing_irene.ipynb` | Irene | Figures + H3 findings |

All paths are managed via `cfg.yaml` — no hardcoded paths in any notebook.

---

## Data Cleaning Methodology

### Diana — `raw_eCO2data_cleaning_Diana.ipynb`

Source: Our World in Data CO₂ dataset (79 columns, 1750–2024).

| # | Technique | Detail |
|---|-----------|--------|
| 1 | Column selection | Reduced 79 raw columns to 11 relevant features |
| 2 | Time window filtering | Kept only 2014–2024 |
| 3 | Column renaming | Shortened verbose names (e.g. `co2_including_luc` → `co2_luc`) |
| 4 | Regional aggregate removal | Dropped 36 non-country rows (continents, income groups) using ISO code filter |
| 5 | Microstate exclusion | Removed Monaco, San Marino, Vatican (emissions absorbed into France/Italy) |
| 6 | Antarctica exclusion | No government, no policy-relevant data |
| 7 | Region mapping | Joined OWID region file to enable continental aggregation |
| 8 | Kosovo preserved | No ISO code but valid sovereign country — retained explicitly |

### Irene — `wrangle_clean_irene.ipynb`

Sources: UN GDP data, UN Population data, World Bank renewables data.

| # | Technique | Detail |
|---|-----------|--------|
| 1 | Null check | Confirmed zero nulls in GDP source before any transformation |
| 2 | Duplicate check | Confirmed zero duplicates across all source files |
| 3 | Column renaming | Standardised to `country`, `year`, `GDP`, `prct_access_elec`, `prct_renew_prod`, `prct_renew_cons` |
| 4 | Unit column drop | Removed `Unit` metadata column (currency label, not needed for analysis) |
| 5 | Wide-to-long reshape | World Bank data pivoted from year-as-columns to long format using `pd.melt()` |
| 6 | Long-to-wide pivot | Melted rows pivoted back on `series_name` to produce one column per indicator per country-year |
| 7 | Type conversion | `..` strings (World Bank missing marker) converted to NaN and dropped; `year` enforced as integer |
| 8 | GDP per capita | Computed `gdp_per_cap = GDP / population` |
| 9 | Config-driven I/O | All file paths managed via `cfg.yaml` — no hardcoded paths in the notebook |

### Team — `final_clean_merge.ipynb`

| # | Technique | Detail |
|---|-----------|--------|
| 1 | Multi-source merge | Joined renewables + GDP/population + CO₂/energy datasets on `country` + `year` |
| 2 | Country name harmonisation | Resolved naming mismatches across UN, World Bank, and OWID conventions |
| 3 | Secondary source merge | World Bank GDP/population data merged as secondary source to fill UN data gaps |
| 4 | Null imputation | Missing `GDP`, `gdp_per_cap`, and `population` values filled from secondary source using `.fillna()` |
| 5 | Duplicate column cleanup | Post-merge `_x`/`_y` suffixed columns collapsed and renamed |
| 6 | Final null check | Confirmed zero nulls across all 13 columns after imputation |
| 7 | Final shape | 1,323 rows × 13 columns — clean, zero nulls, exported via config path |

---

## Derived Metrics (EDA Notebooks)

| Column | Formula | Notebook | Purpose |
|--------|---------|----------|---------|
| `co2_int` | `co2 / GDP` | Diana | CO₂ intensity — Scenario A (fossil + industrial only) |
| `co2_luc_int` | `co2_luc / GDP` | Diana | CO₂ intensity — Scenario B (full footprint incl. land-use) |
| `d_co2_int` | year-over-year diff of `co2_int` per country | Diana | Rate of decoupling (Scenario A) |
| `d_co2_luc_int` | year-over-year diff of `co2_luc_int` per country | Diana | Rate of decoupling (Scenario B) |
| `d_renew_share` | year-over-year diff of `prct_renew_cons` per country | Diana | Rate of renewable adoption |
| `co2_per_cap` | `(co2 * 1_000_000) / population` | Irene | CO₂ burden per person (tonnes) |
| `welfare_ratio` | `co2_per_cap / (prct_access_elec / 100)` | Irene | CO₂ cost per unit of electricity benefit received |
| `gdp_group` | `pd.qcut(gdp_per_cap, q=4)` | Irene | Wealth quartile classification (Q1 poorest → Q4 richest) |

---

## Database Schema

The relational schema is fully designed and normalised to **3NF**. No database was instantiated for this project phase — schema only.

**Schema design tools:** Miro (ERD diagram) + drawDB (SQL DDL export)  
**Files:** `sql_scripts/ERD_Miro.png` · `sql_scripts/MiniProject_GDP_CO2_schema.sql`

### Tables

| Table | Role |
|-------|------|
| `fact_energy` | Energy metrics per record: electricity access, primary consumption, renewable production/consumption |
| `fact_emissions` | CO₂ and CO₂-LUC values |
| `fact_economy` | GDP, population, GDP per capita |
| `region` | Region name + ISO code lookup |
| `country` | Central dimension linking all fact tables + region via foreign keys |

---

## Key Findings

> ⚠️ Formal statistical tests still pending. These are preliminary observations from EDA.

### H1 — CO₂ Intensity Decline (Scenarios A & B)

**Scenario A (fossil + industrial, `co2_int`):**
- **Europe** is the only region showing a consistent downward CO₂ intensity trend across the full 2014–2020 window.
- **Asia** holds the highest CO₂ intensity by far, with a sharp spike in 2019–2020.
- **South America** diverges upward after 2017, bucking the global trend.
- Most regions declined 2015–2018, then reversed after 2018. The 2020 dip in some regions is partly COVID-driven, not structural decoupling.

**Scenario B (full footprint including land-use, `co2_luc_int`):**
- **Africa** replaces Asia as the most intense region when land-use is included.
- **South America** moves sharply closer to Asia — land-use change (primarily deforestation) is the mechanism. The gap between Scenario A and B for South America is the clearest evidence of **emissions displacement rather than elimination**.
- Europe remains the least CO₂-intense region across both scenarios.

### H2 — Renewable Penetration as the Mechanism

- Renewable-to-CO₂ correlation is region- and period-specific: Europe, North America and South America do show clearer signals; Africa, Asia and Oceania  show none.
- The production/consumption gap reveals an export dynamic: some regions produce more renewables than they consume domestically. Specially for the regions Africa, Asia, Oceania and North America
  
- **H2 Verdict:** partially supported. Renewables are a contributing factor but not the sole driver.
- some regions show a widening gap between renewable production and consumption, suggesting clean energy is being exported rather than used to decarbonise domestic energy systems.

### H3 — Electricity Access & CO₂

- **Wealth-access relationship confirmed:** richer regions have near-universal electricity access; Africa averages ~50% despite being a globally significant total emitter.
- **Mid-income countries (Q3) are the heaviest total emitters** — more than the richest group, suggesting peak industrialisation drives absolute emissions more than wealth itself. CO₂ per capita, however, rises consistently with wealth.
- **High-emissions, low-access pattern is real and concentrated:** India, Russia, Indonesia, Nigeria, and South Africa generate above-median CO₂ while significant portions of their populations lack electricity access.
- **Nigeria is the starkest case:** among the lowest electricity access (~56%) in the top 15 total emitters — emissions clearly not serving its own population.
- **Electricity access improved across all regions 2014–2020**, but Africa's gap relative to the rest remains large at period end.
- **Verdict:** H3 is partially confirmed. The wealth-access relationship is clearly supported and the high-CO₂/low-access pattern is real. Confirming the full exploitation framing would require additional trade/export-of-emissions evidence.

---

## Known Limitations

- **COVID 2020:** the CO₂ dip visible in 2020 for some regions is partly driven by economic contraction, not structural decoupling — endpoint delta interpretation requires this caveat.
- **GDP metric:** OWID uses PPP (2011 international $). Valid for trend comparison, but not current USD headline numbers.

- **Africa data:** Africa's trend is outlier-sensitive and requires country-level decomposition before any regional claim holds.
- **Total CO₂ size bias (H3):** large countries like India and Russia will always appear in high-emission rankings by total volume regardless of efficiency. Per-capita figures should be read alongside totals.
- **Electricity access reporting lag:** World Bank data for some African nations may lag real conditions by 1–2 years.
- Country name mismatches between UN, World Bank, and OWID required manual harmonisation in `final_clean_merge.ipynb`.


