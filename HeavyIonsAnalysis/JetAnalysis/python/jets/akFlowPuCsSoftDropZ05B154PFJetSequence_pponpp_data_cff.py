import FWCore.ParameterSet.Config as cms

from PhysicsTools.PatAlgos.mcMatchLayer0.jetMatch_cfi import patJetGenJetMatch, patJetPartonMatch
from PhysicsTools.PatAlgos.recoLayer0.jetCorrFactors_cfi import patJetCorrFactors
from PhysicsTools.PatAlgos.producersLayer1.jetProducer_cfi import patJets

from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *

from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akFlowPuCsSoftDropZ05B154PFmatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akFlowPuCsSoftDropZ05B154PFJets"),
    matched = cms.InputTag("ak4GenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.4
    )

akFlowPuCsSoftDropZ05B154PFmatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDropZ05B154GenJets"),
    matched = cms.InputTag("ak4GenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.4
    )

akFlowPuCsSoftDropZ05B154PFparton = patJetPartonMatch.clone(
    src = cms.InputTag("akFlowPuCsSoftDropZ05B154PFJets"),
    matched = cms.InputTag("genParticles"))

akFlowPuCsSoftDropZ05B154PFcorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
    levels   = cms.vstring('L2Relative','L2L3Residual'),
    src = cms.InputTag("akFlowPuCsSoftDropZ05B154PFJets"),
    payload = "AK4PF"
    )

akFlowPuCsSoftDropZ05B154PFJetID = cms.EDProducer(
    'JetIDProducer',
    JetIDParams,
    src = cms.InputTag('akFlowPuCsSoftDropZ05B154CaloJets'))

# akFlowPuCsSoftDropZ05B154PFclean = heavyIonCleanedGenJets.clone(
#     src = cms.InputTag('ak4GenJets'))

akFlowPuCsSoftDropZ05B154PFbTagger = bTaggers(
    "akFlowPuCsSoftDropZ05B154PF",
    0.4)

# create objects locally since they dont load properly otherwise
akFlowPuCsSoftDropZ05B154PFPatJetFlavourAssociationLegacy = akFlowPuCsSoftDropZ05B154PFbTagger.PatJetFlavourAssociationLegacy
akFlowPuCsSoftDropZ05B154PFPatJetPartons = akFlowPuCsSoftDropZ05B154PFbTagger.PatJetPartons
akFlowPuCsSoftDropZ05B154PFJetTracksAssociatorAtVertex = akFlowPuCsSoftDropZ05B154PFbTagger.JetTracksAssociatorAtVertex
akFlowPuCsSoftDropZ05B154PFJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akFlowPuCsSoftDropZ05B154PFSimpleSecondaryVertexHighEffBJetTags = akFlowPuCsSoftDropZ05B154PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akFlowPuCsSoftDropZ05B154PFSimpleSecondaryVertexHighPurBJetTags = akFlowPuCsSoftDropZ05B154PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akFlowPuCsSoftDropZ05B154PFCombinedSecondaryVertexBJetTags = akFlowPuCsSoftDropZ05B154PFbTagger.CombinedSecondaryVertexBJetTags
akFlowPuCsSoftDropZ05B154PFCombinedSecondaryVertexV2BJetTags = akFlowPuCsSoftDropZ05B154PFbTagger.CombinedSecondaryVertexV2BJetTags
akFlowPuCsSoftDropZ05B154PFJetBProbabilityBJetTags = akFlowPuCsSoftDropZ05B154PFbTagger.JetBProbabilityBJetTags
akFlowPuCsSoftDropZ05B154PFSoftPFMuonByPtBJetTags = akFlowPuCsSoftDropZ05B154PFbTagger.SoftPFMuonByPtBJetTags
akFlowPuCsSoftDropZ05B154PFSoftPFMuonByIP3dBJetTags = akFlowPuCsSoftDropZ05B154PFbTagger.SoftPFMuonByIP3dBJetTags
akFlowPuCsSoftDropZ05B154PFTrackCountingHighEffBJetTags = akFlowPuCsSoftDropZ05B154PFbTagger.TrackCountingHighEffBJetTags
akFlowPuCsSoftDropZ05B154PFTrackCountingHighPurBJetTags = akFlowPuCsSoftDropZ05B154PFbTagger.TrackCountingHighPurBJetTags
akFlowPuCsSoftDropZ05B154PFPatJetPartonAssociationLegacy = akFlowPuCsSoftDropZ05B154PFbTagger.PatJetPartonAssociationLegacy
akFlowPuCsSoftDropZ05B154PFPatJetPartonAssociationLegacy.partons = "myPartons"

