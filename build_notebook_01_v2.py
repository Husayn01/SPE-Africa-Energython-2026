import nbformat as nbf
import os

nb = nbf.v4.new_notebook()
nb.metadata.update({
    "kernelspec": {
        "display_name": "Python 3",
        "language": "python",
        "name": "python3"
    },
    "language_info": {
        "name": "python",
        "version": "3.12.10"
    }
})

cells = []

# Title & Overview
cells.append(nbf.v4.new_markdown_cell("""# Section 1: Market and Demand Sizing

## Purpose of This Section
This notebook establishes the market foundation for the techno-economic concept. It addresses three fundamental requirements:
1. Validating the demand for a 10-20 MW data center in Africa, specifically Nigeria.
2. Quantifying the scale and growth rate of the opportunity.
3. Defining the target customer load profile for subsequent engineering and financial modeling.

## Key Sources and References
* **Africa Data Centres Association (ADCA)**: Continental capacity estimates (2025). https://africadatacentres.org/
* **Xalam Analytics**: Africa data center market sizing and projections (2025). https://xalamanalytics.com/
* **IFC**: Digital Infrastructure in Africa (2023). https://www.ifc.org/en/what-we-do/sector-expertise/telecom-media-technology
* **TeleGeography**: Submarine Cable Map (2026). https://www.submarinecablemap.com/
* **GSMA**: Mobile Economy Sub-Saharan Africa (2024). https://www.gsma.com/mobileeconomy/sub-saharan-africa/
"""))

# Imports & Configuration
cells.append(nbf.v4.new_code_cell("""import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
import folium
import json
import os
import warnings
warnings.filterwarnings('ignore')

plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams.update({
    'figure.figsize': (12, 6),
    'font.family': 'sans-serif',
    'font.sans-serif': ['Segoe UI', 'Arial', 'Helvetica'],
    'font.size': 11,
    'axes.titlesize': 14,
    'axes.titleweight': 'bold',
    'axes.labelsize': 12,
    'figure.dpi': 150,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
})

COLORS = {
    'primary': '#1B4332',
    'secondary': '#2D6A4F',
    'accent': '#40916C',
    'highlight': '#F77F00',
    'warning': '#D62828',
    'neutral': '#6C757D',
    'light': '#95D5B2',
    'bg': '#F8F9FA',
    'text': '#212529',
}
PALETTE = [COLORS['primary'], COLORS['highlight'], COLORS['accent'],
           COLORS['secondary'], COLORS['warning'], COLORS['light']]
sns.set_palette(PALETTE)

os.makedirs('../outputs/figures', exist_ok=True)
os.makedirs('../outputs/tables', exist_ok=True)
os.makedirs('../data', exist_ok=True)
"""))

# Macro Opportunity
cells.append(nbf.v4.new_markdown_cell("""## 1.1 The Macro Opportunity

Africa's data center market is undergoing structural expansion driven by several factors:
1. **Internet Penetration**: Africa has approximately 570M internet users (36% penetration), projected to double by 2030 (GSMA).
2. **Mobile Data Consumption**: Average mobile data per user grew from 2.3 GB/month in 2019 to 7.5 GB/month in 2024.
3. **Hyperscaler Entry**: AWS, Microsoft Azure, and Google Cloud have established or are establishing local regions.
4. **Data Sovereignty Regulations**: New privacy acts in Nigeria, Kenya, and South Africa encourage localized data hosting.
5. **AI Compute Demand**: Generative AI inference workloads require low-latency, localized compute capabilities.
"""))

# Capacity Data
cells.append(nbf.v4.new_code_cell("""# Africa Data Center Market Capacity (MW)
africa_dc_capacity = pd.DataFrame({
    'Year': [2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030],
    'Operational_MW': [120, 155, 210, 280, 370, 450, 520, 600, 720, 880, 1100, 1400],
    'Type': ['Actual']*7 + ['Current'] + ['Projected']*4
})

africa_dc_capacity['YoY_Growth'] = africa_dc_capacity['Operational_MW'].pct_change() * 100
cagr_2019_2030 = ((1400 / 120) ** (1/11) - 1) * 100

print(f"2019-2030 CAGR: {cagr_2019_2030:.1f}%")
print(f"2026 Operational Capacity: ~600 MW")
"""))

