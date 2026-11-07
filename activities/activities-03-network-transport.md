

## Activity: Link comparison

Ask students to rank the following four candidate links by:

- Expected propagation delay
- Capacity predictability
- Ease of synchronization
- Deployment speed
- Vulnerability to a single physical cut or obstruction

| Candidate | Link description |
|:----------|:-----------------|
| 1 | 15 km fiber link |
| 2 | 30 km microwave link |
| 3 | LEO feeder link |
| 4 | GEO feeder link |

Prompt for discussion:

- Which link is fastest to deploy?
- Which one is most predictable in capacity?
- Which is easiest to synchronize across a network?
- Which is most fragile to a single point of failure?

## Which candidate link usually has the lowest propagation delay?  {.quiz-question}

- [15 km fiber link]{.correct}
- 30 km microwave link
- LEO feeder link
- GEO feeder link

## Which link is most vulnerable to a single physical cut or obstruction? {.quiz-question}

- 15 km fiber link
- 30 km microwave link
- [LEO feeder link]{.correct}
- GEO feeder link

> Discuss: a long terrestrial path has a single point of failure, but a satellite path also depends on the satellite/gateway geometry and network routing.

## Which option is usually the fastest to deploy in a remote site? {.quiz-question}

- [LEO feeder link]{.correct}
- 15 km fiber link
- 30 km microwave link
- GEO feeder link

## Which link is most predictable in capacity? {.quiz-question}

- 15 km fiber link {data-explanation= "Fiber links are usually more predictable than satellite links, which depend on geometry and weather conditions."}
- [30 km microwave link]{.correct data-explanation= "Microwave links are usually more predictable than satellite links, which depend on geometry and weather conditions."}
- LEO feeder link {data-explanation= "Satellite links are usually less predictable than terrestrial links, which depend on geometry and weather conditions."}
- GEO feeder link



## Gateway and ISL subscription

choose the preferred route for each application.

| Application        | Preferred route                                                           | Reason                                         |
| ------------------ | ------------------------------------------------------------------------- | ---------------------------------------------- |
| Voice              | Usually the lower-delay route, provided loss and jitter remain acceptable | Sensitive to RTT, jitter, and queueing         |
| Bulk file transfer | Route with greater residual capacity                                      | Less sensitive to propagation delay            |
| Web browsing       | Depends on RTT, congestion, and retransmissions                           | Interactive but usually less strict than voice |
| Critical control   | Most reliable route, possibly with duplication                            | Continuity is more important than efficiency   |


