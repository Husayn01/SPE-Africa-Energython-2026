# Handover Document: SPE Africa Energython 2026

## 1. What This Project Is

This is a submission for the **SPE Africa Energython 2026**, a student competition run by the SPE Asset Management Technical Section. The theme is **"Molecule to Megabyte"**: design a decision-ready techno-economic concept for powering a **10-20 MW data center** using a natural-gas-fired plant.

### Competition Details

| Item | Detail |
|------|--------|
| **Finals** | 20 September 2026, Virtual (Shark Tank-style pitch) |
| **Deliverables** | 10-minute standalone video + 15-70 detailed presentation slides |
| **Judging Weights** | Innovation 20%, Technical Rigor 25%, Financial Model 25%, Presentation 30% |
| **Prizes** | $2,000 / $1,500 / $1,000 (1st / 2nd / 3rd) |
| **Sponsor** | Kenyon International |
| **Eligibility** | SPE Student Chapters in Africa Region, teams of 3-5 students |
| **Key Deadline** | 31 August 2026 (video + slides submission) |
| **Excluded fuels** | Nuclear and coal. Geothermal and hydrogen are eligible alternatives. |

### What Teams Must Address

The challenge description (see `Challenge description.txt` in the repo root) requires teams to cover:
1. Gas supply and logistics
2. Transportation and off-take agreements
3. Generation equipment selection
4. Full financial modeling

---

## 2. Winning Solutions from Other Regions (Inspiration)

Five regional editions have already completed. The user studied these and made deliberate choices informed by what won.

### North America (January 2026, Houston)

| Rank | Team | Concept | Key Lesson |
|------|------|---------|------------|
| 1st | **SynerGAS** (U. Wyoming) | 15 MW behind-the-meter, modular reciprocating gas engines, N+1 redundancy | Speed-to-market (12-14 months vs 3-7 year grid queue). Practical, achievable scale. |
| 2nd | **Sierra Solutions** (UT Austin) | Investment-grade concept with modular engines, flexible gas sourcing, structured pricing | Financial rigor and commercial creativity matter. |
| 3rd | **Rising Stars** (Texas A&M Intl) | Combined-cycle plant balancing reliability, efficiency, reduced water use | Combined cycle can work but adds complexity. |

### India-APAC (March 2026, Mumbai)

| Rank | Team | Concept | Key Lesson |
|------|------|---------|------------|
| 1st | **UPES** (Dehradun) | 25 MW hydrogen-natural gas hybrid | Bold ESG angle with hydrogen integration. |
| 2nd | **Team Iron Throne** (IIT ISM/MIT WPU/NIT Trichy) | Hydrogen-blended baseload + offshore wind integration | Sophisticated commercial model, 99.999% availability target. |

### Europe (July 2026)

| Rank | Team | Concept | Key Lesson |
|------|------|---------|------------|
| 1st | **Velogas** (IFP School, France) | LNG/CNG virtual pipeline + Monte Carlo sensitivity analysis | Investment-grade financial rigor and risk quantification won. |

### What We Took from These Winners

The user and I distilled the winning pattern into six elements our submission must have:
1. **Decision-Grade Integration**: Thermodynamics to electrical to financial model, seamlessly linked.
2. **Behind-the-Meter Speed**: 12-14 month deployment, avoiding grid queue delays.
3. **Tier III Reliability**: N+1 generation mapped to 99.982% data center availability.
4. **Tri-generation (CCHP)**: Waste heat from engines drives absorption chillers for cooling. PUE target of 1.18.
5. **Decarbonization Roadmap**: Phased hydrogen/solar/carbon credit overlay across the project lifetime.
6. **Monte Carlo Risk Analysis**: 10,000-iteration sensitivity analysis, not just a single base case.

---

## 3. Our Concept at a Glance

