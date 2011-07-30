#Insta-Snorby - The Official Turnkey Snorby Appliance

##Description
Insta-Snorby is a "quick and dirty" Snorby IDS sensor that's perfect for testing out Snorby and other various bundled IDS components in your environment.

Insta-Snorby is designed to get you up and running viewing and actioning events, tuning rulesets, and testing configurations in your environment in a matter of minutes, not days.

If you're new to NSM, Insta-Snorby is a great solution to get you focused on actually improving your analysis skills instead of messing with flags you need to set on some obscure configure script.

##Appliance Details
Insta-Snorby is a modified Ubuntu 10.04 [Turnkey Linux Appliance](http://www.turnkeylinux.org/)

##Bundled Components
Insta-Snorby comes bundled (or is capable of downloading) the following security tools and applications:

###Snorby
* Snorby dependencies and prerequisites (sendmail, imagemagick, wkhtmltopdf)
* Snorby Web Application
* Apache2 (with Phusion Passenger) and MySQL 5 

###Snort
* Snort IDS 2.9.x.x - [More Info](http://www.snort.org/)
* Barnyard2 - [More Info](http://)
* Latest Emerging Threats Ruleset - [More Info](http://www.emergingthreats.net/)
* Latest VRT ruleset (with user supplied oinkcode) - [More Info](http://www.snort.org/snort-rules/?#rules)
* Pulled Pork - [More Info](http://code.google.com/p/pulledpork/)

###Other Tools
* Open-FPC (for full PCAP in Snorby) - [More Info](http://www.openfpc.org/)

##Installation
1. Download the latest .iso from [Snorby.org](http://snorby.org/)
2. Boot the ISO to your commodity or virtualized hardware.
3. Follow the on-screen instructions (hard disk installation highly recommended)
4. Login to the Snorby interface and begin your quest to become an NSM hero!

##Feedback/Support
1. [Snorby Issues Page](https://github.com/Snorby/snorby/issues)
2. [Snorby Mailing List](http://groups.google.com/group/snorby)
3. Twitter - Jason Meller - @jmeller / Dustin Webber - @dwebber