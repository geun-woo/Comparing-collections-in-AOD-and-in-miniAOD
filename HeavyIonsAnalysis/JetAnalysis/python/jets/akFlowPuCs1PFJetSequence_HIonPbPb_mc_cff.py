import FWCore.ParameterSet.Config as cms

from PhysicsTools.PatAlgos.mcMatchLayer0.jetMatch_cfi import patJetGenJetMatch, patJetPartonMatch
from PhysicsTools.PatAlgos.recoLayer0.jetCorrFactors_cfi import patJetCorrFactors
from PhysicsTools.PatAlgos.producersLayer1.jetProducer_cfi import patJets

from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *

from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akFlowPuCs1PFmatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akFlowPuCs1PFJets"),
    matched = cms.InputTag("ak1HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.1
    )

akFlowPuCs1PFmatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("ak1HiSignalGenJets"),
    matched = cms.InputTag("ak1HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.1
    )

akFlowPuCs1PFparton = patJetPartonMatch.clone(
    src = cms.InputTag("akFlowPuCs1PFJets"),
    matched = cms.InputTag("hiSignalGenParticles"))

akFlowPuCs1PFcorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
    levels   = cms.vstring('L2Relative'),
    src = cms.InputTag("akFlowPuCs1PFJets"),
    payload = "AK1PF"
    )

akFlowPuCs1PFJetID = cms.EDProducer(
    'JetIDProducer',
    JetIDParams,
    src = cms.InputTag('akFlowPuCs1CaloJets'))

# akFlowPuCs1PFclean = heavyIonCleanedGenJets.clone(
#     src = cms.InputTag('ak1HiSignalGenJets'))

akFlowPuCs1PFbTagger = bTaggers(
    "akFlowPuCs1PF",
    0.1)

# create objects locally since they dont load properly otherwise
akFlowPuCs1PFPatJetFlavourAssociationLegacy = akFlowPuCs1PFbTagger.PatJetFlavourAssociationLegacy
akFlowPuCs1PFPatJetPartons = akFlowPuCs1PFbTagger.PatJetPartons
akFlowPuCs1PFJetTracksAssociatorAtVertex = akFlowPuCs1PFbTagger.JetTracksAssociatorAtVertex
akFlowPuCs1PFJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akFlowPuCs1PFSimpleSecondaryVertexHighEffBJetTags = akFlowPuCs1PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akFlowPuCs1PFSimpleSecondaryVertexHighPurBJetTags = akFlowPuCs1PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akFlowPuCs1PFCombinedSecondaryVertexBJetTags = akFlowPuCs1PFbTagger.CombinedSecondaryVertexBJetTags
akFlowPuCs1PFCombinedSecondaryVertexV2BJetTags = akFlowPuCs1PFbTagger.CombinedSecondaryVertexV2BJetTags
akFlowPuCs1PFJetBProbabilityBJetTags = akFlowPuCs1PFbTagger.JetBProbabilityBJetTags
akFlowPuCs1PFSoftPFMuonByPtBJetTags = akFlowPuCs1PFbTagger.SoftPFMuonByPtBJetTags
akFlowPuCs1PFSoftPFMuonByIP3dBJetTags = akFlowPuCs1PFbTagger.SoftPFMuonByIP3dBJetTags
akFlowPuCs1PFTrackCountingHighEffBJetTags = akFlowPuCs1PFbTagger.TrackCountingHighEffBJetTags
akFlowPuCs1PFTrackCountingHighPurBJetTags = akFlowPuCs1PFbTagger.TrackCountingHighPurBJetTags
akFlowPuCs1PFPatJetPartonAssociationLegacy = akFlowPuCs1PFbTagger.PatJetPartonAssociationLegacy
akFlowPuCs1PFPatJetPartonAssociationLegacy.partons = "signalPartons"

akFlowPuCs1PFImpactParameterTagInfos = akFlowPuCs1PFbTagger.ImpactParameterTagInfos
akFlowPuCs1PFImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akFlowPuCs1PFJetProbabilityBJetTags = akFlowPuCs1PFbTagger.JetProbabilityBJetTags

