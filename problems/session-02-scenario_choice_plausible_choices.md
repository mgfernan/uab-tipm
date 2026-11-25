# Session 2: Orbit and beam strategy scenario choice

## Scenario: plausible choices

These are starting points for discussion, not answer keys. Accept other choices when students make a sound case from the stated requirements.

| Scenario | Plausible orbit and beam choice | Reasoning and trade-off |
|---|---|---|
| Remote schools | **GEO + broad beams** | Persistent, wide-area coverage suits a few low-density sites, and asynchronous lessons can tolerate higher delay. The trade-off is higher propagation delay and less capacity per area than targeted spot beams. |
| Busy shipping lane | **LEO + moving/steered spot beams** | Lower propagation delay and moving beams suit a corridor with mobile, concentrated demand. The trade-off is frequent handovers and coordination complexity. |
| Regional disaster communications | **GEO + broad beams** | Persistent regional coverage and fewer handovers suit basic voice, messaging, and coordination across a wide area. The trade-off is higher delay and potentially limited broadband capacity. LEO or a hybrid could be preferable if rapid deployment, high throughput, or low latency becomes the priority. |
| Rural broadband hotspot | **LEO + several smaller spot beams** | Smaller beams can concentrate capacity around the town and support spatial reuse. The trade-off is more complex beam management and less efficient service to the surrounding sparse area. |
| Polar research stations | **LEO with polar coverage + steered beams** | A polar-capable constellation can serve high latitudes and direct resources toward the stations. Continuity depends on constellation design and handovers; MEO or GEO could be argued for if availability and fewer handovers dominate. |
| Connected aircraft | **LEO + moving/steered beams** | Beams can follow aircraft routes and concentrate capacity there, while LEO offers lower delay. The trade-off is frequent handovers and demanding tracking. MEO is a reasonable alternative if fewer handovers matter more than latency. |
| Environmental sensors | **LEO + broad or quasi-fixed beams** | Small, periodic messages do not require highly concentrated capacity, so broad coverage can be suitable. Students may also argue for GEO where persistent coverage matters and delay is unimportant. Consider access efficiency and battery life. |
| Major event | **LEO + several small spot beams** | Capacity can be concentrated over the event and divided among high-demand zones. The trade-off is planning for satellite capacity and beam availability at a specific place and time. A temporary terrestrial system or hybrid is also worth considering. |

## Debrief

- Which requirement most influenced your choice: coverage, capacity, latency, mobility, or continuity?
- What changed when you prioritized a different requirement?
- Which assumption would you check first in a real design?
- Could a hybrid system resolve a trade-off that one orbit and beam strategy cannot?
