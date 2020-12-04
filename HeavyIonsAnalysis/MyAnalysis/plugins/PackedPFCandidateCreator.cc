// -*- C++ -*-
//
// Package:    PackedPFCandidate
// Class:      PackedPFCandidateCreator
// 
/**\class PackedPFCandidate PackedPFCandidateCreator HeavyIonsAnalysis/PackedPFCandidate/plugins/PackedPFCandidateCreator.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Geunwoo Kim
//         Created:  Sat, 30 May 2020 2:20:07 KST
//
//

// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/stream/EDProducer.h"
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
#include "DataFormats/Candidate/interface/Candidate.h"


class PackedPFCandidateCreator : public edm::stream::EDProducer<> {
public:
  /// constructor from parameter set
  explicit PackedPFCandidateCreator(const edm::ParameterSet&);
  /// destructor
  ~PackedPFCandidateCreator() override;

private:
  /// process one event
  void produce(edm::Event&, const edm::EventSetup&) override;
  /// verbosity
  int mVerbose;
  /// token of source collection
  edm::EDGetTokenT<std::vector<pat::PackedCandidate>> tok_src_;
  /// Et threshold
  double mEtThreshold;
  /// E threshold
  double mEThreshold;
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
PackedPFCandidateCreator::PackedPFCandidateCreator(const edm::ParameterSet& iConfig)
    : mVerbose(iConfig.getUntrackedParameter<int>("verbose", 0)),
      mEtThreshold(iConfig.getParameter<double>("minimumEt")),
      mEThreshold(iConfig.getParameter<double>("minimumE")) {
  tok_src_ = consumes<std::vector<pat::PackedCandidate>>(iConfig.getParameter<edm::InputTag>("src"));

  produces<reco::CandidateCollection>();
}

//
// destructor
//
PackedPFCandidateCreator::~PackedPFCandidateCreator()
{
  // do anything here that needs to be done at desctruction time
  // (e.g. close files, deallocate resources etc.)
}

void PackedPFCandidateCreator::produce(edm::Event& iEvent, const edm::EventSetup& iSetup) {
  edm::Handle<std::vector<pat::PackedCandidate>> packedPFCandidates;
  iEvent.getByToken(tok_src_, packedPFCandidates);

  auto cands = std::make_unique<reco::CandidateCollection>();
  cands->reserve(packedPFCandidates->size());
  int idx = 0;
   for(std::vector<pat::PackedCandidate>::const_iterator it = packedPFCandidates->begin(); it != packedPFCandidates->end(); ++it){
     const pat::PackedCandidate &pf = *it;
     if (mVerbose >= 2) {
      std::cout << "PackedPFCandidateCreator::produce-> " << idx << "PackedPFCandidates et/energy: " << pf.et() << '/' << pf.energy() << " is...";
      }
    if (pf.et() >= mEtThreshold && pf.energy() >= mEThreshold) {
      cands->push_back(pf);
      if (mVerbose >= 2)
        std::cout << "accepted: pt/eta/phi:" << pf.pt() << '/' << pf.eta() << '/' << pf.phi() << std::endl;
    }
    else {
      if (mVerbose >= 2) {
        std::cout << "rejected" << std::endl;
      }
    }
    if (mVerbose >= 1) {
      std::cout << "PackedPFCandidateCreator::produce-> " << cands->size() << " candidates created" << std::endl;
    }
    idx++;
  }
  iEvent.put(std::move(cands));
}

DEFINE_FWK_MODULE(PackedPFCandidateCreator);