import FWCore.ParameterSet.Config as cms

from PhysicsTools.PatAlgos.mcMatchLayer0.jetMatch_cfi import patJetGenJetMatch, patJetPartonMatch
from PhysicsTools.PatAlgos.recoLayer0.jetCorrFactors_cfi import patJetCorrFactors
from PhysicsTools.PatAlgos.producersLayer1.jetProducer_cfi import patJets

from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *

from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akFlowPuCs6PFmatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akFlowPuCs6PFJets"),
    matched = cms.InputTag("ak6GenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.6
    )

akFlowPuCs6PFmatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("ak6GenJets"),
    matched = cms.InputTag("ak6GenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.6
    )

akFlowPuCs6PFparton = patJetPartonMatch.clone(
    src = cms.InputTag("akFlowPuCs6PFJets"),
    matched = cms.InputTag("genParticles"))

akFlowPuCs6PFcorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
    levels   = cms.vstring('L2Relative'),
    src = cms.InputTag("akFlowPuCs6PFJets"),
    payload = "AK6PF"
    )

akFlowPuCs6PFJetID = cms.EDProducer(
    'JetIDProducer',
    JetIDParams,
    src = cms.InputTag('akFlowPuCs6CaloJets'))

# akFlowPuCs6PFclean = heavyIonCleanedGenJets.clone(
#     src = cms.InputTag('ak6GenJets'))

akFlowPuCs6PFbTagger = bTaggers(
    "akFlowPuCs6PF",
    0.6)

# create objects locally since they dont load properly otherwise
akFlowPuCs6PFPatJetFlavourAssociationLegacy = akFlowPuCs6PFbTagger.PatJetFlavourAssociationLegacy
akFlowPuCs6PFPatJetPartons = akFlowPuCs6PFbTagger.PatJetPartons
akFlowPuCs6PFJetTracksAssociatorAtVertex = akFlowPuCs6PFbTagger.JetTracksAssociatorAtVertex
akFlowPuCs6PFJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akFlowPuCs6PFSimpleSecondaryVertexHighEffBJetTags = akFlowPuCs6PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akFlowPuCs6PFSimpleSecondaryVertexHighPurBJetTags = akFlowPuCs6PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akFlowPuCs6PFCombinedSecondaryVertexBJetTags = akFlowPuCs6PFbTagger.CombinedSecondaryVertexBJetTags
akFlowPuCs6PFCombinedSecondaryVertexV2BJetTags = akFlowPuCs6PFbTagger.CombinedSecondaryVertexV2BJetTags
akFlowPuCs6PFJetBProbabilityBJetTags = akFlowPuCs6PFbTagger.JetBProbabilityBJetTags
akFlowPuCs6PFSoftPFMuonByPtBJetTags = akFlowPuCs6PFbTagger.SoftPFMuonByPtBJetTags
akFlowPuCs6PFSoftPFMuonByIP3dBJetTags = akFlowPuCs6PFbTagger.SoftPFMuonByIP3dBJetTags
akFlowPuCs6PFTrackCountingHighEffBJetTags = akFlowPuCs6PFbTagger.TrackCountingHighEffBJetTags
akFlowPuCs6PFTrackCountingHighPurBJetTags = akFlowPuCs6PFbTagger.TrackCountingHighPurBJetTags
akFlowPuCs6PFPatJetPartonAssociationLegacy = akFlowPuCs6PFbTagger.PatJetPartonAssociationLegacy
akFlowPuCs6PFPatJetPartonAssociationLegacy.partons = "myPartons"

akFlowPuCs6PFImpactParameterTagInfos = akFlowPuCs6PFbTagger.ImpactParameterTagInfos
akFlowPuCs6PFImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akFlowPuCs6PFJetProbabilityBJetTags = akFlowPuCs6PFbTagger.JetProbabilityBJetTags

