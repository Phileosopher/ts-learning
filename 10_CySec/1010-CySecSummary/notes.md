https://thebestvpn.com - consider all the VPNs available and a plan on how to do it
  A could cycle through all the free VPNs
  B could be using THE best
  Mozilla VPN
    https://blog.mozilla.org/futurereleases/2020/06/18/introducing-firefox-private-network-vpns-official-product-the-mozilla-vpn/
    https://news.ycombinator.com/item?id=23565192
  CloudFlare has a VPN as well


# Practical Linux Hardening Guide
  https://github.com/trimstray/the-practical-linux-hardening-guide
  https://news.ycombinator.com/item?id=18992930



Lifelock
  Make a list of the things that Lifelock is tracking
  Maybe make a cybersecurity list??

FROM NORDVPN TEST
  Only give permissions to things the app/plugin NEEDS
  Avoid showing publicly available personal details
    Alternately, use the wrong personal details
  When reading TOS, read the policies on:
    data security
    data sharing w/ 3rd parties
    data collection
  tools for online browsing:
    VPN
    incognito mode
    Tor browser
    ad blockers
    clear browsing history
    proxy servers
  Even then, FB/GOOG/TW/etc can still collect data without an account
  install all legit updates immediately
  Wifi:
    secure password
    disable SSID on router
    WPA2/WPA3 encryption
    enable MAC address filtering on router
  Password security???
  Malware causes:
    opening random downloaded files
    clicking on unknown links
    visiting suspicious sites
    opening emails from unknown sources
  ways you can get hacked
    sending pictures to unknown recipients
    accessing a nearish-but-not-quite website (www.facbook.com)
  metadata collection???
    IP
    uploaded photos
    time spent on website
    resolution of device
  how to detect phony sites
    not the same web URL, but close
    SSL certificate is self-verified, unverified or missing
  IoT problems
    no encryption
    no-password access
    no standards/regulation on many things
    discreet audio/video recording
  ways you can get in trouble from OTHER groups getting hacked
    you stored credit card info on someone's website (for convenience)
    you use the same password across multiple websites
Cisco Networking Academy - CySec
  https://www.netacad.com/portal/learning
  Cybersecurity Essentials - EN 0118
  Intro to Cybersecurity - EN 1217
https://www.youtube.com/channel/UCm9K6rby98W8JigLoZOh6FQ
Sec+
  https://www.comptia.org/training/practice-questions/security-501-practice-questions
  Take the test ($339)
  Examcompass.com practice tests
  Professor messer's videos
  https://certpages.com/Comptia/Security+/
  Sec+ - https://www.examcompass.com/
  Jason Dion practice tests
  Darril Gibson has a Sec+ book
Everything it takes to be "safe"
  Double-verify ALL app permissions
  Delete any unnecessary software off the computer
  hardening, top to bottom
What information could do
  With your passport number, someone could:
    Book an international flight as you
    Apply for anything that requires proof of identity documentation with the government, e.g. Working with children check
    Activate a SIM card (and so get an internet connection that’s traceable to you, not them, hiding them from the government)
    Create a fake physical passport from a template, with the correct passport number (which they then use to cross a border, open a bank account, or anything)
  with a password, soemoene could
    login to that particular computer (if 2FA wasn't enabled
    login to ANY other site that had the same password/email combo
CySec hardening concepts
  cysec training platform
    https://www.reddit.com/r/netsecstudents/comments/d8zi08/i_built_a_cloudbased_cyber_security_training/
  Disable/remove Native VLAN
  Check for redirects and diversions
    #62* redirect
    *#21# diversions
    ##002# remove redirections
  Packet analyzer for phones
    *#*#197328640#*#*
    UMTS RR Information (cell ID#)
    MM Info > Serving PLMN (area code)
    Netmonitor website (OpenCellID, e.g.)
  Record all relevant information
    IMEIs of all devices #06#
WebDevChecklist - Security
  Follow best practices
    ASafaaWeb security analyzer
    Observatory by Mozilla
  Cross-site scripting
    XSS cheat sheet
    DOM based XSS cheat sheet
    Free XSS scanner
  Cross-site request forgery
    Explanation and walkthrough
    CSRF cheat sheet
  Secure connection (SSL) (OPTIONAL)
    Setup SSL on IIS 7
    Setup SSL on Apache
    SSL Server Test
  HTTP Strict Transport Security (OPTIONAL)
    MDN Overview
    OWASP Overview
  Enable Content Security Policy (OPTIONAL)
    Content Security Policy
    MDN Guide
    OWASP Overview
      CSP Tester
We can apply obfuscation in our own lives by using practices and technologies that make use of it, including:
  The secure browser Tor, which (among other anti-surveillance technologies) muddles our Internet activity with that of other Tor users, concealing our trail in that of many others.
  The browser plugins TrackMeNot and AdNauseam, which explore obfuscation techniques by issuing many fake search requests and loading and clicking every ad, respectively.
  The browser extension Go Rando, which randomly chooses your emotional “reactions” on Facebook, interfering with their emotional profiling and analysis.
  Playful experiments like Adam Harvey’s “HyperFace” project, finding patterns on textiles that fool facial recognition systems – not by hiding your face, but by creating the illusion of many faces.
<li>Dial *67 in North America to make calls labeled as anonymous</li>