akFlowPuCs1PFSecondaryVertexTagInfos = akFlowPuCs1PFbTagger.SecondaryVertexTagInfos
akFlowPuCs1PFSimpleSecondaryVertexHighEffBJetTags = akFlowPuCs1PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akFlowPuCs1PFSimpleSecondaryVertexHighPurBJetTags = akFlowPuCs1PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akFlowPuCs1PFCombinedSecondaryVertexBJetTags = akFlowPuCs1PFbTagger.CombinedSecondaryVertexBJetTags
akFlowPuCs1PFCombinedSecondaryVertexV2BJetTags = akFlowPuCs1PFbTagger.CombinedSecondaryVertexV2BJetTags

akFlowPuCs1PFSecondaryVertexNegativeTagInfos = akFlowPuCs1PFbTagger.SecondaryVertexNegativeTagInfos
akFlowPuCs1PFNegativeSimpleSecondaryVertexHighEffBJetTags = akFlowPuCs1PFbTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akFlowPuCs1PFNegativeSimpleSecondaryVertexHighPurBJetTags = akFlowPuCs1PFbTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akFlowPuCs1PFNegativeCombinedSecondaryVertexBJetTags = akFlowPuCs1PFbTagger.NegativeCombinedSecondaryVertexBJetTags
akFlowPuCs1PFPositiveCombinedSecondaryVertexBJetTags = akFlowPuCs1PFbTagger.PositiveCombinedSecondaryVertexBJetTags
akFlowPuCs1PFNegativeCombinedSecondaryVertexV2BJetTags = akFlowPuCs1PFbTagger.NegativeCombinedSecondaryVertexV2BJetTags
akFlowPuCs1PFPositiveCombinedSecondaryVertexV2BJetTags = akFlowPuCs1PFbTagger.PositiveCombinedSecondaryVertexV2BJetTags

akFlowPuCs1PFSoftPFMuonsTagInfos = akFlowPuCs1PFbTagger.SoftPFMuonsTagInfos
akFlowPuCs1PFSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akFlowPuCs1PFSoftPFMuonBJetTags = akFlowPuCs1PFbTagger.SoftPFMuonBJetTags
akFlowPuCs1PFSoftPFMuonByIP3dBJetTags = akFlowPuCs1PFbTagger.SoftPFMuonByIP3dBJetTags
akFlowPuCs1PFSoftPFMuonByPtBJetTags = akFlowPuCs1PFbTagger.SoftPFMuonByPtBJetTags
akFlowPuCs1PFNegativeSoftPFMuonByPtBJetTags = akFlowPuCs1PFbTagger.NegativeSoftPFMuonByPtBJetTags
akFlowPuCs1PFPositiveSoftPFMuonByPtBJetTags = akFlowPuCs1PFbTagger.PositiveSoftPFMuonByPtBJetTags
akFlowPuCs1PFPatJetFlavourIdLegacy = cms.Sequence(akFlowPuCs1PFPatJetPartonAssociationLegacy*akFlowPuCs1PFPatJetFlavourAssociationLegacy)
# Not working with our PU sub, but keep it here for reference
# akFlowPuCs1PFPatJetFlavourAssociation = akFlowPuCs1PFbTagger.PatJetFlavourAssociation
# akFlowPuCs1PFPatJetFlavourId = cms.Sequence(akFlowPuCs1PFPatJetPartons*akFlowPuCs1PFPatJetFlavourAssociation)

akFlowPuCs1PFJetBtaggingIP = cms.Sequence(
    akFlowPuCs1PFImpactParameterTagInfos *
    akFlowPuCs1PFTrackCountingHighEffBJetTags +
    akFlowPuCs1PFTrackCountingHighPurBJetTags +
    akFlowPuCs1PFJetProbabilityBJetTags +
    akFlowPuCs1PFJetBProbabilityBJetTags
    )