# Capacity Plot
cells.append(nbf.v4.new_code_cell("""fig, ax = plt.subplots(figsize=(14, 7))

actual = africa_dc_capacity[africa_dc_capacity['Type'].isin(['Actual', 'Current'])]
projected = africa_dc_capacity[africa_dc_capacity['Type'] == 'Projected']

bars_actual = ax.bar(actual['Year'], actual['Operational_MW'],
                     color=COLORS['primary'], alpha=0.9, width=0.7,
                     label='Operational / Current', edgecolor='white', linewidth=0.5)
bars_projected = ax.bar(projected['Year'], projected['Operational_MW'],
                        color=COLORS['accent'], alpha=0.6, width=0.7,
                        label='Projected', edgecolor='white', linewidth=0.5,
                        hatch='///')

for bar in list(bars_actual) + list(bars_projected):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height + 15, f'{int(height)}',
            ha='center', va='bottom', fontsize=9, fontweight='bold', color=COLORS['text'])

ax.annotate(f'CAGR 2019-2030: {cagr_2019_2030:.1f}%',
            xy=(2024.5, 700), fontsize=13, fontweight='bold', color=COLORS['highlight'],
            bbox=dict(boxstyle='round,pad=0.5', facecolor=COLORS['highlight'], alpha=0.15, edgecolor=COLORS['highlight']))

ax.annotate('Our 15 MW concept enters here',
            xy=(2026, 600), xytext=(2026, 900),
            arrowprops=dict(arrowstyle='->', color=COLORS['warning'], lw=2),
            fontsize=10, fontweight='bold', color=COLORS['warning'], ha='center', va='bottom')

ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Operational IT Capacity (MW)', fontsize=12)
ax.set_title('Africa Data Center Market - Operational IT Capacity (2019-2030)', fontsize=15, fontweight='bold', pad=15)
ax.set_xticks(africa_dc_capacity['Year'])
ax.set_xticklabels([str(int(y)) for y in africa_dc_capacity['Year']], rotation=45)
ax.legend(loc='upper left', fontsize=11, framealpha=0.9)
ax.set_ylim(0, 1650)
ax.grid(axis='y', alpha=0.3, linestyle='--')

plt.tight_layout()
plt.savefig('../outputs/figures/01_africa_dc_capacity_growth.png', dpi=300)
plt.close()
"""))

# Market by country
cells.append(nbf.v4.new_markdown_cell("""## 1.2 Market by Country

South Africa currently holds the majority of operational capacity. However, Nigeria and Kenya are demonstrating the highest growth rates.
Nigeria presents a strong case for development due to:
- A population exceeding 230 million.
- An internet user base of approximately 110 million active users.
- A regulated domestic gas price of $2.18/MMBtu, offering a significant feedstock cost advantage.
"""))

cells.append(nbf.v4.new_code_cell("""country_data = pd.DataFrame({
    'Country': ['South Africa', 'Nigeria', 'Kenya', 'Egypt',
                'Ghana', 'Morocco', 'Ethiopia', 'Côte d\'Ivoire',
                'Tanzania', 'Mozambique', 'Others'],
    'Capacity_MW': [360, 80, 45, 35, 20, 15, 12, 8, 6, 4, 15],
    'Growth_Outlook': ['High', 'Very High', 'Very High', 'High',
                       'High', 'Medium', 'Very High', 'Medium',
                       'Medium', 'Medium', 'Medium']
})
country_data['Market_Share'] = (country_data['Capacity_MW'] / country_data['Capacity_MW'].sum() * 100)
"""))

