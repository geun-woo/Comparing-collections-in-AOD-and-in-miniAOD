import FWCore.ParameterSet.Config as cms

from PhysicsTools.PatAlgos.mcMatchLayer0.jetMatch_cfi import patJetGenJetMatch, patJetPartonMatch
from PhysicsTools.PatAlgos.recoLayer0.jetCorrFactors_cfi import patJetCorrFactors
from PhysicsTools.PatAlgos.producersLayer1.jetProducer_cfi import patJets

from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *

from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akFlowPuCs4PFmatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akFlowPuCs4PFJets"),
    matched = cms.InputTag("ak4HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.4
    )

akFlowPuCs4PFmatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("ak4HiSignalGenJets"),
    matched = cms.InputTag("ak4HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.4
    )

akFlowPuCs4PFparton = patJetPartonMatch.clone(
    src = cms.InputTag("akFlowPuCs4PFJets"),
    matched = cms.InputTag("hiSignalGenParticles"))

akFlowPuCs4PFcorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
    levels   = cms.vstring('L2Relative'),
    src = cms.InputTag("akFlowPuCs4PFJets"),
    payload = "AK4PF"
    )

akFlowPuCs4PFJetID = cms.EDProducer(
    'JetIDProducer',
    JetIDParams,
    src = cms.InputTag('akFlowPuCs4CaloJets'))

# akFlowPuCs4PFclean = heavyIonCleanedGenJets.clone(
#     src = cms.InputTag('ak4HiSignalGenJets'))

akFlowPuCs4PFbTagger = bTaggers(
    "akFlowPuCs4PF",
    0.4)

# create objects locally since they dont load properly otherwise
akFlowPuCs4PFPatJetFlavourAssociationLegacy = akFlowPuCs4PFbTagger.PatJetFlavourAssociationLegacy
akFlowPuCs4PFPatJetPartons = akFlowPuCs4PFbTagger.PatJetPartons
akFlowPuCs4PFJetTracksAssociatorAtVertex = akFlowPuCs4PFbTagger.JetTracksAssociatorAtVertex
akFlowPuCs4PFJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akFlowPuCs4PFSimpleSecondaryVertexHighEffBJetTags = akFlowPuCs4PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akFlowPuCs4PFSimpleSecondaryVertexHighPurBJetTags = akFlowPuCs4PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akFlowPuCs4PFCombinedSecondaryVertexBJetTags = akFlowPuCs4PFbTagger.CombinedSecondaryVertexBJetTags
akFlowPuCs4PFCombinedSecondaryVertexV2BJetTags = akFlowPuCs4PFbTagger.CombinedSecondaryVertexV2BJetTags
akFlowPuCs4PFJetBProbabilityBJetTags = akFlowPuCs4PFbTagger.JetBProbabilityBJetTags
akFlowPuCs4PFSoftPFMuonByPtBJetTags = akFlowPuCs4PFbTagger.SoftPFMuonByPtBJetTags
akFlowPuCs4PFSoftPFMuonByIP3dBJetTags = akFlowPuCs4PFbTagger.SoftPFMuonByIP3dBJetTags
akFlowPuCs4PFTrackCountingHighEffBJetTags = akFlowPuCs4PFbTagger.TrackCountingHighEffBJetTags
akFlowPuCs4PFTrackCountingHighPurBJetTags = akFlowPuCs4PFbTagger.TrackCountingHighPurBJetTags
akFlowPuCs4PFPatJetPartonAssociationLegacy = akFlowPuCs4PFbTagger.PatJetPartonAssociationLegacy
akFlowPuCs4PFPatJetPartonAssociationLegacy.partons = "signalPartons"

akFlowPuCs4PFImpactParameterTagInfos = akFlowPuCs4PFbTagger.ImpactParameterTagInfos
akFlowPuCs4PFImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akFlowPuCs4PFJetProbabilityBJetTags = akFlowPuCs4PFbTagger.JetProbabilityBJetTags

