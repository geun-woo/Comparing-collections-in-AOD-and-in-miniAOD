// -*- C++ -*-
//
// Package:    TowerMakerAnalyzer
// Class:      TowerMakerAnalyzer
// 
/**\class TowerMakerAnalyzer TowerMakerAnalyzer HiAnalysis/HiMinBias/plugins/TowerMakerAnalyzer.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Geunwoo Kim
//         Created:  Sat, 9 May 2020 03:19:07 KST
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

#include "DataFormats/CaloTowers/interface/CaloTowerCollection.h"

#include <TTree.h>
#include <TMath.h>

//
// class declaration
//
class TowerMakerAnalyzer : public edm::EDAnalyzer{
public:
  explicit TowerMakerAnalyzer(const edm::ParameterSet&);
  ~TowerMakerAnalyzer();

private:
  virtual void beginJob() override;
  virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
  virtual void endJob() override;

  // ----------member data ---------------------------
  unsigned int nEvents;

  // TFileService
  edm::Service<TFileService> fs;

  // TTree
  TTree* myTree;

  // towerMaker
  static const unsigned int Max_tower_size = 10000;
  unsigned int tower_size;
  //
  float tower_eta[Max_tower_size];
  float tower_phi[Max_tower_size];
  //
  float tower_emEt[Max_tower_size];
  float tower_hadEt[Max_tower_size];
  float tower_Et[Max_tower_size];
  //
  float tower_emEnergy[Max_tower_size];
  float tower_hadEnergy[Max_tower_size];
  float tower_Energy[Max_tower_size];
  //
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
  edm::EDGetTokenT<edm::SortedCollection<CaloTower,edm::StrictWeakOrdering<CaloTower> >> towerMakerToken_;
};

//
// constants, enums and typedefs
//

//
// static data member definitions
//

//
// constructor
//
TowerMakerAnalyzer::TowerMakerAnalyzer(const edm::ParameterSet& iConfig):
  towerMakerToken_(consumes<edm::SortedCollection<CaloTower,edm::StrictWeakOrdering<CaloTower> >>(iConfig.getParameter<edm::InputTag>("srcTowerMaker")))
{
  //now do what ever initialization is needed
  
}

//
// destructor
//
TowerMakerAnalyzer::~TowerMakerAnalyzer()
{
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)
}

void
TowerMakerAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  nEvents++;

  edm::Handle<edm::SortedCollection<CaloTower,edm::StrictWeakOrdering<CaloTower> >> collTowerMaker;
  iEvent.getByToken(towerMakerToken_, collTowerMaker);
  //
  tower_size = 0;
  n_hfPosTh2 = 0;
  n_hfPosTh3 = 0;
  n_hfPosTh4 = 0;
  n_hfPosTh5 = 0;
  n_hfNegTh2 = 0;
  n_hfNegTh3 = 0;
  n_hfNegTh4 = 0;
  n_hfNegTh5 = 0;
  //
  if(collTowerMaker.isValid()) {
    for(edm::SortedCollection<CaloTower,edm::StrictWeakOrdering<CaloTower> >::const_iterator it = collTowerMaker->begin(); it != collTowerMaker->end(); ++it) {
      //if(fabs(it->eta()) < 3.0 || fabs(it->eta()) > 5.0)continue; // only HF
      tower_eta[tower_size]    = it->eta();
      tower_phi[tower_size]    = it->phi();
      // Transverse Energy (Et; em + had) 
      tower_emEt[tower_size]   = it->emEt();
      tower_hadEt[tower_size]  = it->hadEt();
      //tower_Et[tower_size] = tower_emEt[tower_size] + tower_hadEt[tower_size];
      tower_Et[tower_size] = it->et();
      // Energy (em + had)
      tower_emEnergy[tower_size]   = it->emEnergy();
      tower_hadEnergy[tower_size]  = it->hadEnergy();
      //tower_Energy[tower_size] = tower_emEnergy[tower_size] + tower_hadEnergy[tower_size];
      tower_Energy[tower_size] = it->energy();
      //
      tower_size++;
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
      //
    }
  }
  n_hfFiltersOut[0] = TMath::Min(n_hfPosTh2, n_hfNegTh2);
  n_hfFiltersOut[1] = TMath::Min(n_hfPosTh3, n_hfNegTh3);
  n_hfFiltersOut[2] = TMath::Min(n_hfPosTh4, n_hfNegTh4);
  n_hfFiltersOut[3] = TMath::Min(n_hfPosTh5, n_hfNegTh5);

  myTree->Fill();
  return;
}

void 
TowerMakerAnalyzer::beginJob()
{
  nEvents = 0;
  //
  myTree = fs->make<TTree>("myTree","My TTree of TowerMaker");
  myTree->Branch("tower_size", &tower_size, "tower_size/i" );
  myTree->Branch("tower_eta", tower_eta, "tower_eta[tower_size]F");
  myTree->Branch("tower_phi", tower_phi, "tower_phi[tower_size]/F");
  //
  myTree->Branch("tower_emEt", tower_emEt, "tower_emEt[tower_size]/F");
  myTree->Branch("tower_hadEt", tower_hadEt, "tower_hadEt[tower_size]/F");
  myTree->Branch("tower_Et", tower_Et, "tower_Et[tower_size]/F");
  //
  myTree->Branch("tower_emEnergy", tower_emEnergy, "tower_emEnergy[tower_size]/F");
  myTree->Branch("tower_hadEnergy", tower_hadEnergy, "tower_hadEnergy[tower_size]/F");
  myTree->Branch("tower_Energy", tower_Energy, "tower_Energy[tower_size]/F");
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
  return;
}

void 
TowerMakerAnalyzer::endJob() {
  std::cout << "Total number of events = " << nEvents << std::endl;
  return;
}

DEFINE_FWK_MODULE(TowerMakerAnalyzer);