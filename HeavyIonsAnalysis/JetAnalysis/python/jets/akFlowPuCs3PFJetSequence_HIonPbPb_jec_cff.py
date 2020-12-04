import FWCore.ParameterSet.Config as cms

from PhysicsTools.PatAlgos.mcMatchLayer0.jetMatch_cfi import patJetGenJetMatch, patJetPartonMatch
from PhysicsTools.PatAlgos.recoLayer0.jetCorrFactors_cfi import patJetCorrFactors
from PhysicsTools.PatAlgos.producersLayer1.jetProducer_cfi import patJets

from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *

from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akFlowPuCs3PFmatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akFlowPuCs3PFJets"),
    matched = cms.InputTag("ak3HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.3
    )

akFlowPuCs3PFmatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("ak3HiSignalGenJets"),
    matched = cms.InputTag("ak3HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.3
    )

akFlowPuCs3PFparton = patJetPartonMatch.clone(
    src = cms.InputTag("akFlowPuCs3PFJets"),
    matched = cms.InputTag("hiSignalGenParticles"))

akFlowPuCs3PFcorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
    levels   = cms.vstring('L2Relative'),
    src = cms.InputTag("akFlowPuCs3PFJets"),
    payload = "AK3PF"
    )

akFlowPuCs3PFJetID = cms.EDProducer(
    'JetIDProducer',
    JetIDParams,
    src = cms.InputTag('akFlowPuCs3CaloJets'))

# akFlowPuCs3PFclean = heavyIonCleanedGenJets.clone(
#     src = cms.InputTag('ak3HiSignalGenJets'))

akFlowPuCs3PFbTagger = bTaggers(
    "akFlowPuCs3PF",
    0.3)

# create objects locally since they dont load properly otherwise
akFlowPuCs3PFPatJetFlavourAssociationLegacy = akFlowPuCs3PFbTagger.PatJetFlavourAssociationLegacy
akFlowPuCs3PFPatJetPartons = akFlowPuCs3PFbTagger.PatJetPartons
akFlowPuCs3PFJetTracksAssociatorAtVertex = akFlowPuCs3PFbTagger.JetTracksAssociatorAtVertex
akFlowPuCs3PFJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akFlowPuCs3PFSimpleSecondaryVertexHighEffBJetTags = akFlowPuCs3PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akFlowPuCs3PFSimpleSecondaryVertexHighPurBJetTags = akFlowPuCs3PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akFlowPuCs3PFCombinedSecondaryVertexBJetTags = akFlowPuCs3PFbTagger.CombinedSecondaryVertexBJetTags
akFlowPuCs3PFCombinedSecondaryVertexV2BJetTags = akFlowPuCs3PFbTagger.CombinedSecondaryVertexV2BJetTags
akFlowPuCs3PFJetBProbabilityBJetTags = akFlowPuCs3PFbTagger.JetBProbabilityBJetTags
akFlowPuCs3PFSoftPFMuonByPtBJetTags = akFlowPuCs3PFbTagger.SoftPFMuonByPtBJetTags
akFlowPuCs3PFSoftPFMuonByIP3dBJetTags = akFlowPuCs3PFbTagger.SoftPFMuonByIP3dBJetTags
akFlowPuCs3PFTrackCountingHighEffBJetTags = akFlowPuCs3PFbTagger.TrackCountingHighEffBJetTags
akFlowPuCs3PFTrackCountingHighPurBJetTags = akFlowPuCs3PFbTagger.TrackCountingHighPurBJetTags
akFlowPuCs3PFPatJetPartonAssociationLegacy = akFlowPuCs3PFbTagger.PatJetPartonAssociationLegacy
akFlowPuCs3PFPatJetPartonAssociationLegacy.partons = "signalPartons"

akFlowPuCs3PFImpactParameterTagInfos = akFlowPuCs3PFbTagger.ImpactParameterTagInfos
akFlowPuCs3PFImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akFlowPuCs3PFJetProbabilityBJetTags = akFlowPuCs3PFbTagger.JetProbabilityBJetTags