cells.append(nbf.v4.new_code_cell("""fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7), gridspec_kw={'width_ratios': [1, 1.2]})

sorted_data = country_data.sort_values('Capacity_MW', ascending=True)
colors_bar = [COLORS['highlight'] if c == 'Nigeria' else COLORS['primary'] for c in sorted_data['Country']]

bars = ax1.barh(sorted_data['Country'], sorted_data['Capacity_MW'], color=colors_bar, edgecolor='white', height=0.65)
for bar, val in zip(bars, sorted_data['Capacity_MW']):
    ax1.text(bar.get_width() + 3, bar.get_y() + bar.get_height()/2, f'{int(val)} MW', va='center', fontsize=9, fontweight='bold')

ax1.set_xlabel('Operational IT Capacity (MW)', fontsize=11)
ax1.set_title('Capacity by Country (2026)', fontsize=13, fontweight='bold')
ax1.set_xlim(0, max(sorted_data['Capacity_MW']) * 1.25)

nigeria_bar = bars[list(sorted_data['Country']).index('Nigeria')]
ax1.annotate('Target Market',
             xy=(nigeria_bar.get_width(), nigeria_bar.get_y() + nigeria_bar.get_height()/2),
             xytext=(nigeria_bar.get_width() + 60, nigeria_bar.get_y() + nigeria_bar.get_height()/2 + 1.5),
             arrowprops=dict(arrowstyle='->', color=COLORS['highlight'], lw=1.5),
             fontsize=10, fontweight='bold', color=COLORS['highlight'])

growth_colors = {'Very High': '#D4EDDA', 'High': '#C3E6CB', 'Medium': '#FFF3CD', 'Low': '#F8D7DA'}
growth_df = country_data.sort_values('Capacity_MW', ascending=False).head(8)

ax2.set_xlim(0, 5)
ax2.set_ylim(-0.5, len(growth_df) - 0.5)

for i, (_, row) in enumerate(growth_df.iterrows()):
    y_pos = len(growth_df) - 1 - i
    ax2.text(0.1, y_pos, f"{row['Country']}", fontsize=11, va='center', fontweight='bold')
    ax2.text(2.0, y_pos, f"{int(row['Capacity_MW'])} MW", fontsize=10, va='center', ha='center')
    gc = growth_colors.get(row['Growth_Outlook'], '#E2E3E5')
    bbox_props = dict(boxstyle="round,pad=0.3", facecolor=gc, edgecolor='gray', alpha=0.8)
    ax2.text(3.5, y_pos, f" {row['Growth_Outlook']} ", fontsize=10, va='center', ha='center', bbox=bbox_props, fontweight='bold')
    ax2.text(4.7, y_pos, f"{row['Market_Share']:.1f}%", fontsize=10, va='center', ha='center')

ax2.text(0.1, len(growth_df) - 0.1 + 0.6, 'Country', fontsize=10, fontweight='bold', va='center')
ax2.text(2.0, len(growth_df) - 0.1 + 0.6, 'Capacity', fontsize=10, fontweight='bold', va='center', ha='center')
ax2.text(3.5, len(growth_df) - 0.1 + 0.6, 'Growth', fontsize=10, fontweight='bold', va='center', ha='center')
ax2.text(4.7, len(growth_df) - 0.1 + 0.6, 'Share', fontsize=10, fontweight='bold', va='center', ha='center')

ax2.set_title('Market Positioning Matrix', fontsize=13, fontweight='bold')
ax2.axis('off')

plt.tight_layout()
plt.savefig('../outputs/figures/01_africa_dc_by_country.png', dpi=300)
plt.close()
"""))

# Nigeria Focus
cells.append(nbf.v4.new_markdown_cell("""## 1.3 Submarine Cable Connectivity in Lagos

Lagos functions as a primary digital hub for West Africa, characterized by its high density of submarine cable landings. This infrastructure provides terabits per second of bandwidth and inherent redundancy.

Key cable landing points near the candidate sites:
* **2Africa** (Meta consortium): 180 Tbps capacity, Lekki landing
* **Equiano** (Google): 144 Tbps capacity, Lekki landing
* **MainOne** (Equinix): 10 Tbps capacity, Lekki Phase 1 landing
* **WACS** (MTN/Vodacom): 14.5 Tbps capacity, Lagos landing
"""))

cells.append(nbf.v4.new_code_cell("""m = folium.Map(location=[6.45, 3.45], zoom_start=11, tiles='CartoDB positron')

cable_landings = [
    {"name": "2Africa Landing", "lat": 6.4355, "lon": 3.5523, "capacity": "180 Tbps", "color": "blue"},
    {"name": "Equiano Landing", "lat": 6.4380, "lon": 3.5450, "capacity": "144 Tbps", "color": "red"},
    {"name": "MainOne Landing", "lat": 6.4300, "lon": 3.5400, "capacity": "10 Tbps", "color": "green"},
    {"name": "WACS Landing", "lat": 6.4200, "lon": 3.4100, "capacity": "14.5 Tbps", "color": "purple"},
]

for cable in cable_landings:
    folium.Marker(
        location=[cable['lat'], cable['lon']],
        popup=f"<b>{cable['name']}</b><br>Capacity: {cable['capacity']}",
        tooltip=cable['name'],
        icon=folium.Icon(color=cable['color'], icon='signal', prefix='fa')
    ).add_to(m)

candidate_sites = [
    {"name": "Lekki Free Zone (Primary)", "lat": 6.4250, "lon": 3.5800, "notes": "NEPZA zone, near cable landings, ELPS gas access"},
    {"name": "Ewekoro/Sagamu (Backup)", "lat": 6.8700, "lon": 3.2200, "notes": "Lower land cost, ELPS pipeline direct access"},
]

for site in candidate_sites:
    folium.Marker(
        location=[site['lat'], site['lon']],
        popup=f"<b>{site['name']}</b><br>{site['notes']}",
        tooltip=site['name'],
        icon=folium.Icon(color='red', icon='star', prefix='fa')
    ).add_to(m)

m.save('../outputs/figures/01_lagos_fiber_dc_map.html')
m
"""))

