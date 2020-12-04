import FWCore.ParameterSet.Config as cms

from PhysicsTools.PatAlgos.mcMatchLayer0.jetMatch_cfi import patJetGenJetMatch, patJetPartonMatch
from PhysicsTools.PatAlgos.recoLayer0.jetCorrFactors_cfi import patJetCorrFactors
from PhysicsTools.PatAlgos.producersLayer1.jetProducer_cfi import patJets

from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *

from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akFlowPuCs5PFmatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akFlowPuCs5PFJets"),
    matched = cms.InputTag("ak5HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.5
    )

akFlowPuCs5PFmatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("ak5HiSignalGenJets"),
    matched = cms.InputTag("ak5HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.5
    )

akFlowPuCs5PFparton = patJetPartonMatch.clone(
    src = cms.InputTag("akFlowPuCs5PFJets"),
    matched = cms.InputTag("hiSignalGenParticles"))

akFlowPuCs5PFcorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
    levels   = cms.vstring('L2Relative','L2L3Residual'),
    src = cms.InputTag("akFlowPuCs5PFJets"),
    payload = "AK5PF"
    )

akFlowPuCs5PFJetID = cms.EDProducer(
    'JetIDProducer',
    JetIDParams,
    src = cms.InputTag('akFlowPuCs5CaloJets'))

# akFlowPuCs5PFclean = heavyIonCleanedGenJets.clone(
#     src = cms.InputTag('ak5HiSignalGenJets'))

akFlowPuCs5PFbTagger = bTaggers(
    "akFlowPuCs5PF",
    0.5)

# create objects locally since they dont load properly otherwise
akFlowPuCs5PFPatJetFlavourAssociationLegacy = akFlowPuCs5PFbTagger.PatJetFlavourAssociationLegacy
akFlowPuCs5PFPatJetPartons = akFlowPuCs5PFbTagger.PatJetPartons
akFlowPuCs5PFJetTracksAssociatorAtVertex = akFlowPuCs5PFbTagger.JetTracksAssociatorAtVertex
akFlowPuCs5PFJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akFlowPuCs5PFSimpleSecondaryVertexHighEffBJetTags = akFlowPuCs5PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akFlowPuCs5PFSimpleSecondaryVertexHighPurBJetTags = akFlowPuCs5PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akFlowPuCs5PFCombinedSecondaryVertexBJetTags = akFlowPuCs5PFbTagger.CombinedSecondaryVertexBJetTags
akFlowPuCs5PFCombinedSecondaryVertexV2BJetTags = akFlowPuCs5PFbTagger.CombinedSecondaryVertexV2BJetTags
akFlowPuCs5PFJetBProbabilityBJetTags = akFlowPuCs5PFbTagger.JetBProbabilityBJetTags
akFlowPuCs5PFSoftPFMuonByPtBJetTags = akFlowPuCs5PFbTagger.SoftPFMuonByPtBJetTags
akFlowPuCs5PFSoftPFMuonByIP3dBJetTags = akFlowPuCs5PFbTagger.SoftPFMuonByIP3dBJetTags
akFlowPuCs5PFTrackCountingHighEffBJetTags = akFlowPuCs5PFbTagger.TrackCountingHighEffBJetTags
akFlowPuCs5PFTrackCountingHighPurBJetTags = akFlowPuCs5PFbTagger.TrackCountingHighPurBJetTags
akFlowPuCs5PFPatJetPartonAssociationLegacy = akFlowPuCs5PFbTagger.PatJetPartonAssociationLegacy
akFlowPuCs5PFPatJetPartonAssociationLegacy.partons = "signalPartons"

akFlowPuCs5PFImpactParameterTagInfos = akFlowPuCs5PFbTagger.ImpactParameterTagInfos
akFlowPuCs5PFImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akFlowPuCs5PFJetProbabilityBJetTags = akFlowPuCs5PFbTagger.JetProbabilityBJetTags

