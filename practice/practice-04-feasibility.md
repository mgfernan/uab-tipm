# Practice 4: Feasibility, regulation, and deployment

## Purpose

Decide whether the service and architecture developed in Practices 1–3 can be deployed and sustained. Compare at least two credible alternatives, make costs and energy visible, check regulatory dependencies, and propose a staged rollout with measurable decision gates.

## Inputs from Practices 1–3

Bring the service targets and demand forecast, platform/radio design, node/beam and terminal counts, transport/gateway design, expected availability, and remaining technical risks. Keep the alternatives comparable: both should serve the same user need and state where their service levels differ.

## Group discussion script

### 1. What is being compared?

1. What is the baseline design from the previous practices?
2. Which alternative could meet the same need with a different balance of coverage, capacity, delay, resilience, or deployment effort?
3. Are the alternatives TN, NTN, and hybrid variants, different orbits/platforms, shared versus dedicated infrastructure, or different rollout scopes?
4. What service targets are common to both options, and where does one option provide a lower service level?
5. Which assumptions should be held constant to make the comparison fair (demand, timeframe, geography, availability, and terminal ownership)?
6. What evidence would cause the group to switch from the preferred option to the alternative?

**Record:** a comparison table with two or more options and the same scope, horizon, and service assumptions.

### 2. What must be purchased or built?

For each alternative, list cost items and quantities before assigning prices.

1. What access infrastructure is required: sites, antennas, radio units, satellite capacity, terminals, gateways, or spectrum rights?
2. What transport and core changes are required: fiber/backhaul, feeder links, gateways, data-centre capacity, integration, or redundancy?
3. What user equipment must customers or the operator purchase? Who pays, and what is the expected replacement lifetime?
4. What installation, civil works, site acquisition, launch, commissioning, and integration costs apply?
5. Which assets can be reused, leased, shared, or bought as a service? What are the implications for control and availability?
6. Which costs scale mainly with geographic coverage, number of sites/users, capacity, or service lifetime?
7. Which major cost item has the weakest estimate? Use a range and identify the source or rationale.

**Record:** a CAPEX list of quantities × unit cost/range, marking reused, shared, leased, and newly built items.

### 3. What will it cost to operate?

1. What recurring costs arise from sites, power, backhaul, spectrum, satellite capacity, gateway operation, cloud/core, maintenance, and support?
2. Which costs are fixed, and which rise with traffic, users, geography, or number of terminals?
3. How many staff or service partners are needed for monitoring, repair, customer support, and field maintenance?
4. What replacement and refresh cycles should be included over the project lifetime?
5. How do service-level agreements, outages, insurance, or capacity reservations affect recurring cost?
6. What is the estimated total cost of ownership over a stated number of years? Which discount rate or simplifying assumption is used if calculating NPV?
7. What unit-cost measure helps compare options (cost per covered site, active user, GB, connected device, or service hour)?

**Record:** annual OPEX categories, project lifetime, and a simple TCO (or NPV) estimate with assumptions clearly labelled.

### 4. How does demand affect viability?

1. What user adoption or traffic level is needed to justify the fixed infrastructure cost?
2. What are the low, expected, and high demand cases? Which assumptions differ between them?
3. At what load does capacity expansion become necessary, and what is the cost of that expansion?
4. Does revenue or avoided loss scale with users, coverage, data volume, or service tier?
5. What price, funding source, or service contract would cover recurring costs? Who is the payer and who receives the benefit?
6. What is the break-even adoption/load or payback period under the expected case?
7. What happens to unit cost if take-up is half the forecast or traffic doubles?

**Record:** low/base/high scenario table with demand, major cost/revenue outcomes, and the break-even assumption.

### 5. What energy and environmental constraints matter?

1. Which elements consume the most energy: user terminals, radio nodes, gateways, transport, data processing, or satellite operations?
2. Which energy use is always-on and which scales with traffic or active beams/cells?
3. Can sleep modes, adaptive capacity, renewable power, efficient terminals, or shared infrastructure reduce consumption?
4. What service or availability penalty might accompany each energy-saving measure?
5. What is a useful energy metric for this service (kWh/site-year, energy per GB, energy per connected user, or backup duration)?
6. Are sites remote or power-constrained? What backup runtime and maintenance access are needed?
7. What lifecycle impacts matter beyond operational energy (equipment replacement, battery disposal, launches, or construction)?

**Record:** main energy drivers, one reduction measure, its service trade-off, and the metric the group would monitor.

### 6. Can the design legally and operationally use the spectrum and infrastructure?

1. Which service links and frequency bands are proposed (user/access, feeder/backhaul, and any inter-platform links)?
2. Who authorizes or coordinates each band in the deployment jurisdictions? Is the usage licensed, shared, or otherwise constrained?
3. Are there power, antenna, emission, interference, or terminal conditions that could limit the design?
4. Does the service require cross-border coordination, landing rights, earth-station approval, site permits, or aviation/maritime permissions?
5. Who owns or operates the satellites, gateways, spectrum, sites, and user terminals? What agreements are needed?
6. What user-data, privacy, cybersecurity, or lawful-intercept obligations could affect the architecture or supplier choice?
7. Which regulatory assumption is a hard deployment dependency rather than a detail to resolve later?

**Record:** a dependency checklist (authority/permission, responsible party, evidence needed, and status). Do not present an assumed band or permission as confirmed without a source.

### 7. What deployment plan reduces risk?

1. Which limited pilot area or user group would test the riskiest assumptions?
2. What would the pilot measure (coverage, capacity, latency, availability, energy, adoption, or operating cost)?
3. What thresholds would justify expansion, redesign, or stopping?
4. Which locations/users should be served first, and why?
5. What can be shared or reused in the pilot, and what must be built before meaningful results are possible?
6. What is the order of rollout stages, and which investment decision occurs at each stage?
7. What fallback keeps the service useful if a supplier, gateway, spectrum approval, or demand forecast fails?

**Record:** a phased rollout with stage, scope, evidence/exit criteria, investment gate, and contingency.

### 8. Which alternative should the group recommend?

1. Which option best meets mandatory service targets at acceptable lifecycle cost and energy use?
2. Which option has the largest technical, regulatory, supply, or demand risk?
3. What trade-off is the group consciously accepting (for example, lower peak capacity for wider coverage, or higher CAPEX for lower latency)?
4. What sensitivity most changes the recommendation?
5. What must be verified before a real deployment decision?
6. Can the recommendation be stated in one sentence that includes the intended users, network approach, and main limitation?

## Practice 4 decision sheet

- At least two comparable deployment alternatives and a reasoned recommendation.
- CAPEX/OPEX assumptions, lifetime, and a simple TCO/NPV or unit-cost comparison.
- Low/base/high demand sensitivity and break-even driver.
- Main energy drivers and a chosen energy metric.
- Spectrum, licensing, permits, ownership, and operational dependencies requiring verification.
- Phased rollout plan with measurable gates and contingencies.
- Top three risks, each with likelihood/impact reasoning and a mitigation or validation action.

## Where to revisit

CAPEX, OPEX, TCO, NPV, break-even, energy efficiency, regulation and spectrum, deployment strategies, sharing, and coverage trade-offs in Sessions 4–7.
