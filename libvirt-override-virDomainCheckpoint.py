    def getConnect(self):
        """Get the connection that owns the domain that a checkpoint was created for"""
        return self.connect()

    def getDomain(self):
        """Get the domain that a checkpoint was created for"""
        return self.domain()

    def listChildren(self, flags=0):
        """List all child checkpoints and returns a list of checkpoint objects"""
        ret = libvirtmod.virDomainCheckpointListChildren(self._o, flags)
        if ret is None:
            raise libvirtError("virDomainCheckpointListChildren() failed", conn=self)

        retlist = list()
        for chkptr in ret:
            retlist.append(virDomainCheckpoint(self, _obj=chkptr))

        return retlist
