from HiggsAnalysis.CombinedLimit.PhysicsModel import *
import ROOT
#my simple model
#In this model, we only fit for simple POIs e.g. f and \mu.

class DASModel(PhysicsModel):
    def doParametersOfInterest(self):
        """Create POI and other parameters, and define the POI set."""
        self.modelBuilder.doVar("f[0,0,10]")
        self.modelBuilder.doVar("mu[0,0,10]")
	self.modelBuilder.factory_('expr::f_mu("@0*@1",f, mu)')
        self.modelBuilder.doSet("POI", ",".join(['f','mu']))
        #self.modelBuilder.doSet("POI", ",".join(['r_bbH']))

    def getYieldScale(self, bin, process):
        if self.DC.isSignal[process] and process == "WminusH_htt":
            print 'Scaling %s/%s by mu' % (bin, process)
            return "mu"
        if self.DC.isSignal[process] and process == "WplusH_htt":
            print 'Scaling %s/%s by f*mu' % (bin, process)
	    
            #f_mu = ROOT.RooFormulaVar("fmu", "f*mu", "@0*@1", ROOT.RooArgList(self.modelBuilder.out.var("f"),self.modelBuilder.out.var("mu")))	     
            return "f_mu"

            
        else : return 1

dasModel = DASModel()
