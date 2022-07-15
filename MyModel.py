from HiggsAnalysis.CombinedLimit.PhysicsModel import *
import ROOT
#My Model
"""In this model, we fit for POIs e.g. A and \mu in form of \alpha and \beta."""
class DASModel(PhysicsModel):
    def doParametersOfInterest(self):
        """Create POI and other parameters, and define the POI set."""
        self.modelBuilder.doVar("A[0,0,10]")
        self.modelBuilder.doVar("mu[0,0,10]")
        self.modelBuilder.doVar("Xs_plus[0.84]")
        self.modelBuilder.doVar("Xs_minus[0.5328]")
	self.modelBuilder.factory_('expr::alpha(\"@0*(1+@1)*(@2+@3)/(2*@2)\",mu, A,Xs_plus,Xs_minus)')
	self.modelBuilder.factory_('expr::beta(\"@0*(1-@1)*(@2+@3)/(2*@3)\",mu,A,Xs_plus,Xs_minus)')
        self.modelBuilder.doSet("POI", ",".join(['A','mu']))

    def getYieldScale(self, bin, process):
        if self.DC.isSignal[process] and process == "WminusH_htt":
            print 'Scaling %s/%s by Beta' % (bin, process)
            return "beta"
        if self.DC.isSignal[process] and process == "WplusH_htt":
            print 'Scaling %s/%s by Alpha' % (bin, process)
	    
            return "alpha"

            
        else : return 1

dasModel = DASModel()