akFlowPuCs1PFJetBtaggingSV = cms.Sequence(
    akFlowPuCs1PFImpactParameterTagInfos *
    akFlowPuCs1PFSecondaryVertexTagInfos *
    akFlowPuCs1PFSimpleSecondaryVertexHighEffBJetTags +
    akFlowPuCs1PFSimpleSecondaryVertexHighPurBJetTags +
    akFlowPuCs1PFCombinedSecondaryVertexBJetTags +
    akFlowPuCs1PFCombinedSecondaryVertexV2BJetTags
    )

akFlowPuCs1PFJetBtaggingNegSV = cms.Sequence(
    akFlowPuCs1PFImpactParameterTagInfos *
    akFlowPuCs1PFSecondaryVertexNegativeTagInfos *
    akFlowPuCs1PFNegativeSimpleSecondaryVertexHighEffBJetTags +
    akFlowPuCs1PFNegativeSimpleSecondaryVertexHighPurBJetTags +
    akFlowPuCs1PFNegativeCombinedSecondaryVertexBJetTags +
    akFlowPuCs1PFPositiveCombinedSecondaryVertexBJetTags +
    akFlowPuCs1PFNegativeCombinedSecondaryVertexV2BJetTags +
    akFlowPuCs1PFPositiveCombinedSecondaryVertexV2BJetTags
    )

akFlowPuCs1PFJetBtaggingMu = cms.Sequence(
    akFlowPuCs1PFSoftPFMuonsTagInfos *
    akFlowPuCs1PFSoftPFMuonBJetTags +
    akFlowPuCs1PFSoftPFMuonByIP3dBJetTags +
    akFlowPuCs1PFSoftPFMuonByPtBJetTags +
    akFlowPuCs1PFNegativeSoftPFMuonByPtBJetTags +
    akFlowPuCs1PFPositiveSoftPFMuonByPtBJetTags
    )

akFlowPuCs1PFJetBtagging = cms.Sequence(
    akFlowPuCs1PFJetBtaggingIP
    * akFlowPuCs1PFJetBtaggingSV
    # * akFlowPuCs1PFJetBtaggingNegSV
    # * akFlowPuCs1PFJetBtaggingMu
    )

