// -*- C++ -*-
//
// Package:    PackedPFCandidateAnalyzer
// Class:      PackedPFCandidateAnalyzer
// 
/**\class PackedPFCandidateAnalyzer PackedPFCandidateAnalyzer HiAnalysis/HiMinBias/plugins/PackedPFCandidateAnalyzer.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Geunwoo Kim
//         Created:  Wed, 13 May 2020 15:49:07 KST
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/ConsumesCollector.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/TrackReco/interface/TrackFwd.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "DataFormats/PatCandidates/interface/PackedCandidate.h"

#include <TTree.h>
#include <TMath.h>

//
// class declaration
//

class PackedPFCandidateAnalyzer : public edm::EDAnalyzer {
public:
  explicit PackedPFCandidateAnalyzer(const edm::ParameterSet&);
  ~PackedPFCandidateAnalyzer();


private:
  virtual void beginJob() override;
  virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
  virtual void endJob() override;

  virtual void beginRun(edm::Run const&, edm::EventSetup const&);
  virtual void endRun(edm::Run const&, edm::EventSetup const&);
  virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);
  virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);

  // ----------member data ---------------------------
  edm::Service<TFileService> fs;
  TTree *myTree;

  unsigned int nEvents_;
  //
  static const unsigned int Max_packedPFCand_size = 10000;
  unsigned int packedPFCand_size;
  
  float packedPFCand_eta[Max_packedPFCand_size];
  float packedPFCand_phi[Max_packedPFCand_size];
  
  float packedPFCand_emEt[Max_packedPFCand_size];
  float packedPFCand_hadEt[Max_packedPFCand_size];
  float packedPFCand_Et[Max_packedPFCand_size];
  
  float packedPFCand_emEnergy[Max_packedPFCand_size];
  float packedPFCand_hadEnergy[Max_packedPFCand_size];
  float packedPFCand_Energy[Max_packedPFCand_size];
  
  unsigned int n_hfPosTh2;
  unsigned int n_hfPosTh3;
  unsigned int n_hfPosTh4;
  unsigned int n_hfPosTh5;
  unsigned int n_hfNegTh2;
  unsigned int n_hfNegTh3;
  unsigned int n_hfNegTh4;
  unsigned int n_hfNegTh5;
  unsigned int n_hfFiltersOut[4];
  //
  edm::EDGetTokenT<std::vector<pat::PackedCandidate>> packedPFCandidateToken;
};

//
// constants, enums and typedefs
//

//
// static data member definitions
//

//
// constructors and destructor
//

PackedPFCandidateAnalyzer::PackedPFCandidateAnalyzer(const edm::ParameterSet& iConfig):
  packedPFCandidateToken(consumes<std::vector<pat::PackedCandidate>>(iConfig.getParameter<edm::InputTag>("srcPackedPFCand")))
{
  //now do what ever initialization is needed
}


PackedPFCandidateAnalyzer::~PackedPFCandidateAnalyzer()
{
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)
}



//
// member functions
//

// ------------ method called for each event  ------------
void
PackedPFCandidateAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  nEvents_++;

  edm::Handle<std::vector<pat::PackedCandidate>> collPackedPFCandidates;
  iEvent.getByToken(packedPFCandidateToken, collPackedPFCandidates);
  
  packedPFCand_size = 0;
  n_hfPosTh2 = 0;
  n_hfPosTh3 = 0;
  n_hfPosTh4 = 0;
  n_hfPosTh5 = 0;
  n_hfNegTh2 = 0;
  n_hfNegTh3 = 0;
  n_hfNegTh4 = 0;
  n_hfNegTh5 = 0;
  for(std::vector<pat::PackedCandidate>::const_iterator it = collPackedPFCandidates->begin(); it != collPackedPFCandidates->end(); ++it){
    if(it->pdgId() == 1 || it->pdgId() == 2){ //pdgId : 1 and 2 for hardronic and em particles in HF
        //if(fabs(it->eta()) < 3.0 || fabs(it->eta()) > 5.0)continue; //only HF
        packedPFCand_eta[packedPFCand_size] = it->eta();
        packedPFCand_phi[packedPFCand_size] = it->phi();
        // Transverse Energy (Et; em + had)
        if(it->pdgId() == 1)packedPFCand_hadEt[packedPFCand_size] = it->et();
        if(it->pdgId() == 2)packedPFCand_emEt[packedPFCand_size] = it->et();
        packedPFCand_Et[packedPFCand_size] = it->et();
        // Energy (em + had)
        if(it->pdgId() == 1)packedPFCand_hadEnergy[packedPFCand_size] = it->energy();
        if(it->pdgId() == 2)packedPFCand_emEnergy[packedPFCand_size] = it->energy();
        packedPFCand_Energy[packedPFCand_size] = it->energy();
        packedPFCand_size++;
        //
        if(it->pt() >= 0 && it->eta() >= 3.0 && it->eta() <= 6.0){
        if(it->et() >= 0.0 && it->energy() >= 2.0){
          n_hfPosTh2++;
        }
        if(it->et() >= 0.0 && it->energy() >= 3.0){
          n_hfPosTh3++;
        }
        if(it->et() >= 0.0 && it->energy() >= 4.0){
          n_hfPosTh4++;
        }
        if(it->et() >= 0.0 && it->energy() >= 5.0){
          n_hfPosTh5++;
        }
      }
      if(it->pt() >= 0 && it->eta() <= -3.0 && it->eta() >= -6.0){
        if(it->et() >= 0.0 && it->energy() >= 2.0){
          n_hfNegTh2++;
        }
        if(it->et() >= 0.0 && it->energy() >= 3.0){
          n_hfNegTh3++;
        }
        if(it->et() >= 0.0 && it->energy() >= 4.0){
          n_hfNegTh4++;
        }
        if(it->et() >= 0.0 && it->energy() >= 5.0){
          n_hfNegTh5++;
        }
      }
    }
  }
  
  n_hfFiltersOut[0] = TMath::Min(n_hfPosTh2, n_hfNegTh2);
  n_hfFiltersOut[1] = TMath::Min(n_hfPosTh3, n_hfNegTh3);
  n_hfFiltersOut[2] = TMath::Min(n_hfPosTh4, n_hfNegTh4);
  n_hfFiltersOut[3] = TMath::Min(n_hfPosTh5, n_hfNegTh5);

  myTree->Fill();
}

// ------------ method called once each job just before starting event loop  ------------
void 
PackedPFCandidateAnalyzer::beginJob()
{
  nEvents_ = 0;
  //
  myTree = fs->make<TTree>("myTree","My TTree of PackedPFCandidates");
  //
  myTree->Branch("packedPFCand_size", &packedPFCand_size, "packedPFCand_size/i" );
  myTree->Branch("packedPFCand_eta", packedPFCand_eta, "packedPFCand_eta[packedPFCand_size]F");
  myTree->Branch("packedPFCand_phi", packedPFCand_phi, "packedPFCand_phi[packedPFCand_size]/F");
  //
  myTree->Branch("packedPFCand_emEt", packedPFCand_emEt, "packedPFCand_emEt[packedPFCand_size]/F");
  myTree->Branch("packedPFCand_hadEt", packedPFCand_hadEt, "packedPFCand_hadEt[packedPFCand_size]/F");
  myTree->Branch("packedPFCand_Et", packedPFCand_Et, "packedPFCand_Et[packedPFCand_size]/F");
  //
  myTree->Branch("packedPFCand_emEnergy", packedPFCand_emEnergy, "packedPFCand_emEnergy[packedPFCand_size]/F");
  myTree->Branch("packedPFCand_hadEnergy", packedPFCand_hadEnergy, "packedPFCand_hadEnergy[packedPFCand_size]/F");
  myTree->Branch("packedPFCand_Energy", packedPFCand_Energy, "packedPFCand_Energy[packedPFCand_size]/F");
  //
  myTree->Branch("n_hfPosTh2", &n_hfPosTh2, "n_hfPosTh2/i" );
  myTree->Branch("n_hfPosTh3", &n_hfPosTh3, "n_hfPosTh3/i" );
  myTree->Branch("n_hfPosTh4", &n_hfPosTh4, "n_hfPosTh4/i" );
  myTree->Branch("n_hfPosTh5", &n_hfPosTh5, "n_hfPosTh5/i" );
  myTree->Branch("n_hfNegTh2", &n_hfNegTh2, "n_hfNegTh2/i" );
  myTree->Branch("n_hfNegTh3", &n_hfNegTh3, "n_hfNegTh3/i" );
  myTree->Branch("n_hfNegTh4", &n_hfNegTh4, "n_hfNegTh4/i" );
  myTree->Branch("n_hfNegTh5", &n_hfNegTh5, "n_hfNegTh5/i" );
  myTree->Branch("n_hfFiltersOut", n_hfFiltersOut, "n_hfFiltersOut[4]/i");
}

// ------------ method called once each job just after ending the event loop  ------------
void 
PackedPFCandidateAnalyzer::endJob()
{
  std::cout << "Total number of events = " << nEvents_ << std::endl;
}

// ------------ method called when starting to processes a run  ------------
void
PackedPFCandidateAnalyzer::beginRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void
PackedPFCandidateAnalyzer::endRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void
PackedPFCandidateAnalyzer::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void
PackedPFCandidateAnalyzer::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

//define this as a plug-in
DEFINE_FWK_MODULE(PackedPFCandidateAnalyzer);