akFlowPuCs4PFSecondaryVertexTagInfos = akFlowPuCs4PFbTagger.SecondaryVertexTagInfos
akFlowPuCs4PFSimpleSecondaryVertexHighEffBJetTags = akFlowPuCs4PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akFlowPuCs4PFSimpleSecondaryVertexHighPurBJetTags = akFlowPuCs4PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akFlowPuCs4PFCombinedSecondaryVertexBJetTags = akFlowPuCs4PFbTagger.CombinedSecondaryVertexBJetTags
akFlowPuCs4PFCombinedSecondaryVertexV2BJetTags = akFlowPuCs4PFbTagger.CombinedSecondaryVertexV2BJetTags

akFlowPuCs4PFSecondaryVertexNegativeTagInfos = akFlowPuCs4PFbTagger.SecondaryVertexNegativeTagInfos
akFlowPuCs4PFNegativeSimpleSecondaryVertexHighEffBJetTags = akFlowPuCs4PFbTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akFlowPuCs4PFNegativeSimpleSecondaryVertexHighPurBJetTags = akFlowPuCs4PFbTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akFlowPuCs4PFNegativeCombinedSecondaryVertexBJetTags = akFlowPuCs4PFbTagger.NegativeCombinedSecondaryVertexBJetTags
akFlowPuCs4PFPositiveCombinedSecondaryVertexBJetTags = akFlowPuCs4PFbTagger.PositiveCombinedSecondaryVertexBJetTags
akFlowPuCs4PFNegativeCombinedSecondaryVertexV2BJetTags = akFlowPuCs4PFbTagger.NegativeCombinedSecondaryVertexV2BJetTags
akFlowPuCs4PFPositiveCombinedSecondaryVertexV2BJetTags = akFlowPuCs4PFbTagger.PositiveCombinedSecondaryVertexV2BJetTags

akFlowPuCs4PFSoftPFMuonsTagInfos = akFlowPuCs4PFbTagger.SoftPFMuonsTagInfos
akFlowPuCs4PFSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akFlowPuCs4PFSoftPFMuonBJetTags = akFlowPuCs4PFbTagger.SoftPFMuonBJetTags
akFlowPuCs4PFSoftPFMuonByIP3dBJetTags = akFlowPuCs4PFbTagger.SoftPFMuonByIP3dBJetTags
akFlowPuCs4PFSoftPFMuonByPtBJetTags = akFlowPuCs4PFbTagger.SoftPFMuonByPtBJetTags
akFlowPuCs4PFNegativeSoftPFMuonByPtBJetTags = akFlowPuCs4PFbTagger.NegativeSoftPFMuonByPtBJetTags
akFlowPuCs4PFPositiveSoftPFMuonByPtBJetTags = akFlowPuCs4PFbTagger.PositiveSoftPFMuonByPtBJetTags
akFlowPuCs4PFPatJetFlavourIdLegacy = cms.Sequence(akFlowPuCs4PFPatJetPartonAssociationLegacy*akFlowPuCs4PFPatJetFlavourAssociationLegacy)
# Not working with our PU sub, but keep it here for reference
# akFlowPuCs4PFPatJetFlavourAssociation = akFlowPuCs4PFbTagger.PatJetFlavourAssociation
# akFlowPuCs4PFPatJetFlavourId = cms.Sequence(akFlowPuCs4PFPatJetPartons*akFlowPuCs4PFPatJetFlavourAssociation)

akFlowPuCs4PFJetBtaggingIP = cms.Sequence(
    akFlowPuCs4PFImpactParameterTagInfos *
    akFlowPuCs4PFTrackCountingHighEffBJetTags +
    akFlowPuCs4PFTrackCountingHighPurBJetTags +
    akFlowPuCs4PFJetProbabilityBJetTags +
    akFlowPuCs4PFJetBProbabilityBJetTags
    )

akFlowPuCs4PFJetBtaggingSV = cms.Sequence(
    akFlowPuCs4PFImpactParameterTagInfos *
    akFlowPuCs4PFSecondaryVertexTagInfos *
    akFlowPuCs4PFSimpleSecondaryVertexHighEffBJetTags +
    akFlowPuCs4PFSimpleSecondaryVertexHighPurBJetTags +
    akFlowPuCs4PFCombinedSecondaryVertexBJetTags +
    akFlowPuCs4PFCombinedSecondaryVertexV2BJetTags
    )

