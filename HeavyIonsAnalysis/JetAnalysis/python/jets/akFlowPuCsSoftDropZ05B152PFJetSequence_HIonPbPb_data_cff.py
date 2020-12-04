import FWCore.ParameterSet.Config as cms

from PhysicsTools.PatAlgos.mcMatchLayer0.jetMatch_cfi import patJetGenJetMatch, patJetPartonMatch
from PhysicsTools.PatAlgos.recoLayer0.jetCorrFactors_cfi import patJetCorrFactors
from PhysicsTools.PatAlgos.producersLayer1.jetProducer_cfi import patJets

from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *

from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akFlowPuCsSoftDropZ05B152PFmatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akFlowPuCsSoftDropZ05B152PFJets"),
    matched = cms.InputTag("ak2HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.2
    )

akFlowPuCsSoftDropZ05B152PFmatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDropZ05B152HiSignalGenJets"),
    matched = cms.InputTag("ak2HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.2
    )

akFlowPuCsSoftDropZ05B152PFparton = patJetPartonMatch.clone(
    src = cms.InputTag("akFlowPuCsSoftDropZ05B152PFJets"),
    matched = cms.InputTag("hiSignalGenParticles"))

akFlowPuCsSoftDropZ05B152PFcorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
    levels   = cms.vstring('L2Relative','L2L3Residual'),
    src = cms.InputTag("akFlowPuCsSoftDropZ05B152PFJets"),
    payload = "AK2PF"
    )

akFlowPuCsSoftDropZ05B152PFJetID = cms.EDProducer(
    'JetIDProducer',
    JetIDParams,
    src = cms.InputTag('akFlowPuCsSoftDropZ05B152CaloJets'))

# akFlowPuCsSoftDropZ05B152PFclean = heavyIonCleanedGenJets.clone(
#     src = cms.InputTag('ak2HiSignalGenJets'))

akFlowPuCsSoftDropZ05B152PFbTagger = bTaggers(
    "akFlowPuCsSoftDropZ05B152PF",
    0.2)

# create objects locally since they dont load properly otherwise
akFlowPuCsSoftDropZ05B152PFPatJetFlavourAssociationLegacy = akFlowPuCsSoftDropZ05B152PFbTagger.PatJetFlavourAssociationLegacy
akFlowPuCsSoftDropZ05B152PFPatJetPartons = akFlowPuCsSoftDropZ05B152PFbTagger.PatJetPartons
akFlowPuCsSoftDropZ05B152PFJetTracksAssociatorAtVertex = akFlowPuCsSoftDropZ05B152PFbTagger.JetTracksAssociatorAtVertex
akFlowPuCsSoftDropZ05B152PFJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akFlowPuCsSoftDropZ05B152PFSimpleSecondaryVertexHighEffBJetTags = akFlowPuCsSoftDropZ05B152PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akFlowPuCsSoftDropZ05B152PFSimpleSecondaryVertexHighPurBJetTags = akFlowPuCsSoftDropZ05B152PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akFlowPuCsSoftDropZ05B152PFCombinedSecondaryVertexBJetTags = akFlowPuCsSoftDropZ05B152PFbTagger.CombinedSecondaryVertexBJetTags
akFlowPuCsSoftDropZ05B152PFCombinedSecondaryVertexV2BJetTags = akFlowPuCsSoftDropZ05B152PFbTagger.CombinedSecondaryVertexV2BJetTags
akFlowPuCsSoftDropZ05B152PFJetBProbabilityBJetTags = akFlowPuCsSoftDropZ05B152PFbTagger.JetBProbabilityBJetTags
akFlowPuCsSoftDropZ05B152PFSoftPFMuonByPtBJetTags = akFlowPuCsSoftDropZ05B152PFbTagger.SoftPFMuonByPtBJetTags
akFlowPuCsSoftDropZ05B152PFSoftPFMuonByIP3dBJetTags = akFlowPuCsSoftDropZ05B152PFbTagger.SoftPFMuonByIP3dBJetTags
akFlowPuCsSoftDropZ05B152PFTrackCountingHighEffBJetTags = akFlowPuCsSoftDropZ05B152PFbTagger.TrackCountingHighEffBJetTags
akFlowPuCsSoftDropZ05B152PFTrackCountingHighPurBJetTags = akFlowPuCsSoftDropZ05B152PFbTagger.TrackCountingHighPurBJetTags
akFlowPuCsSoftDropZ05B152PFPatJetPartonAssociationLegacy = akFlowPuCsSoftDropZ05B152PFbTagger.PatJetPartonAssociationLegacy
akFlowPuCsSoftDropZ05B152PFPatJetPartonAssociationLegacy.partons = "signalPartons"

