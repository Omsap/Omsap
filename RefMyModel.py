from HiggsAnalysis.CombinedLimit.PhysicsModel import *
import ROOT
#My Model
#In this model, we fit for POIs e.g. A and \mu in form of \alpha and \beta.
"""f_mmt_2016 = ROOT.TFile("htt_mmt_2016.input.root")
f_mmt_2017 = ROOT.TFile("htt_mmt_minus_2017.input.root")  #this file includes both plus and minus's.
f_mmt_2018 = ROOT.TFile("htt_mmt_2018.input.root")

f_mtt_2016 = ROOT.TFile("htt_mtt_2016.input.root")
f_mtt_2017 = ROOT.TFile("htt_mtt_2017.input.root")
f_mtt_2018 = ROOT.TFile("htt_mtt_2018.input.root")

f_ett_2016 = ROOT.TFile("htt_ett_2016.input.root")
f_ett_2017 = ROOT.TFile("htt_ett_2017.input.root")
f_ett_2018 = ROOT.TFile("htt_ett_2018.input.root")

f_emt_2016 = ROOT.TFile("htt_emt_2016.input.root")
f_emt_2017 = ROOT.TFile("htt_emt_2017.input.root")
f_emt_2018 = ROOT.TFile("htt_emt_2018.input.root")

channel = ["eet","emt","mtt","mmt"]
year = ["2016","2017","2018"]
Np, Nm = 0,0

h_m_mtt_2016 = f_mtt_2016.Get("mtt"+"_minus/WminusH_htt125")
h_m_mtt_2017 = f_mtt_2017.Get("mtt"+"_minus/WminusH_htt125")
h_m_mtt_2018 = f_mtt_2018.Get("mtt"+"_minus/WminusH_htt125")

h_m_ett_2016 = f_ett_2016.Get("ett"+"_minus/WminusH_htt125")
h_m_ett_2017 = f_ett_2017.Get("ett"+"_minus/WminusH_htt125")
h_m_ett_2018 = f_ett_2018.Get("ett"+"_minus/WminusH_htt125")

h_m_mmt_2016 = f_mmt_2016.Get("mmt"+"_high_minus/WminusH_htt125")
h_m_mmt_2017 = f_mmt_2017.Get("mmt"+"_high_minus/WminusH_htt125")
h_m_mmt_2018 = f_mmt_2018.Get("mmt"+"_high_minus/WminusH_htt125")

h_m_emt_2016 = f_emt_2016.Get("emt"+"_high_minus/WminusH_htt125")
h_m_emt_2017 = f_emt_2017.Get("emt"+"_high_minus/WminusH_htt125")
h_m_emt_2018 = f_emt_2018.Get("emt"+"_high_minus/WminusH_htt125")

Nm = h_m_mmt_2016.Integral() + h_m_mmt_2017.Integral() +h_m_mmt_2018.Integral() + h_m_ett_2016.Integral() + h_m_ett_2017.Integral() +h_m_ett_2018.Integral() +h_m_mmt_2016.Integral() + h_m_mtt_2017.Integral() +h_m_mtt_2018.Integral() + h_m_emt_2016.Integral() + h_m_emt_2017.Integral() +h_m_emt_2018.Integral()


h_p_mtt_2016 = f_mtt_2016.Get("mtt"+"_plus/WminusH_htt125")
h_p_mtt_2017 = f_mtt_2017.Get("mtt"+"_plus/WminusH_htt125")
h_p_mtt_2018 = f_mtt_2018.Get("mtt"+"_plus/WminusH_htt125")

h_p_ett_2016 = f_ett_2016.Get("ett"+"_plus/WminusH_htt125")
h_p_ett_2017 = f_ett_2017.Get("ett"+"_plus/WminusH_htt125")
h_p_ett_2018 = f_ett_2018.Get("ett"+"_plus/WminusH_htt125")

h_p_mmt_2016 = f_mmt_2016.Get("mmt"+"_high_plus/WminusH_htt125")
h_p_mmt_2017 = f_mmt_2017.Get("mmt"+"_high_plus/WminusH_htt125")
h_p_mmt_2018 = f_mmt_2018.Get("mmt"+"_high_plus/WminusH_htt125")

h_p_emt_2016 = f_emt_2016.Get("emt"+"_high_plus/WminusH_htt125")
h_p_emt_2017 = f_emt_2017.Get("emt"+"_high_plus/WminusH_htt125")
h_p_emt_2018 = f_emt_2018.Get("emt"+"_high_plus/WminusH_htt125")

Np = h_p_mmt_2016.Integral() + h_p_mmt_2017.Integral() +h_p_mmt_2018.Integral() + h_p_ett_2016.Integral() + h_p_ett_2017.Integral() +h_p_ett_2018.Integral() +h_p_mmt_2016.Integral() + h_p_mtt_2017.Integral() +h_p_mtt_2018.Integral() + h_p_emt_2016.Integral() + h_p_emt_2017.Integral() +h_p_emt_2018.Integral()
"""
"""for ch in channel:
	for y in year:
		

		if ch == "ett" or ch == "mtt":
			h_minus = locals()["f_"+ch+"_"+y].Get(channel+"_minus/WminusH_htt125")
			Nm += h_minus.Integral()
			h_plus = locals()["f_"+ch+"_"+y].Get(channel+"_plus/WplusH_htt125")
			Np += h_plus.Integral()
		elif ch == "emt" or ch == "mmt":
			h_minus = locals()["f_"+ch+"_"+y].Get(channel+"_high_minus/WminusH_htt125")
			Nm += h_minus.Integral()
			h_plus = locals()["f_"+ch+"_"+y].Get(channel+"_high_plus/WplusH_htt125")
			Np += h_plus.Integral()
"""
class DASModel(PhysicsModel):
    def doParametersOfInterest(self):
        """Create POI and other parameters, and define the POI set."""
        self.modelBuilder.doVar("A[0,0,10]")
        self.modelBuilder.doVar("mu[0,0,10]")
	#Xs_plus = ROOT.RooRealVar("Xs_plus","", 0.84)
	#Xs_minus = ROOT.RooRealVar("Xs_minus","",0.5328)
	#self.modelBuilder.factory_('expr::alpha("@0*@1*(Np+Nm)/(2*Np)",A, mu)')
	#self.modelBuilder.factory_('expr::beta("@1*(1-@0)*(Np+Nm)/(2*Nm)",A, mu)')
	#self.modelBuilder.factory_('expr::alpha("@0*(1+@1)*(Xs_plus+Xs_minus)/(2*Xs_plus)",mu, A)')
	#self.modelBuilder.factory_('expr::beta("@0*(1-A)*(Xs_plus+Xs_minus)/(2*Xs_minus)",mu,A)')
	self.modelBuilder.factory_('expr::alpha("@0*(1+@1)*(0.84+0.5328)/(2*0.84)",mu, A)')
	self.modelBuilder.factory_('expr::beta("@0*(1-@1)*(0.84+0.5328)/(2*0.5328)",mu,A)')
        self.modelBuilder.doSet("POI", ",".join(['A','mu']))
        #self.modelBuilder.doSet("POI", ",".join(['r_bbH']))

    def getYieldScale(self, bin, process):
        if self.DC.isSignal[process] and process == "WminusH_htt":
            print 'Scaling %s/%s by Beta' % (bin, process)
            return "beta"
        if self.DC.isSignal[process] and process == "WplusH_htt":
            print 'Scaling %s/%s by Alpha' % (bin, process)
	    
            #f_mu = ROOT.RooFormulaVar("fmu", "f*mu", "@0*@1", ROOT.RooArgList(self.modelBuilder.out.var("f"),self.modelBuilder.out.var("mu")))	     
            return "alpha"

            
        else : return 1

dasModel = DASModel()
