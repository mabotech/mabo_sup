

"""restart app/service"""

import subprocess




class Controller(object):
    """class"""
    def __init__(self):
        pass
        
    
    def listen(self):
        """listen restart command"""
        pass
        
    def alert(self):
        """send mail"""
        pass
    
def restart(service):
    
    """restart"""
    #cmd /c "net stop "Service Name" & sc start "Service Name"" ?
    cmd = "net stop %s" % (service)
    
    proc1 = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)

    output = proc1.communicate()[0]
    
    print(output)

    cmd = "net start %s" % (service)    
    
    proc2 = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)

    output = proc2.communicate()[0]    
    
    print(output)
    
    
def main():
    """test"""
    service = "_nginx_1.7.0"
    
    restart(service)
    
if __name__ == "__main__":
    main()