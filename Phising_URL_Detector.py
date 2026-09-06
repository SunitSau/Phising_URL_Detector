def URLCheck(url):
    url=url.strip()
    score=0
    warn=[]
    
    if url.startswith("http://"):
        score+=1
        warn.append("Unencrptd http insted of https (secure)")

    cUrl=url.replace("https://","").replace("http://","")
    domain=cUrl.split("/")[0]
    subpart=domain.split(".")

    if len(subpart)==4:
        score+=2
        warn.append("Uses raw ip insted of domain ")

    if "@" in url:
        score+=2
        warn.append("Contains @ symbol (Offen used to obscure host).")

    if "-" in domain:
        score+=1 
        warn.append("Domain Contains hyphens (often mimics the brands).")

    Keyword=["verify","secure","update","bank","free","claim"]
    for word in Keyword:
        if word in url.lower() and not url.startswith(f"https://www.{word}.com"):
            score+=1 
            warn.append(f"Contains urgent keyword: {word}.")

    if score==0:
        status="Safe"
        print("[+] Status: Safe (No obvious red flag detected)")
    elif score<=3:
        status="Suspicious"
        print("[?] Status: Suspicious (Proced with caution)")
    else:
        status="High risk ()"
        print("[!] Status: High risk (Phising likely or malicious link)")

    if warn:
        print("Reasons:")
        for reason in warn:
            print(f"-{reason}")

    return status

#this part is to test function
link=input("Enter link to scan: ")
URLCheck(link)
