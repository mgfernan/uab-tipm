# Deployment strategies


## Deployment decisions

This activity aims at defining several deployment decisions based on several scenarios.

Activity flow:

1. Several discussion **groups** will be formed
2. Each group will be assigned a certain **scenario**
3. Task: choose multiple **decision options** among the ones listed below
4. Place the selected decision option cards in the order in which you would deploy them
5. Be prepared to answer:
   1. What is the reason behind your first decision option?
   2. What bottleneck does each decision address?
6. Each group will be given an event card (listed below)
7. How this event would disrupt your decision?
8. Would you reorder your deployment sequence? Explain why.

### Scenarios

| Group | Scenario                            | Likely pressure                  |
| ----- | ----------------------------------- | -------------------------------- |
| A     | Rural broadband, sparse population  | Coverage / capacity              |
| B     | Maritime connectivity               | No terrestrial network           |
| C     | Dense urban NTN                     | Spectrum / terrestrial offload   |
| D     | Disaster response                   | Rapid deployment / resilience    |
| E     | Global IoT network                  | Coverage / terminal cost         |
| F     | High-latency-sensitive applications | Connectivity architecture / ISLs |


### Decision options

```mermaid
flowchart TB

    subgraph ROW1[" "]
        direction LR
        A["🛰️<br/><b>LAUNCH MORE<br/>SATELLITES</b><br/><small>Space capacity</small>"]
        B["📡<br/><b>ADD<br/>GATEWAYS</b><br/><small>Ground capacity</small>"]
        C["📶<br/><b>ADD<br/>SPECTRUM</b><br/><small>Radio resources</small>"]
    end

    subgraph ROW2[" "]
        direction LR
        D["📱<br/><b>IMPROVE USER<br/>TERMINALS</b><br/><small>Link performance</small>"]
        E["🔗<br/><b>DEPLOY<br/>ISLs</b><br/><small>Satellite connectivity</small>"]
        F["🗼<br/><b>OFFLOAD TO<br/>TERRESTRIAL</b><br/><small>Terrestrial 5G</small>"]
    end

    classDef card fill:#ffffff,stroke:#333333,stroke-width:2px,color:#222;
    class A,B,C,D,E,F card;

    style ROW1 fill:none,stroke:none
    style ROW2 fill:none,stroke:none
```

### Event cards

```mermaid
flowchart TB

    subgraph ROW1[" "]
        direction LR
        A["📈<br/><b>DEMAND EXPLODES</b><br/><small>Traffic becomes 10× higher<br/>than forecast</small>"]
        B["🚀<br/><b>LAUNCHES DELAYED</b><br/><small>New satellites cannot be<br/>deployed for 18 months</small>"]
        C["📶<br/><b>SPECTRUM CONSTRAINED</b><br/><small>No additional spectrum<br/>can be obtained</small>"]
    end

    subgraph ROW2[" "]
        direction LR
        D["🌍<br/><b>TERRESTRIAL EXPANDS</b><br/><small>5G coverage reaches<br/>most target areas</small>"]
        E["⚡<br/><b>MAJOR OUTAGE</b><br/><small>Terrestrial networks fail<br/>across a large region</small>"]
        F["💰<br/><b>BUDGET CUT</b><br/><small>Only 40% of the planned<br/>investment is available</small>"]
    end

    classDef card fill:#ffffff,stroke:#333333,stroke-width:2px,color:#222;
    class A,B,C,D,E,F card;

    style ROW1 fill:none,stroke:none
    style ROW2 fill:none,stroke:none
```