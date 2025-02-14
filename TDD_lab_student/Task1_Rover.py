
class rovar(object):
 
    _LOWER_CONSTANTS = "bcdfhjklmnpqrstvwxz"
    _UPPER_CONSTANTS = "BCFGHJKLMNPQRSTVWXZ"
 
    def enrove(self, normal: str)-> str:
        """Encode the string in rovarspraket.
        Args:
            normal (str): Normal string
        Returns:
            (str) Encoded String
        """
        if normal is None:
            return None
       
        builder = ""
        for c in normal:
            if c in self._LOWER_CONSTANTS:
                builder += c+'o'+c
            elif c in self._UPPER_CONSTANTS:
                builder += c+'O'+c
            else:
                builder += c
       
        return builder
 
    def derove(self, rov:str)->str:
        """ 
            Decode a string from rovarspraket.
            Args:
                normal (str): Encoded string
            Returns:
                (str) Normal string
        """
        if rov is None:
            return None
       
        for c in self._LOWER_CONSTANTS:
            find = c+'o'+c
            rov = rov.replace(find, c)
       
        for c in self._UPPER_CONSTANTS:
            find = c+'O'+c
            rov = rov.replace(find, c)
 
        return rov