akFlowPuCsSoftDropZ05B154PFImpactParameterTagInfos = akFlowPuCsSoftDropZ05B154PFbTagger.ImpactParameterTagInfos
akFlowPuCsSoftDropZ05B154PFImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akFlowPuCsSoftDropZ05B154PFJetProbabilityBJetTags = akFlowPuCsSoftDropZ05B154PFbTagger.JetProbabilityBJetTags

akFlowPuCsSoftDropZ05B154PFSecondaryVertexTagInfos = akFlowPuCsSoftDropZ05B154PFbTagger.SecondaryVertexTagInfos
akFlowPuCsSoftDropZ05B154PFSimpleSecondaryVertexHighEffBJetTags = akFlowPuCsSoftDropZ05B154PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akFlowPuCsSoftDropZ05B154PFSimpleSecondaryVertexHighPurBJetTags = akFlowPuCsSoftDropZ05B154PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akFlowPuCsSoftDropZ05B154PFCombinedSecondaryVertexBJetTags = akFlowPuCsSoftDropZ05B154PFbTagger.CombinedSecondaryVertexBJetTags
akFlowPuCsSoftDropZ05B154PFCombinedSecondaryVertexV2BJetTags = akFlowPuCsSoftDropZ05B154PFbTagger.CombinedSecondaryVertexV2BJetTags

akFlowPuCsSoftDropZ05B154PFSecondaryVertexNegativeTagInfos = akFlowPuCsSoftDropZ05B154PFbTagger.SecondaryVertexNegativeTagInfos
akFlowPuCsSoftDropZ05B154PFNegativeSimpleSecondaryVertexHighEffBJetTags = akFlowPuCsSoftDropZ05B154PFbTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akFlowPuCsSoftDropZ05B154PFNegativeSimpleSecondaryVertexHighPurBJetTags = akFlowPuCsSoftDropZ05B154PFbTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akFlowPuCsSoftDropZ05B154PFNegativeCombinedSecondaryVertexBJetTags = akFlowPuCsSoftDropZ05B154PFbTagger.NegativeCombinedSecondaryVertexBJetTags
akFlowPuCsSoftDropZ05B154PFPositiveCombinedSecondaryVertexBJetTags = akFlowPuCsSoftDropZ05B154PFbTagger.PositiveCombinedSecondaryVertexBJetTags
akFlowPuCsSoftDropZ05B154PFNegativeCombinedSecondaryVertexV2BJetTags = akFlowPuCsSoftDropZ05B154PFbTagger.NegativeCombinedSecondaryVertexV2BJetTags
akFlowPuCsSoftDropZ05B154PFPositiveCombinedSecondaryVertexV2BJetTags = akFlowPuCsSoftDropZ05B154PFbTagger.PositiveCombinedSecondaryVertexV2BJetTags

