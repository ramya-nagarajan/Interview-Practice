class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        l = IP.split(".")
        print l
        size = len(l)
        if size < 4:
            #print l 
            return "Neither"
        for a in l:
            if a:
                if(len(a) > 1 and int(a) ==0): 
                    return "Neither" 
            
                if(int(a)> 255):  
                    return "Neither"    
            else:
                return "Neither"
        
        return "IPV4"
    
        
        