akFlowPuCs4PFJetBtaggingNegSV = cms.Sequence(
    akFlowPuCs4PFImpactParameterTagInfos *
    akFlowPuCs4PFSecondaryVertexNegativeTagInfos *
    akFlowPuCs4PFNegativeSimpleSecondaryVertexHighEffBJetTags +
    akFlowPuCs4PFNegativeSimpleSecondaryVertexHighPurBJetTags +
    akFlowPuCs4PFNegativeCombinedSecondaryVertexBJetTags +
    akFlowPuCs4PFPositiveCombinedSecondaryVertexBJetTags +
    akFlowPuCs4PFNegativeCombinedSecondaryVertexV2BJetTags +
    akFlowPuCs4PFPositiveCombinedSecondaryVertexV2BJetTags
    )

akFlowPuCs4PFJetBtaggingMu = cms.Sequence(
    akFlowPuCs4PFSoftPFMuonsTagInfos *
    akFlowPuCs4PFSoftPFMuonBJetTags +
    akFlowPuCs4PFSoftPFMuonByIP3dBJetTags +
    akFlowPuCs4PFSoftPFMuonByPtBJetTags +
    akFlowPuCs4PFNegativeSoftPFMuonByPtBJetTags +
    akFlowPuCs4PFPositiveSoftPFMuonByPtBJetTags
    )

akFlowPuCs4PFJetBtagging = cms.Sequence(
    akFlowPuCs4PFJetBtaggingIP
    * akFlowPuCs4PFJetBtaggingSV
    # * akFlowPuCs4PFJetBtaggingNegSV
    # * akFlowPuCs4PFJetBtaggingMu
    )

akFlowPuCs4PFpatJetsWithBtagging = patJets.clone(
    jetSource = cms.InputTag("akFlowPuCs4PFJets"),
    genJetMatch            = cms.InputTag("akFlowPuCs4PFmatch"),
    genPartonMatch         = cms.InputTag("akFlowPuCs4PFparton"),
    jetCorrFactorsSource   = cms.VInputTag(cms.InputTag("akFlowPuCs4PFcorr")),
    JetPartonMapSource     = cms.InputTag("akFlowPuCs4PFPatJetFlavourAssociationLegacy"),
    JetFlavourInfoSource   = cms.InputTag("akFlowPuCs4PFPatJetFlavourAssociation"),
    trackAssociationSource = cms.InputTag("akFlowPuCs4PFJetTracksAssociatorAtVertex"),
    useLegacyJetMCFlavour  = True,
    discriminatorSources   = cms.VInputTag(
        cms.InputTag("akFlowPuCs4PFSimpleSecondaryVertexHighEffBJetTags"),
        cms.InputTag("akFlowPuCs4PFSimpleSecondaryVertexHighPurBJetTags"),
        cms.InputTag("akFlowPuCs4PFCombinedSecondaryVertexBJetTags"),
        cms.InputTag("akFlowPuCs4PFCombinedSecondaryVertexV2BJetTags"),
        cms.InputTag("akFlowPuCs4PFJetBProbabilityBJetTags"),
        cms.InputTag("akFlowPuCs4PFJetProbabilityBJetTags"),
        # cms.InputTag("akFlowPuCs4PFSoftPFMuonByPtBJetTags"),
        # cms.InputTag("akFlowPuCs4PFSoftPFMuonByIP3dBJetTags"),
        cms.InputTag("akFlowPuCs4PFTrackCountingHighEffBJetTags"),
        cms.InputTag("akFlowPuCs4PFTrackCountingHighPurBJetTags"),
        ),
    tagInfoSources = cms.VInputTag(cms.InputTag("akFlowPuCs4PFImpactParameterTagInfos"),cms.InputTag("akFlowPuCs4PFSecondaryVertexTagInfos")),
    jetIDMap = cms.InputTag("akFlowPuCs4PFJetID"),
    addBTagInfo = True,
    addTagInfos = True,
    addDiscriminators = True,
    addAssociatedTracks = True,
    addJetCharge = False,
    addJetID = False,
    getJetMCFlavour = True,
    addGenPartonMatch = True,
    addGenJetMatch = True,
    embedGenJetMatch = True,
    embedGenPartonMatch = True,
    # embedCaloTowers = False,
    # embedPFCandidates = True
    )