akFlowPuCsSoftDropZ05B154PFSoftPFMuonsTagInfos = akFlowPuCsSoftDropZ05B154PFbTagger.SoftPFMuonsTagInfos
akFlowPuCsSoftDropZ05B154PFSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akFlowPuCsSoftDropZ05B154PFSoftPFMuonBJetTags = akFlowPuCsSoftDropZ05B154PFbTagger.SoftPFMuonBJetTags
akFlowPuCsSoftDropZ05B154PFSoftPFMuonByIP3dBJetTags = akFlowPuCsSoftDropZ05B154PFbTagger.SoftPFMuonByIP3dBJetTags
akFlowPuCsSoftDropZ05B154PFSoftPFMuonByPtBJetTags = akFlowPuCsSoftDropZ05B154PFbTagger.SoftPFMuonByPtBJetTags
akFlowPuCsSoftDropZ05B154PFNegativeSoftPFMuonByPtBJetTags = akFlowPuCsSoftDropZ05B154PFbTagger.NegativeSoftPFMuonByPtBJetTags
akFlowPuCsSoftDropZ05B154PFPositiveSoftPFMuonByPtBJetTags = akFlowPuCsSoftDropZ05B154PFbTagger.PositiveSoftPFMuonByPtBJetTags
akFlowPuCsSoftDropZ05B154PFPatJetFlavourIdLegacy = cms.Sequence(akFlowPuCsSoftDropZ05B154PFPatJetPartonAssociationLegacy*akFlowPuCsSoftDropZ05B154PFPatJetFlavourAssociationLegacy)
# Not working with our PU sub, but keep it here for reference
# akFlowPuCsSoftDropZ05B154PFPatJetFlavourAssociation = akFlowPuCsSoftDropZ05B154PFbTagger.PatJetFlavourAssociation
# akFlowPuCsSoftDropZ05B154PFPatJetFlavourId = cms.Sequence(akFlowPuCsSoftDropZ05B154PFPatJetPartons*akFlowPuCsSoftDropZ05B154PFPatJetFlavourAssociation)

akFlowPuCsSoftDropZ05B154PFJetBtaggingIP = cms.Sequence(
    akFlowPuCsSoftDropZ05B154PFImpactParameterTagInfos *
    akFlowPuCsSoftDropZ05B154PFTrackCountingHighEffBJetTags +
    akFlowPuCsSoftDropZ05B154PFTrackCountingHighPurBJetTags +
    akFlowPuCsSoftDropZ05B154PFJetProbabilityBJetTags +
    akFlowPuCsSoftDropZ05B154PFJetBProbabilityBJetTags
    )

akFlowPuCsSoftDropZ05B154PFJetBtaggingSV = cms.Sequence(
    akFlowPuCsSoftDropZ05B154PFImpactParameterTagInfos *
    akFlowPuCsSoftDropZ05B154PFSecondaryVertexTagInfos *
    akFlowPuCsSoftDropZ05B154PFSimpleSecondaryVertexHighEffBJetTags +
    akFlowPuCsSoftDropZ05B154PFSimpleSecondaryVertexHighPurBJetTags +
    akFlowPuCsSoftDropZ05B154PFCombinedSecondaryVertexBJetTags +
    akFlowPuCsSoftDropZ05B154PFCombinedSecondaryVertexV2BJetTags
    )

akFlowPuCsSoftDropZ05B154PFJetBtaggingNegSV = cms.Sequence(
    akFlowPuCsSoftDropZ05B154PFImpactParameterTagInfos *
    akFlowPuCsSoftDropZ05B154PFSecondaryVertexNegativeTagInfos *
    akFlowPuCsSoftDropZ05B154PFNegativeSimpleSecondaryVertexHighEffBJetTags +
    akFlowPuCsSoftDropZ05B154PFNegativeSimpleSecondaryVertexHighPurBJetTags +
    akFlowPuCsSoftDropZ05B154PFNegativeCombinedSecondaryVertexBJetTags +
    akFlowPuCsSoftDropZ05B154PFPositiveCombinedSecondaryVertexBJetTags +
    akFlowPuCsSoftDropZ05B154PFNegativeCombinedSecondaryVertexV2BJetTags +
    akFlowPuCsSoftDropZ05B154PFPositiveCombinedSecondaryVertexV2BJetTags
    )

akFlowPuCsSoftDropZ05B154PFJetBtaggingMu = cms.Sequence(
    akFlowPuCsSoftDropZ05B154PFSoftPFMuonsTagInfos *
    akFlowPuCsSoftDropZ05B154PFSoftPFMuonBJetTags +
    akFlowPuCsSoftDropZ05B154PFSoftPFMuonByIP3dBJetTags +
    akFlowPuCsSoftDropZ05B154PFSoftPFMuonByPtBJetTags +
    akFlowPuCsSoftDropZ05B154PFNegativeSoftPFMuonByPtBJetTags +
    akFlowPuCsSoftDropZ05B154PFPositiveSoftPFMuonByPtBJetTags
    )

