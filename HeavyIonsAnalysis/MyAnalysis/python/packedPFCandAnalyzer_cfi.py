import FWCore.ParameterSet.Config as cms

packedPFCandAnalyzer = cms.EDAnalyzer(
    "PackedPFCandidateAnalyzer",
    srcPackedPFCand = cms.InputTag("packedPFCandidates")
    )