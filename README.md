# chroma
> [!CAUTION]
> Just like Certipy, please only use this tool in contained, lab environments, or in authorized scenarios such as penetration tests with written authorization provided by your rules of engagement. 

All in one Python script to exploit ADCS privilege escalation using [Certipy](https://github.com/ly4k/Certipy) by [ly4k](https://github.com/ly4k); methods I've seen in labs such as ESC1, ESC2, ESC3, ESC16,

Named after the one and only Chroma who was helped me a bunch through learning blue team cybersec, HTB labs, etc.

Credit is due to [ly4k](https://github.com/ly4k) who created Certipy; I only made this script because:
1. I have the time to do it.
2. Bored and wanted to make my own "tool".
3. I have consistently screwed up Certipy commands, between supplying the wrong UPN and facing odd clock-skew issues, so this is made to help me beat the horribl HTB servers and provide a more central approach to exploiting ADCS.

# agenda
I plan to write this in Python mainly using the `subprocess` module to call commands BUT I might make a Bash script alternative, or just write this in Bash entirely. Time will tell.

User runs script, selects ESC to exploit. Inputs variables such as DC IP, UPN target, authenticating user and plaintext password or hash, domain CA, etc.
Suggest evil-winrm to winrm onto DCs/other machines with port 5389 open to winrm, using hash given by Certipy.
