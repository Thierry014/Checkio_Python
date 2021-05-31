class Dns:
    def __init__(self, domains):
        # self.dns = [x for x in dns]  if dns is a list of domain name 
        # domains 
        self.domains = domains
    
    def update_dns(self,domain_name, new_domain_name, new_ipa):
        # check whether updated domain_name exist ? 
        if domain_name in self.domains:
            # update ip and domain => remove old, create new 
            self.domains.pop(domain_name)
            self.domains[new_domain_name] = new_ipa
        
    
    def check_matched_ipa(self,domain_name):
        for domain in self.domains.keys():
            if domain == domain_name:
                return self.domains[domain_name]
            else:
                return None


myDns = Dns({'www.google.com':'127.0.0.21' , 'www.w3cschool.com':'132.23.345.234'})

myDns.update_dns('www.google.com','www.yahoo.com','123,456,789,000')
print(myDns.check_matched_ipa('www.w3cschool.com'))
print(myDns.check_matched_ipa('www.w2cschool.com'))
print(myDns.domains)
