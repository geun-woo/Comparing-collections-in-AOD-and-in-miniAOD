import FWCore.ParameterSet.Config as cms

from PhysicsTools.PatAlgos.mcMatchLayer0.jetMatch_cfi import patJetGenJetMatch, patJetPartonMatch
from PhysicsTools.PatAlgos.recoLayer0.jetCorrFactors_cfi import patJetCorrFactors
from PhysicsTools.PatAlgos.producersLayer1.jetProducer_cfi import patJets

from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *

from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akFlowPuCs2PFmatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akFlowPuCs2PFJets"),
    matched = cms.InputTag("ak2GenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.2
    )

akFlowPuCs2PFmatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("ak2GenJets"),
    matched = cms.InputTag("ak2GenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.2
    )

akFlowPuCs2PFparton = patJetPartonMatch.clone(
    src = cms.InputTag("akFlowPuCs2PFJets"),
    matched = cms.InputTag("genParticles"))

akFlowPuCs2PFcorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
    levels   = cms.vstring('L2Relative','L2L3Residual'),
    src = cms.InputTag("akFlowPuCs2PFJets"),
    payload = "AK2PF"
    )

akFlowPuCs2PFJetID = cms.EDProducer(
    'JetIDProducer',
    JetIDParams,
    src = cms.InputTag('akFlowPuCs2CaloJets'))

# akFlowPuCs2PFclean = heavyIonCleanedGenJets.clone(
#     src = cms.InputTag('ak2GenJets'))

akFlowPuCs2PFbTagger = bTaggers(
    "akFlowPuCs2PF",
    0.2)

# create objects locally since they dont load properly otherwise
akFlowPuCs2PFPatJetFlavourAssociationLegacy = akFlowPuCs2PFbTagger.PatJetFlavourAssociationLegacy
akFlowPuCs2PFPatJetPartons = akFlowPuCs2PFbTagger.PatJetPartons
akFlowPuCs2PFJetTracksAssociatorAtVertex = akFlowPuCs2PFbTagger.JetTracksAssociatorAtVertex
akFlowPuCs2PFJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akFlowPuCs2PFSimpleSecondaryVertexHighEffBJetTags = akFlowPuCs2PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akFlowPuCs2PFSimpleSecondaryVertexHighPurBJetTags = akFlowPuCs2PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akFlowPuCs2PFCombinedSecondaryVertexBJetTags = akFlowPuCs2PFbTagger.CombinedSecondaryVertexBJetTags
akFlowPuCs2PFCombinedSecondaryVertexV2BJetTags = akFlowPuCs2PFbTagger.CombinedSecondaryVertexV2BJetTags
akFlowPuCs2PFJetBProbabilityBJetTags = akFlowPuCs2PFbTagger.JetBProbabilityBJetTags
akFlowPuCs2PFSoftPFMuonByPtBJetTags = akFlowPuCs2PFbTagger.SoftPFMuonByPtBJetTags
akFlowPuCs2PFSoftPFMuonByIP3dBJetTags = akFlowPuCs2PFbTagger.SoftPFMuonByIP3dBJetTags
akFlowPuCs2PFTrackCountingHighEffBJetTags = akFlowPuCs2PFbTagger.TrackCountingHighEffBJetTags
akFlowPuCs2PFTrackCountingHighPurBJetTags = akFlowPuCs2PFbTagger.TrackCountingHighPurBJetTags
akFlowPuCs2PFPatJetPartonAssociationLegacy = akFlowPuCs2PFbTagger.PatJetPartonAssociationLegacy
akFlowPuCs2PFPatJetPartonAssociationLegacy.partons = "myPartons"

akFlowPuCs2PFImpactParameterTagInfos = akFlowPuCs2PFbTagger.ImpactParameterTagInfos
akFlowPuCs2PFImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akFlowPuCs2PFJetProbabilityBJetTags = akFlowPuCs2PFbTagger.JetProbabilityBJetTags

