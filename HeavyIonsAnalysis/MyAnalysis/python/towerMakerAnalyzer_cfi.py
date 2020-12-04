import FWCore.ParameterSet.Config as cms

towerMakerAnalyzer = cms.EDAnalyzer(
    "TowerMakerAnalyzer",
    srcTowerMaker = cms.InputTag("towerMaker")
    )