To understand how to measure the efficiency of a distributed system, let’s
assume we have an operation that runs in a distributed manner and delivers a
set of items as result. Two standard measures of its efficiency are the
response time (or latency) that denotes the delay to obtain the first item and
the throughput (or bandwidth) which denotes the number of items delivered in a
given time unit (e.g., a second). The two measures correspond to the following
unit costs:

Number of messages globally sent by the nodes of the system regardless of the
message size. Size of messages representing the volume of data exchanges. The
complexity of operations supported by distributed data structures (e.g.,
searching for a specific key in a distributed index) can be characterized as a
function of one of these cost units. Generally speaking, the analysis of a
distributed structure in terms of ‘number of messages’ is over-simplistic. It
ignores the impact of many aspects, including the network topology, the network
load, and its variation, the possible heterogeneity of the software and
hardware components involved in data processing and routing, etc. However, it
is quite difficult to develop a precise cost model that would accurately take
into account all these performance factors; therefore, we have to live with
rough but robust estimates of the system behavior.
