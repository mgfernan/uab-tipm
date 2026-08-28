# Radio dimensioning

## Platform trade-off sprint

Goal: decide the best orbit-platform option for a service, then defend the FoV and latency consequences.

### Workflow

1. Form groups
2. Each group:
   1. Picks one scenario from the table below
   2. Select one orbit-platform option and one FoV strategy
3. Estimate (qualitative) impacts on coverage, capacity, latency, and handover complexity
4. Be prepared for a 2-minute pitch to defend your choice

### Scenarios

| Group | Service scenario | Priority constraints |
| ----- | ---------------- | -------------------- |
| A | Remote education in rural region | Wide coverage, low cost terminals |
| B | Maritime connectivity corridor | Continuous coverage, moderate throughput |
| C | Dense urban backhaul support | High capacity, spectrum reuse |
| D | Emergency communications after disaster | Fast deployment, resilient coverage |

### Candidate options

| Option | Orbit + platform | Typical FoV behavior | Expected trade-off |
| ------ | ---------------- | -------------------- | ------------------ |
| 1 | GEO HTS | Large visible area, stable geometry | High delay, fewer handovers |
| 2 | MEO constellation | Medium visible area | Balanced delay and constellation size |
| 3 | LEO mega-constellation | Small visible area per satellite | Low delay, frequent handovers |
| 4 | HAPS + NTN complement | Regional footprint, quasi-stationary | Fast local deployment, limited footprint |

### Discussion points

For your assigned scenario, produce:

- One architecture choice: orbit-platform option and why.
- One FoV sketch: approximate footprint and overlap strategy.
- One latency statement: whether target applications are feasible.
- One scaling rule: increase beams, gateways, or satellites first?

You can use this quick decision frame:

- Larger FoV usually reduces satellite count but can reduce per-area capacity.
- Smaller FoV usually improves spatial reuse but increases handover and control complexity.
- Lower altitude usually improves RTT but requires denser constellation management.

### Debrief questions

- Which scenario benefited most from small FoV and why?
- Where can large FoV become a capacity bottleneck?
- Which option is most robust to demand uncertainty?
- What would change first if latency target is cut in half?
