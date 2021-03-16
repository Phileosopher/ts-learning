FROM BEN BRYAN
  Many folks (especially locals since we have ISPs such as Ting rolling out gigabit in North Idaho) have asked which Firewall or Router to get for Gigabit Internet. Instead of answering the same question over and over, I made this post to link to. Maybe that’s why you’re reading this right now.
  After 20-years in IT, I’ve standardized on five firewall technologies depending on the purpose and environment:
    Simple Router for non-techies: AmpliFi
    Small/Medium Network Routers: EdgeRouter or UniFi Security Gateway
    Scalable: EdgeRouter or UniFi Security Gateway
    Mission Critical or Virtual routers: pfSense or OPNsense
    Large Networks/Enterprise: At this point, we’re beyond my domain of knowledge. It’s best to let the networking engineers do what they’re good at.
  Below are a few choices from those product lines, but first, some things you need to know:
    Security Updates. It is imperative to keep a router/firewall up to date. Otherwise, it will get hacked. I prefer devices that can be configured to update themselves automatically. Many firewall vendors require you to maintain a licensing subscription to receive security updates. pfSense, OPNsense, AmpliFi, EdgeRouter, and UniFi do not require this–you pay for the hardware once but get free security updates for the life of the device (usually 5 to 10 years…or practically forever with pfSense/OPNsense). You should have a plan to lifecycle equipment before the vendor stops providing updates.
    Intrusion Detection System (IDS). An advanced security feature that scans traffic for malicious activity. This is commonly done by looking at packets in network traffic to see if they match signatures of attack patterns. Another method is to scan for traffic anomalies or see if the traffic is coming from or going to known compromised hosts or poor reputation networks.
    Intrusion Prevention System (IPS). It automatically blocks anything detected by the IDS. An IPS device can stop port scans, malware, viruses, and exploits that would otherwise pass through a firewall. If you have open ports to the internet I strongly advise having an IPS in place.
    Honeypot. This is a fake device that may appear to be vulnerable. One implementation of this is it can sit on your network and will report if anything tries to scan or hack into it. This is useful to find compromised hosts or threats on your network.
    Deep Packet Inspection (DPI). A feature that allows you to get detailed information about the traffic on the network.
    Unified Threat Management (UTM). That means the device combines multiple security features on a single machine. A typical setup would be a Firewall, IDS, IPS on the same device.
    Next-Generation Firewall (NGFW). Very similar to UTM, NGFW looks beyond traditional means to stop threats. It uses deep packet inspection, IPS, application awareness, and sometimes machine learning.
    Packets Per Second (PPS). This is the speed at which a router or firewall is capable of sending traffic. This is usually measured in millions of PPS.
    Wireless Routers. I prefer to use “No WiFi” routers and run my own separate Wireless APs, but if you want to keep things simple (which is usually just fine for a house) some routers have built-in Wireless. You will probably not get Gigabit Wireless unless you have very clear channels. The fastest APs on the market now are WiFi 6. However, the game-changer is when WiFi 6E comes out. WiFi 6 run on 2.4GHz and 5GHz, but there’s limited bandwidth available. WiFi 6E will add the 6GHz band and a lot of spectrum. I am predicting it will be much faster than gigabit–you’ll need to plug your AP into a 2.5Gbe or 10Gbe port to take advantage of it (or aggregate multiple gigabit ports together).
    Wired Router. All of the routers below are wired. Be aware that some other routers have very few wired ethernet ports these days. If you don’t have enough wired routers, purchase a switch to extend it.
    Router Modem. Some devices combine the router and modem into one. This is often what an ISP will provide you. I like to keep mine separate.
    Up/Down. Most providers will advertise their speed like this. 500/100 Mbps, 100/20 Mbps. The first number is the download speed, the second is the upload. If the up and down are the same speed sometimes one number is given but it’s referred to as symmetrical, e.g. “gigabit symmetrical” means 1000/1000 Mbps. If only one number is given without the word symmetrical it refers only to the download speed, and that means the upload speed is very slow.
    Router vs. Firewall. These are actually different technologies, but it makes make a lot of sense to combine them, especially if you have multiple LANs or VLANs. So the two terms are often used interchangeably. A firewall either allows or denies network traffic to pass through, and a router determines which path network traffic should take to get to its destination.
  Mother-in-Law Router: AmpliFi HD (With WiFi)
    ​AmpliFi HD (Amazon)
    What drove me to find the AmpliFi HD was searching for a good router for non-tech people who want a home router. I want something they can install themselves that keeps itself secure and updated by default, and built-in WiFi and mesh-networking, so they don’t have to run ethernet cables in large houses to expand the range. The AmpliFi HD has not disappointed.
      Best for people that just want something simple that works.
      Simple setup with pictures on the screen of what to do next. You can set it up from an Android or iOS device, and once set up, it can be entirely controlled using the App.
      To enable Gigabit speeds, enable hardware offloading for NAT.
      Secure by default and automatically keeps itself updated.
      If there is a problem with your internet, it tells you what the problem is right on the screen. This makes it simple to know if there is a problem with your ISP, router, or your computer.
      You can purchase wireless extenders that plug into a wall outlet.
      Built-in WiFi 802.11AC (not WiFi 6 unfortunately).
      Blends in with your furniture.
      Target: People who just need a simple router+wireless AP. Or want something that looks nice on a bookshelf.
    Drawbacks: It’s a pretty basic router without many advanced features. It has what a normal person would want, even a separate guest network. But if you have advanced needs or a homelab, this probably isn’t the option for you.
    I eat my own dog food. My own Mother-In-Law uses this.
  Open Source Router: pfSense Netgate XG-7100
    ​pfSense XG-7100 (Netgate)
    If someone told me they wanted a firewall that could flex with their unknown future needs, I would pick pfSense. That is because it is flexible enough to handle almost any situation. pfSense is a very capable firewall appliance. It combines the best open-source technologies and puts them into one device. It can be installed in a high-availability configuration, making it suitable for mission-critical environments. It’s a lot more than a firewall; it’s a UTM with a lot of features. It supports just about any functionality you’d like, including IDS/IPS, dual WAN, etc. Since pfSense is free and open-source, many people run it in a VM on VMware or Proxmox (which is a fantastic idea because if an update breaks something, you can rollback the snapshot) or a white box server. The software is free, so you can virtualize it, build your own, purchase directly from Netgate or get a small device like the Protecti Vault 6.
    A fork of pfSense is OPNSense, and actually, if I were to pick between the two, I’d probably install pfSense at a business, but OPNSense in my homelab. pfSense has a slower release cadence making it ideal for a stable environment. OPNSense has frequent releases making it better when you might want to use the latest firewall technology.
    Target: Homelab enthusiasts, businesses, and organizations who prefer to trust open-source software.
  Budget Router: ER-X
    ​Ubiquiti EdgeRouter ER-X (Amazon)
    This is the best gigabit router under $100. Don’t let the size fool you. This has an ASIC (Application Specific Integrated Circuit) processor onboard, allowing it to match or outperform more expensive routers by offloading tasks expensive to a CPU.
      If you have a fleet of them, they can be managed using the UNMS controller.
      Turn on hardware offload to the ASIC processor to enable gigabit speeds.
      The ER-X SFP model is the same but adds an SFP port for fiber-optic connections and 24v Passive PoE ports.
      GUI or Command-line interface with tab-complete.
      Automatic updates possible via the UNMS controller.
      Dual-WAN failover and load-balancing.
    Drawbacks:
      Maximum routing capability on the ER-X and ER-X SFP is limited to 1Gbps total. So you will be able to upload at a gigabit or download at a gigabit, but if doing both at the same time, or routing traffic between multiple LANs, it’s going to be limited to a total of 1Gbps throughput. For smaller sites, this is never going to be an issue.
      Using the ASIC processor to take advantage of gigabit disables some advanced features (like Deep Packet Inspection and QoS).
    For a faster option see the ER-6P which has 1.8 Gbps throughput.
    ER-6P
    Target use: MSPs, or small businesses where professionals have a lot of sites and need central management.
  Comprehensive Router: UniFi Dream Machine Pro
    ​UniFi Dream Machine Pro.
    This is my favorite, and what I use in my homelab. I value security, simplicity, and scalability. So I take a wholistic, meaning a comprehensive approach to networking. Instead of managing ad-hoc devices, I like all of my networking equipment to be managed centrally. This saves me time and allows me to operate at a higher level instead of getting stuck in the weeds.
    Instead of thinking about firewalls, managed switches, and Wireless APs, I think about the network as a whole.
    Configure things at the network level, and the UniFi Controller takes care of the rest. It pushes the necessary configurations to all the devices. This allows for flexibility, making network changes in minutes instead of hours and days instead of months.
    The UniFi Dream Machine Pro is the UTM in UniFi’s lineup, here are its features:
      Intrusion Detection System (IDS)
      Intrusion Prevention System (IPS)
      Easy per Country blocking (click on a world map to block)
      Honeypot. Watches your internal network for devices that behave suspiciously (such as a port scan) and reports them to you.
      Dual WAN and LTE WAN failover options.
      Capable of sustaining 3.5Gbps throughput with every security feature on (including VLAN tagging and IDS/IPS).
      Built-in Controllers for Network (Wireless APs and Switches), Protect (Video surveillance), Talk (VoIP phones), and Access (Door locks), making it a great all-in-one device in 1U to deploy at a site.
      Auto-updates itself for security updates.
      Target: Businesses, Homelabs.
    Drawbacks:
      Some advanced features such as advanced custom DNS and MAC address cloning aren’t in the GUI yet and require 3rd party UDM Utilities on the command line.
      An external UniFi Controller cannot adopt it. It must use its internal controller. That’s fine for single-site networks but would be a pain for MSPs.
      There is some risk to running all of the features on a single device.
  Enterprise Firewall: Palo Alto Borg
  Palo Alto Borg Cube
  Of course, there are also Enterprise-class firewalls and routers such as Juniper (which powers Cloudflare), Cisco, Fortinet, and Palo Alto. It’s hard to argue that Palo Alto isn’t at the top (in both highest cost and features).
  Comparison Chart
  Questions
    Q. If my router has Gigabit Ethernet ports does that mean it will do Gigabit?
    Not necessarily. The router’s ability to process packets, packet size, number of firewall rules, intrusion detection system, etc., all impact performance.
    Q. Can’t I flash DD-WRT on my Linksys?
    No, DD-WRT doesn’t get regular security updates.
    Q. Can a modem and router be combined?
    Yes, ISPs often combined them into a Router Modem. I prefer to keep them separate.
    Q. What’s the best Gigabit router for gaming?
    Try to get the one with the brightest lights. That makes them go faster.
    Q. What kind of Ethernet Cables Should I use?
    CAT6A. CAT6A can go up to 10Gbe at 100 meters (328 feet) and supports PoE. If I was building a brand new house and wiring it up I would do CAT6A. For runs longer than 100 meters use fiber. I use Monoprice cables.