akFlowPuCs6PFSecondaryVertexTagInfos = akFlowPuCs6PFbTagger.SecondaryVertexTagInfos
akFlowPuCs6PFSimpleSecondaryVertexHighEffBJetTags = akFlowPuCs6PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akFlowPuCs6PFSimpleSecondaryVertexHighPurBJetTags = akFlowPuCs6PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akFlowPuCs6PFCombinedSecondaryVertexBJetTags = akFlowPuCs6PFbTagger.CombinedSecondaryVertexBJetTags
akFlowPuCs6PFCombinedSecondaryVertexV2BJetTags = akFlowPuCs6PFbTagger.CombinedSecondaryVertexV2BJetTags

akFlowPuCs6PFSecondaryVertexNegativeTagInfos = akFlowPuCs6PFbTagger.SecondaryVertexNegativeTagInfos
akFlowPuCs6PFNegativeSimpleSecondaryVertexHighEffBJetTags = akFlowPuCs6PFbTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akFlowPuCs6PFNegativeSimpleSecondaryVertexHighPurBJetTags = akFlowPuCs6PFbTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akFlowPuCs6PFNegativeCombinedSecondaryVertexBJetTags = akFlowPuCs6PFbTagger.NegativeCombinedSecondaryVertexBJetTags
akFlowPuCs6PFPositiveCombinedSecondaryVertexBJetTags = akFlowPuCs6PFbTagger.PositiveCombinedSecondaryVertexBJetTags
akFlowPuCs6PFNegativeCombinedSecondaryVertexV2BJetTags = akFlowPuCs6PFbTagger.NegativeCombinedSecondaryVertexV2BJetTags
akFlowPuCs6PFPositiveCombinedSecondaryVertexV2BJetTags = akFlowPuCs6PFbTagger.PositiveCombinedSecondaryVertexV2BJetTags

akFlowPuCs6PFSoftPFMuonsTagInfos = akFlowPuCs6PFbTagger.SoftPFMuonsTagInfos
akFlowPuCs6PFSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akFlowPuCs6PFSoftPFMuonBJetTags = akFlowPuCs6PFbTagger.SoftPFMuonBJetTags
akFlowPuCs6PFSoftPFMuonByIP3dBJetTags = akFlowPuCs6PFbTagger.SoftPFMuonByIP3dBJetTags
akFlowPuCs6PFSoftPFMuonByPtBJetTags = akFlowPuCs6PFbTagger.SoftPFMuonByPtBJetTags
akFlowPuCs6PFNegativeSoftPFMuonByPtBJetTags = akFlowPuCs6PFbTagger.NegativeSoftPFMuonByPtBJetTags
akFlowPuCs6PFPositiveSoftPFMuonByPtBJetTags = akFlowPuCs6PFbTagger.PositiveSoftPFMuonByPtBJetTags
akFlowPuCs6PFPatJetFlavourIdLegacy = cms.Sequence(akFlowPuCs6PFPatJetPartonAssociationLegacy*akFlowPuCs6PFPatJetFlavourAssociationLegacy)
# Not working with our PU sub, but keep it here for reference
# akFlowPuCs6PFPatJetFlavourAssociation = akFlowPuCs6PFbTagger.PatJetFlavourAssociation
# akFlowPuCs6PFPatJetFlavourId = cms.Sequence(akFlowPuCs6PFPatJetPartons*akFlowPuCs6PFPatJetFlavourAssociation)

akFlowPuCs6PFJetBtaggingIP = cms.Sequence(
    akFlowPuCs6PFImpactParameterTagInfos *
    akFlowPuCs6PFTrackCountingHighEffBJetTags +
    akFlowPuCs6PFTrackCountingHighPurBJetTags +
    akFlowPuCs6PFJetProbabilityBJetTags +
    akFlowPuCs6PFJetBProbabilityBJetTags
    )

akFlowPuCs6PFJetBtaggingSV = cms.Sequence(
    akFlowPuCs6PFImpactParameterTagInfos *
    akFlowPuCs6PFSecondaryVertexTagInfos *
    akFlowPuCs6PFSimpleSecondaryVertexHighEffBJetTags +
    akFlowPuCs6PFSimpleSecondaryVertexHighPurBJetTags +
    akFlowPuCs6PFCombinedSecondaryVertexBJetTags +
    akFlowPuCs6PFCombinedSecondaryVertexV2BJetTags
    )