akFlowPuCs5PFSecondaryVertexTagInfos = akFlowPuCs5PFbTagger.SecondaryVertexTagInfos
akFlowPuCs5PFSimpleSecondaryVertexHighEffBJetTags = akFlowPuCs5PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akFlowPuCs5PFSimpleSecondaryVertexHighPurBJetTags = akFlowPuCs5PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akFlowPuCs5PFCombinedSecondaryVertexBJetTags = akFlowPuCs5PFbTagger.CombinedSecondaryVertexBJetTags
akFlowPuCs5PFCombinedSecondaryVertexV2BJetTags = akFlowPuCs5PFbTagger.CombinedSecondaryVertexV2BJetTags

akFlowPuCs5PFSecondaryVertexNegativeTagInfos = akFlowPuCs5PFbTagger.SecondaryVertexNegativeTagInfos
akFlowPuCs5PFNegativeSimpleSecondaryVertexHighEffBJetTags = akFlowPuCs5PFbTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akFlowPuCs5PFNegativeSimpleSecondaryVertexHighPurBJetTags = akFlowPuCs5PFbTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akFlowPuCs5PFNegativeCombinedSecondaryVertexBJetTags = akFlowPuCs5PFbTagger.NegativeCombinedSecondaryVertexBJetTags
akFlowPuCs5PFPositiveCombinedSecondaryVertexBJetTags = akFlowPuCs5PFbTagger.PositiveCombinedSecondaryVertexBJetTags
akFlowPuCs5PFNegativeCombinedSecondaryVertexV2BJetTags = akFlowPuCs5PFbTagger.NegativeCombinedSecondaryVertexV2BJetTags
akFlowPuCs5PFPositiveCombinedSecondaryVertexV2BJetTags = akFlowPuCs5PFbTagger.PositiveCombinedSecondaryVertexV2BJetTags

akFlowPuCs5PFSoftPFMuonsTagInfos = akFlowPuCs5PFbTagger.SoftPFMuonsTagInfos
akFlowPuCs5PFSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akFlowPuCs5PFSoftPFMuonBJetTags = akFlowPuCs5PFbTagger.SoftPFMuonBJetTags
akFlowPuCs5PFSoftPFMuonByIP3dBJetTags = akFlowPuCs5PFbTagger.SoftPFMuonByIP3dBJetTags
akFlowPuCs5PFSoftPFMuonByPtBJetTags = akFlowPuCs5PFbTagger.SoftPFMuonByPtBJetTags
akFlowPuCs5PFNegativeSoftPFMuonByPtBJetTags = akFlowPuCs5PFbTagger.NegativeSoftPFMuonByPtBJetTags
akFlowPuCs5PFPositiveSoftPFMuonByPtBJetTags = akFlowPuCs5PFbTagger.PositiveSoftPFMuonByPtBJetTags
akFlowPuCs5PFPatJetFlavourIdLegacy = cms.Sequence(akFlowPuCs5PFPatJetPartonAssociationLegacy*akFlowPuCs5PFPatJetFlavourAssociationLegacy)
# Not working with our PU sub, but keep it here for reference
# akFlowPuCs5PFPatJetFlavourAssociation = akFlowPuCs5PFbTagger.PatJetFlavourAssociation
# akFlowPuCs5PFPatJetFlavourId = cms.Sequence(akFlowPuCs5PFPatJetPartons*akFlowPuCs5PFPatJetFlavourAssociation)

akFlowPuCs5PFJetBtaggingIP = cms.Sequence(
    akFlowPuCs5PFImpactParameterTagInfos *
    akFlowPuCs5PFTrackCountingHighEffBJetTags +
    akFlowPuCs5PFTrackCountingHighPurBJetTags +
    akFlowPuCs5PFJetProbabilityBJetTags +
    akFlowPuCs5PFJetBProbabilityBJetTags
    )

akFlowPuCs5PFJetBtaggingSV = cms.Sequence(
    akFlowPuCs5PFImpactParameterTagInfos *
    akFlowPuCs5PFSecondaryVertexTagInfos *
    akFlowPuCs5PFSimpleSecondaryVertexHighEffBJetTags +
    akFlowPuCs5PFSimpleSecondaryVertexHighPurBJetTags +
    akFlowPuCs5PFCombinedSecondaryVertexBJetTags +
    akFlowPuCs5PFCombinedSecondaryVertexV2BJetTags
    )

