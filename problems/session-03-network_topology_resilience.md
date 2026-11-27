# Session 3: NTN network topology under stress

## Purpose

Practice choosing a network topology for a non-terrestrial network (NTN) and then adapting it when conditions change. There is no single correct answer: a good proposal connects the scenario's priorities to where traffic enters the network, how it crosses space, where it lands on the ground, and what happens when something breaks.

## Activity

Work in teams of 2 to 3. Pick one scenario below and one stress event assigned by your instructor (or choose one yourselves). Answer the questions in order; record your assumptions and calculations. Use the reference values below where needed, selecting one value rather than an entire range.

This activity will help you practice the following skills:
- **Network design:** Choose a topology and justify it based on traffic demand, capacity, and latency.
- **Resilience analysis:** Identify how a stress event affects the network and propose a solution to maintain service.
- **Capacity planning:** Calculate link utilization and identify potential bottlenecks.

## Phase 1: Nominal design (before the event)

1. **Calculate demand.** How much traffic must the network carry in the busy hour? Multiply the number of users by the active fraction, if given, and by the rate per active user. Express the result in Gbps. If the scenario already gives traffic per user in the busy hour, do not apply another activity factor.
2. **Choose a path.** Which orbit and which space-segment strategy will you use, and why?
   - **Bent pipe:** the satellite relays traffic to a gateway it can see.
   - **ISL mesh:** satellites route traffic over inter-satellite links (ISLs) to a satellite that can see a gateway.
   - **Hybrid:** use direct gateway links where possible and ISLs for other traffic or as a fallback.
3. **Draw the topology.** Draw users, at least one satellite, gateway(s), the core/point of presence (PoP), and the destination. Mark the normal path with arrows. How many gateways do you need, where are they, and which satellites can see them? If using ISLs, draw them too. For this exercise, state your visibility assumptions; you do not need to calculate orbits.
4. **Check capacity.** Pick capacities from the tables and state how traffic is distributed. For the busiest beam and each link on the normal path, calculate:

   **load / capacity x 100 = utilization (%)**

   Include the satellite-to-gateway feeder, any ISL, and gateway-to-core link. If the scenario does not specify the busiest beam's share, assume one and explain it. Which link is most utilized? If a link exceeds 70-80%, consider adding capacity or changing the design. This is a planning target, not a hard limit.
5. **Estimate delay.** Use the orbit delay table for a direct user-satellite-gateway path and add a round trip over the assumed terrestrial distance. Add ISL propagation and processing for each hop, counting both directions. State distances and assumptions; this is an estimate, not a guarantee.

## Phase 2: One stress event

1. **Locate the disruption.** What fails, degrades, or receives more traffic? Mark it on your sketch. For a surge, state how much demand is in the affected beam(s); do not automatically multiply the entire region's demand. For a partial degradation, assume and state the remaining capacity.
2. **Check the original path.** Recalculate the load and utilization of the affected link or node. Can it still carry its traffic? Which other links may be affected? If a link or node is unavailable, identify the traffic that loses its path rather than dividing by zero.
3. **Find an alternative.** Draw a new path around the disruption, if one exists. Can the satellites see the proposed gateway, and are the needed ISLs and ground paths available? If no path exists (for example, because the core is unreachable), say which services remain reachable and which do not.
4. **Check the revised path.** Calculate the load and utilization of the alternative links, including any traffic already using them. Can they carry the combined load? Estimate the change in round-trip delay from the added or removed path segments. If there is not enough capacity, how much traffic can be served and which services should be prioritized?
5. **Compare and improve.** What changed for users in capacity, delay, or availability? What extra resource or topology change would improve resilience, and what cost or trade-off would it introduce?

**Stress events** (apply to your chosen scenario):

| # | Event | What changes |
|---|-------|--------------|
| A | **Traffic surge** | Demand rises 3x in the busiest beam(s), e.g. evening peak, news event, festival. |
| B | **Gateway failure or degradation** | The main gateway is lost or its feeder capacity is reduced (power, fibre cut, storm/rain fade, cyber incident). |
| C | **ISL failure or congestion** | A cross-plane ISL fails, or one ISL path carries more than it can. |
| D | **Satellite loss** | One satellite is out of service in the area; neighbours must cover it. |
| E | **Core/PoP outage** | The terrestrial core is unreachable; only local or regional services can continue. |
| F | **Combined** | A surge (A) happens while a gateway is down (B). |

## Phase 3: Justification

Prepare a short statement using your answers:

> Our nominal topology is ___ with ___ gateways because ___. It carries ___ Gbps, and its most utilized link is ___ at ___%. When ___ happened, ___ was affected. We [rerouted via ___ / could not reroute because ___]; the revised path carries ___ Gbps with ___ as its most utilized link. Users experience ___. To improve resilience we would ___, at the cost of ___.

## Scenarios

Each scenario lists key traffic assumptions you may use.

### 1. Remote region broadband (rural/remote communities)
- Region of about 500 km radius, 20,000 households, mostly asynchronous and web use.
- Busy-hour demand: about 2 Mbps per active household, 10% active simultaneously.
- Nearest suitable gateway sites are far away and few.