akFlowPuCs6PFJetBtaggingNegSV = cms.Sequence(
    akFlowPuCs6PFImpactParameterTagInfos *
    akFlowPuCs6PFSecondaryVertexNegativeTagInfos *
    akFlowPuCs6PFNegativeSimpleSecondaryVertexHighEffBJetTags +
    akFlowPuCs6PFNegativeSimpleSecondaryVertexHighPurBJetTags +
    akFlowPuCs6PFNegativeCombinedSecondaryVertexBJetTags +
    akFlowPuCs6PFPositiveCombinedSecondaryVertexBJetTags +
    akFlowPuCs6PFNegativeCombinedSecondaryVertexV2BJetTags +
    akFlowPuCs6PFPositiveCombinedSecondaryVertexV2BJetTags
    )

akFlowPuCs6PFJetBtaggingMu = cms.Sequence(
    akFlowPuCs6PFSoftPFMuonsTagInfos *
    akFlowPuCs6PFSoftPFMuonBJetTags +
    akFlowPuCs6PFSoftPFMuonByIP3dBJetTags +
    akFlowPuCs6PFSoftPFMuonByPtBJetTags +
    akFlowPuCs6PFNegativeSoftPFMuonByPtBJetTags +
    akFlowPuCs6PFPositiveSoftPFMuonByPtBJetTags
    )

akFlowPuCs6PFJetBtagging = cms.Sequence(
    akFlowPuCs6PFJetBtaggingIP
    * akFlowPuCs6PFJetBtaggingSV
    # * akFlowPuCs6PFJetBtaggingNegSV
    # * akFlowPuCs6PFJetBtaggingMu
    )