akFlowPuCs5PFJetBtaggingNegSV = cms.Sequence(
    akFlowPuCs5PFImpactParameterTagInfos *
    akFlowPuCs5PFSecondaryVertexNegativeTagInfos *
    akFlowPuCs5PFNegativeSimpleSecondaryVertexHighEffBJetTags +
    akFlowPuCs5PFNegativeSimpleSecondaryVertexHighPurBJetTags +
    akFlowPuCs5PFNegativeCombinedSecondaryVertexBJetTags +
    akFlowPuCs5PFPositiveCombinedSecondaryVertexBJetTags +
    akFlowPuCs5PFNegativeCombinedSecondaryVertexV2BJetTags +
    akFlowPuCs5PFPositiveCombinedSecondaryVertexV2BJetTags
    )

akFlowPuCs5PFJetBtaggingMu = cms.Sequence(
    akFlowPuCs5PFSoftPFMuonsTagInfos *
    akFlowPuCs5PFSoftPFMuonBJetTags +
    akFlowPuCs5PFSoftPFMuonByIP3dBJetTags +
    akFlowPuCs5PFSoftPFMuonByPtBJetTags +
    akFlowPuCs5PFNegativeSoftPFMuonByPtBJetTags +
    akFlowPuCs5PFPositiveSoftPFMuonByPtBJetTags
    )

akFlowPuCs5PFJetBtagging = cms.Sequence(
    akFlowPuCs5PFJetBtaggingIP
    * akFlowPuCs5PFJetBtaggingSV
    # * akFlowPuCs5PFJetBtaggingNegSV
    # * akFlowPuCs5PFJetBtaggingMu
    )

akFlowPuCs5PFpatJetsWithBtagging = patJets.clone(
    jetSource = cms.InputTag("akFlowPuCs5PFJets"),
    genJetMatch            = cms.InputTag("akFlowPuCs5PFmatch"),
    genPartonMatch         = cms.InputTag("akFlowPuCs5PFparton"),
    jetCorrFactorsSource   = cms.VInputTag(cms.InputTag("akFlowPuCs5PFcorr")),
    JetPartonMapSource     = cms.InputTag("akFlowPuCs5PFPatJetFlavourAssociationLegacy"),
    JetFlavourInfoSource   = cms.InputTag("akFlowPuCs5PFPatJetFlavourAssociation"),
    trackAssociationSource = cms.InputTag("akFlowPuCs5PFJetTracksAssociatorAtVertex"),
    useLegacyJetMCFlavour  = True,
    discriminatorSources   = cms.VInputTag(
        cms.InputTag("akFlowPuCs5PFSimpleSecondaryVertexHighEffBJetTags"),
        cms.InputTag("akFlowPuCs5PFSimpleSecondaryVertexHighPurBJetTags"),
        cms.InputTag("akFlowPuCs5PFCombinedSecondaryVertexBJetTags"),
        cms.InputTag("akFlowPuCs5PFCombinedSecondaryVertexV2BJetTags"),
        cms.InputTag("akFlowPuCs5PFJetBProbabilityBJetTags"),
        cms.InputTag("akFlowPuCs5PFJetProbabilityBJetTags"),
        # cms.InputTag("akFlowPuCs5PFSoftPFMuonByPtBJetTags"),
        # cms.InputTag("akFlowPuCs5PFSoftPFMuonByIP3dBJetTags"),
        cms.InputTag("akFlowPuCs5PFTrackCountingHighEffBJetTags"),
        cms.InputTag("akFlowPuCs5PFTrackCountingHighPurBJetTags"),
        ),
    tagInfoSources = cms.VInputTag(cms.InputTag("akFlowPuCs5PFImpactParameterTagInfos"),cms.InputTag("akFlowPuCs5PFSecondaryVertexTagInfos")),
    jetIDMap = cms.InputTag("akFlowPuCs5PFJetID"),
    addBTagInfo = True,
    addTagInfos = True,
    addDiscriminators = True,
    addAssociatedTracks = True,
    addJetCharge = False,
    addJetID = False,
    getJetMCFlavour = False,
    addGenPartonMatch = False,
    addGenJetMatch = False,
    embedGenJetMatch = False,
    embedGenPartonMatch = False,
    # embedCaloTowers = False,
    # embedPFCandidates = True
    )