akFlowPuCsSoftDropZ05B154PFJetBtagging = cms.Sequence(
    akFlowPuCsSoftDropZ05B154PFJetBtaggingIP
    * akFlowPuCsSoftDropZ05B154PFJetBtaggingSV
    # * akFlowPuCsSoftDropZ05B154PFJetBtaggingNegSV
    # * akFlowPuCsSoftDropZ05B154PFJetBtaggingMu
    )

akFlowPuCsSoftDropZ05B154PFpatJetsWithBtagging = patJets.clone(
    jetSource = cms.InputTag("akFlowPuCsSoftDropZ05B154PFJets"),
    genJetMatch            = cms.InputTag("akFlowPuCsSoftDropZ05B154PFmatch"),
    genPartonMatch         = cms.InputTag("akFlowPuCsSoftDropZ05B154PFparton"),
    jetCorrFactorsSource   = cms.VInputTag(cms.InputTag("akFlowPuCsSoftDropZ05B154PFcorr")),
    JetPartonMapSource     = cms.InputTag("akFlowPuCsSoftDropZ05B154PFPatJetFlavourAssociationLegacy"),
    JetFlavourInfoSource   = cms.InputTag("akFlowPuCsSoftDropZ05B154PFPatJetFlavourAssociation"),
    trackAssociationSource = cms.InputTag("akFlowPuCsSoftDropZ05B154PFJetTracksAssociatorAtVertex"),
    useLegacyJetMCFlavour  = True,
    discriminatorSources   = cms.VInputTag(
        cms.InputTag("akFlowPuCsSoftDropZ05B154PFSimpleSecondaryVertexHighEffBJetTags"),
        cms.InputTag("akFlowPuCsSoftDropZ05B154PFSimpleSecondaryVertexHighPurBJetTags"),
        cms.InputTag("akFlowPuCsSoftDropZ05B154PFCombinedSecondaryVertexBJetTags"),
        cms.InputTag("akFlowPuCsSoftDropZ05B154PFCombinedSecondaryVertexV2BJetTags"),
        cms.InputTag("akFlowPuCsSoftDropZ05B154PFJetBProbabilityBJetTags"),
        cms.InputTag("akFlowPuCsSoftDropZ05B154PFJetProbabilityBJetTags"),
        # cms.InputTag("akFlowPuCsSoftDropZ05B154PFSoftPFMuonByPtBJetTags"),
        # cms.InputTag("akFlowPuCsSoftDropZ05B154PFSoftPFMuonByIP3dBJetTags"),
        cms.InputTag("akFlowPuCsSoftDropZ05B154PFTrackCountingHighEffBJetTags"),
        cms.InputTag("akFlowPuCsSoftDropZ05B154PFTrackCountingHighPurBJetTags"),
        ),
    tagInfoSources = cms.VInputTag(cms.InputTag("akFlowPuCsSoftDropZ05B154PFImpactParameterTagInfos"),cms.InputTag("akFlowPuCsSoftDropZ05B154PFSecondaryVertexTagInfos")),
    jetIDMap = cms.InputTag("akFlowPuCsSoftDropZ05B154PFJetID"),
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

akFlowPuCsSoftDropZ05B154PFNjettiness = Njettiness.clone(
    src = cms.InputTag("akFlowPuCsSoftDropZ05B154PFJets"),
    R0  = cms.double(0.4)
    )

akFlowPuCsSoftDropZ05B154PFpatJetsWithBtagging.userData.userFloats.src += [
    'akFlowPuCsSoftDropZ05B154PFNjettiness:tau1',
    'akFlowPuCsSoftDropZ05B154PFNjettiness:tau2',
    'akFlowPuCsSoftDropZ05B154PFNjettiness:tau3']

akFlowPuCsSoftDropZ05B154PFJetAnalyzer = inclusiveJetAnalyzer.clone(
    jetTag = cms.InputTag("akFlowPuCsSoftDropZ05B154PFpatJetsWithBtagging"),
    genjetTag = 'ak4GenJets',
    rParam = 0.4,
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
    bTagJetName = cms.untracked.string("akFlowPuCsSoftDropZ05B154PF"),
    jetName = cms.untracked.string("akFlowPuCsSoftDropZ05B154PF"),
    genPtMin = cms.untracked.double(5),
    hltTrgResults = cms.untracked.string('TriggerResults::'+'HISIGNAL'),
    doTower = cms.untracked.bool(False),
    doSubJets = cms.untracked.bool(True),
    doGenSubJets = cms.untracked.bool(False),
    subjetGenTag = cms.untracked.InputTag("akSoftDropZ05B154GenJets"),
    doGenTaus = cms.untracked.bool(False),
    genTau1 = cms.InputTag("akSoftDropZ05B154GenNjettiness","tau1"),
    genTau2 = cms.InputTag("akSoftDropZ05B154GenNjettiness","tau2"),
    genTau3 = cms.InputTag("akSoftDropZ05B154GenNjettiness","tau3"),
    doGenSym = cms.untracked.bool(False),
    genSym = cms.InputTag("akSoftDropZ05B154GenJets","sym"),
    genDroppedBranches = cms.InputTag("akSoftDropZ05B154GenJets","droppedBranches")
    )

akFlowPuCsSoftDropZ05B154PFJetSequence_mc = cms.Sequence(
    # akFlowPuCsSoftDropZ05B154PFclean
    # *
    akFlowPuCsSoftDropZ05B154PFmatch
    # *
    # akFlowPuCsSoftDropZ05B154PFmatchGroomed
    *
    akFlowPuCsSoftDropZ05B154PFparton
    *
    akFlowPuCsSoftDropZ05B154PFcorr
    # *
    # akFlowPuCsSoftDropZ05B154PFJetID
    *
    akFlowPuCsSoftDropZ05B154PFPatJetFlavourIdLegacy
    # *
    # akFlowPuCsSoftDropZ05B154PFPatJetFlavourId # Use legacy algo till PU implemented
    *
    akFlowPuCsSoftDropZ05B154PFJetTracksAssociatorAtVertex
    *
    akFlowPuCsSoftDropZ05B154PFJetBtagging
    *
    # No constituents for calo jets in pp. Must be removed for pp calo jets but
    # I'm not sure how to do this transparently (Marta)
    akFlowPuCsSoftDropZ05B154PFNjettiness
    *
    akFlowPuCsSoftDropZ05B154PFpatJetsWithBtagging
    *
    akFlowPuCsSoftDropZ05B154PFJetAnalyzer
    )

akFlowPuCsSoftDropZ05B154PFJetSequence_data = cms.Sequence(
    akFlowPuCsSoftDropZ05B154PFcorr
    *
    # akFlowPuCsSoftDropZ05B154PFJetID
    # *
    akFlowPuCsSoftDropZ05B154PFJetTracksAssociatorAtVertex
    *
    akFlowPuCsSoftDropZ05B154PFJetBtagging
    *
    akFlowPuCsSoftDropZ05B154PFNjettiness
    *
    akFlowPuCsSoftDropZ05B154PFpatJetsWithBtagging
    *
    akFlowPuCsSoftDropZ05B154PFJetAnalyzer
    )

akFlowPuCsSoftDropZ05B154PFJetSequence_mb = cms.Sequence(
    akFlowPuCsSoftDropZ05B154PFJetSequence_mc)
akFlowPuCsSoftDropZ05B154PFJetSequence_jec = cms.Sequence(
    akFlowPuCsSoftDropZ05B154PFJetSequence_mc)

akFlowPuCsSoftDropZ05B154PFJetSequence = cms.Sequence(
    akFlowPuCsSoftDropZ05B154PFJetSequence_data)
akFlowPuCsSoftDropZ05B154PFpatJetsWithBtagging.userData.userFloats.src += ['akFlowPuCsSoftDropZ05B154PFJets:sym']
akFlowPuCsSoftDropZ05B154PFpatJetsWithBtagging.userData.userInts.src += ['akFlowPuCsSoftDropZ05B154PFJets:droppedBranches']