akFlowPuCs4PFNjettiness = Njettiness.clone(
    src = cms.InputTag("akFlowPuCs4PFJets"),
    R0  = cms.double(0.4)
    )

akFlowPuCs4PFpatJetsWithBtagging.userData.userFloats.src += [
    'akFlowPuCs4PFNjettiness:tau1',
    'akFlowPuCs4PFNjettiness:tau2',
    'akFlowPuCs4PFNjettiness:tau3']

akFlowPuCs4PFJetAnalyzer = inclusiveJetAnalyzer.clone(
    jetTag = cms.InputTag("akFlowPuCs4PFpatJetsWithBtagging"),
    genjetTag = 'ak4HiSignalGenJets',
    rParam = 0.4,
    matchJets = cms.untracked.bool(False),
    matchTag = 'patJetsWithBtagging',
    pfCandidateLabel = cms.untracked.InputTag('particleFlowTmp'),
    trackTag = cms.InputTag("hiGeneralTracks"),
    fillGenJets = True,
    isMC = True,
    doSubEvent = True,
    useHepMC = cms.untracked.bool(False),
    genParticles = cms.untracked.InputTag("genParticles"),
    eventInfoTag = cms.InputTag("generator"),
    doLifeTimeTagging = cms.untracked.bool(True),
    doLifeTimeTaggingExtras = cms.untracked.bool(False),
    bTagJetName = cms.untracked.string("akFlowPuCs4PF"),
    jetName = cms.untracked.string("akFlowPuCs4PF"),
    genPtMin = cms.untracked.double(5),
    hltTrgResults = cms.untracked.string('TriggerResults::'+'HISIGNAL'),
    doTower = cms.untracked.bool(True),
    doSubJets = cms.untracked.bool(False),
    doGenSubJets = cms.untracked.bool(False),
    subjetGenTag = cms.untracked.InputTag("ak4GenJets"),
    doGenTaus = cms.untracked.bool(True),
    genTau1 = cms.InputTag("ak4HiGenNjettiness","tau1"),
    genTau2 = cms.InputTag("ak4HiGenNjettiness","tau2"),
    genTau3 = cms.InputTag("ak4HiGenNjettiness","tau3"),
    doGenSym = cms.untracked.bool(False),
    genSym = cms.InputTag("ak4GenJets","sym"),
    genDroppedBranches = cms.InputTag("ak4GenJets","droppedBranches")
    )

akFlowPuCs4PFJetSequence_mc = cms.Sequence(
    # akFlowPuCs4PFclean
    # *
    akFlowPuCs4PFmatch
    # *
    # akFlowPuCs4PFmatchGroomed
    *
    akFlowPuCs4PFparton
    *
    akFlowPuCs4PFcorr
    # *
    # akFlowPuCs4PFJetID
    *
    akFlowPuCs4PFPatJetFlavourIdLegacy
    # *
    # akFlowPuCs4PFPatJetFlavourId # Use legacy algo till PU implemented
    *
    akFlowPuCs4PFJetTracksAssociatorAtVertex
    *
    akFlowPuCs4PFJetBtagging
    *
    # No constituents for calo jets in pp. Must be removed for pp calo jets but
    # I'm not sure how to do this transparently (Marta)
    akFlowPuCs4PFNjettiness
    *
    akFlowPuCs4PFpatJetsWithBtagging
    *
    akFlowPuCs4PFJetAnalyzer
    )

akFlowPuCs4PFJetSequence_data = cms.Sequence(
    akFlowPuCs4PFcorr
    *
    # akFlowPuCs4PFJetID
    # *
    akFlowPuCs4PFJetTracksAssociatorAtVertex
    *
    akFlowPuCs4PFJetBtagging
    *
    akFlowPuCs4PFNjettiness
    *
    akFlowPuCs4PFpatJetsWithBtagging
    *
    akFlowPuCs4PFJetAnalyzer
    )

akFlowPuCs4PFJetSequence_mb = cms.Sequence(
    akFlowPuCs4PFJetSequence_mc)
akFlowPuCs4PFJetSequence_jec = cms.Sequence(
    akFlowPuCs4PFJetSequence_mc)

akFlowPuCs4PFJetSequence = cms.Sequence(
    akFlowPuCs4PFJetSequence_mc)