akFlowPuCsSoftDropZ05B152PFImpactParameterTagInfos = akFlowPuCsSoftDropZ05B152PFbTagger.ImpactParameterTagInfos
akFlowPuCsSoftDropZ05B152PFImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akFlowPuCsSoftDropZ05B152PFJetProbabilityBJetTags = akFlowPuCsSoftDropZ05B152PFbTagger.JetProbabilityBJetTags

akFlowPuCsSoftDropZ05B152PFSecondaryVertexTagInfos = akFlowPuCsSoftDropZ05B152PFbTagger.SecondaryVertexTagInfos
akFlowPuCsSoftDropZ05B152PFSimpleSecondaryVertexHighEffBJetTags = akFlowPuCsSoftDropZ05B152PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akFlowPuCsSoftDropZ05B152PFSimpleSecondaryVertexHighPurBJetTags = akFlowPuCsSoftDropZ05B152PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akFlowPuCsSoftDropZ05B152PFCombinedSecondaryVertexBJetTags = akFlowPuCsSoftDropZ05B152PFbTagger.CombinedSecondaryVertexBJetTags
akFlowPuCsSoftDropZ05B152PFCombinedSecondaryVertexV2BJetTags = akFlowPuCsSoftDropZ05B152PFbTagger.CombinedSecondaryVertexV2BJetTags

akFlowPuCsSoftDropZ05B152PFSecondaryVertexNegativeTagInfos = akFlowPuCsSoftDropZ05B152PFbTagger.SecondaryVertexNegativeTagInfos
akFlowPuCsSoftDropZ05B152PFNegativeSimpleSecondaryVertexHighEffBJetTags = akFlowPuCsSoftDropZ05B152PFbTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akFlowPuCsSoftDropZ05B152PFNegativeSimpleSecondaryVertexHighPurBJetTags = akFlowPuCsSoftDropZ05B152PFbTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akFlowPuCsSoftDropZ05B152PFNegativeCombinedSecondaryVertexBJetTags = akFlowPuCsSoftDropZ05B152PFbTagger.NegativeCombinedSecondaryVertexBJetTags
akFlowPuCsSoftDropZ05B152PFPositiveCombinedSecondaryVertexBJetTags = akFlowPuCsSoftDropZ05B152PFbTagger.PositiveCombinedSecondaryVertexBJetTags
akFlowPuCsSoftDropZ05B152PFNegativeCombinedSecondaryVertexV2BJetTags = akFlowPuCsSoftDropZ05B152PFbTagger.NegativeCombinedSecondaryVertexV2BJetTags
akFlowPuCsSoftDropZ05B152PFPositiveCombinedSecondaryVertexV2BJetTags = akFlowPuCsSoftDropZ05B152PFbTagger.PositiveCombinedSecondaryVertexV2BJetTags