akFlowPuCs2PFSecondaryVertexTagInfos = akFlowPuCs2PFbTagger.SecondaryVertexTagInfos
akFlowPuCs2PFSimpleSecondaryVertexHighEffBJetTags = akFlowPuCs2PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akFlowPuCs2PFSimpleSecondaryVertexHighPurBJetTags = akFlowPuCs2PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akFlowPuCs2PFCombinedSecondaryVertexBJetTags = akFlowPuCs2PFbTagger.CombinedSecondaryVertexBJetTags
akFlowPuCs2PFCombinedSecondaryVertexV2BJetTags = akFlowPuCs2PFbTagger.CombinedSecondaryVertexV2BJetTags

akFlowPuCs2PFSecondaryVertexNegativeTagInfos = akFlowPuCs2PFbTagger.SecondaryVertexNegativeTagInfos
akFlowPuCs2PFNegativeSimpleSecondaryVertexHighEffBJetTags = akFlowPuCs2PFbTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akFlowPuCs2PFNegativeSimpleSecondaryVertexHighPurBJetTags = akFlowPuCs2PFbTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akFlowPuCs2PFNegativeCombinedSecondaryVertexBJetTags = akFlowPuCs2PFbTagger.NegativeCombinedSecondaryVertexBJetTags
akFlowPuCs2PFPositiveCombinedSecondaryVertexBJetTags = akFlowPuCs2PFbTagger.PositiveCombinedSecondaryVertexBJetTags
akFlowPuCs2PFNegativeCombinedSecondaryVertexV2BJetTags = akFlowPuCs2PFbTagger.NegativeCombinedSecondaryVertexV2BJetTags
akFlowPuCs2PFPositiveCombinedSecondaryVertexV2BJetTags = akFlowPuCs2PFbTagger.PositiveCombinedSecondaryVertexV2BJetTags

akFlowPuCs2PFSoftPFMuonsTagInfos = akFlowPuCs2PFbTagger.SoftPFMuonsTagInfos
akFlowPuCs2PFSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akFlowPuCs2PFSoftPFMuonBJetTags = akFlowPuCs2PFbTagger.SoftPFMuonBJetTags
akFlowPuCs2PFSoftPFMuonByIP3dBJetTags = akFlowPuCs2PFbTagger.SoftPFMuonByIP3dBJetTags
akFlowPuCs2PFSoftPFMuonByPtBJetTags = akFlowPuCs2PFbTagger.SoftPFMuonByPtBJetTags
akFlowPuCs2PFNegativeSoftPFMuonByPtBJetTags = akFlowPuCs2PFbTagger.NegativeSoftPFMuonByPtBJetTags
akFlowPuCs2PFPositiveSoftPFMuonByPtBJetTags = akFlowPuCs2PFbTagger.PositiveSoftPFMuonByPtBJetTags
akFlowPuCs2PFPatJetFlavourIdLegacy = cms.Sequence(akFlowPuCs2PFPatJetPartonAssociationLegacy*akFlowPuCs2PFPatJetFlavourAssociationLegacy)
# Not working with our PU sub, but keep it here for reference
# akFlowPuCs2PFPatJetFlavourAssociation = akFlowPuCs2PFbTagger.PatJetFlavourAssociation
# akFlowPuCs2PFPatJetFlavourId = cms.Sequence(akFlowPuCs2PFPatJetPartons*akFlowPuCs2PFPatJetFlavourAssociation)

akFlowPuCs2PFJetBtaggingIP = cms.Sequence(
    akFlowPuCs2PFImpactParameterTagInfos *
    akFlowPuCs2PFTrackCountingHighEffBJetTags +
    akFlowPuCs2PFTrackCountingHighPurBJetTags +
    akFlowPuCs2PFJetProbabilityBJetTags +
    akFlowPuCs2PFJetBProbabilityBJetTags
    )

