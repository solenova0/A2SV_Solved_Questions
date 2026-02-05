class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        count = defaultdict(int)
    
        for v in cpdomains:
            num, domain = v.split()
            num = int(num)
            
            parts = domain.split(".")
            
            for i in range(len(parts)):
                subdomain = ".".join(parts[i:])
                count[subdomain] += num
        
        return [f"{v} {k}" for k, v in count.items()]