akFlowPuCsSoftDropZ05B152PFSoftPFMuonsTagInfos = akFlowPuCsSoftDropZ05B152PFbTagger.SoftPFMuonsTagInfos
akFlowPuCsSoftDropZ05B152PFSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akFlowPuCsSoftDropZ05B152PFSoftPFMuonBJetTags = akFlowPuCsSoftDropZ05B152PFbTagger.SoftPFMuonBJetTags
akFlowPuCsSoftDropZ05B152PFSoftPFMuonByIP3dBJetTags = akFlowPuCsSoftDropZ05B152PFbTagger.SoftPFMuonByIP3dBJetTags
akFlowPuCsSoftDropZ05B152PFSoftPFMuonByPtBJetTags = akFlowPuCsSoftDropZ05B152PFbTagger.SoftPFMuonByPtBJetTags
akFlowPuCsSoftDropZ05B152PFNegativeSoftPFMuonByPtBJetTags = akFlowPuCsSoftDropZ05B152PFbTagger.NegativeSoftPFMuonByPtBJetTags
akFlowPuCsSoftDropZ05B152PFPositiveSoftPFMuonByPtBJetTags = akFlowPuCsSoftDropZ05B152PFbTagger.PositiveSoftPFMuonByPtBJetTags
akFlowPuCsSoftDropZ05B152PFPatJetFlavourIdLegacy = cms.Sequence(akFlowPuCsSoftDropZ05B152PFPatJetPartonAssociationLegacy*akFlowPuCsSoftDropZ05B152PFPatJetFlavourAssociationLegacy)
# Not working with our PU sub, but keep it here for reference
# akFlowPuCsSoftDropZ05B152PFPatJetFlavourAssociation = akFlowPuCsSoftDropZ05B152PFbTagger.PatJetFlavourAssociation
# akFlowPuCsSoftDropZ05B152PFPatJetFlavourId = cms.Sequence(akFlowPuCsSoftDropZ05B152PFPatJetPartons*akFlowPuCsSoftDropZ05B152PFPatJetFlavourAssociation)

akFlowPuCsSoftDropZ05B152PFJetBtaggingIP = cms.Sequence(
    akFlowPuCsSoftDropZ05B152PFImpactParameterTagInfos *
    akFlowPuCsSoftDropZ05B152PFTrackCountingHighEffBJetTags +
    akFlowPuCsSoftDropZ05B152PFTrackCountingHighPurBJetTags +
    akFlowPuCsSoftDropZ05B152PFJetProbabilityBJetTags +
    akFlowPuCsSoftDropZ05B152PFJetBProbabilityBJetTags
    )

akFlowPuCsSoftDropZ05B152PFJetBtaggingSV = cms.Sequence(
    akFlowPuCsSoftDropZ05B152PFImpactParameterTagInfos *
    akFlowPuCsSoftDropZ05B152PFSecondaryVertexTagInfos *
    akFlowPuCsSoftDropZ05B152PFSimpleSecondaryVertexHighEffBJetTags +
    akFlowPuCsSoftDropZ05B152PFSimpleSecondaryVertexHighPurBJetTags +
    akFlowPuCsSoftDropZ05B152PFCombinedSecondaryVertexBJetTags +
    akFlowPuCsSoftDropZ05B152PFCombinedSecondaryVertexV2BJetTags
    )

akFlowPuCsSoftDropZ05B152PFJetBtaggingNegSV = cms.Sequence(
    akFlowPuCsSoftDropZ05B152PFImpactParameterTagInfos *
    akFlowPuCsSoftDropZ05B152PFSecondaryVertexNegativeTagInfos *
    akFlowPuCsSoftDropZ05B152PFNegativeSimpleSecondaryVertexHighEffBJetTags +
    akFlowPuCsSoftDropZ05B152PFNegativeSimpleSecondaryVertexHighPurBJetTags +
    akFlowPuCsSoftDropZ05B152PFNegativeCombinedSecondaryVertexBJetTags +
    akFlowPuCsSoftDropZ05B152PFPositiveCombinedSecondaryVertexBJetTags +
    akFlowPuCsSoftDropZ05B152PFNegativeCombinedSecondaryVertexV2BJetTags +
    akFlowPuCsSoftDropZ05B152PFPositiveCombinedSecondaryVertexV2BJetTags
    )

akFlowPuCsSoftDropZ05B152PFJetBtaggingMu = cms.Sequence(
    akFlowPuCsSoftDropZ05B152PFSoftPFMuonsTagInfos *
    akFlowPuCsSoftDropZ05B152PFSoftPFMuonBJetTags +
    akFlowPuCsSoftDropZ05B152PFSoftPFMuonByIP3dBJetTags +
    akFlowPuCsSoftDropZ05B152PFSoftPFMuonByPtBJetTags +
    akFlowPuCsSoftDropZ05B152PFNegativeSoftPFMuonByPtBJetTags +
    akFlowPuCsSoftDropZ05B152PFPositiveSoftPFMuonByPtBJetTags
    )

akFlowPuCsSoftDropZ05B152PFJetBtagging = cms.Sequence(
    akFlowPuCsSoftDropZ05B152PFJetBtaggingIP
    * akFlowPuCsSoftDropZ05B152PFJetBtaggingSV
    # * akFlowPuCsSoftDropZ05B152PFJetBtaggingNegSV
    # * akFlowPuCsSoftDropZ05B152PFJetBtaggingMu
    )

