from HiggsAnalysis.CombinedLimit.PhysicsModel import *
import ROOT
#My Model
#In this model, we fit for POIs e.g. A and \mu in form of \alpha and \beta.
class DASModel(PhysicsModel):
    def doParametersOfInterest(self):
        """Create POI and other parameters, and define the POI set."""
        self.modelBuilder.doVar("A[0,0,10]")
        self.modelBuilder.doVar("mu[0,0,10]")
	Xs_plus = ROOT.RooRealVar("Xs_plus","", 0.84)
	Xs_minus = ROOT.RooRealVar("Xs_minus","",0.5328)
	xs_m = Xs_minus.getVal()
	xs_p = Xs_plus.getVal()
	#self.modelBuilder.factory_('expr::alpha("@0*@1*(Np+Nm)/(2*Np)",A, mu)')
	#self.modelBuilder.factory_('expr::beta("@1*(1-@0)*(Np+Nm)/(2*Nm)",A, mu)')
	#self.modelBuilder.factory_('expr::alpha(\"@0*(1+@1)*(@2+@3)/(2*@2)\",ROOT.RooArgList(mu,A,Xs_plus,Xs_minus))')
	#self.modelBuilder.factory_('expr::beta(\"@0*(1-@1)*(@2+@3)/(2*@2)\",ROOT.RooArgList(mu,A,Xs_plus,Xs_minus))')
	self.modelBuilder.factory_('expr::alpha(\"@0*(1+@1)*(0.84+0.5328)/(2*0.84)\",mu, A)')
	self.modelBuilder.factory_('expr::beta(\"@0*(1-@1)*(0.84+0.5328)/(2*0.5328)\",mu,A)')
        self.modelBuilder.doSet("POI", ",".join(['A','mu']))
        #self.modelBuilder.doSet("POI", ",".join(['r_bbH']))

    def getYieldScale(self, bin, process):
        if self.DC.isSignal[process] and process == "WminusH_htt":
            print 'Scaling %s/%s by Beta' % (bin, process)
            return "beta"
        if self.DC.isSignal[process] and process == "WplusH_htt":
            print 'Scaling %s/%s by Alpha' % (bin, process)
	    
            return "alpha"

            
        else : return 1

dasModel = DASModel()