### 2. Maritime corridor
- 400 ships along a 2,000 km sea route, each with 20 Mbps average busy-hour demand.
- Demand moves with the ships; a single gateway on land may be 1,000+ km away.

### 3. Regional disaster communications
- 5,000 terminals spread across a large region, each 64 kbps average (voice, messaging, low-rate data).
- Local terrestrial gateways may be damaged; priority traffic must survive.

### 4. Polar research stations
- 10 stations at high latitude, each 5 Mbps average.
- Few or no gateway sites in the polar region; GEO coverage is poor.

### 5. Connected aircraft on oceanic routes
- 300 aircraft over an ocean, each 50 Mbps average busy-hour (shared by passengers).
- No gateways under the route; traffic has to be hauled to a coastal gateway.

### 6. Major event
- 50,000 attendees in a 5 km area, 5% active at 5 Mbps each, for 3 days.
- A temporary gateway is on site or nearby; Internet backhaul is the constraint.

### 7. Direct-to-device messaging service
- 1 million subscribers in a large region, 1% active in the busy hour, 10 kbps each for text and low-rate data.
- Satellite beams are very large and coverage is shared with a terrestrial Mobile Network Operator (MNO) core.

## Reference values (typical, order of magnitude)

Use these as starting points. Values can vary a lot by system, frequency band, and year. If you use other values or do not find the ones you need, make an assumption and justify them.

### User link (service link)

| Item | Typical value |
|------|---------------|
| GEO High Throughput satellite (HTS) total throughput | 100-500 Gbps (very high throughput up to about 1 Tbps) |
| GEO spot beam (Ka) | 1-5 Gbps per beam, 100-200+ beams; about 0.5 deg beam, 200-500 km diameter |
| MEO (about 8,000 km) satellite | 10-50 Gbps per satellite; tens of beams |
| LEO (about 500-600 km) satellite | 15-100 Gbps per satellite; 16-48 beams, 20-50 km beam footprint (Ku/Ka) |
| LEO beam peak capacity | 0.3-1.5 Gbps per beam, shared by all users in the cell |
| User terminal (flat panel/VSAT) | 50-500 Mbps down, 10-50 Mbps up (LEO); 10-100 Mbps down (GEO) |
| Aircraft / maritime terminal | 100-350 Mbps down per terminal |
| Handheld / IoT | 1-100 kbps (narrowband); direct-to-device LEO beams about 1-20 Mbps total per beam |

### Feeder links (satellite to gateway)

| Item | Typical value |
|------|---------------|
| Per feeder link (LEO, Ka) | 5-20 Gbps |
| Per gateway site (LEO) | 20-100 Gbps aggregate |
| Per GEO gateway | 10-50 Gbps in HTS systems with several gateways |
| Gateway visibility (LEO, 25 deg elevation) | Radius of about 1,000 km; pass duration of 3-10 min per satellite |

### Inter-satellite links (ISL)

| Item | Typical value |
|------|---------------|
| Optical ISL (LEO, intra-plane) | 10-200 Gbps per link, 4-5 links per satellite typical; range up to 5,000+ km |
| Optical ISL (cross-plane) | 10-100 Gbps; needs tracking, can degrade near the poles |
| RF ISL (Ka/V band) | 0.1-5 Gbps per link |
| Constellation aggregate across a region | multiple Tbps total, but 100s of Gbps in one path |
| Propagation delay (vacuum) | 3.3 ms per 1,000 km, i.e. faster than fibre (about 5 ms per 1,000 km) |
| Onboard processing delay | about 0.1-1 ms per hop (switching, queueing) |
| Per-ISL hop distance (LEO, 550 km, 72 planes) | about 1,000-4,000 km |

### Orbit delays (round-trip propagation, user to satellite to gateway and back, bent pipe)

| Orbit | Approximate RTT contribution |
|-------|--------------------------|
| LEO (500-600 km) | about 5 ms |
| MEO (8,000 km) | at least about 50 ms |
| GEO (35,786 km) | at least about 240 ms |

These are propagation estimates for four satellite-to-ground legs; actual slant ranges, processing, queueing and terrestrial paths add delay.

### Ground and backhaul

| Item | Typical value |
|------|---------------|
| Gateway to core/PoP link | 10-400 Gbps fibre (per site); redundant paths in good designs |
| Terrestrial fibre latency | about 5 ms per 1,000 km |
| Gateway power and teleport availability | 99.9-99.99% with redundancy |
| Core/PoP processing | Several Tbps; usually not the first bottleneck |
| Mobile-network backhaul for Device-to-Device (D2D) | 1-10 Gbps per site |

### Rules of thumb

- Aggregate busy-hour demand = (subscribers x % active x rate per active user).
- Per-beam load is the sum of the busy-hour traffic assigned to that beam. If demand already includes the active fraction, do not divide it by an overbooking factor again.
- A satellite's feeder capacity should be at least equal to the traffic that it carries in bent-pipe mode. With ISLs, the egress gateway must absorb traffic from many satellites.
- For an ISL hop, calculate propagation from its length in each direction and add processing in each direction; do not forget the ground leg. A reroute can also change the satellite-to-ground distance.
- Losing a gateway moves its traffic to the next gateway. Check the extra distance, delay, ISL load, and gateway headroom (aim for N+1).
