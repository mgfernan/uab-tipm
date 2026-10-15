# Practice 1: Define the service and its requirements

## Purpose

Turn a broad connectivity idea into a service definition that can be checked by the later radio, transport, and feasibility practices. The group may choose a terrestrial network (TN), a non-terrestrial network (NTN), or a hybrid TN–NTN design. Do not choose technology first: begin with users, context, and the problem to solve.

## Group discussion script

Discuss the questions in order. Write down assumptions when evidence is unavailable, and distinguish facts from guesses. Every numerical target should have a unit, a measurement point, and a time or geographic scope.

### 1. What problem are we solving?

1. Who experiences the connectivity problem? Name a user group or operational role, rather than “everyone.”
2. Where and when does the problem occur? Describe the places, time periods, and whether users or endpoints move.
3. What do users do today when connectivity is absent or poor? What fails, slows down, or costs more?
4. Is the gap caused by no coverage, insufficient capacity, unreliable service, mobility, resilience needs, or a combination?
5. What is the consequence of service interruption? Is the service safety-critical, business-critical, or best-effort?
6. What would count as a useful improvement from the user’s point of view?

**Record:** one sentence describing the problem, the affected users, and the consequence of leaving it unsolved.

### 2. What service will the group provide?

1. What application or communication service is being delivered (for example, broadband access, telemetry, voice, messaging, or emergency connectivity)?
2. Is the network carrying user-to-user traffic, user-to-cloud traffic, machine telemetry, or several classes?
3. What does one user or device send and receive? Estimate typical and peak data rate, message size, and session frequency.
4. How many users/devices are registered, and how many are active at the same time?
5. Which traffic is uplink-heavy, downlink-heavy, symmetric, periodic, or bursty?
6. Does the application tolerate buffering, retransmissions, or delayed delivery? Which traffic needs interactive response?
7. What existing service or network could complement the proposed service?

**Record:** service description, endpoint types, traffic direction, and at least two traffic classes if their needs differ.

### 3. What is the deployment scenario?

1. Which scenario best describes the service: urban, rural, industrial, mobility, remote, maritime, aeronautical, or a combination?
2. What is the geographic footprint? Give an approximate area, route, or set of locations.
3. How many users/devices are expected per site, square kilometre, vehicle, vessel, or other useful unit?
4. Where are the busiest locations and busiest periods? What is the expected peak-to-average demand ratio?
5. Are there obstructions, terrain, indoor locations, weather exposure, or access constraints that affect connectivity?
6. Does demand move over time or across the footprint? At what speed or frequency?
7. Is existing terrestrial coverage available? If so, where does it meet or fail the service need?

**Record:** a small scenario table with location/segment, user density, mobility, existing coverage, and peak-demand notes.

### 4. Should the design use TN, NTN, or both?

1. Which parts of the footprint can a terrestrial network serve? Which parts are uncovered, difficult to reach, or vulnerable to a single terrestrial failure?
2. What specific gap would NTN fill: ubiquity, continuity, scalability, resilience, or another stated need?
3. Could a TN-only design satisfy the same service requirements? What would it require in sites, backhaul, or deployment time?
4. Could an NTN-only design meet the demand in dense areas, or would capacity and shared-beam loading become limiting?
5. In a hybrid design, where does traffic switch between TN and NTN? Is NTN a primary access, an extension, or a fallback?
6. What does the user equipment need to support the chosen access (fixed terminal, handheld device, antenna, dual connectivity, or gateway)?
7. Which assumptions about satellite, aerial, or terrestrial infrastructure are outside the group’s control?

**Record:** selected network scope (TN / NTN / hybrid), the role of each segment, and the strongest reason for that choice.

### 5. What level of service is required?

For each traffic class, discuss and fill the table. If the group cannot defend an exact number yet, provide a range and explain what would determine it.

| Requirement | Discussion prompt | Group target |
|---|---|---|
| Coverage | Which locations, route segments, altitude/indoor conditions, and population must be served? | |
| Downlink rate | What rate does one active user need, and what is the aggregate busy-hour demand? | |
| Uplink rate | What rate do users/devices need to send, and how many transmit concurrently? | |
| Latency | Is the application interactive? Specify one-way or round-trip and the measurement endpoints. | |
| Availability | What fraction of time must the service work, over what interval and area? | |
| Reliability | What is the consequence of a failed packet/session, and is a target needed? | |
| Mobility/continuity | What speeds, handovers, and interruption times are acceptable? | |
| Capacity | What busy-hour load and growth must the system support? | |
| Security/privacy | What data or access controls matter to users or operators? | |

1. Which metric directly affects the application, and which is only a network proxy?
2. Are the targets per user, per cell/beam, per site, or end-to-end?
3. Is a percentile needed (for example, a latency bound for most transactions) instead of an average?
4. What happens if a target is missed: degraded operation, delayed delivery, or service failure?

### 6. Which requirements are essential?

1. Which requirements are mandatory for the service to be useful or safe?
2. Which are desirable but could be relaxed to lower cost or complexity?
3. Are any requirements in conflict—for example, low latency versus wide coverage, high capacity versus low terminal cost, or availability versus energy use?
4. If one target must be relaxed, which can move first, and what consequence is acceptable?
5. What is the minimum viable service for a first deployment?

**Record:** mark each requirement as **must**, **should**, or **could**, with a short justification and an acceptance check.

### 7. What do we still not know?

1. Which assumptions most strongly affect demand or the service targets?
2. What evidence could validate each assumption (operator data, user survey, public coverage map, application measurements, or a reference design)?
3. Which unknown must be resolved before radio dimensioning, and which can remain a sensitivity range?
4. What result in the next practice would make the group reconsider its service definition?

## Practice 1 decision sheet

Before moving on, the group should be able to hand over:

- A concise problem and service statement.
- The chosen TN, NTN, or hybrid scope and why it is needed.
- A scenario/footprint description and a first demand estimate.
- A table of measurable QoS/KPI targets, with units and scope.
- Must/should/could priorities and unresolved assumptions.

## Where to revisit

NTN use cases, demand models and user density, service classes, traffic and QoS, capacity/latency/availability KPIs, deployment scenarios, and requirement definition in Session 1.
