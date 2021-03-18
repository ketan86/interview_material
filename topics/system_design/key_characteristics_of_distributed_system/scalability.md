Scalability is the capability of a system, process, or a network to grow and
manage increased demand. Any distributed system that can continuously evolve in
order to support the growing amount of work is considered to be scalable.

A system may have to scale because of many reasons like increased data volume
or increased amount of work, e.g., number of transactions. A scalable system
would like to achieve this scaling without performance loss.

Generally, the performance of a system, although designed (or claimed) to be
scalable, declines with the system size due to the management or environment
cost. For instance, network speed may become slower because machines tend to be
far apart from one another. More generally, some tasks may not be distributed,
either because of their inherent atomic nature or because of some flaw in the
system design. At some point, such tasks would limit the speed-up obtained by
distribution. A scalable architecture avoids this situation and attempts to
balance the load on all the participating nodes evenly.

Horizontal vs. Vertical Scaling: Horizontal scaling means that you scale by
adding more servers into your pool of resources whereas Vertical scaling means
that you scale by adding more power (CPU, RAM, Storage, etc.) to an existing
server.

With horizontal-scaling it is often easier to scale dynamically by adding more
machines into the existing pool; Vertical-scaling is usually limited to the
capacity of a single server and scaling beyond that capacity often involves
downtime and comes with an upper limit.

Good examples of horizontal scaling are Cassandra and MongoDB as they both
provide an easy way to scale horizontally by adding more machines to meet
growing needs. Similarly, a good example of vertical scaling is MySQL as it
allows for an easy way to scale vertically by switching from smaller to bigger
machines. However, this process often involves downtime.

widget Vertical scaling vs. Horizontal scaling
