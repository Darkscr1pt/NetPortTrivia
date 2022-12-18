import random

# Dictionary containing protocol/service names and their corresponding port number.
# Feel free to add or remove entries as you please.
ports = {
    "Echo": "7",
    "FTP": "21",
    "SFTP": "22",
    "SSH/SCP": "22",
    "Telnet": "23",
    "SMTP (Message Relay)": "25",
    "Whois": "43",
    "TACACS": "49",
    "DNS": "53",
    "DHCP Server": "67",
    "DHCP Client": "68",
    "TFTP": "69",
    "Finger": "79",
    "HTTP": "80",
    "Kerberos": "88",
    "Microsoft Exchange (X.400)": "102",
    "POP3": "110",
    "Linux RPC": "111",
    "NTP": "123",
    "Microsoft RPC": "135",
    "NetBIOS (Name Resolution)": "137",
    "NetBIOS (Datagram Service)": "138",
    "NetBIOS (Session Service)": "139",
    "IMAP": "143",
    "SNMP (Agent)": "161",
    "SNMP (Manager)": "162",
    "BGP": "179",
    "AppleTalk": "201",
    "LDAP": "389",
    "HTTPS": "443",
    "SMTP over SSL": "465",
    "rexec": "512",
    "rlogin": "513",
    "Syslog": "514",
    "RIP": "520",
    "DHCPv6 Client": "546",
    "DHCPv6 Server": "547",
    "SMTP (Message Submission)": "587",
    "Microsoft DCOM": "593",
    "LDAP over SSL": "636",
    "Microsoft Exchange Routing Engine (RESvc)": "691",
    "iSCSI Initiator": "860",
    "VMware Server": "902",
    "FTPS Client": "989",
    "FTPS Server": "990",
    "IMAP over SSL": "993",
    "POP3 over SSL": "995",
    "OpenVPN": "1194",
    "Nessus": "1241",
    "Oracle SQL (Old)": "1521",
    "RADIUS (Authentication and Authorization)": "1812",
    "RADIUS (Accounting)": "1813",
    "NFS": "2049",
    "Oracle SQL (New)": "2483",
    "Oracle SQL over SSL (New)": "2484",
    "GLBP": "3222",
    "iSCSI Target": "3260",
    "Global Catalog": "3268",
    "MySQL": "3306",
    "RDP": "3389",
    "SIP": "5060",
    "Cisco Jabber": "5222",
    "PostgreSQL": "5432",
    "Nagios": "5666",
    "VNC": "5900",
    "X11": "6000",
    "IRC": "6667",
    "HTTP Proxy": "8080",
    "TOR": "9001",
}


def npt():
    # Score counter.
    score = 0
    while score < 20:
        # Picks a random service name from dictionary.
        service_name = random.choice(list(ports))
        print("Your score is: " + str(score) + "\n")
        print(service_name + "\n")
        port_number = input("Type the number of the port that matches the above service name: ")
        print("")
        # If the random service name and the user input exist as a pair in the dictionary, add one point to the score.
        if (service_name, port_number) in ports.items():
            print("Correct!")
            score += 1
        # Otherwise, present the correct answer and subtract one point from the score.
        else:
            answer = (ports[service_name])
            print("Wrong!")
            print("The correct answer is " + str(answer))
            score -= 1
            # If the score goes below -2 points - game over and exit application.
            if score < -2:
                print("Game over: You lost too many points.\n")
                exit()
    # If the score hits 20 points - mission accomplished and exit application.
    print("Congratulations! You've earned 20 points!")
    exit()


print("")
print("-------------------")
print("Network Port Trivia")
print("-------------------")
print("")

npt()