| Parameter | Value |
|-----------|-------|
| **IT Load** | 15 MW (colocation data center) |
| **Installed Generation** | 18 MW (4 x 4.5 MW reciprocating gas engines, N+1 config) |
| **Location** | Lekki Free Zone, Lagos, Nigeria (primary); Ewekoro/Sagamu (backup) |
| **Gas Source** | ELPS pipeline ($2.18/MMBtu regulated domestic price) + CNG/LNG virtual pipeline backup |
| **Engine Technology** | Reciprocating gas engines (Wartsila 20V34SG or INNIO Jenbacher J920) |
| **Efficiency** | 48-50% electrical (simple cycle); >80% overall with tri-gen |
| **PUE Target** | 1.18 (via double-effect LiBr absorption chillers using waste heat) |
| **Data Center Tier** | Tier III (99.982% uptime, concurrently maintainable) |
| **Anchor Tenant** | Colocation operator (Rack Centre / Equinix / Africa Data Centres) |
| **PPA Structure** | Behind-the-meter corporate PPA, USD-denominated |
| **CAPEX (Power Plant)** | ~$20M ($1,100-1,650/kW) |
| **Annual Revenue** | ~$15.3M (at $0.12/kWh blended tariff) |
| **Annual OPEX** | ~$5.0M |
| **Target LCOE** | $0.07-0.08/kWh |
| **Project IRR** | >16% |
| **Equity IRR** | >22% |
| **Innovation Overlay** | Flare gas capture from Niger Delta (carbon credits); phased solar PV + BESS; H2 blending roadmap |

---

## 4. Project Architecture: The 9-Notebook Pipeline

The work is structured as a sequential pipeline of Jupyter Notebooks. Each notebook produces data files (CSV, JSON) and figures (PNG) that feed into subsequent notebooks.

| # | Notebook | Purpose | Status |
|---|----------|---------|--------|
| 01 | `01_market_and_demand.ipynb` | Market sizing, country selection, fiber connectivity, 8,760-hour load profile | **Complete** (but has open bugs, see Section 6) |
| 02 | `02_site_selection_gis.ipynb` | Multi-Criteria Decision Analysis (MCDA), GIS scoring of candidate sites | **Not started** |
| 03 | `03_gas_supply_and_logistics.ipynb` | Gas sourcing, pipeline vs virtual pipeline, GSA terms, fuel cost modeling | **Not started** |
| 04 | `04_power_generation.ipynb` | Engine selection, N+1 configuration, heat balance, CCHP/tri-gen modeling | **Not started** |
| 05 | `05_process_design.ipynb` | Gas conditioning, electrical SLD, cooling system, Tier III architecture | **Not started** |
| 06 | `06_commercial_agreements.ipynb` | GSA, GTA, PPA term sheets, risk mitigation instruments | **Not started** |
| 07 | `07_financial_model.ipynb` | CAPEX/OPEX, DCF, NPV/IRR/LCOE, WACC, DSCR, sensitivity, Monte Carlo | **Not started** |
| 08 | `08_esg_and_decarbonization.ipynb` | Carbon intensity, flare gas credits, H2 roadmap, phased decarb plan | **Not started** |
| 09 | `09_executive_summary.ipynb` | Consolidated dashboard, key metrics, presentation-ready outputs | **Not started** |

### Data Flow Between Notebooks

```
01_market_and_demand
    outputs: section_01_load_profile.csv, section_01_ramp_projection.csv, section_01_market_summary.json
        |
        v
02_site_selection_gis
    reads: section_01 outputs
    outputs: section_02_site_scores.csv, section_02_selected_site.json
        |
        v
03_gas_supply_and_logistics
    reads: section_02 selected site
    outputs: section_03_fuel_cost.csv, section_03_gas_supply.json
        |
        v
04_power_generation
    reads: section_01 load profile, section_03 fuel cost
    outputs: section_04_engine_config.json, section_04_heat_balance.csv
        |
        v
05_process_design
    reads: section_04 engine config
    outputs: section_05_system_architecture.json, section_05_sld_data.json
        |
        v
06_commercial_agreements
    reads: section_03 gas supply, section_04 engine config
    outputs: section_06_contract_terms.json
        |
        v
07_financial_model
    reads: ALL previous section outputs
    outputs: section_07_dcf.csv, section_07_sensitivity.csv, section_07_monte_carlo.csv
        |
        v
08_esg_and_decarbonization
    reads: section_04 heat balance, section_07 financial outputs
    outputs: section_08_emissions.csv, section_08_carbon_credits.json
        |
        v
09_executive_summary
    reads: ALL section outputs
    outputs: consolidated dashboard, presentation-ready figures
```

