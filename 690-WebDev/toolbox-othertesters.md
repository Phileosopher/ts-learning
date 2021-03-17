# Toolbox - web testers

* [SpecuCheck](https://github.com/ionescu007/SpecuCheck) for Windows reports on the state of fixes for Meltdown and Spectre. Technically it should not be here as it is not an online tester, but rather a pair of EXE files you need to download and run.

## WebRTC can leak public IP address while on VPN

* Test if WebRTC is enabled at [https://diafygi.github.io/webrtc-ips/](https://diafygi.github.io/webrtc-ips/). The site "secretly makes requests to STUN servers that can log your request. These requests do not show up in developer consoles and cannot be blocked by browser plugins (AdBlock, Ghostery, etc.)"
* Test for leakage at [https://ipleak.net](https://ipleak.net/)
* The [WebRTC Leak Test](https://www.browserleaks.com/webrtc) at BrowserLeaks.com
* VPN provider Mullvad has a tester page [https://am.i.mullvad.net](https://am.i.mullvad.net/) that tests WebRTC, DNS servers and more
* PrivacyTools.io has a [WebRTC Leak Test](https://www.privacytools.io/webrtc.html)
* [Trickle ICE](https://webrtc.github.io/samples/src/content/peerconnection/trickle-ice/) - click on the red Bather Candidates button near the bottom of the page
* Read more about this [from Mullvad VPN](https://mullvad.net/en/guides/webrtc/) (undated) and from [BestVPN](https://www.bestvpn.com/blog/31048/the-webrtc-vpn-bug-and-how-to-fix-it/) (Nov. 2015). Note that Internet Explorer and Safari are safe as they do not support WebRTC at all.
* Firefox: disable WebRTC -> about:config and toggle media.peerconnection.enabled to false
* Chrome requires an extension. [WebRTC Leak Prevent](https://chrome.google.com/webstore/detail/webrtc-leak-prevent/eiadekoaikejlgdbkbdfeijglgfdalml?hl=en) works with Chrome version 42 and newer, some options require Chrome version 48. The [WebRTC Network Limiter](https://chrome.google.com/webstore/detail/webrtc-network-limiter/npeicpdbkakmehahjeeohfdhnlpdklia) prevent IP leaks without fully disabling WebRTC functionality. It is an official Google extension.
* [uBlock Origin](https://github.com/gorhill/uBlock#ublock-origin) can also help. See [Prevent WebRTC from leaking local IP address](https://github.com/gorhill/uBlock/wiki/Prevent-WebRTC-from-leaking-local-IP-address) by Raymond Hill author of uBlock Origin.

## Internet connection Speed Tests

* [fast.com](https://fast.com/) is from Netflix. By default, it only reports on download speed, but you can get it to also test uploads by clicking the "Show More Info" button. It also reports on Latency. No ads/trackers. Do not run this while connected to a 4G/LTE network (long story).
* [SpeedTest.net](https://www.speedtest.net/) is pretty much the unofficial standard. Also available as an app for iOS and Android. Lots of ads and trackers.
* The [LibreSpeed Speedtest](https://librespeed.org/) runs fairly quickly. No ads/trackers.
* Cloudflare has a speed test at [speed.cloudflare.com](https://speed.cloudflare.com/). Like SpeedTest.net it automatically runs the test against a Cloudflare server that is physically near you. Unlike SpeedTest.net, you can not change the server it tests with. For download speeds, it run multiple tests using four different sized files and reports on the speed for each file size. It also measures Latency and Jitter. It does not measure upload speed (as of June 2020). No ads/trackers. Like Fast.com it is good for non-techies as there is no button to click to run the test. In September 2020 I did some comparison of speed testers and this reported a much slower speed than all the others.
* The Open Broadband Speed Test at [InternetHealthTest.org](http://internethealthtest.org/) runs multiple speed tests from multiple locations, so it takes a while to complete.
* The [Cool Fast Internet Download Speed Test](https://www.cfspeed.com/) by Jerry Jongerius works in any browser.
* The [SpeakEasy Speed Test](https://speakeasy.net/speedtest/) has been around forever.
* Other speed tests: [speedof.me](http://speedof.me/), openspeedtest.com and www.bandwidthplace.com
* The [DSLreports.com speed test](https://www.dslreports.com/speedtest) seems to have died, as of September 2020. It is the only one I know of that reports on Buffer Bloat.
* At [testmy.net](https://testmy.net/) you can chose to test upload or download speed individually.

## Google

* Google security checkup [myaccount.google.com/intro/security-checkup](https://myaccount.google.com/intro/security-checkup)
* See the data Google has on you at [myactivity.google.com](https://myactivity.google.com). Activity Controls is perhaps the most important section as it lets you stop some types of data collection. Read more [from Leo Notenboom](https://askleo.com/google-remembers-realize/).

## Website Security Tests

* The SSL Labs [SSL Server Test](https://www.ssllabs.com/ssltest/) reports many techie details of the SSL configuration on a server. From Qualys. This is well respected and has been around for a long time.
* Similar to the SSL Labs test, High-Tech Bridge offers an [SSL Server Test](https://www.htbridge.com/ssl/)
* ImmuniWeb offers a [Website Security Test](https://www.immuniweb.com/websec/) and an [SSL Security Test](https://www.immuniweb.com/ssl/).
* Mozilla [Observatory](https://observatory.mozilla.org/) tests assorted security aspects. Released Aug. 2016.
* [COMODO SSL Analyzer](https://sslanalyzer.comodoca.com/)
* [CryptCheck](https://tls.imirhil.fr) shows which cipher suites are used with TLS 1.2, which with TLS 1.1 and which with TLS 1.0. Also clearly shows whether Perfect Forward Secrecy is supported for each cipher suite (green PFS or orange NO PFS).
* The SSL/TLS test at [sslping.com](https://sslping.com) takes only a few seconds and reports on weak ciphers, old protocols and assorted certificate errors. It does not, however, report on either DV vs. EV status or Perfect Forward Secrecy. It also does not support IPv6 and reports are limited to one IP address per domain. [See a review](https://ctrl.blog/entry/review-sslping).
* The weakdh.org site [can test for](https://weakdh.org/sysadmin.html) Logjam, weak Diffie Hellman keys and Forward Secrecy
* [10 Online Tool to Test SSL, TLS and Latest Vulnerability](https://geekflare.com/ssl-test-certificate/) by Chandan Kumar July 2016
* The [DigiCert SSL Installation Diagnostics tool](https://www.digicert.com/help) validates digital certificates
* The POODLE, FREAK, Logjam and Heartbleed sections of this page have links to test servers for these vulnerabilities
* At the [Google Transparency Report](https://www.google.com/transparencyreport/https/ct/?hl=en) you can check if a certificate is transparent. This will [become more important](https://www.nimbushosting.co.uk/transparent-ssl/) in October 2017.

## Website Non-security Tests

Some of these merely claim to be speed testers but they all illuminate a lot about what goes under underneath a web page. For example, where the ads and trackers come from.

* [Pingdom Tools](http://tools.pingdom.com/) has a website speed test and ping speed tests.
* [Dotcom-Monitor](https://www.dotcom-tools.com/) offers similar tools and more.
* Google has a [Mobile-Friendly test](https://www.google.com/webmasters/tools/mobile-friendly/)
* [GTMetrix](https://gtmetrix.com/) claims to give you insight on how well your site loads and provide recommendations on how to optimize it.
* [Website Speed Test](https://tools.keycdn.com/speed) from KeyCDN.
* Google has a [Page Speed Insights](https://developers.google.com/speed/pagespeed/insights/) test that reports on mobile friendly issues.
* [urlscan.io](https://urlscan.io) analyses websites and the resources they request. Much like the Inspector of your browser, it lets you see the individual resources that are requested when a site is loaded. This allows inexperienced users to see what a particular website is requesting in the background. By Jojo.
* [Web Page Test](https://webpagetest.org/) is an open source project that is primarily being developed and supported by Google as part of our efforts to make the web faster.
* [Web Server Vulnerability Scan with Nikto](https://pentest-tools.com/website-vulnerability-scanning/web-server-scanner-nikto)
* [Web Cookies](https://webcookies.org/) scans a website for HTTP cookies, Flash, HTML5 localStorage, sessionStorage, CANVAS, supercookies, evercookies as well as SSL/TLS and HTTP security
* [cookieserve.com](https://cookieserve.com/) reports on the cookies set by a website.

## Website malware and tracking tests

* The [Virus Total URL Scanner](https://www.virustotal.com/en/#url) gets opinions from over 30 different sources.
* [Blacklight](https://themarkup.org/blacklight/) from The Markup runs a privacy test on a website. I recommend it.
* [Sucuri Website Malware and Security Scanner](https://sitecheck.sucuri.net)
* [urlscan.io](https://urlscan.io/)
* [Tinfoil Security](https://www.tinfoilsecurity.com/) empowers DevOps with Security, whatever that means. Steve Gibson was impressed with their service on the [Sept. 20, 2016 episode](https://www.grc.com/sn/sn-578.htm) of Security Now.
* From [Quttera](https://quttera.com/scanwebsite): "Check any website/domain for web malware and web threats online. Site check report with web threats, iframes, malicious redirects and hidden obfuscated JavaScript will be generated at the end of the website scan."
* Zscaler [Zulu URL Risk Analyzer](http://zulu.zscaler.com/)
* [Unmask Parasites](http://www.unmaskparasites.com/) tests if a web page contains hidden illicit content.
* [Google safe browsing](https://www.google.com/transparencyreport/safebrowsing/diagnostic/?hl=en)
* [WebPulse Site Review Request](https://sitereview.bluecoat.com/sitereview.jsp) from Blue Coat
* OpenDNS has a [Site Checker](http://www.opendns.com/support/checker/) with crowd sourced website opinions.
* [Web of Trust](http://www.mywot.com/) offers crowd sourced website opinions on their website. They also have web browser plugins.
* [urlQuery.net](http://urlquery.net/) detects and analyzes web-based malware offering detailed information about the activities a browser does while visiting a site
* [Norton Safe Web](http://safeweb.norton.com/) from Symantec
* Much like this list, Lenny Zeltser has is own list of [Free Online Tools for Looking Up Potentially Malicious Websites](http://zeltser.com/combating-malicious-software/lookup-malicious-websites.html)

## CHROMEBOOKS

Newer ones get Linux apps and 5 years of bug fixes.

* [Auto Update Policy](https://support.google.com/chrome/a/answer/6220366?hl=en) by Google lets you look up how long a Chromebook model will get bug fixes (a.ka. the Auto Update Expiration date)
* [Some Chromebooks Won't Get Linux Apps. Here's What You Can Do Instead](https://www.howtogeek.com/394049/some-chromebooks-wont-get-linux-apps-but-heres-what-you-can-do-instead/) by Tom Westrick Nov 7, 2018. Has a list of Chromebooks that will not get Linux apps which requires Linux kernel 3.14 or later.
* [Developer Information for Chrome OS Devices](https://www.chromium.org/chromium-os/developer-information-for-chrome-os-devices) by Google. See when a Chromebook was released and which version of the Linux kernel it runs.

## BAD CERTIFICATES

One way to verify that your browser is working correctly when it comes to validating certificates is to purposely give it a bad certificate.

* [Hanno Böck](http://hboeck.de/) offers a certificate signed by a Certificate Autority that is not trusted by any web browser: [https://badcert-generic.tlsfun.de](https://badcert-generic.tlsfun.de/)
* [Steve Gibson](https://grc.com) has a sample revoked certificate: [https://revoked.grc.com](https://revoked.grc.com/)
* Hanno Böck also has a certificate that is both expired and self-signed: [https://expired.tlsfun.de](https://expired.tlsfun.de/)
* The mother of all these test sites is [badssl.com](https://badssl.com/), but there is no documentation at all. Shame.
* Kenn White created [https://bogus.lessonslearned.org](https://bogus.lessonslearned.org) which presents the [self-signed eDellRoot certificate](http://arstechnica.com/security/2015/11/dell-does-superfish-ships-pcs-with-self-signed-root-certificates/) that was discovered in Nov. 2015. The cert was, sadly, accepted by Chrome on Windows but Firefox correctly warned about it.
* Test for cellular ISP tracking beacons at [lessonslearned.org/sniff](http://lessonslearned.org/sniff) by Kenn White. ATT, Verizon, Sprint, Bell Canada and Vodacom are/were inserting "super cookies" into hidden web page headers when connected to their 3G/4G data networks (does not apply with WiFi). If you are not being tracked the "Broadcast UID" is blank. The page explains the issue in detail. There is no HTTPS version of this page because the cellphone companies can not insert data into HTTPS traffic.
* On Facebook, you can view the devices that are logged in to your account [here](https://www.facebook.com/settings?tab=security&section=sessions&view). It should also show approximately where in the world those devices are located.
* The [Cloudflare Encrypted SNI checker](https://www.cloudflare.com/ssl/encrypted-sni/) is not yet (Sept. 2018) very useful as no one yet uses Encrypted SNI. It also tests for TLS 1.3 another very new protocol. It tests for secure DNS too, but in my tests it was never sure about the result. Finally, it tests for DNSSEC.

## Test your web browser

* Test if the auto-fill feature of your browser is silently leaking information [anttiviljami.github.io/browser-autofill-phishing](https://anttiviljami.github.io/browser-autofill-phishing/)
* [How's My SSL?](https://www.howsmyssl.com/) reports the version of SSL/TLS being used, whether the browser supports forward secrecy, whether it is vulnerable to the BEAST attack and much more. Every test is explained reasonably well.
* [www.deviceinfo.me](https://www.deviceinfo.me/) reports a ton of information about your web browser and its environment.
* [Panopticlick](https://panopticlick.eff.org/) from the EFF is a great example of browser fingerprinting. Sadly, you may be unique.
* [Qualys BrowserCheck](https://browsercheck.qualys.com/) scans your browser and plugins to see if they are up-to-date.
* Qualys SSL Labs also has an [SSL Client Test](https://www.ssllabs.com/ssltest/viewMyClient.html) that reports on the SSL/TLS Capabilities of your web browser. This includes, but is not limited to, testing whether the browser is vulnerable to the Logjam, FREAK and POODLE flaws.
* The [weakdh.org](https://weakdh.org/) website tests for the Logjam vulnerability. It is the home office for this flaw. If your browser is vulnerable there will be a red horizontal stripe at the top of the page saying "Warning! Your web browser is vulnerable to Logjam and can be tricked into using weak encryption. You should update your browser."
* The [Mozilla Plugin Check](http://www.mozilla.com/en-US/plugincheck/). Originally, this only worked with Firefox, but in May 2010, it was [extended to work with other browsers](http://blog.mozilla.com/security/2010/05/11/plugin-check-for-everyone/) as well.
Oct 19, 2014: This is very unreliable. ## Don't trust it## . I have seen old plug-ins flagged as up to date too many times.
May 23, 2015: Support for other browsers has been withdrawn, it only supports Firefox
* The [YouTube HTML5 Video Player](http://youtube.com/html5) page shows if the browser is using Flash or HTML5
* The Cyscape [Browser Capabilities Test Page](http://www.cyscape.com/showbrow.asp) relies on their BrowserHawk product.

## Public IP Address

* [IPChicken](http://ipchicken.com) is my favorite website for ## reporting on your IP address## . The "Name Address" field often makes the ISP name obvious.
* A new entrant in this crowded field [www.unix.com/what-is-my-ip.php](http://www.unix.com/what-is-my-ip.php) has a very user friendly format.
* Dyn offers a minimal interface: [checkip.dyndns.com](http://checkip.dyndns.com/).
* Synology also offers a minimal interface: [checkip.synology.com](http://checkip.synology.com).
* Some VPN providers post both your IP address and your ISP at the top of their home page. Some that do this are [PrivateInternetAccess](https://www.privateinternetaccess.com), [NordVPN](https://nordvpn.com/) and [IVPN](https://www.ivpn.net/). Tunnelbear offers the same information at [bearsmyip.com](https://bearsmyip.com/).
* VPN provider Perfect Privacy [reports your public IP address](https://www.perfect-privacy.com/check-ip/) for both IPv4 and IPv6 along with your physical location and a DNS server.
* [whoer.net](https://whoer.net/) reports your public IP address, your ISP and a ton of information about your computer
* This page [www.ip-adress.com/what\_is\_my\_ip/](http://www.ip-adress.com/what_is_my_ip/) reports the usual stuff and adds some information about your browser.
* A Google search for "ip" returns your public IP address. A duckduckgo.com search for "ip" returns both your public IP address and your location.
* Find other websites hosted on a given IP address at [yougetsignal.com/tools/web-sites-on-web-server](http://www.yougetsignal.com/tools/web-sites-on-web-server/)
* And, you can also find other websites hosted on a given IP address at [https://www.urlvoid.com/ip/1.2.3.4](https://www.urlvoid.com/ip/1.2.3.4) (obviously change the IP address)

## IP version 6 (IPv6) Public IP address

* Is the router you are sitting behind enabled for IP version 6 (IPv6)? Test it at [whatismyv6.com](http://whatismyv6.com/) or [www.ipaddress.com](https://www.ipaddress.com)
* Wireshark has a simple [IPv4 and IPv6 Connectivity Test](https://www.wireshark.org/tools/v46status.html)
* VPN provider Perfect Privacy [reports your public IP address](https://www.perfect-privacy.com/check-ip/) for IPv4 and IPv6
* Synology offers a minimal display of the public IPv6 address at [checkipv6.synology.com](http://checkipv6.synology.com/)

## Physical Location

* A demo of the MaxMind service at [maxmind.com/en/locate-my-ip-address](https://www.maxmind.com/en/locate-my-ip-address) show the physical location of your current public IP address
* Maxmind data is also used at [geoip.nekudo.com](https://geoip.nekudo.com) but it does not display your IP address.
* [iplocation.net](https://www.iplocation.net/) checks your public IP address with mulitple location services

## Host name(s)

Given an IP address, find the name of the computer, a.k.a. its hostname.

* [ismyportopen.com/hostname-from-ip-address](http://ismyportopen.com/hostname-from-ip-address/)
* [iplocation.net/reverse-dns](https://www.iplocation.net/reverse-dns)
* [ipaddress.com/reverse-ip-lookup](https://www.ipaddress.com/reverse-ip-lookup)
* [ipinfo.io](https://ipinfo.io)
* [Reverse IP to Domains Lookup](http://www.ipfingerprints.com/reverseip.php) at ipfingerprints.com finds other websites hosted on the same server

## Email

* At [mxtoolbox.com](http://mxtoolbox.com/) you can look up the MX records for a domain. These mail exchanger records identify the recieving email server(s) for a domain.
* Test email for the availability of TLS at [checktls.com](http://www.checktls.com). This feature encrypts email as it is sent from one email server to another.
* Inquire into SPF records for a domain at [SPF Record Testing Tools](http://www.kitterman.com/spf/validate.html) from Kitterman Technical Services. Use this to see if a domain has an [SPF record](http://tools.ietf.org/html/rfc7208), what it is and whether it is valid or not.
* The [dmarcia DMARC Inspector](https://dmarcian.com/dmarc-inspector/) checks for and displays [DMARC](https://dmarc.org/wiki/FAQ) records for a domain.
* Test the privacy of your email client at [emailprivacytester.com](https://emailprivacytester.com/) by Mike Cardwell

## LCD MONITORS

* [pxcalc.com](http://pxcalc.com/) is handy for showing your current monitor resolution and converting it to both an aspect ratio and DPI.
* [LCD monitor technology and tests](http://www.techmind.org/lcd/index.html) at Techmind.org
* [The Lagom LCD monitor test pages](http://www.lagom.nl/lcd-test/) at www.lagom.nl includes tests for contrast, sharpness, gradient, response time and much more.
* [testmyscreen.com](https://testmyscreen.com)
* [www.eizo.be/monitor-test](https://www.eizo.be/monitor-test/)
* The [Backlight Bleed Test](https://www.lightbleedtest.com/) has example of backlight bleeding and tests for it.
* The [LCD Repair page](http://www.flexcode.org/lcd2.html) at flexcode.og offers screens of solid colors to test for bad pixels

## OTHER

* Given a MAC address, find the company that it is assigned to at [macvendors.com](https://macvendors.com) or [macvendorlookup.com](https://www.macvendorlookup.com) or [whatsmyip.org/mac-address-lookup](http://www.whatsmyip.org/mac-address-lookup/)
* The [Outgoing port tester](http://portquiz.net) at portquiz.net listens on all TCP ports, allowing you to test any outbound TCP port. The one exception seems to be the file sharing port 445.
* Check if your email address has been exposed in a data breach at [haveibeenpwned.com](https://haveibeenpwned.com/)
* Check where a short URL really leads: [checkshorturl.com](https://www.checkshorturl.com) and [urlxray.com](http://urlxray.com/) (HTTP only)
* Infected thumb drives: In [Test your defenses against malicious USB flash drives](http://blogs.computerworld.com/test_your_defenses_against_malicious_usb_flash_drives) I provide a sample autorun.inf file that can be used on a thumb drive to test how well a Windows machine is defended against malware that may live on a USB flash drive. January 2009.
* Official documentation from Microsoft about how to block the installation of Windows 10 on computers running Windows 7 and 8: [How to manage Windows 10 notification and upgrade options](https://support.microsoft.com/en-us/kb/3080351)
* Chose and review your Google privacy settings at [https://myaccount.google.com/intro/privacy](https://myaccount.google.com/intro/privacy)
* Check if you are logged in to the TOR network at [check.torproject.org](https://check.torproject.org/)
* Test if a website is reachable from multiple locations [at siteuptime.com](http://www.siteuptime.com/users/quickcheck.php).
* Test if [your credit card was stolen](http://ismycreditcardstolen.com/)
* The [Social Network Login Status Detector Demo](http://www.tomanthony.co.uk/tools/detect-social-network-logins/) detects if you are logged in to Facebook, Twitter, Google or Google Plus.
* Adobe has a ## [Flash tester web page](http://www.adobe.com/software/flash/about/)##  (they don't call it that) that reports the currently installed version of Flash and the latest version for assorted browsers/OSs. Windows users need to run this test for *all* browsers installed on their system as each can be using a different version of the Flash player. My [flashtester.org](http://flashtester.org/) site has a version history of Flash and provides a simple name to remember when looking for Adobe's Flash tester page.
* The Adobe ## Flash Player Settings Manager##  are web pages that let you configure Flash cookies (a.k.a. [local shared objects](http://www.adobe.com/products/flashplayer/articles/lso/)) as well control how often Adobe checks for updates to the Flash player. For more from Adobe on this see: [Flash Player Help](http://www.macromedia.com/support/documentation/en/flashplayer/help/settings_manager.html) and [How to manage and disable Local Shared Objects](http://kb.adobe.com/selfservice/viewContent.do?externalId=52697ee8&sliceId=2).
1.The [Global privacy settings](http://www.macromedia.com/support/documentation/en/flashplayer/help/settings_manager02.html) page controls whether Flash based web sites can use your camera or microphone
2.[Global Storage Settings](http://www.macromedia.com/support/documentation/en/flashplayer/help/settings_manager03.html) control how much disk space websites can use to store information, or you can prohibit websites from storing any information at all
3.[Global Security Settings](http://www.macromedia.com/support/documentation/en/flashplayer/help/settings_manager04.html) lets you specify if SWF or FLV content that uses older security rules can access the Internet. Beats me too what that means.
4.At the [Website Privacy Settings](http://www.macromedia.com/support/documentation/en/flashplayer/help/settings_manager06.html) page you get a list of websites you've visited. For each you can specify rules about using your camera or microphone or storing data on your computer.
5.This what Adobe says about the [Website Storage Settings](http://www.macromedia.com/support/documentation/en/flashplayer/help/settings_manager07.html) panel: "Use this panel to specify storage settings for any or all of the websites that have requested permission to use your camera or microphone or to store information on your computer."
* Test [HTML5 local storage](http://www.pcpro.co.uk/blogs/wp-content/uploads/2010/09/say-hello.html) Enter your name, then reload the page.
* [dnscheck.iis.se](http://dnscheck.iis.se/) offers a health check of the DNS servers for a domain
* [Eric Gerds Plugin Detection](http://www.pinlady.net/PluginDetect/) detects Java, [QuickTime](http://www.pinlady.net/PluginDetect/QuickTimeDetect.htm), Flash, Shockwave, Windows Media Player, DevalVR, Silverlight and the VLC Player.
* Eric Gerd (above) does not report the latest version of ## [QuickTime](http://www.apple.com/quicktime/)## , but you can see it at Apple's [QuickTime download](http://www.apple.com/quicktime/download/) page.
* The [PC Pitstop Quick Program Scan](http://pcpitstop.com/spycheck/scan.asp) is an ActiveX based test that tells you what's running on your computer, including background processes. For each process, it reports who made it and what it is. Most importantly, perhaps, processes are color coded based on threat level: unknown, safe, optional, spyware/adware, virus. Only works with Internet Explorer and will not run if IE is run in restricted mode with DropMyRights.
* The [Conficker Eye Chart](http://www.confickerworkinggroup.org/infection_test/cfeyechart.html) is a simple web page that reports whether your computer is ## infected with the Conficker worm## . Joe Stewart came up with the idea and he has [a copy of the same page](http://www.joestewart.org/cfeyechart.html) at his personal website. The H security also has an online [Conficker tester](http://www.h-online.com/security/services/browsercheck/tests/conficker/test.shtml).
* The [JavaScript tester](http://javatester.org/javascript.html) page on this site verifies if JavaScript is working (at least working on this site, it may not work on other sites if you use the Firefox NoScript extension), reports the version of JavaScript your web browser supports and displays your browsers "user agent", a string of characters that websites can use to identify which web browser you are using.
* Adobe has a page which tests for ## [Shockwave](http://www.adobe.com/shockwave/welcome/)##  ([alternate link](http://www.macromedia.com/shockwave/welcome/)). This page used to test for both Flash and Shockwave, no more.
* Adobe does not have an page that tests AIR, as far as I know. But they do have [instructions for manually checking file properities](http://helpx.adobe.com/air/kb/determine-version-air-runtime.html) on Windows, Mac OS X and Linux. On Windows, you can check in the Control Panel just as with all other software.
* Test your brain at the [Prevention Magazine Brainpower Assessment Quiz](http://www.prevention.com/brainq/). They say to allow 15 minutes for the test.
* Learn about Firefox Location-Aware Browsing at [Does Firefox share my location with websites?](http://www.mozilla.com/en-US/firefox/geolocation/) There used to an online demo but it has been removed. Firefox and Google locate you based on both your IP address and nearby Wi-Fi networks.
* The ## [Intel Driver Update Utilities](http://www.intel.com/support/detect.htm)##  will (in theory) auto-detect if you have Intel hardware for video, audio, Wi-Fi or Ethernet. Each is a separate utility and they only support Windows. If one of the utilities finds Intel hardware, then it reports whether you have the latest driver or not. Each utility works with either IE using ActiveX or Firefox using Java. Be warned though, I tested them and found [they failed to correctly detect Intel hardware](http://blogs.computerworld.com/14656/updating_intel_drivers) most of the time.
* [ClickJacking demos](http://www.grc.com/sn/notes-168.htm) put together by Steve Gibson in October 2008. As of May 2009 the demos seem to have gone stale, not sure.
* [Test if your ISP is manipulating BitTorrent traffic](http://broadband.mpi-sws.org/transparency/bttest-mlab.php) from the Max Planck Institute for Software Systems

## Windows Update

Conficker and other malware blocks access to Windows Update. A quick and easy way to verify that Windows Update is working correctly is to manually run Microsoft's Malicious Software Removal Tool. In Windowx XP, do Start -> Run -> "mrt.exe". In Vista, click the Start button and type "mrt" into the search box to locate the mrt.exe file. For more see my February 5, 2009 blog posting [What you don't know about the Windows Malicious Software Removal Tool](http://blogs.computerworld.com/what_you_dont_know_about_the_windows_malicious_software_removal_tool).

* Testing VRML plugins: [cic.nist.gov/vrml/vbdetect.html](http://cic.nist.gov/vrml/vbdetect.html)
* Mickey Segal has a [Configuration Test](http://segal.org/java/configuration/index.html) for Java that is very similar to the Version page here

* Another Java tester is available from [Duckware](http://www.duckware.com/support/javahelp.html). They also have an [online tester](http://www.duckware.com/tech/javafailure.html) for the bug in Java 7 Update 25 (and later?) that causes a Java warning message to [display the wrong program name](http://www.duckware.com/tech/javacodesigningfailure.html). (added Aug 28, 2013)
* Another Java tester is available at [gemal.dk](http://gemal.dk/browserspy/java.html) as part of their [BrowserSpy](http://browserspy.dk/). Read more [about BrowserSpy](http://blogs.techrepublic.com.com/security/?p=3118).
* A low end Java tester is available from [upshot.com](http://www.upshot.com/login/javatest/logo/javavmtest.html)
* Click and Learn has a [browser tester](http://www.clickandlearn.at/browsercheck/) in German that tests Java, Flash, Acrobat, Windows Media player and more.
* ScanIt has a web [browser security tester](http://bcheck.scanit.be/bcheck/) (a bit off this subject, but good to know)

* [www.mailtester.com](http://www.mailtester.com) ## validates an email address##  and reports on the email server

* [www.dnsstuff.com](http://www.dnsstuff.com) offers domain name tests, IP tests and hostname tests

* PC Pitstop has an [ActiveX tester](http://www.pcpitstop.com/testax.asp), very similar in concept to the Version page on this site. Martin Heller [has one too](http://mheller.com/testax.htm).

* [Testvirus.org](http://testvirus.org) allows you to send a harmless test virus to any email address. If your mail server or email hosting provider is running anti-virus software, these emails should get blocked.

* This isn't a tester, just a useful page. Microsoft's free [Office Online File Converters and Viewers](http://office.microsoft.com/en-us/downloads/HA010449811033.aspx)
* Who made that Ethernet network adapter? See the [Wireshark OUI Lookup Tool](http://www.wireshark.org/tools/oui-lookup.html) or [query the IEEE directly](http://standards.ieee.org/develop/regauth/oui/public.html). You can also download the [full list in plain text](http://standards.ieee.org/develop/regauth/oui/oui.txt) from the IEEE.
* Secure web pages are a sham. The page [Test Secure Form](https://cc-nanny.appspot.com/test-secure-page) is a perfect example, the URL is HTTPS yet data entered into the form is not secure. Yes, everything you have been told about website security is wrong.
* [WhoIs lookup](http://whois.domaintools.com) at DomainTools.com
* [WhoIs lookup](https://dnsimple.com/whois) at DNS Simple
* [DNSdumpster.com](https://DNSdumpster.com) discovers host names related to a domain
* [builtwith.com](https://builtwith.com/) is used to find out what websites are built with
* CentralOps.net has a number of online techie networking tools. I like their [NsLookup](http://centralops.net/co/NsLookup.aspx) and [Domain Dossier](http://centralops.net/co/DomainDossier.aspx?dom_whois=1&net_whois=1&dom_dns=1).
* The [ICSI Netalyzr](http://netalyzr.icsi.berkeley.edu/) tests your Internet connection for signs of trouble. Very techie stuff. Requires Java. From their website: *The International Computer Science Institute (ICSI) is a leading center for research in computer science and one of the few independent, non-profit research institutes in the United States.*

## Apple GoToFail bug

from Feb 2014. Only applies to iOS 6, iOS7 and OS X 10.9. These tests only work in web browsers, but if an Apple device is vulnerable, the problem also exists with many, if not most apps that use the operating system for SSL/TLS security. [See Wired.](http://www.wired.com/threatlevel/2014/02/gotofail/)

* [ssllabs.com/ssltest/viewMyClient.htm](https://www.ssllabs.com/ssltest/viewMyClient.html) from a trusted source. Look for the section called "iOS and OS X TLS Authentication Vulnerability"
* [www.imperialviolet.org:1266](https://www.imperialviolet.org:1266) from a trusted source
* [gotofail.com](https://gotofail.com/) from an unknown source

## POODLE

flaw in SSL v3 from October 2014. SSLv3 is old and buggy, POODLE will hopefully be the nail in the coffin that gets software providers to remove it from both clients (mostly web browsers) and servers. These sites test either your web browser or a website for the presence of SSL version 3. No support for SSL3 is the right answer.

* Server Test: [Qualys SSL Server Test](https://www.ssllabs.com/ssltest/). The mother of all server testers. Only tests the official HTTPS port, 443.
* Server Test: [www.tinfoilsecurity.com/poodle](https://www.tinfoilsecurity.com/poodle) can test HTTPS on *any* port.
* Browser Test: [SSL Labs Client test](https://www.ssllabs.com/ssltest/viewMyClient.html)
* Browser Test: [poodle.io](https://poodle.io/) from the University of Michigan
* Browser Test: [www.poodletest.com](https://www.poodletest.com/)

## Heartbleed

from April 2014. Tests if a web server is vulnerable to the [Heartbleed](http://heartbleed.com/) flaw in OpenSSL.

* SSL Labs Server Test: [https://www.ssllabs.com/ssltest/](https://www.ssllabs.com/ssltest/). If all is well it will say "This server is not vulnerable to the Heartbleed attack. (Experimental)". [Read more](https://community.qualys.com/blogs/securitylabs/2014/04/08/ssl-labs-test-for-the-heartbleed-attack).
* Netcraft has [a browser plugin](http://news.netcraft.com/archives/2014/04/17/netcraft-releases-heartbleed-indicator-for-chrome-firefox-and-opera.html) for Chrome, Firefox and Opera. Netcraft is very qualified for testing both Heartbleed and for certificate revocation. Recommended.
* The [Crowdstrike Heartbleed Scanner](http://www.crowdstrike.com/community-tools/) can not only scan remote servers it can also scan your local area network. This lets it test for Heartbleed on your router, NAS or other local device. In addition, it tests many secure services, such as email and FTP, whereas other scanners just focus on websites. Unlike all the other testers on this page, this is Windows software that has to be downloaded. It is free, small and portable.
* [https://lastpass.com/heartbleed](https://lastpass.com/heartbleed/) from Lastpass. If all is well is should say "Vulnerable: No" with the No in green.
* [http://filippo.io/Heartbleed](http://filippo.io/Heartbleed/) by Filippo Valsorda. My least favorite option.

## FREAK attack on SSL/TLS

March 4, 2015. A 10 year old flaw in SSL/TLS encryption was uncovered. The flaw can exist both in web browser and web server software.

* Test your web browser at [https://freakattack.com](https://freakattack.com/) The site also has links to good articles on the subject
* Test a website at [https://tools.keycdn.com/freak](https://tools.keycdn.com/freak)

## SUPERFISH

Feb. 2015. Lenovo pre-installed adware called superfish that broke HTTPS/SSL security on their Windows 8 consumer PCs.

* Superfish CA test by Filippo Valsorda [https://filippo.io/Badfish/](https://filippo.io/Badfish/)
* LastPass Superfish Checker [https://lastpass.com/superfish](https://lastpass.com/superfish/)
* Filippo Valsorda originally tested just for Superfish, but later expanded his online tester to look for all instances of software from Komodia which underlies Superfish. Software from Komodia can be found in many other products besides Superfish. But Komodia is not the only product that, in effect, does a man-in-the-middle attack to break the encryption offered on HTTPS web pages. Back in April 2013 Steve Gibson released an online [certificate fingerprint tester](https://www.grc.com/fingerprints.htm) that detects any and all such MITM attacks. I blogged about this service here [Steve Gibson's Fingerprint service detects SSL man in the middle spying](http://www.computerworld.com/article/2475102/cybercrime-hacking/steve-gibson-s-fingerprint-service-detects-ssl-man-in-the-middle-spying.html).

## Logjam flaw (May 2015)

* The [weakdh.org](https://weakdh.org/) website was created in May 2015 to document and test for the Logjam vulnerability. If your browser is vulnerable there will be a red horizontal stripe at the top of the page saying *"Warning! Your web browser is vulnerable to Logjam and can be tricked into using weak encryption. You should update your browser."* If all is well, a blue stripe will say *"Good News! Your browser is safe against the Logjam attack."*
* The [Guide to Deploying Diffie-Hellman for TLS](https://weakdh.org/sysadmin.html) at the weakdh.org site has a server test
* Qualys [SSL Client Test](https://www.ssllabs.com/ssltest/viewMyClient.html) shows whether the browser is vulnerable to the Logjam flaw (among a lot of other information)
* [TLS Logjam Check](https://tools.keycdn.com/logjam) from KeyCDN can test if a server is vulnerable

Test your popup blocker at

* [www.popupcheck.com](http://www.popupcheck.com)
* [www.popuptest.com](http://www.popuptest.com/)
* [www.meaya.com/testpop](http://www.meaya.com/testpop/)
* [www.dummysoftware.com/popupdummy\_testpage.html](http://www.dummysoftware.com/popupdummy_testpage.html)