akFlowPuCs2PFJetBtaggingSV = cms.Sequence(
    akFlowPuCs2PFImpactParameterTagInfos *
    akFlowPuCs2PFSecondaryVertexTagInfos *
    akFlowPuCs2PFSimpleSecondaryVertexHighEffBJetTags +
    akFlowPuCs2PFSimpleSecondaryVertexHighPurBJetTags +
    akFlowPuCs2PFCombinedSecondaryVertexBJetTags +
    akFlowPuCs2PFCombinedSecondaryVertexV2BJetTags
    )

akFlowPuCs2PFJetBtaggingNegSV = cms.Sequence(
    akFlowPuCs2PFImpactParameterTagInfos *
    akFlowPuCs2PFSecondaryVertexNegativeTagInfos *
    akFlowPuCs2PFNegativeSimpleSecondaryVertexHighEffBJetTags +
    akFlowPuCs2PFNegativeSimpleSecondaryVertexHighPurBJetTags +
    akFlowPuCs2PFNegativeCombinedSecondaryVertexBJetTags +
    akFlowPuCs2PFPositiveCombinedSecondaryVertexBJetTags +
    akFlowPuCs2PFNegativeCombinedSecondaryVertexV2BJetTags +
    akFlowPuCs2PFPositiveCombinedSecondaryVertexV2BJetTags
    )

akFlowPuCs2PFJetBtaggingMu = cms.Sequence(
    akFlowPuCs2PFSoftPFMuonsTagInfos *
    akFlowPuCs2PFSoftPFMuonBJetTags +
    akFlowPuCs2PFSoftPFMuonByIP3dBJetTags +
    akFlowPuCs2PFSoftPFMuonByPtBJetTags +
    akFlowPuCs2PFNegativeSoftPFMuonByPtBJetTags +
    akFlowPuCs2PFPositiveSoftPFMuonByPtBJetTags
    )

akFlowPuCs2PFJetBtagging = cms.Sequence(
    akFlowPuCs2PFJetBtaggingIP
    * akFlowPuCs2PFJetBtaggingSV
    # * akFlowPuCs2PFJetBtaggingNegSV
    # * akFlowPuCs2PFJetBtaggingMu
    )