---

## 5. File System Layout

```
SPE Africa Energython/
|
|-- .agents/
|   |-- AGENTS.md                          # Project rules (DO NOT push to GitHub)
|
|-- .gitignore                             # Ignores .agents/, TEACHING_GUIDE.md, __pycache__, .venv, etc.
|
|-- Challenge description.txt              # Original competition brief (scraped from SPE website)
|-- TEACHING_GUIDE.md                      # Simplified explanations for the user (DO NOT push to GitHub)
|
|-- notebooks/
|   |-- 01_market_and_demand.ipynb         # Section 1 (complete, has bugs)
|
|-- data/
|   |-- section_01_load_profile.csv        # 8,760-hour load profile (Hour, Month, IT_Load_MW, etc.)
|   |-- section_01_ramp_projection.csv     # 10-year utilization ramp (Year, IT_Load_MW, etc.)
|   |-- section_01_market_summary.json     # Design parameters, market context, gas economics
|
|-- outputs/
|   |-- figures/
|   |   |-- 01_africa_dc_capacity_growth.png
|   |   |-- 01_africa_dc_by_country.png
|   |   |-- 01_lagos_fiber_dc_map.html     # DEPRECATED: was folium, now replaced by static matplotlib
|   |   |-- 01_load_profile_analysis.png
|   |-- tables/                            # Empty, created for future use
|
|-- references/
|   |-- data sources/
|       |-- ref links.txt                  # Gas flare tracker and pipeline map links
|
|-- dashboard/                             # Empty, reserved for future dashboard work
|
|-- fix_height.py                          # STALE TEMP FILE: should be deleted
```

### Virtual Environment

The project uses a shared virtual environment located at:
```
C:\Users\Jinxxx\Desktop\Hussaini\SPE Africa Geothermal Datathon 2026\.venv
```

This environment has all the core data science libraries pre-installed: pandas, numpy, matplotlib, seaborn, folium, nbformat, jupyter, scipy, numpy-financial. The `geopandas` and `contextily` packages are **NOT** installed (checked and confirmed missing).

To run notebooks via nbconvert:
```powershell
$env:PYTHONIOENCODING="utf-8"
& "C:\Users\Jinxxx\Desktop\Hussaini\SPE Africa Geothermal Datathon 2026\.venv\Scripts\jupyter.exe" nbconvert --execute --inplace "notebooks\01_market_and_demand.ipynb"
```

### GitHub Repository

| Item | Detail |
|------|--------|
| **URL** | https://github.com/Husayn01/SPE-Africa-Energython-2026 |
| **Visibility** | Private |
| **Default Branch** | master |
| **Auth** | `gh` CLI authenticated as `Husayn01` via keyring |
| **Git config** | user.name = "Husayn01", user.email = "husayn01@github.local" (local to repo) |

---

## 6. Known Issues and Unfinished Business

### Bug: Notebook 01 has a broken capacity growth chart

The variable `height` was accidentally renamed to `sans` by a text-processing script. The fix script `fix_height.py` exists in the repo root but was never fully applied and committed. The notebook on disk currently has the error, and the last `git push` pushed it with the error output embedded.

**To fix**: Run `fix_height.py`, re-execute the notebook, delete the script, commit, and push. Or simply edit the notebook cell directly: change `sans = bar.get_height()` to `height = bar.get_height()`.

### Bug: `plt.close()` vs `plt.show()` issue

The user reported that charts were not displaying inline in their notebook viewer. The original code used `plt.close()` after `plt.savefig()`, which suppresses inline display. The user manually changed some to `plt.show()`. The current notebook state is mixed. **Going forward, always use `plt.show()` after `plt.savefig()` and never `plt.close()` in any notebook.**