akFlowPuCs3PFSecondaryVertexTagInfos = akFlowPuCs3PFbTagger.SecondaryVertexTagInfos
akFlowPuCs3PFSimpleSecondaryVertexHighEffBJetTags = akFlowPuCs3PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akFlowPuCs3PFSimpleSecondaryVertexHighPurBJetTags = akFlowPuCs3PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akFlowPuCs3PFCombinedSecondaryVertexBJetTags = akFlowPuCs3PFbTagger.CombinedSecondaryVertexBJetTags
akFlowPuCs3PFCombinedSecondaryVertexV2BJetTags = akFlowPuCs3PFbTagger.CombinedSecondaryVertexV2BJetTags

akFlowPuCs3PFSecondaryVertexNegativeTagInfos = akFlowPuCs3PFbTagger.SecondaryVertexNegativeTagInfos
akFlowPuCs3PFNegativeSimpleSecondaryVertexHighEffBJetTags = akFlowPuCs3PFbTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akFlowPuCs3PFNegativeSimpleSecondaryVertexHighPurBJetTags = akFlowPuCs3PFbTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akFlowPuCs3PFNegativeCombinedSecondaryVertexBJetTags = akFlowPuCs3PFbTagger.NegativeCombinedSecondaryVertexBJetTags
akFlowPuCs3PFPositiveCombinedSecondaryVertexBJetTags = akFlowPuCs3PFbTagger.PositiveCombinedSecondaryVertexBJetTags
akFlowPuCs3PFNegativeCombinedSecondaryVertexV2BJetTags = akFlowPuCs3PFbTagger.NegativeCombinedSecondaryVertexV2BJetTags
akFlowPuCs3PFPositiveCombinedSecondaryVertexV2BJetTags = akFlowPuCs3PFbTagger.PositiveCombinedSecondaryVertexV2BJetTags

akFlowPuCs3PFSoftPFMuonsTagInfos = akFlowPuCs3PFbTagger.SoftPFMuonsTagInfos
akFlowPuCs3PFSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akFlowPuCs3PFSoftPFMuonBJetTags = akFlowPuCs3PFbTagger.SoftPFMuonBJetTags
akFlowPuCs3PFSoftPFMuonByIP3dBJetTags = akFlowPuCs3PFbTagger.SoftPFMuonByIP3dBJetTags
akFlowPuCs3PFSoftPFMuonByPtBJetTags = akFlowPuCs3PFbTagger.SoftPFMuonByPtBJetTags
akFlowPuCs3PFNegativeSoftPFMuonByPtBJetTags = akFlowPuCs3PFbTagger.NegativeSoftPFMuonByPtBJetTags
akFlowPuCs3PFPositiveSoftPFMuonByPtBJetTags = akFlowPuCs3PFbTagger.PositiveSoftPFMuonByPtBJetTags
akFlowPuCs3PFPatJetFlavourIdLegacy = cms.Sequence(akFlowPuCs3PFPatJetPartonAssociationLegacy*akFlowPuCs3PFPatJetFlavourAssociationLegacy)
# Not working with our PU sub, but keep it here for reference
# akFlowPuCs3PFPatJetFlavourAssociation = akFlowPuCs3PFbTagger.PatJetFlavourAssociation
# akFlowPuCs3PFPatJetFlavourId = cms.Sequence(akFlowPuCs3PFPatJetPartons*akFlowPuCs3PFPatJetFlavourAssociation)

akFlowPuCs3PFJetBtaggingIP = cms.Sequence(
    akFlowPuCs3PFImpactParameterTagInfos *
    akFlowPuCs3PFTrackCountingHighEffBJetTags +
    akFlowPuCs3PFTrackCountingHighPurBJetTags +
    akFlowPuCs3PFJetProbabilityBJetTags +
    akFlowPuCs3PFJetBProbabilityBJetTags
    )

