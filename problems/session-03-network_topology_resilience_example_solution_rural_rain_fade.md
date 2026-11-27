# Session 3: Example solution (rural broadband, gateway rain fade)

This is one possible instructor solution to [the guided activity](./session-03-network_topology_resilience.md). The rain-fade example is now **event B** (gateway failure or degradation); event C in the current activity is an ISL failure. The capacities and geometry below are illustrative assumptions, not a design for a specific constellation.

## Phase 1: Nominal design

### 1. Calculate demand

20,000 households x 10% active x 2 Mbps = **4,000 Mbps = 4 Gbps** in the busy hour. The active fraction is already included; do not apply overbooking again.

Assume the busiest beam covers 2,000 of these households, with the same active fraction. Its load is 2,000 x 10% x 2 Mbps = **0.4 Gbps**. The other beams carry the remaining 3.6 Gbps.

### 2. Choose a path

Choose **LEO with a hybrid topology**: use a direct feeder when a suitable gateway is visible and an ISL to reach a second gateway otherwise. This provides a backup path while keeping some traffic on a direct path.

### 3. Draw the topology

```text
Users -- beams --> S1 -- feeder --> G1 -- fibre --> Core/PoP --> Internet
                   |
                   +-- ISL --> S2 -- feeder --> G2 -- fibre --> Core/PoP
```

- Assume the households are concentrated in cells that S1 can serve with its available beams, and S1 can see G1; S2 can see G2. An optical ISL connects S1 and S2. For simplicity, assume these paths remain available, including through satellite handovers, during the event.
- G1 and G2 are geographically separated to reduce the chance of a shared storm, though this does not guarantee independent weather.
- Both gateways have working paths to the core. In the nominal state, **60%** of traffic (2.4 Gbps) uses G1 and **40%** (1.6 Gbps) uses S2 and G2.
- For a tractable calculation, assume all traffic to each gateway passes through one feeder link; both satellites and the beams have sufficient capacity. A real network would need to verify visibility, handovers, beam coverage, and per-satellite traffic.

### 4. Check capacity

Select a 1 Gbps capacity for the busiest beam, 10 Gbps per feeder, 10 Gbps for the ISL, and 10 Gbps for each gateway-to-core link. Assume S1 and S2 can each handle at least 20 Gbps of the indicated traffic.

| Resource | Nominal load | Capacity | Utilization |
|----------|--------------|----------|-------------|
| Busiest beam | 0.4 Gbps | 1 Gbps | 40% |
| S1 traffic | 4 Gbps | 20 Gbps | 20% |
| G1 feeder and G1-to-core fibre | 2.4 Gbps each | 10 Gbps each | 24% |
| S1-S2 ISL, G2 feeder and G2-to-core fibre | 1.6 Gbps each | 10 Gbps each | 16% |
| S2 relayed traffic | 1.6 Gbps | 20 Gbps | 8% |

The **busiest beam** has the highest utilization, 40%. All resources are below the 70-80% planning target.

### 5. Estimate delay

Assume each path has 1,000 km of user-to-satellite distance, 1,000 km of satellite-to-gateway distance, and 1,000 km of gateway-to-core fibre. At 3.3 ms per 1,000 km in space and 5 ms per 1,000 km in fibre, the direct-path round trip is:

2 x (3.3 + 3.3 + 5) = **23.2 ms**.

Assume the ISL is 2,000 km long and adds 0.5 ms processing per direction. The G2 path adds 2 x (6.6 + 0.5) = **14.2 ms**, giving **37.4 ms**. These estimates omit other processing and queueing and assume the ground and satellite-to-ground distances are the same for both paths.

## Phase 2: Event B — rain fade at G1

### 6. Locate the disruption

Heavy rain degrades the **G1 feeder link**. For this exercise, assume its capacity falls from 10 Gbps to **2 Gbps** for several hours. The G1-to-core fibre remains operational; G2 and the ISL are unaffected. A specific fade in dB does not by itself determine the remaining capacity, which depends on the link budget and coding.

### 7. Check the original path

The G1 feeder still has 2.4 Gbps offered to it, but only 2 Gbps capacity: 2.4 / 2 x 100 = **120%**. It cannot carry all its traffic; at most 2 Gbps can pass, leaving at least 0.4 Gbps unserved if nothing changes. The G1 fibre remains at 24% offered load and is not the limiting link.

### 8. Find an alternative

Move all 2.4 Gbps from G1 onto the existing path through S2 and G2:

```text
Users -- beams --> S1 -- ISL --> S2 -- feeder --> G2 -- fibre --> Core/PoP --> Internet
```

This works under the visibility and availability assumptions in step 3. In a real constellation the operator must confirm those conditions throughout the outage.

### 9. Check the revised path

G2 already carried 1.6 Gbps. After rerouting, the ISL, G2 feeder and G2 fibre each carry 1.6 + 2.4 = **4 Gbps**, or **40%** of 10 Gbps. S2 handles 4 / 20 = **20%** of its assumed capacity. The busiest beam remains at 40%. All 4 Gbps can therefore be served under these assumptions.

For traffic moved from G1 to G2, the assumed extra ISL adds **14.2 ms RTT**, increasing the estimated RTT from 23.2 to 37.4 ms. Traffic already using G2 has no path change. Actual delay could differ if the alternate feeder or fibre path is longer or congestion adds queueing.

### 10. Compare and improve

The rerouted users retain their busy-hour throughput but have higher estimated latency; a handover may also briefly interrupt them. If G2 or its path cannot carry all 4 Gbps, prioritize voice and interactive services and limit bulk transfers.

A further geographically diverse gateway and independent backhaul could provide another option if G2 is also affected. It adds site, equipment and operating costs and still needs suitable satellite visibility or ISL paths.

## Phase 3: Justification

> Our nominal topology is a hybrid LEO network with two gateways because it offers a direct path and an alternative route. It carries 4 Gbps, and its most utilized link is the busiest beam at 40%. When rain reduced the G1 feeder to 2 Gbps, its offered load reached 120%. We rerouted via S2 and G2; the revised path carries 4 Gbps, with the ISL, G2 feeder and fibre each at 40%. Rerouted users see an estimated 14.2 ms extra RTT and may experience a brief interruption. To improve resilience we would add a geographically diverse gateway and backhaul, at additional cost.
