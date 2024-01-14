CISA warns that attackers are now exploiting a critical Microsoft SharePoint privilege escalation vulnerability that can be chained with another critical bug for remote code execution.

Tracked as CVE-2023-29357, the security flaw enables remote attackers to get admin privileges on unpatched servers by circumventing authentication using spoofed JWT auth tokens.


"An attacker who has gained access to spoofed JWT authentication tokens can use them to execute a network attack which bypasses authentication and allows them to gain access to the privileges of an authenticated user," Microsoft explains.
"An attacker who successfully exploited this vulnerability could gain administrator privileges. The attacker needs no privileges nor does the user need to perform any action."

Remote attackers can also execute arbitrary code on compromised SharePoint servers via command injection when chaining this flaw with the CVE-2023-24955 SharePoint Server remote code execution vulnerability.

This Microsoft SharePoint Server exploit chain was successfully demoed by STAR Labs researcher Jang (Nguyễn Tiến Giang) during last year's March 2023 Pwn2Own contest in Vancouver, earning a $100,000 reward.

The researcher published a technical analysis on September 25 describing the exploitation process in detail.
Just one day later, a security researcher also released a CVE-2023-29357 proof-of-concept exploit on GitHub.

Even though the exploit does not grant remote code execution on targeted systems, since it's not a complete exploit for the chain demoed at Pwn2Own, its author said attackers could chain it with the CVE-2023-24955 bug themselves for RCE.

"The script outputs details of admin users with elevated privileges and can operate in both single and mass exploit modes," the PoC exploit's developer says.

"However, to maintain an ethical stance, this script does not contain functionalities to perform RCE and is meant solely for educational purposes and lawful and authorized testing."
Since then, other PoC exploits for this chain have surfaced online, lowering the exploitation bar and allowing even lesser-skilled threat actors to deploy it in attacks.

While it has yet to provide additional details on CVE-2023-29357 active exploitation, CISA added the vulnerability to its Known Exploited Vulnerabilities Catalog and now requires U.S. federal agencies to patch it by the end of the month, on January 31.