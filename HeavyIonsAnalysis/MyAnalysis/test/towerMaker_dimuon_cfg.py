import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.VarParsing as VarParsing

# set up process
process = cms.Process("TowerMaker")

# setup 'analysis'  options
options = VarParsing.VarParsing ('analysis')

# Input and Output File Names
options.outputFile = "towerMaker_dimuon_myTree.root"
#options.secondaryOutputFile = ".root"
options.inputFiles = 'file:/cms/ldap_home/gekim/Data/MinBias/D993B187-FDC6-CB44-991F-CA023BDEEC00.root'
options.maxEvents = -1 # -1 means all events

# get and parse the command line arguments
options.parseArguments()

# initialize MessageLogger and output report
process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.threshold = 'INFO'
process.MessageLogger.categories.append('TowerMaker')
process.MessageLogger.cerr.INFO = cms.untracked.PSet(limit = cms.untracked.int32(-1))

process.source = cms.Source("PoolSource", fileNames = cms.untracked.vstring(options.inputFiles))

process.minbias = cms.EDAnalyzer("TowerMakerAnalyzer", srcTowerMaker = cms.InputTag("towerMaker"))

process.options          = cms.untracked.PSet(wantSummary = cms.untracked.bool(True))
process.maxEvents        = cms.untracked.PSet( input = cms.untracked.int32(options.maxEvents))
process.TFileService     = cms.Service("TFileService", fileName = cms.string(options.outputFile))
process.path             = cms.Path(process.minbias)