akFlowPuCs3PFJetBtaggingSV = cms.Sequence(
    akFlowPuCs3PFImpactParameterTagInfos *
    akFlowPuCs3PFSecondaryVertexTagInfos *
    akFlowPuCs3PFSimpleSecondaryVertexHighEffBJetTags +
    akFlowPuCs3PFSimpleSecondaryVertexHighPurBJetTags +
    akFlowPuCs3PFCombinedSecondaryVertexBJetTags +
    akFlowPuCs3PFCombinedSecondaryVertexV2BJetTags
    )

akFlowPuCs3PFJetBtaggingNegSV = cms.Sequence(
    akFlowPuCs3PFImpactParameterTagInfos *
    akFlowPuCs3PFSecondaryVertexNegativeTagInfos *
    akFlowPuCs3PFNegativeSimpleSecondaryVertexHighEffBJetTags +
    akFlowPuCs3PFNegativeSimpleSecondaryVertexHighPurBJetTags +
    akFlowPuCs3PFNegativeCombinedSecondaryVertexBJetTags +
    akFlowPuCs3PFPositiveCombinedSecondaryVertexBJetTags +
    akFlowPuCs3PFNegativeCombinedSecondaryVertexV2BJetTags +
    akFlowPuCs3PFPositiveCombinedSecondaryVertexV2BJetTags
    )

akFlowPuCs3PFJetBtaggingMu = cms.Sequence(
    akFlowPuCs3PFSoftPFMuonsTagInfos *
    akFlowPuCs3PFSoftPFMuonBJetTags +
    akFlowPuCs3PFSoftPFMuonByIP3dBJetTags +
    akFlowPuCs3PFSoftPFMuonByPtBJetTags +
    akFlowPuCs3PFNegativeSoftPFMuonByPtBJetTags +
    akFlowPuCs3PFPositiveSoftPFMuonByPtBJetTags
    )

akFlowPuCs3PFJetBtagging = cms.Sequence(
    akFlowPuCs3PFJetBtaggingIP
    * akFlowPuCs3PFJetBtaggingSV
    # * akFlowPuCs3PFJetBtaggingNegSV
    # * akFlowPuCs3PFJetBtaggingMu
    )