akFlowPuCs1PFpatJetsWithBtagging = patJets.clone(
    jetSource = cms.InputTag("akFlowPuCs1PFJets"),
    genJetMatch            = cms.InputTag("akFlowPuCs1PFmatch"),
    genPartonMatch         = cms.InputTag("akFlowPuCs1PFparton"),
    jetCorrFactorsSource   = cms.VInputTag(cms.InputTag("akFlowPuCs1PFcorr")),
    JetPartonMapSource     = cms.InputTag("akFlowPuCs1PFPatJetFlavourAssociationLegacy"),
    JetFlavourInfoSource   = cms.InputTag("akFlowPuCs1PFPatJetFlavourAssociation"),
    trackAssociationSource = cms.InputTag("akFlowPuCs1PFJetTracksAssociatorAtVertex"),
    useLegacyJetMCFlavour  = True,
    discriminatorSources   = cms.VInputTag(
        cms.InputTag("akFlowPuCs1PFSimpleSecondaryVertexHighEffBJetTags"),
        cms.InputTag("akFlowPuCs1PFSimpleSecondaryVertexHighPurBJetTags"),
        cms.InputTag("akFlowPuCs1PFCombinedSecondaryVertexBJetTags"),
        cms.InputTag("akFlowPuCs1PFCombinedSecondaryVertexV2BJetTags"),
        cms.InputTag("akFlowPuCs1PFJetBProbabilityBJetTags"),
        cms.InputTag("akFlowPuCs1PFJetProbabilityBJetTags"),
        # cms.InputTag("akFlowPuCs1PFSoftPFMuonByPtBJetTags"),
        # cms.InputTag("akFlowPuCs1PFSoftPFMuonByIP3dBJetTags"),
        cms.InputTag("akFlowPuCs1PFTrackCountingHighEffBJetTags"),
        cms.InputTag("akFlowPuCs1PFTrackCountingHighPurBJetTags"),
        ),
    tagInfoSources = cms.VInputTag(cms.InputTag("akFlowPuCs1PFImpactParameterTagInfos"),cms.InputTag("akFlowPuCs1PFSecondaryVertexTagInfos")),
    jetIDMap = cms.InputTag("akFlowPuCs1PFJetID"),
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

akFlowPuCs1PFNjettiness = Njettiness.clone(
    src = cms.InputTag("akFlowPuCs1PFJets"),
    R0  = cms.double(0.1)
    )

akFlowPuCs1PFpatJetsWithBtagging.userData.userFloats.src += [
    'akFlowPuCs1PFNjettiness:tau1',
    'akFlowPuCs1PFNjettiness:tau2',
    'akFlowPuCs1PFNjettiness:tau3']

akFlowPuCs1PFJetAnalyzer = inclusiveJetAnalyzer.clone(
    jetTag = cms.InputTag("akFlowPuCs1PFpatJetsWithBtagging"),
    genjetTag = 'ak1HiSignalGenJets',
    rParam = 0.1,
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
    bTagJetName = cms.untracked.string("akFlowPuCs1PF"),
    jetName = cms.untracked.string("akFlowPuCs1PF"),
    genPtMin = cms.untracked.double(5),
    hltTrgResults = cms.untracked.string('TriggerResults::'+'HISIGNAL'),
    doTower = cms.untracked.bool(True),
    doSubJets = cms.untracked.bool(False),
    doGenSubJets = cms.untracked.bool(False),
    subjetGenTag = cms.untracked.InputTag("ak1GenJets"),
    doGenTaus = cms.untracked.bool(True),
    genTau1 = cms.InputTag("ak1HiGenNjettiness","tau1"),
    genTau2 = cms.InputTag("ak1HiGenNjettiness","tau2"),
    genTau3 = cms.InputTag("ak1HiGenNjettiness","tau3"),
    doGenSym = cms.untracked.bool(False),
    genSym = cms.InputTag("ak1GenJets","sym"),
    genDroppedBranches = cms.InputTag("ak1GenJets","droppedBranches")
    )

akFlowPuCs1PFJetSequence_mc = cms.Sequence(
    # akFlowPuCs1PFclean
    # *
    akFlowPuCs1PFmatch
    # *
    # akFlowPuCs1PFmatchGroomed
    *
    akFlowPuCs1PFparton
    *
    akFlowPuCs1PFcorr
    # *
    # akFlowPuCs1PFJetID
    *
    akFlowPuCs1PFPatJetFlavourIdLegacy
    # *
    # akFlowPuCs1PFPatJetFlavourId # Use legacy algo till PU implemented
    *
    akFlowPuCs1PFJetTracksAssociatorAtVertex
    *
    akFlowPuCs1PFJetBtagging
    *
    # No constituents for calo jets in pp. Must be removed for pp calo jets but
    # I'm not sure how to do this transparently (Marta)
    akFlowPuCs1PFNjettiness
    *
    akFlowPuCs1PFpatJetsWithBtagging
    *
    akFlowPuCs1PFJetAnalyzer
    )

akFlowPuCs1PFJetSequence_data = cms.Sequence(
    akFlowPuCs1PFcorr
    *
    # akFlowPuCs1PFJetID
    # *
    akFlowPuCs1PFJetTracksAssociatorAtVertex
    *
    akFlowPuCs1PFJetBtagging
    *
    akFlowPuCs1PFNjettiness
    *
    akFlowPuCs1PFpatJetsWithBtagging
    *
    akFlowPuCs1PFJetAnalyzer
    )

akFlowPuCs1PFJetSequence_mb = cms.Sequence(
    akFlowPuCs1PFJetSequence_mc)
akFlowPuCs1PFJetSequence_jec = cms.Sequence(
    akFlowPuCs1PFJetSequence_mc)

akFlowPuCs1PFJetSequence = cms.Sequence(
    akFlowPuCs1PFJetSequence_mc)
