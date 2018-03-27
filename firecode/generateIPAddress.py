"""
# Amazon 

You are given a String containing at least 4 numbers that represented an IPv4 Address, 
but the separator data - i.e. the dots that separate each Byte in a 4 Byte Ipv4 address, has been lost. 
Write a method - generate_ip_address that takes in this String and returns a List of strings containing all possible IPv4 Addresses 
that can be generated from the given sequence of decimal integers.
"""

# Collections module has already been imported.
def checkValidIP(ip):
    if(ip.count('.') != 3):
        return False 
    
    ip = ip.split('.')

    for seg in ip:
        if(len(seg) > 3):
            return False
            
        if(int(seg) < 0 or int(seg) > 255):
            return False
        # 00 -> False
        if(len(seg) > 1 and int(seg) == 0):
            return False 
    
    return True 


def generate_ip_address(ip):          
    if(len(ip)) > 12: 
        return []
    
    result = []
    n = len(ip)

    for i in range(1, n - 2):
        for j in range(i+1, n - 1):
            for k in range(j+1, n):
                temp = ip 
                temp = temp[:i] + "." + temp[i:j] + "." + temp[j:k] + "." + temp[k:]
                if(checkValidIP(temp)):
                    result.append(temp)
    
    return result