akFlowPuCs6PFpatJetsWithBtagging = patJets.clone(
    jetSource = cms.InputTag("akFlowPuCs6PFJets"),
    genJetMatch            = cms.InputTag("akFlowPuCs6PFmatch"),
    genPartonMatch         = cms.InputTag("akFlowPuCs6PFparton"),
    jetCorrFactorsSource   = cms.VInputTag(cms.InputTag("akFlowPuCs6PFcorr")),
    JetPartonMapSource     = cms.InputTag("akFlowPuCs6PFPatJetFlavourAssociationLegacy"),
    JetFlavourInfoSource   = cms.InputTag("akFlowPuCs6PFPatJetFlavourAssociation"),
    trackAssociationSource = cms.InputTag("akFlowPuCs6PFJetTracksAssociatorAtVertex"),
    useLegacyJetMCFlavour  = True,
    discriminatorSources   = cms.VInputTag(
        cms.InputTag("akFlowPuCs6PFSimpleSecondaryVertexHighEffBJetTags"),
        cms.InputTag("akFlowPuCs6PFSimpleSecondaryVertexHighPurBJetTags"),
        cms.InputTag("akFlowPuCs6PFCombinedSecondaryVertexBJetTags"),
        cms.InputTag("akFlowPuCs6PFCombinedSecondaryVertexV2BJetTags"),
        cms.InputTag("akFlowPuCs6PFJetBProbabilityBJetTags"),
        cms.InputTag("akFlowPuCs6PFJetProbabilityBJetTags"),
        # cms.InputTag("akFlowPuCs6PFSoftPFMuonByPtBJetTags"),
        # cms.InputTag("akFlowPuCs6PFSoftPFMuonByIP3dBJetTags"),
        cms.InputTag("akFlowPuCs6PFTrackCountingHighEffBJetTags"),
        cms.InputTag("akFlowPuCs6PFTrackCountingHighPurBJetTags"),
        ),
    tagInfoSources = cms.VInputTag(cms.InputTag("akFlowPuCs6PFImpactParameterTagInfos"),cms.InputTag("akFlowPuCs6PFSecondaryVertexTagInfos")),
    jetIDMap = cms.InputTag("akFlowPuCs6PFJetID"),
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

akFlowPuCs6PFNjettiness = Njettiness.clone(
    src = cms.InputTag("akFlowPuCs6PFJets"),
    R0  = cms.double(0.6)
    )

akFlowPuCs6PFpatJetsWithBtagging.userData.userFloats.src += [
    'akFlowPuCs6PFNjettiness:tau1',
    'akFlowPuCs6PFNjettiness:tau2',
    'akFlowPuCs6PFNjettiness:tau3']

akFlowPuCs6PFJetAnalyzer = inclusiveJetAnalyzer.clone(
    jetTag = cms.InputTag("akFlowPuCs6PFpatJetsWithBtagging"),
    genjetTag = 'ak6GenJets',
    rParam = 0.6,
    matchJets = cms.untracked.bool(False),
    matchTag = 'patJetsWithBtagging',
    pfCandidateLabel = cms.untracked.InputTag('particleFlow'),
    trackTag = cms.InputTag("generalTracks"),
    fillGenJets = True,
    isMC = True,
    doSubEvent = True,
    useHepMC = cms.untracked.bool(False),
    genParticles = cms.untracked.InputTag("genParticles"),
    eventInfoTag = cms.InputTag("generator"),
    doLifeTimeTagging = cms.untracked.bool(True),
    doLifeTimeTaggingExtras = cms.untracked.bool(False),
    bTagJetName = cms.untracked.string("akFlowPuCs6PF"),
    jetName = cms.untracked.string("akFlowPuCs6PF"),
    genPtMin = cms.untracked.double(5),
    hltTrgResults = cms.untracked.string('TriggerResults::'+'HISIGNAL'),
    doTower = cms.untracked.bool(False),
    doSubJets = cms.untracked.bool(False),
    doGenSubJets = cms.untracked.bool(False),
    subjetGenTag = cms.untracked.InputTag("ak6GenJets"),
    doGenTaus = cms.untracked.bool(True),
    genTau1 = cms.InputTag("ak6GenNjettiness","tau1"),
    genTau2 = cms.InputTag("ak6GenNjettiness","tau2"),
    genTau3 = cms.InputTag("ak6GenNjettiness","tau3"),
    doGenSym = cms.untracked.bool(False),
    genSym = cms.InputTag("ak6GenJets","sym"),
    genDroppedBranches = cms.InputTag("ak6GenJets","droppedBranches")
    )

akFlowPuCs6PFJetSequence_mc = cms.Sequence(
    # akFlowPuCs6PFclean
    # *
    akFlowPuCs6PFmatch
    # *
    # akFlowPuCs6PFmatchGroomed
    *
    akFlowPuCs6PFparton
    *
    akFlowPuCs6PFcorr
    # *
    # akFlowPuCs6PFJetID
    *
    akFlowPuCs6PFPatJetFlavourIdLegacy
    # *
    # akFlowPuCs6PFPatJetFlavourId # Use legacy algo till PU implemented
    *
    akFlowPuCs6PFJetTracksAssociatorAtVertex
    *
    akFlowPuCs6PFJetBtagging
    *
    # No constituents for calo jets in pp. Must be removed for pp calo jets but
    # I'm not sure how to do this transparently (Marta)
    akFlowPuCs6PFNjettiness
    *
    akFlowPuCs6PFpatJetsWithBtagging
    *
    akFlowPuCs6PFJetAnalyzer
    )

akFlowPuCs6PFJetSequence_data = cms.Sequence(
    akFlowPuCs6PFcorr
    *
    # akFlowPuCs6PFJetID
    # *
    akFlowPuCs6PFJetTracksAssociatorAtVertex
    *
    akFlowPuCs6PFJetBtagging
    *
    akFlowPuCs6PFNjettiness
    *
    akFlowPuCs6PFpatJetsWithBtagging
    *
    akFlowPuCs6PFJetAnalyzer
    )

akFlowPuCs6PFJetSequence_mb = cms.Sequence(
    akFlowPuCs6PFJetSequence_mc)
akFlowPuCs6PFJetSequence_jec = cms.Sequence(
    akFlowPuCs6PFJetSequence_mc)

akFlowPuCs6PFJetSequence = cms.Sequence(
    akFlowPuCs6PFJetSequence_mc)


akFlowPuCs6PFJetAnalyzer.matchJets = cms.untracked.bool(True)
akFlowPuCs6PFJetAnalyzer.matchTag = cms.untracked.InputTag("ak6PFpatJetsWithBtagging")