akFlowPuCs2PFpatJetsWithBtagging = patJets.clone(
    jetSource = cms.InputTag("akFlowPuCs2PFJets"),
    genJetMatch            = cms.InputTag("akFlowPuCs2PFmatch"),
    genPartonMatch         = cms.InputTag("akFlowPuCs2PFparton"),
    jetCorrFactorsSource   = cms.VInputTag(cms.InputTag("akFlowPuCs2PFcorr")),
    JetPartonMapSource     = cms.InputTag("akFlowPuCs2PFPatJetFlavourAssociationLegacy"),
    JetFlavourInfoSource   = cms.InputTag("akFlowPuCs2PFPatJetFlavourAssociation"),
    trackAssociationSource = cms.InputTag("akFlowPuCs2PFJetTracksAssociatorAtVertex"),
    useLegacyJetMCFlavour  = True,
    discriminatorSources   = cms.VInputTag(
        cms.InputTag("akFlowPuCs2PFSimpleSecondaryVertexHighEffBJetTags"),
        cms.InputTag("akFlowPuCs2PFSimpleSecondaryVertexHighPurBJetTags"),
        cms.InputTag("akFlowPuCs2PFCombinedSecondaryVertexBJetTags"),
        cms.InputTag("akFlowPuCs2PFCombinedSecondaryVertexV2BJetTags"),
        cms.InputTag("akFlowPuCs2PFJetBProbabilityBJetTags"),
        cms.InputTag("akFlowPuCs2PFJetProbabilityBJetTags"),
        # cms.InputTag("akFlowPuCs2PFSoftPFMuonByPtBJetTags"),
        # cms.InputTag("akFlowPuCs2PFSoftPFMuonByIP3dBJetTags"),
        cms.InputTag("akFlowPuCs2PFTrackCountingHighEffBJetTags"),
        cms.InputTag("akFlowPuCs2PFTrackCountingHighPurBJetTags"),
        ),
    tagInfoSources = cms.VInputTag(cms.InputTag("akFlowPuCs2PFImpactParameterTagInfos"),cms.InputTag("akFlowPuCs2PFSecondaryVertexTagInfos")),
    jetIDMap = cms.InputTag("akFlowPuCs2PFJetID"),
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

akFlowPuCs2PFNjettiness = Njettiness.clone(
    src = cms.InputTag("akFlowPuCs2PFJets"),
    R0  = cms.double(0.2)
    )

akFlowPuCs2PFpatJetsWithBtagging.userData.userFloats.src += [
    'akFlowPuCs2PFNjettiness:tau1',
    'akFlowPuCs2PFNjettiness:tau2',
    'akFlowPuCs2PFNjettiness:tau3']

akFlowPuCs2PFJetAnalyzer = inclusiveJetAnalyzer.clone(
    jetTag = cms.InputTag("akFlowPuCs2PFpatJetsWithBtagging"),
    genjetTag = 'ak2GenJets',
    rParam = 0.2,
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
    bTagJetName = cms.untracked.string("akFlowPuCs2PF"),
    jetName = cms.untracked.string("akFlowPuCs2PF"),
    genPtMin = cms.untracked.double(5),
    hltTrgResults = cms.untracked.string('TriggerResults::'+'HISIGNAL'),
    doTower = cms.untracked.bool(False),
    doSubJets = cms.untracked.bool(False),
    doGenSubJets = cms.untracked.bool(False),
    subjetGenTag = cms.untracked.InputTag("ak2GenJets"),
    doGenTaus = cms.untracked.bool(False),
    genTau1 = cms.InputTag("ak2GenNjettiness","tau1"),
    genTau2 = cms.InputTag("ak2GenNjettiness","tau2"),
    genTau3 = cms.InputTag("ak2GenNjettiness","tau3"),
    doGenSym = cms.untracked.bool(False),
    genSym = cms.InputTag("ak2GenJets","sym"),
    genDroppedBranches = cms.InputTag("ak2GenJets","droppedBranches")
    )

akFlowPuCs2PFJetSequence_mc = cms.Sequence(
    # akFlowPuCs2PFclean
    # *
    akFlowPuCs2PFmatch
    # *
    # akFlowPuCs2PFmatchGroomed
    *
    akFlowPuCs2PFparton
    *
    akFlowPuCs2PFcorr
    # *
    # akFlowPuCs2PFJetID
    *
    akFlowPuCs2PFPatJetFlavourIdLegacy
    # *
    # akFlowPuCs2PFPatJetFlavourId # Use legacy algo till PU implemented
    *
    akFlowPuCs2PFJetTracksAssociatorAtVertex
    *
    akFlowPuCs2PFJetBtagging
    *
    # No constituents for calo jets in pp. Must be removed for pp calo jets but
    # I'm not sure how to do this transparently (Marta)
    akFlowPuCs2PFNjettiness
    *
    akFlowPuCs2PFpatJetsWithBtagging
    *
    akFlowPuCs2PFJetAnalyzer
    )

akFlowPuCs2PFJetSequence_data = cms.Sequence(
    akFlowPuCs2PFcorr
    *
    # akFlowPuCs2PFJetID
    # *
    akFlowPuCs2PFJetTracksAssociatorAtVertex
    *
    akFlowPuCs2PFJetBtagging
    *
    akFlowPuCs2PFNjettiness
    *
    akFlowPuCs2PFpatJetsWithBtagging
    *
    akFlowPuCs2PFJetAnalyzer
    )

akFlowPuCs2PFJetSequence_mb = cms.Sequence(
    akFlowPuCs2PFJetSequence_mc)
akFlowPuCs2PFJetSequence_jec = cms.Sequence(
    akFlowPuCs2PFJetSequence_mc)

akFlowPuCs2PFJetSequence = cms.Sequence(
    akFlowPuCs2PFJetSequence_data)
