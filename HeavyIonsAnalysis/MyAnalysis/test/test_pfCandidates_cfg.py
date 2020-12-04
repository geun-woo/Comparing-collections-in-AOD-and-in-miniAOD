import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.VarParsing as VarParsing

# set up process
process = cms.Process("PackedPFCandidate")

# setup 'analysis'  options
options = VarParsing.VarParsing ('analysis')

# Input and Output File Names
options.outputFile = "packedPFCand_minbias_myTree.root"
#options.secondaryOutputFile = ".root"
options.inputFiles = 'file:/cms/ldap_home/gekim/Data/MinBias/reMiniAOD_DATA_PAT_MB.root'
options.maxEvents = -1 # -1 means all events

# get and parse the command line arguments
options.parseArguments()

# initialize MessageLogger and output report
process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.threshold = 'INFO'
process.MessageLogger.categories.append('PackedPFCandidate')
process.MessageLogger.cerr.INFO = cms.untracked.PSet(limit = cms.untracked.int32(-1))

process.source = cms.Source("PoolSource", fileNames = cms.untracked.vstring(options.inputFiles))

process.minbias = cms.EDAnalyzer("PackedPFCandidateAnalyzer", srcPackedPFCand = cms.InputTag("packedPFCandidates"))

process.options          = cms.untracked.PSet(wantSummary = cms.untracked.bool(True))
process.maxEvents        = cms.untracked.PSet( input = cms.untracked.int32(options.maxEvents))
process.TFileService     = cms.Service("TFileService", fileName = cms.string(options.outputFile))
process.path             = cms.Path(process.minbias)