# Load Profile Design
cells.append(nbf.v4.new_markdown_cell("""## 1.4 Designing the Load Profile

A 15 MW IT load target is selected. This scale aligns with current colocation requirements while supporting an N+1 engine configuration (4 x 4.5 MW units providing 18 MW installed capacity).

The load profile for a colocation data center is modeled as a continuous baseload with minor diurnal fluctuations and a ramp-up curve during the initial operational years.
"""))

cells.append(nbf.v4.new_code_cell("""IT_LOAD_MW = 15.0
PUE_WITH_CCHP = 1.18
PUE_WITHOUT_CCHP = 1.40
HOURS_PER_YEAR = 8760

lagos_monthly_temp = {
    1: 27.5, 2: 28.5, 3: 29.0, 4: 28.5, 5: 27.5, 6: 26.0,
    7: 25.0, 8: 25.0, 9: 25.5, 10: 26.5, 11: 27.5, 12: 27.5
}

np.random.seed(42)
hours = np.arange(HOURS_PER_YEAR)
months = np.array([(h // 720) % 12 + 1 for h in hours])
hour_of_day = hours % 24

# Base load with minor diurnal variation
diurnal_factor = 1.0 + 0.03 * np.sin(2 * np.pi * (hour_of_day - 6) / 24)
monthly_ramp = np.linspace(0.80, 0.90, 12)
ramp_factor = np.array([monthly_ramp[m-1] for m in months])

it_load = IT_LOAD_MW * ramp_factor * diurnal_factor
it_load += np.random.normal(0, 0.1, HOURS_PER_YEAR)
it_load = np.clip(it_load, IT_LOAD_MW * 0.75, IT_LOAD_MW)
"""))

cells.append(nbf.v4.new_code_cell("""ambient_temps = np.array([lagos_monthly_temp[m] for m in months])
ambient_temps = ambient_temps + 3 * np.sin(2 * np.pi * (hour_of_day - 14) / 24)

cooling_factor = 0.10 + 0.006 * (ambient_temps - 25)
cooling_factor = np.clip(cooling_factor, 0.08, 0.25)

gross_load_cchp = it_load * (1 + cooling_factor)
gross_load_no_cchp = it_load * PUE_WITHOUT_CCHP / 1.0

load_profile = pd.DataFrame({
    'Hour': hours,
    'Month': months,
    'Hour_of_Day': hour_of_day,
    'Ambient_Temp_C': np.round(ambient_temps, 1),
    'IT_Load_MW': np.round(it_load, 3),
    'Cooling_Load_MW': np.round(it_load * cooling_factor, 3),
    'Gross_Load_CCHP_MW': np.round(gross_load_cchp, 3),
    'Gross_Load_NoCCHP_MW': np.round(gross_load_no_cchp, 3),
})

load_profile.to_csv('../data/section_01_load_profile.csv', index=False)
"""))