akFlowPuCs5PFNjettiness = Njettiness.clone(
    src = cms.InputTag("akFlowPuCs5PFJets"),
    R0  = cms.double(0.5)
    )

akFlowPuCs5PFpatJetsWithBtagging.userData.userFloats.src += [
    'akFlowPuCs5PFNjettiness:tau1',
    'akFlowPuCs5PFNjettiness:tau2',
    'akFlowPuCs5PFNjettiness:tau3']

akFlowPuCs5PFJetAnalyzer = inclusiveJetAnalyzer.clone(
    jetTag = cms.InputTag("akFlowPuCs5PFpatJetsWithBtagging"),
    genjetTag = 'ak5HiSignalGenJets',
    rParam = 0.5,
    matchJets = cms.untracked.bool(False),
    matchTag = 'patJetsWithBtagging',
    pfCandidateLabel = cms.untracked.InputTag('particleFlow'),
    trackTag = cms.InputTag("generalTracks"),
    fillGenJets = False,
    isMC = False,
    doSubEvent = False,
    useHepMC = cms.untracked.bool(False),
    genParticles = cms.untracked.InputTag("genParticles"),
    eventInfoTag = cms.InputTag("generator"),
    doLifeTimeTagging = cms.untracked.bool(True),
    doLifeTimeTaggingExtras = cms.untracked.bool(False),
    bTagJetName = cms.untracked.string("akFlowPuCs5PF"),
    jetName = cms.untracked.string("akFlowPuCs5PF"),
    genPtMin = cms.untracked.double(5),
    hltTrgResults = cms.untracked.string('TriggerResults::'+'HISIGNAL'),
    doTower = cms.untracked.bool(False),
    doSubJets = cms.untracked.bool(False),
    doGenSubJets = cms.untracked.bool(False),
    subjetGenTag = cms.untracked.InputTag("ak5GenJets"),
    doGenTaus = cms.untracked.bool(False),
    genTau1 = cms.InputTag("ak5HiGenNjettiness","tau1"),
    genTau2 = cms.InputTag("ak5HiGenNjettiness","tau2"),
    genTau3 = cms.InputTag("ak5HiGenNjettiness","tau3"),
    doGenSym = cms.untracked.bool(False),
    genSym = cms.InputTag("ak5GenJets","sym"),
    genDroppedBranches = cms.InputTag("ak5GenJets","droppedBranches")
    )

akFlowPuCs5PFJetSequence_mc = cms.Sequence(
    # akFlowPuCs5PFclean
    # *
    akFlowPuCs5PFmatch
    # *
    # akFlowPuCs5PFmatchGroomed
    *
    akFlowPuCs5PFparton
    *
    akFlowPuCs5PFcorr
    # *
    # akFlowPuCs5PFJetID
    *
    akFlowPuCs5PFPatJetFlavourIdLegacy
    # *
    # akFlowPuCs5PFPatJetFlavourId # Use legacy algo till PU implemented
    *
    akFlowPuCs5PFJetTracksAssociatorAtVertex
    *
    akFlowPuCs5PFJetBtagging
    *
    # No constituents for calo jets in pp. Must be removed for pp calo jets but
    # I'm not sure how to do this transparently (Marta)
    akFlowPuCs5PFNjettiness
    *
    akFlowPuCs5PFpatJetsWithBtagging
    *
    akFlowPuCs5PFJetAnalyzer
    )

akFlowPuCs5PFJetSequence_data = cms.Sequence(
    akFlowPuCs5PFcorr
    *
    # akFlowPuCs5PFJetID
    # *
    akFlowPuCs5PFJetTracksAssociatorAtVertex
    *
    akFlowPuCs5PFJetBtagging
    *
    akFlowPuCs5PFNjettiness
    *
    akFlowPuCs5PFpatJetsWithBtagging
    *
    akFlowPuCs5PFJetAnalyzer
    )

akFlowPuCs5PFJetSequence_mb = cms.Sequence(
    akFlowPuCs5PFJetSequence_mc)
akFlowPuCs5PFJetSequence_jec = cms.Sequence(
    akFlowPuCs5PFJetSequence_mc)

akFlowPuCs5PFJetSequence = cms.Sequence(
    akFlowPuCs5PFJetSequence_data)