### Stale map: Folium replaced with Matplotlib

The folium interactive map caused a "Trust Notebook" error in the user's environment. It was replaced with a static matplotlib scatter plot showing cable landings and candidate sites. The old `01_lagos_fiber_dc_map.html` file in outputs is now stale. The user asked for "a proper standard map with standard labels and a legend, no fancy icons." The current matplotlib version does this but the output PNG may not have been saved under a new name.

### Stale file: `fix_height.py`

This temporary script is still in the repo root and needs to be deleted after applying the fix.

### Missing: `geopandas` and `contextily`

These are needed for Notebook 02 (Site Selection GIS). They must be installed into the virtual environment before that notebook can run.

---

## 7. Strict Style Rules (from `.agents/AGENTS.md`)

These rules are non-negotiable. The user was very explicit about them:

1. **Judge-Facing Tone**: Write everything as if it is the final deliverable for a professional judging panel. No meta-commentary like "this is what judges want to see" or "this section scores points on Technical Rigor." Never break the fourth wall.

2. **Professional Language**: Use natural, human-written phrasing. Avoid words like "deep dive." Avoid excessive use of dashes for emphasis.

3. **No AI Slop / Emojis**: Zero emojis in code, comments, markdown, or filenames. No decorative separators like `# =========` or `# -------`. Keep headers clean: just `## 1.1 The Macro Opportunity`, not `## 1.1 THE MACRO OPPORTUNITY =========`.

4. **Code Structure**: Break overly long code blocks into smaller, logical cells. No massive monolithic cells.

5. **References**: Provide accessible, real URLs for references and data sources. Not just "Source: GSMA" but "Source: [GSMA Mobile Economy Sub-Saharan Africa 2024](https://www.gsma.com/mobileeconomy/sub-saharan-africa/)."

6. **Workspace Cleanliness**: Only retain necessary directories (`notebooks/`, `data/`, `outputs/`, `dashboard/`, `references/`). Clean up any temporary builder scripts immediately after use.

7. **Teaching Guide**: Maintain and update `TEACHING_GUIDE.md` with simplified explanations. This file and `AGENTS.md` must never be pushed to GitHub.

---

## 8. How the Notebook Generation Process Works

Notebooks are generated programmatically using `nbformat` in Python. The workflow is:

1. Write a Python script (e.g., `build_notebook_02.py`) that constructs cells via `nbf.v4.new_markdown_cell()` and `nbf.v4.new_code_cell()`.
2. Run the script to produce the `.ipynb` file.
3. Execute the notebook via `jupyter nbconvert --execute --inplace` to populate outputs.
4. **Delete the builder script immediately** (per workspace cleanliness rule).
5. Commit and push.

### Known Pitfalls

- **Apostrophes in strings**: The `"Cote d'Ivoire"` string caused a SyntaxError because the apostrophe terminated the outer single-quoted string. Use double quotes for the outer string when the content contains apostrophes.
- **Unicode in f-strings inside raw strings**: Caused build errors in earlier attempts. Use `.format()` instead.
- **plt.close() suppresses inline display**: Always use `plt.show()` instead.

---

## 9. Research Already Completed

Four research subagents were dispatched in the earlier conversation and returned detailed findings. The results are consolidated in the master guide artifact at:
```
C:\Users\Jinxxx\.gemini\antigravity\brain\30789bc3-0df3-4f2b-97e3-e436be56c54d\energython_master_guide.md
```

This 786-line document covers:
- Site selection criteria and top 7 ranked candidate sites
- Gas supply pricing across 6 African countries
- Gas transportation options (pipeline vs CNG/LNG virtual pipeline)
- Power generation technology comparison (reciprocating engines vs gas turbines)
- Engine specifications (Wartsila 20V34SG, INNIO Jenbacher J920, CAT CG260-16)
- Complete process design and system architecture
- Gas conditioning components
- Electrical distribution (SLD logic)
- Tri-generation (CCHP) calculations
- Commercial agreement structures (GSA, GTA, PPA)
- Financial modeling parameters (CAPEX, OPEX, WACC, IRR, LCOE, DSCR)
- DFI financing sources (IFC, AfDB, US DFC, FMO, DEG)
- ESG and decarbonization roadmap
- Carbon credit revenue from flare gas
- Presentation strategy for Shark Tank format
- Recommended tool stack
- 4-week execution timeline