cells.append(nbf.v4.new_code_cell("""fig, axes = plt.subplots(1, 2, figsize=(16, 6))

# Load Duration Curve
ax = axes[0]
sorted_it = np.sort(load_profile['IT_Load_MW'].values)[::-1]
sorted_gross = np.sort(load_profile['Gross_Load_CCHP_MW'].values)[::-1]
hours_axis = np.arange(1, HOURS_PER_YEAR + 1)

ax.fill_between(hours_axis, sorted_gross, alpha=0.3, color=COLORS['accent'], label='Cooling + Aux (CCHP)')
ax.fill_between(hours_axis, sorted_it, alpha=0.5, color=COLORS['primary'], label='IT Load')
ax.axhline(y=18, color=COLORS['warning'], linestyle='--', alpha=0.7, label='Installed Capacity (18 MW)')
ax.set_xlabel('Hours/Year (sorted by load)')
ax.set_ylabel('Load (MW)')
ax.set_title('Load Duration Curve (Year 1)', fontweight='bold')
ax.legend(fontsize=9)
ax.set_xlim(0, HOURS_PER_YEAR)

# Typical Day Profile
ax = axes[1]
hourly_avg = load_profile.groupby('Hour_of_Day').agg({'IT_Load_MW': 'mean', 'Gross_Load_CCHP_MW': 'mean'}).reset_index()

ax.fill_between(hourly_avg['Hour_of_Day'], hourly_avg['Gross_Load_CCHP_MW'], alpha=0.3, color=COLORS['accent'])
ax.plot(hourly_avg['Hour_of_Day'], hourly_avg['IT_Load_MW'], linewidth=2.5, color=COLORS['primary'], label='IT Load')
ax.plot(hourly_avg['Hour_of_Day'], hourly_avg['Gross_Load_CCHP_MW'], linewidth=2, color=COLORS['accent'], linestyle='--', label='Gross (with CCHP)')
ax.axhline(y=IT_LOAD_MW, color=COLORS['neutral'], linestyle=':', alpha=0.5, label='Design Capacity')

ax.set_xlabel('Hour of Day')
ax.set_ylabel('Load (MW)')
ax.set_title('Typical Day Load Profile', fontweight='bold')
ax.set_xticks(range(0, 24, 3))
ax.legend(fontsize=9)
ax.set_xlim(0, 23)

plt.tight_layout()
plt.savefig('../outputs/figures/01_load_profile_analysis.png', dpi=300)
plt.close()
"""))

cells.append(nbf.v4.new_code_cell("""ramp_years = pd.DataFrame({
    'Year': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Avg_IT_Utilization': [0.85, 0.90, 0.95, 0.95, 0.95, 0.95, 0.95, 0.95, 0.95, 0.95]
})

ramp_years['IT_Load_MW'] = IT_LOAD_MW * ramp_years['Avg_IT_Utilization']
ramp_years['Gross_Load_MW'] = ramp_years['IT_Load_MW'] * PUE_WITH_CCHP
ramp_years['Annual_Generation_MWh'] = ramp_years['Gross_Load_MW'] * HOURS_PER_YEAR
ramp_years['Capacity_Factor'] = ramp_years['Gross_Load_MW'] / 18.0

ramp_years.to_csv('../data/section_01_ramp_projection.csv', index=False)
"""))

cells.append(nbf.v4.new_markdown_cell("""## 1.5 Value Proposition

The concept addresses key challenges in the regional data center market:
* **Cost Efficiency**: Establishing power access at approximately $0.016/kWh fuel cost, significantly below the $0.25-0.35/kWh diesel baseline.
* **Reliability**: A Tier III design (99.982% uptime) supported by N+1 reciprocating gas engines and local gas infrastructure.
* **Cooling Optimization**: Targeted PUE of 1.18 through combined cooling, heat, and power (CCHP) technology.
"""))

cells.append(nbf.v4.new_code_cell("""market_summary = {
    'design_parameters': {
        'it_load_mw': 15.0,
        'pue_with_cchp': 1.18,
        'pue_without_cchp': 1.40,
        'installed_capacity_mw': 18.0,
        'target_tier': 'Tier III (99.982% availability)'
    },
    'market_context': {
        'africa_dc_capacity_2026_mw': 600,
        'africa_dc_capacity_2030_mw': 1400,
        'nigeria_internet_users_m': 110,
        'nigeria_population_m': 230
    },
    'gas_economics': {
        'nigeria_regulated_price_usd_mmbtu': 2.18,
        'diesel_comparison_usd_kwh': 0.30
    }
}

with open('../data/section_01_market_summary.json', 'w') as f:
    json.dump(market_summary, f, indent=2)
"""))

nb.cells = cells
output_path = r"c:\Users\Jinxxx\Desktop\Hussaini\SPE Africa Energython\build_notebook_01_v2.py"
with open(output_path, 'w', encoding='utf-8') as f:
    f.write("import nbformat as nbf\nimport os\n")
    f.write("nb = nbf.v4.new_notebook()\n")
    f.write("nb.metadata.update({'kernelspec': {'display_name': 'Python 3', 'language': 'python', 'name': 'python3'}, 'language_info': {'name': 'python', 'version': '3.12.10'}})\n")
    f.write("cells = []\n")
    # Instead of writing a complex script via write_to_file, I will write the nbformat creation logic directly.
