[CERT] freeCodeCamp - Information Security and Quality Assurance
It should be possible to run GRE, L2TP, or VXLAN over WireGuard although such tooling probably doesn't exist yet.
  Sure but it hurts a bit to run a tunnel on top of another tunnel, and since you have to run wireguard as-is, you still have to do the static ip thing. It's a bit insane to have ethernet > udp (l2tp) > ip > udp (wireguard) > ip > ethernet. That's at least 128 bytes overhead per frame (udp/ip: 2*48, l2tp: 4, eth: 14, wireguard: 14).