akFlowPuCs3PFpatJetsWithBtagging = patJets.clone(
    jetSource = cms.InputTag("akFlowPuCs3PFJets"),
    genJetMatch            = cms.InputTag("akFlowPuCs3PFmatch"),
    genPartonMatch         = cms.InputTag("akFlowPuCs3PFparton"),
    jetCorrFactorsSource   = cms.VInputTag(cms.InputTag("akFlowPuCs3PFcorr")),
    JetPartonMapSource     = cms.InputTag("akFlowPuCs3PFPatJetFlavourAssociationLegacy"),
    JetFlavourInfoSource   = cms.InputTag("akFlowPuCs3PFPatJetFlavourAssociation"),
    trackAssociationSource = cms.InputTag("akFlowPuCs3PFJetTracksAssociatorAtVertex"),
    useLegacyJetMCFlavour  = True,
    discriminatorSources   = cms.VInputTag(
        cms.InputTag("akFlowPuCs3PFSimpleSecondaryVertexHighEffBJetTags"),
        cms.InputTag("akFlowPuCs3PFSimpleSecondaryVertexHighPurBJetTags"),
        cms.InputTag("akFlowPuCs3PFCombinedSecondaryVertexBJetTags"),
        cms.InputTag("akFlowPuCs3PFCombinedSecondaryVertexV2BJetTags"),
        cms.InputTag("akFlowPuCs3PFJetBProbabilityBJetTags"),
        cms.InputTag("akFlowPuCs3PFJetProbabilityBJetTags"),
        # cms.InputTag("akFlowPuCs3PFSoftPFMuonByPtBJetTags"),
        # cms.InputTag("akFlowPuCs3PFSoftPFMuonByIP3dBJetTags"),
        cms.InputTag("akFlowPuCs3PFTrackCountingHighEffBJetTags"),
        cms.InputTag("akFlowPuCs3PFTrackCountingHighPurBJetTags"),
        ),
    tagInfoSources = cms.VInputTag(cms.InputTag("akFlowPuCs3PFImpactParameterTagInfos"),cms.InputTag("akFlowPuCs3PFSecondaryVertexTagInfos")),
    jetIDMap = cms.InputTag("akFlowPuCs3PFJetID"),
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

akFlowPuCs3PFNjettiness = Njettiness.clone(
    src = cms.InputTag("akFlowPuCs3PFJets"),
    R0  = cms.double(0.3)
    )

akFlowPuCs3PFpatJetsWithBtagging.userData.userFloats.src += [
    'akFlowPuCs3PFNjettiness:tau1',
    'akFlowPuCs3PFNjettiness:tau2',
    'akFlowPuCs3PFNjettiness:tau3']

akFlowPuCs3PFJetAnalyzer = inclusiveJetAnalyzer.clone(
    jetTag = cms.InputTag("akFlowPuCs3PFpatJetsWithBtagging"),
    genjetTag = 'ak3HiSignalGenJets',
    rParam = 0.3,
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
    bTagJetName = cms.untracked.string("akFlowPuCs3PF"),
    jetName = cms.untracked.string("akFlowPuCs3PF"),
    genPtMin = cms.untracked.double(5),
    hltTrgResults = cms.untracked.string('TriggerResults::'+'HISIGNAL'),
    doTower = cms.untracked.bool(True),
    doSubJets = cms.untracked.bool(False),
    doGenSubJets = cms.untracked.bool(False),
    subjetGenTag = cms.untracked.InputTag("ak3GenJets"),
    doGenTaus = cms.untracked.bool(True),
    genTau1 = cms.InputTag("ak3HiGenNjettiness","tau1"),
    genTau2 = cms.InputTag("ak3HiGenNjettiness","tau2"),
    genTau3 = cms.InputTag("ak3HiGenNjettiness","tau3"),
    doGenSym = cms.untracked.bool(False),
    genSym = cms.InputTag("ak3GenJets","sym"),
    genDroppedBranches = cms.InputTag("ak3GenJets","droppedBranches")
    )

akFlowPuCs3PFJetSequence_mc = cms.Sequence(
    # akFlowPuCs3PFclean
    # *
    akFlowPuCs3PFmatch
    # *
    # akFlowPuCs3PFmatchGroomed
    *
    akFlowPuCs3PFparton
    *
    akFlowPuCs3PFcorr
    # *
    # akFlowPuCs3PFJetID
    *
    akFlowPuCs3PFPatJetFlavourIdLegacy
    # *
    # akFlowPuCs3PFPatJetFlavourId # Use legacy algo till PU implemented
    *
    akFlowPuCs3PFJetTracksAssociatorAtVertex
    *
    akFlowPuCs3PFJetBtagging
    *
    # No constituents for calo jets in pp. Must be removed for pp calo jets but
    # I'm not sure how to do this transparently (Marta)
    akFlowPuCs3PFNjettiness
    *
    akFlowPuCs3PFpatJetsWithBtagging
    *
    akFlowPuCs3PFJetAnalyzer
    )

akFlowPuCs3PFJetSequence_data = cms.Sequence(
    akFlowPuCs3PFcorr
    *
    # akFlowPuCs3PFJetID
    # *
    akFlowPuCs3PFJetTracksAssociatorAtVertex
    *
    akFlowPuCs3PFJetBtagging
    *
    akFlowPuCs3PFNjettiness
    *
    akFlowPuCs3PFpatJetsWithBtagging
    *
    akFlowPuCs3PFJetAnalyzer
    )

akFlowPuCs3PFJetSequence_mb = cms.Sequence(
    akFlowPuCs3PFJetSequence_mc)
akFlowPuCs3PFJetSequence_jec = cms.Sequence(
    akFlowPuCs3PFJetSequence_mc)

akFlowPuCs3PFJetSequence = cms.Sequence(
    akFlowPuCs3PFJetSequence_jec)
akFlowPuCs3PFJetAnalyzer.genPtMin = cms.untracked.double(1)
akFlowPuCs3PFJetAnalyzer.jetPtMin = cms.double(1)
