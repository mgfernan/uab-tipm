# Practice 2: Radio design and dimensioning

## Purpose

Use the service definition from Practice 1 to make a first radio design that can plausibly meet the coverage and capacity targets. A group may design a TN, NTN, or hybrid system. State assumptions and use order-of-magnitude estimates where detailed propagation or constellation data is unavailable.

## Inputs from Practice 1

Bring the target footprint, user/device density, busy-hour demand, traffic classes, mobility conditions, and must-have QoS targets. Do not silently change these values: record any revised assumption and why it changed.

## Group discussion script

### 1. Which access platform fits the scenario?

1. Is the proposed access terrestrial, satellite, aerial, or a combination? Which segment serves each part of the footprint?
2. For NTN, which platform class and orbit family (LEO, MEO, GEO, or HAPS) are candidates? What service property makes each plausible?
3. Which matters most to this project: propagation delay, footprint, terminal complexity, capacity, availability, or deployment reach?
4. For a terrestrial segment, what site spacing, terrain, and backhaul availability are plausible?
5. What does the end-user terminal need to see or support? Is a fixed directional terminal acceptable, or must it work while handheld/mobile?
6. Which option can be eliminated early, and what requirement rules it out?

**Record:** candidate platform(s), one rejected option, and the service requirement behind the selection.

### 2. What coverage must the radio layer provide?

1. What is the service area or route length, and how much of it must be covered at once?
2. What minimum elevation angle, cell edge, or indoor/obstructed condition should the design support?
3. For NTN, what slant-range or footprint assumptions are appropriate for the selected orbit and elevation angle?
4. For TN, what cell radius or inter-site distance is plausible for the selected environment and frequency range?
5. How many simultaneous beams, cells, or radio nodes are needed to cover the area? Show the simple geometry or area estimate used.
6. Does the coverage calculation account for overlap needed for handover or resilience?
7. Which locations are coverage-limited even before capacity is considered?

**Record:** coverage geometry, node/beam count estimate, and any overlap or edge-coverage assumption.

### 3. How much traffic must the radio layer carry?

1. From Practice 1, how many devices/users are active in the busy hour?
2. What is the offered uplink and downlink traffic per active user/device? Are the two directions different?
3. What is the aggregate busy-hour throughput for the whole system and per cell/beam?
4. How much additional capacity is needed for burstiness, protocol overhead, retransmissions, and growth?
5. What oversubscription or contention can users tolerate? When is it likely that everyone is active together?
6. Is capacity shared across a footprint or dedicated to individual cells/beams? How does this change a user’s experience?
7. Which is the bottleneck: total spectrum, spectral efficiency, number of beams/cells, or feeder/backhaul capacity?

**Record:** a short calculation from users × activity × per-user rate to busy-hour cell/beam demand, with a stated headroom factor.

### 4. What spectrum and radio resources are plausible?

1. What candidate band(s) suit the access link and the environment? What propagation, antenna, licensing, and terminal implications follow?
2. What bandwidth is available or assumed in each direction? Is the service paired, unpaired, or time-shared?
3. What spectral efficiency is a defensible planning assumption for the link conditions and service? What modulation/coding is using?
4. Using capacity ≈ bandwidth × spectral efficiency (and any reuse/sharing factor), can the candidate bandwidth carry the estimated demand?
5. How many carriers or channels would be required per cell/beam? Is frequency reuse possible, and what interference assumption does it imply?
6. What multiple-access strategy shares radio resources among users, and what trade-off does it make between efficiency, fairness, and latency?
7. Does the estimated bandwidth exceed what is available or plausible? Which design variable could be changed first?

**Record:** candidate band, bandwidth, spectral-efficiency assumption, simple capacity check, and resource-sharing approach.

### 5. Can the radio link close?

For at least one representative link (choose the most challenging uplink or downlink), assemble a simplified link budget.

1. Which endpoint transmits, and which direction is being checked?
2. What are the transmit power, antenna gains, frequency, and representative slant range or cell-edge distance?
3. What free-space path loss follows from frequency and distance?
4. Which additional losses matter (atmosphere/rain, polarization, pointing, body/vehicle blockage, feeder, implementation, or clutter)?
5. What received power or carrier-to-noise/interference ratio results?
6. What threshold is needed for the selected service/modulation assumption, and what margin remains?
7. Is the uplink or downlink harder? Which endpoint constraint drives the answer?
8. If the link does not close, what specific design change could help: antenna gain, power, bandwidth, coding, lower frequency, shorter range, or relaxed service target?

**Record:** the link-budget assumptions, result, margin, and the consequence for terminal or infrastructure design.

### 6. Does latency and mobility fit?

1. Break the end-to-end target into radio access, propagation, processing, transport, and core/application contributions.
2. For NTN, what propagation delay follows from the selected orbit and approximate path length? Does one-way versus round-trip interpretation matter?
3. For TN, what are the likely access and transport contributions, and where are the endpoints measured?
4. How much latency budget is left for retransmission, scheduling, handover, and the rest of the network?
5. How often will a moving user change cell or beam? What interruption or handover rate is acceptable?
6. Does the design need fixed, quasi-fixed, or moving beams? What does beam movement imply for tracking and handover?
7. If the latency target is infeasible, can the application tolerate a different interaction pattern or local processing?

**Record:** a latency budget and the mobility/beam assumptions that affect continuity.

### 7. What is the coverage–capacity compromise?

1. Does the proposed cell/beam cover a large low-density area or a smaller high-demand area?
2. What happens to per-user capacity if one wide-area beam/cell serves more users?
3. Could more/smaller cells or beams relieve congestion? What added cost, handover, interference, or power would result?
4. Which locations need a different strategy from the rest (hotspot offload, terrestrial densification, gateway/beam placement, or service tiering)?
5. What is the first performance failure expected as demand grows: edge coverage, busy-hour capacity, or link margin?

## Practice 2 decision sheet

- Selected platform and orbit/radio assumptions, with at least one rejected candidate.
- Coverage estimate and number of nodes, cells, or beams.
- Busy-hour traffic calculation and capacity headroom.
- Band, bandwidth, spectral-efficiency assumption, and capacity check.
- Representative link budget and link margin.
- Latency budget and mobility/beam strategy.
- Main coverage–capacity trade-off and open questions for transport design.

## Where to revisit

Platform types and orbits, footprint geometry, beams and handover, cell sizing, spectrum and waveforms, spectral efficiency, multiple access, link budget, latency and slant range, and coverage versus densification in Session 2.