**This guide is the primary reference for all technical content going forward.** The numbers, formulas, and benchmarks in it should be used directly in the notebooks.

---

## 10. User Preferences and Working Style

- The user wants to be **taught and guided**, not just handed finished work. Always explain the "why" before the "how."
- The user is using **Jupyter notebooks in VS Code** on Windows.
- The user expects **inline chart display** in the notebook (not just saved PNGs).
- The user dislikes excessive formatting, decorative dividers, or anything that looks auto-generated.
- The user values **accuracy and completeness over speed**.
- The user wants all builder/temp scripts deleted immediately after use.
- The user expects `TEACHING_GUIDE.md` to be updated after each section is completed.
- The user expects regular `git commit` and `git push` after meaningful progress.

---

## 11. Immediate Next Steps

### Priority 1: Fix Notebook 01
1. Fix the `height` variable bug in the capacity growth chart cell.
2. Ensure all chart cells use `plt.show()` instead of `plt.close()`.
3. Delete `fix_height.py` from the repo root.
4. Re-execute the notebook.
5. Commit and push the clean version.

### Priority 2: Build Notebook 02 (Site Selection GIS)
1. Install `geopandas` and `contextily` into the virtual environment if needed for proper GIS maps. If not available, use matplotlib with manual coordinate plotting (as was done for the submarine cable map).
2. Implement Multi-Criteria Decision Analysis (MCDA) scoring 3+ candidate sites:
   - Lekki Free Zone, Lagos (primary)
   - Ewekoro/Sagamu, Ogun State (backup)
   - Niger Delta flare cluster sites (innovation overlay)
3. Score each site against the 8 criteria from the master guide (gas proximity, fiber, grid, water, political stability, land, seismic/flood risk, demand proximity).
4. Produce a weighted scoring matrix, radar/spider charts, and a final site recommendation.
5. Output: `section_02_site_scores.csv`, `section_02_selected_site.json`.

### Priority 3-8: Build Notebooks 03-08
Follow the pipeline structure described in Section 4. Each notebook reads from previous section outputs and produces its own data files and figures.

### Priority 9: Executive Summary and Presentation Materials
Notebook 09 consolidates all outputs. Beyond the notebooks, the final deliverables are:
- A 15-70 slide presentation deck
- A 10-minute standalone video

---

## 12. Key Reference Files and Paths

| File | Path | Purpose |
|------|------|---------|
| Challenge Description | `Challenge description.txt` | Original competition brief |
| AGENTS.md | `.agents/AGENTS.md` | Style rules (local only) |
| Teaching Guide | `TEACHING_GUIDE.md` | User learning document (local only) |
| Master Guide | `C:\Users\Jinxxx\.gemini\antigravity\brain\30789bc3-0df3-4f2b-97e3-e436be56c54d\energython_master_guide.md` | 786-line research compendium |
| Virtual Environment | `C:\Users\Jinxxx\Desktop\Hussaini\SPE Africa Geothermal Datathon 2026\.venv` | Shared Python 3.12 env |
| GitHub Repo | https://github.com/Husayn01/SPE-Africa-Energython-2026 | Private, branch: master |
| Load Profile Data | `data/section_01_load_profile.csv` | 8,760-row hourly load data |
| Ramp Projection | `data/section_01_ramp_projection.csv` | 10-year utilization ramp |
| Market Summary | `data/section_01_market_summary.json` | Key design parameters |
| Gas Flare Tracker | https://nosdra.gasflaretracker.ng/gasflaretracker.html | Nigerian flare site data |
| Pipeline Map | See `references/data sources/ref links.txt` | Google Maps pipeline overlay |
