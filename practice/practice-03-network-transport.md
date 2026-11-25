# Practice 3: Transport and end-to-end architecture

## Purpose

Connect the radio design from Practice 2 to the service endpoints. Decide where traffic is aggregated, how it reaches the core or internet, and how the architecture affects latency, capacity, synchronization, and resilience.

## Inputs from Practices 1 and 2

Checklist of topics from previous practice sessions (may be incomplete):

- [ ] Service requirements (Practice 1)
- [ ] Traffic classes, busy-hour traffic estimates, and latency targets (Practice 1)
- [ ] Footprint (service area, coverage, and mobility assumptions) (Practice 1)
- [ ] Radio design (Practice 2)
- [ ] Radio nodes/cells/beams and their characteristics (Practice 2)

**To keep in mind**: If transport changes the service target, write down the change and revisit Practice 1.

## Group discussion script

### 1. Trace the service path

1. Where does user/device traffic enter the network, and where must it arrive (operator core, public internet, enterprise network, cloud application, or another site)?
2. Draw the path hop by hop from endpoint to application. Which elements are access, transport, gateway, aggregation, and core?
3. Where does traffic leave the radio network? Does each radio node/cell/beam have its own path or share an aggregation point?
4. Where are control functions located, and where does user data flow? Does the service need a local breakout or edge compute location?
5. If your application requires an hybrid TN–NTN design, where does traffic transition between the terrestrial and non-terrestrial segments?
6. Which operators own or manage each segment, and where is an interface or service-level agreement needed? Note: as operator, you may not control all segments, so consider how to handle failures or congestion in a partner network.

**Record:** a network sketch and a list of interfaces, gateways, and ownership boundaries.

### 2. Which transport topology fits?

1. Are radio sites connected in a star, ring, mesh, chain, or a hybrid topology? Why does this fit your application’s needs?
2. Which sites should connect directly to a gateway, and which can aggregate through another site?
3. What are the gateway locations, and are they close to traffic demand, terrestrial fiber, cloud/core facilities, or satellite feeder links?
4. For NTN, is the payload transparent (bent-pipe) or regenerative? Where are the gateway and processing functions in each case?
5. Would inter-satellite links (ISLs) or multi-hop transport be needed? What additional routing, delay, and failure dependencies do they create?
6. What is the consequence if a gateway or aggregation link is lost? Is a second path needed, and can traffic actually fail over?
7. Which topology has the fewest single points of failure without adding unjustifiable cost?

**Record:** selected topology, gateway/aggregation locations, and the failure points that need protection.

### 3. How much backhaul or feeder capacity is needed?

1. What is the peak traffic entering each radio node, beam, gateway, and aggregation link?
2. Does transport carry the radio’s peak theoretical rate or only an expected busy-hour load? What oversubscription ratio is acceptable?
3. How do uplink and downlink demand differ? Can the transport link support the required directionality?
4. What protocol overhead, traffic growth, and burst headroom should be added?
5. Are several cells/beams sharing one feeder, gateway, or terrestrial backhaul? Where does aggregation create a bottleneck?
6. What capacity remains after the busiest link or gateway fails?
7. Which links need reserved capacity for control, emergency, or high-priority traffic?

**Record:** a simple traffic table at each aggregation point, including peak estimate, capacity, and oversubscription assumption.

### 4. What delay does transport add?

1. List the transport hops between the radio edge and the service endpoint. What is the propagation distance on each segment?
2. Estimate propagation delay for fiber, microwave, or satellite paths using the distance and medium assumptions.
3. What additional queueing, switching/routing, gateway, and processing delays are expected?
4. Compare the transport contribution with the latency budget from Practice 2. Is there enough budget left for the core and application?
5. Where should the gateway or application be placed to meet the target? Would edge computing materially reduce the path?
6. Is traffic affected by a distant core? Which are the trade-offs of adding a local node to mitigate this error?
7. Which traffic class of your service is most sensitive to jitter or delay variation?

**Record:** an end-to-end path latency estimate, broken into propagation, processing, and queueing contributions.

### 5. How will the architecture maintain continuity?

1. Which failures matter most? If your application requires NTN, consider aspects such as: radio link closure, beam configuration/strategy, feeder link, gateway, terrestrial backhaul, power, or core connection?
2. What redundancy is required for the service’s availability target? Is it geographic, equipment-level, path-level, or a combination?
3. Does the alternate path have enough capacity, compatible routing, and a different failure domain?
4. How long can detection and failover take before the user sees a service interruption?
5. What happens when a moving user changes cell, beam, satellite, gateway, or access type?
6. Can sessions continue across handover or path changes? Which functions must coordinate to do so?
7. What should happen during partial failure: lower rate, queue traffic, switch access, or stop the service?

**Record:** one normal path and one failure/degraded-mode path, with the expected user-visible behavior.

### 6. What synchronization and operations are required?

1. Which network elements need monitoring, configuration, and software updates, and who operates them?
2. What telemetry would reveal congestion, packet loss, excessive delay, or a failed handover?
3. How are addressing, routing, and mobility handled when users move between access networks or gateways?
4. What security boundary exists between user traffic, management traffic, and partner/operator networks?
5. Which operational dependency is most likely to limit availability even if the radio link works?

**Record:** basic operations/monitoring needs, and any operational dependency requiring validation.

### 7. Does the transport design preserve the service targets?

1. Revisit each must-have from Practice 1. Does the complete path meet the target?
2. What is the largest bottleneck under normal operation and during a failure?
3. Is the selected architecture over-provisioned in one segment and under-provisioned in another?
4. Which assumption would most change the architecture if it proved wrong?
5. What design decision is now fixed, and what needs, potentially, a cost or regulation check due to e.g. spectrum allocation (to be revisited in Practice 4)?

**Record:** bottlenecks of the service, architecture limitations, fallback scenarios and potential trade-offs that require further validation.


## Practice 3 decision sheet

- [ ] End-to-end traffic path and network sketch.
- [ ] Transport topology, gateway/aggregation choices, and transparent/regenerative payload assumption if relevant.
- [ ] Capacity estimates at bottleneck links and aggregation points.
- [ ] Latency contribution and remaining service budget.
- [ ] Normal, redundant, and degraded paths with expected recovery behavior.
- [ ] Synchronization, monitoring, and ownership assumptions.
- [ ] Unresolved bottlenecks and decisions to validate for feasibility.

## Related content

Transport architectures and topologies, gateway and ISL trade-offs, aggregation and oversubscription, latency, synchronization, and reliability.