akFlowPuCsSoftDropZ05B152PFpatJetsWithBtagging = patJets.clone(
    jetSource = cms.InputTag("akFlowPuCsSoftDropZ05B152PFJets"),
    genJetMatch            = cms.InputTag("akFlowPuCsSoftDropZ05B152PFmatch"),
    genPartonMatch         = cms.InputTag("akFlowPuCsSoftDropZ05B152PFparton"),
    jetCorrFactorsSource   = cms.VInputTag(cms.InputTag("akFlowPuCsSoftDropZ05B152PFcorr")),
    JetPartonMapSource     = cms.InputTag("akFlowPuCsSoftDropZ05B152PFPatJetFlavourAssociationLegacy"),
    JetFlavourInfoSource   = cms.InputTag("akFlowPuCsSoftDropZ05B152PFPatJetFlavourAssociation"),
    trackAssociationSource = cms.InputTag("akFlowPuCsSoftDropZ05B152PFJetTracksAssociatorAtVertex"),
    useLegacyJetMCFlavour  = True,
    discriminatorSources   = cms.VInputTag(
        cms.InputTag("akFlowPuCsSoftDropZ05B152PFSimpleSecondaryVertexHighEffBJetTags"),
        cms.InputTag("akFlowPuCsSoftDropZ05B152PFSimpleSecondaryVertexHighPurBJetTags"),
        cms.InputTag("akFlowPuCsSoftDropZ05B152PFCombinedSecondaryVertexBJetTags"),
        cms.InputTag("akFlowPuCsSoftDropZ05B152PFCombinedSecondaryVertexV2BJetTags"),
        cms.InputTag("akFlowPuCsSoftDropZ05B152PFJetBProbabilityBJetTags"),
        cms.InputTag("akFlowPuCsSoftDropZ05B152PFJetProbabilityBJetTags"),
        # cms.InputTag("akFlowPuCsSoftDropZ05B152PFSoftPFMuonByPtBJetTags"),
        # cms.InputTag("akFlowPuCsSoftDropZ05B152PFSoftPFMuonByIP3dBJetTags"),
        cms.InputTag("akFlowPuCsSoftDropZ05B152PFTrackCountingHighEffBJetTags"),
        cms.InputTag("akFlowPuCsSoftDropZ05B152PFTrackCountingHighPurBJetTags"),
        ),
    tagInfoSources = cms.VInputTag(cms.InputTag("akFlowPuCsSoftDropZ05B152PFImpactParameterTagInfos"),cms.InputTag("akFlowPuCsSoftDropZ05B152PFSecondaryVertexTagInfos")),
    jetIDMap = cms.InputTag("akFlowPuCsSoftDropZ05B152PFJetID"),
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

akFlowPuCsSoftDropZ05B152PFNjettiness = Njettiness.clone(
    src = cms.InputTag("akFlowPuCsSoftDropZ05B152PFJets"),
    R0  = cms.double(0.2)
    )

akFlowPuCsSoftDropZ05B152PFpatJetsWithBtagging.userData.userFloats.src += [
    'akFlowPuCsSoftDropZ05B152PFNjettiness:tau1',
    'akFlowPuCsSoftDropZ05B152PFNjettiness:tau2',
    'akFlowPuCsSoftDropZ05B152PFNjettiness:tau3']

akFlowPuCsSoftDropZ05B152PFJetAnalyzer = inclusiveJetAnalyzer.clone(
    jetTag = cms.InputTag("akFlowPuCsSoftDropZ05B152PFpatJetsWithBtagging"),
    genjetTag = 'ak2HiSignalGenJets',
    rParam = 0.2,
    matchJets = cms.untracked.bool(False),
    matchTag = 'patJetsWithBtagging',
    pfCandidateLabel = cms.untracked.InputTag('particleFlowTmp'),
    trackTag = cms.InputTag("hiGeneralTracks"),
    fillGenJets = False,
    isMC = False,
    doSubEvent = False,
    useHepMC = cms.untracked.bool(False),
    genParticles = cms.untracked.InputTag("genParticles"),
    eventInfoTag = cms.InputTag("generator"),
    doLifeTimeTagging = cms.untracked.bool(True),
    doLifeTimeTaggingExtras = cms.untracked.bool(False),
    bTagJetName = cms.untracked.string("akFlowPuCsSoftDropZ05B152PF"),
    jetName = cms.untracked.string("akFlowPuCsSoftDropZ05B152PF"),
    genPtMin = cms.untracked.double(5),
    hltTrgResults = cms.untracked.string('TriggerResults::'+'HISIGNAL'),
    doTower = cms.untracked.bool(True),
    doSubJets = cms.untracked.bool(True),
    doGenSubJets = cms.untracked.bool(False),
    subjetGenTag = cms.untracked.InputTag("akSoftDropZ05B152GenJets"),
    doGenTaus = cms.untracked.bool(False),
    genTau1 = cms.InputTag("akSoftDropZ05B152HiGenNjettiness","tau1"),
    genTau2 = cms.InputTag("akSoftDropZ05B152HiGenNjettiness","tau2"),
    genTau3 = cms.InputTag("akSoftDropZ05B152HiGenNjettiness","tau3"),
    doGenSym = cms.untracked.bool(False),
    genSym = cms.InputTag("akSoftDropZ05B152GenJets","sym"),
    genDroppedBranches = cms.InputTag("akSoftDropZ05B152GenJets","droppedBranches")
    )

akFlowPuCsSoftDropZ05B152PFJetSequence_mc = cms.Sequence(
    # akFlowPuCsSoftDropZ05B152PFclean
    # *
    akFlowPuCsSoftDropZ05B152PFmatch
    # *
    # akFlowPuCsSoftDropZ05B152PFmatchGroomed
    *
    akFlowPuCsSoftDropZ05B152PFparton
    *
    akFlowPuCsSoftDropZ05B152PFcorr
    # *
    # akFlowPuCsSoftDropZ05B152PFJetID
    *
    akFlowPuCsSoftDropZ05B152PFPatJetFlavourIdLegacy
    # *
    # akFlowPuCsSoftDropZ05B152PFPatJetFlavourId # Use legacy algo till PU implemented
    *
    akFlowPuCsSoftDropZ05B152PFJetTracksAssociatorAtVertex
    *
    akFlowPuCsSoftDropZ05B152PFJetBtagging
    *
    # No constituents for calo jets in pp. Must be removed for pp calo jets but
    # I'm not sure how to do this transparently (Marta)
    akFlowPuCsSoftDropZ05B152PFNjettiness
    *
    akFlowPuCsSoftDropZ05B152PFpatJetsWithBtagging
    *
    akFlowPuCsSoftDropZ05B152PFJetAnalyzer
    )

akFlowPuCsSoftDropZ05B152PFJetSequence_data = cms.Sequence(
    akFlowPuCsSoftDropZ05B152PFcorr
    *
    # akFlowPuCsSoftDropZ05B152PFJetID
    # *
    akFlowPuCsSoftDropZ05B152PFJetTracksAssociatorAtVertex
    *
    akFlowPuCsSoftDropZ05B152PFJetBtagging
    *
    akFlowPuCsSoftDropZ05B152PFNjettiness
    *
    akFlowPuCsSoftDropZ05B152PFpatJetsWithBtagging
    *
    akFlowPuCsSoftDropZ05B152PFJetAnalyzer
    )

akFlowPuCsSoftDropZ05B152PFJetSequence_mb = cms.Sequence(
    akFlowPuCsSoftDropZ05B152PFJetSequence_mc)
akFlowPuCsSoftDropZ05B152PFJetSequence_jec = cms.Sequence(
    akFlowPuCsSoftDropZ05B152PFJetSequence_mc)

akFlowPuCsSoftDropZ05B152PFJetSequence = cms.Sequence(
    akFlowPuCsSoftDropZ05B152PFJetSequence_data)
akFlowPuCsSoftDropZ05B152PFpatJetsWithBtagging.userData.userFloats.src += ['akFlowPuCsSoftDropZ05B152PFJets:sym']
akFlowPuCsSoftDropZ05B152PFpatJetsWithBtagging.userData.userInts.src += ['akFlowPuCsSoftDropZ05B152PFJets:droppedBranches']
