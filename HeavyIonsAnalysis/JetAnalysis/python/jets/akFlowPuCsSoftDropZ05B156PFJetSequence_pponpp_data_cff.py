import FWCore.ParameterSet.Config as cms

from PhysicsTools.PatAlgos.mcMatchLayer0.jetMatch_cfi import patJetGenJetMatch, patJetPartonMatch
from PhysicsTools.PatAlgos.recoLayer0.jetCorrFactors_cfi import patJetCorrFactors
from PhysicsTools.PatAlgos.producersLayer1.jetProducer_cfi import patJets

from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *

from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akFlowPuCsSoftDropZ05B156PFmatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akFlowPuCsSoftDropZ05B156PFJets"),
    matched = cms.InputTag("ak6GenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.6
    )

akFlowPuCsSoftDropZ05B156PFmatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDropZ05B156GenJets"),
    matched = cms.InputTag("ak6GenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.6
    )

akFlowPuCsSoftDropZ05B156PFparton = patJetPartonMatch.clone(
    src = cms.InputTag("akFlowPuCsSoftDropZ05B156PFJets"),
    matched = cms.InputTag("genParticles"))

akFlowPuCsSoftDropZ05B156PFcorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
    levels   = cms.vstring('L2Relative','L2L3Residual'),
    src = cms.InputTag("akFlowPuCsSoftDropZ05B156PFJets"),
    payload = "AK6PF"
    )

akFlowPuCsSoftDropZ05B156PFJetID = cms.EDProducer(
    'JetIDProducer',
    JetIDParams,
    src = cms.InputTag('akFlowPuCsSoftDropZ05B156CaloJets'))

# akFlowPuCsSoftDropZ05B156PFclean = heavyIonCleanedGenJets.clone(
#     src = cms.InputTag('ak6GenJets'))

akFlowPuCsSoftDropZ05B156PFbTagger = bTaggers(
    "akFlowPuCsSoftDropZ05B156PF",
    0.6)

# create objects locally since they dont load properly otherwise
akFlowPuCsSoftDropZ05B156PFPatJetFlavourAssociationLegacy = akFlowPuCsSoftDropZ05B156PFbTagger.PatJetFlavourAssociationLegacy
akFlowPuCsSoftDropZ05B156PFPatJetPartons = akFlowPuCsSoftDropZ05B156PFbTagger.PatJetPartons
akFlowPuCsSoftDropZ05B156PFJetTracksAssociatorAtVertex = akFlowPuCsSoftDropZ05B156PFbTagger.JetTracksAssociatorAtVertex
akFlowPuCsSoftDropZ05B156PFJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akFlowPuCsSoftDropZ05B156PFSimpleSecondaryVertexHighEffBJetTags = akFlowPuCsSoftDropZ05B156PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akFlowPuCsSoftDropZ05B156PFSimpleSecondaryVertexHighPurBJetTags = akFlowPuCsSoftDropZ05B156PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akFlowPuCsSoftDropZ05B156PFCombinedSecondaryVertexBJetTags = akFlowPuCsSoftDropZ05B156PFbTagger.CombinedSecondaryVertexBJetTags
akFlowPuCsSoftDropZ05B156PFCombinedSecondaryVertexV2BJetTags = akFlowPuCsSoftDropZ05B156PFbTagger.CombinedSecondaryVertexV2BJetTags
akFlowPuCsSoftDropZ05B156PFJetBProbabilityBJetTags = akFlowPuCsSoftDropZ05B156PFbTagger.JetBProbabilityBJetTags
akFlowPuCsSoftDropZ05B156PFSoftPFMuonByPtBJetTags = akFlowPuCsSoftDropZ05B156PFbTagger.SoftPFMuonByPtBJetTags
akFlowPuCsSoftDropZ05B156PFSoftPFMuonByIP3dBJetTags = akFlowPuCsSoftDropZ05B156PFbTagger.SoftPFMuonByIP3dBJetTags
akFlowPuCsSoftDropZ05B156PFTrackCountingHighEffBJetTags = akFlowPuCsSoftDropZ05B156PFbTagger.TrackCountingHighEffBJetTags
akFlowPuCsSoftDropZ05B156PFTrackCountingHighPurBJetTags = akFlowPuCsSoftDropZ05B156PFbTagger.TrackCountingHighPurBJetTags
akFlowPuCsSoftDropZ05B156PFPatJetPartonAssociationLegacy = akFlowPuCsSoftDropZ05B156PFbTagger.PatJetPartonAssociationLegacy
akFlowPuCsSoftDropZ05B156PFPatJetPartonAssociationLegacy.partons = "myPartons"

akFlowPuCsSoftDropZ05B156PFImpactParameterTagInfos = akFlowPuCsSoftDropZ05B156PFbTagger.ImpactParameterTagInfos
akFlowPuCsSoftDropZ05B156PFImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akFlowPuCsSoftDropZ05B156PFJetProbabilityBJetTags = akFlowPuCsSoftDropZ05B156PFbTagger.JetProbabilityBJetTags

akFlowPuCsSoftDropZ05B156PFSecondaryVertexTagInfos = akFlowPuCsSoftDropZ05B156PFbTagger.SecondaryVertexTagInfos
akFlowPuCsSoftDropZ05B156PFSimpleSecondaryVertexHighEffBJetTags = akFlowPuCsSoftDropZ05B156PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akFlowPuCsSoftDropZ05B156PFSimpleSecondaryVertexHighPurBJetTags = akFlowPuCsSoftDropZ05B156PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akFlowPuCsSoftDropZ05B156PFCombinedSecondaryVertexBJetTags = akFlowPuCsSoftDropZ05B156PFbTagger.CombinedSecondaryVertexBJetTags
akFlowPuCsSoftDropZ05B156PFCombinedSecondaryVertexV2BJetTags = akFlowPuCsSoftDropZ05B156PFbTagger.CombinedSecondaryVertexV2BJetTags

akFlowPuCsSoftDropZ05B156PFSecondaryVertexNegativeTagInfos = akFlowPuCsSoftDropZ05B156PFbTagger.SecondaryVertexNegativeTagInfos
akFlowPuCsSoftDropZ05B156PFNegativeSimpleSecondaryVertexHighEffBJetTags = akFlowPuCsSoftDropZ05B156PFbTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akFlowPuCsSoftDropZ05B156PFNegativeSimpleSecondaryVertexHighPurBJetTags = akFlowPuCsSoftDropZ05B156PFbTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akFlowPuCsSoftDropZ05B156PFNegativeCombinedSecondaryVertexBJetTags = akFlowPuCsSoftDropZ05B156PFbTagger.NegativeCombinedSecondaryVertexBJetTags
akFlowPuCsSoftDropZ05B156PFPositiveCombinedSecondaryVertexBJetTags = akFlowPuCsSoftDropZ05B156PFbTagger.PositiveCombinedSecondaryVertexBJetTags
akFlowPuCsSoftDropZ05B156PFNegativeCombinedSecondaryVertexV2BJetTags = akFlowPuCsSoftDropZ05B156PFbTagger.NegativeCombinedSecondaryVertexV2BJetTags
akFlowPuCsSoftDropZ05B156PFPositiveCombinedSecondaryVertexV2BJetTags = akFlowPuCsSoftDropZ05B156PFbTagger.PositiveCombinedSecondaryVertexV2BJetTags

akFlowPuCsSoftDropZ05B156PFSoftPFMuonsTagInfos = akFlowPuCsSoftDropZ05B156PFbTagger.SoftPFMuonsTagInfos
akFlowPuCsSoftDropZ05B156PFSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akFlowPuCsSoftDropZ05B156PFSoftPFMuonBJetTags = akFlowPuCsSoftDropZ05B156PFbTagger.SoftPFMuonBJetTags
akFlowPuCsSoftDropZ05B156PFSoftPFMuonByIP3dBJetTags = akFlowPuCsSoftDropZ05B156PFbTagger.SoftPFMuonByIP3dBJetTags
akFlowPuCsSoftDropZ05B156PFSoftPFMuonByPtBJetTags = akFlowPuCsSoftDropZ05B156PFbTagger.SoftPFMuonByPtBJetTags
akFlowPuCsSoftDropZ05B156PFNegativeSoftPFMuonByPtBJetTags = akFlowPuCsSoftDropZ05B156PFbTagger.NegativeSoftPFMuonByPtBJetTags
akFlowPuCsSoftDropZ05B156PFPositiveSoftPFMuonByPtBJetTags = akFlowPuCsSoftDropZ05B156PFbTagger.PositiveSoftPFMuonByPtBJetTags
akFlowPuCsSoftDropZ05B156PFPatJetFlavourIdLegacy = cms.Sequence(akFlowPuCsSoftDropZ05B156PFPatJetPartonAssociationLegacy*akFlowPuCsSoftDropZ05B156PFPatJetFlavourAssociationLegacy)
# Not working with our PU sub, but keep it here for reference
# akFlowPuCsSoftDropZ05B156PFPatJetFlavourAssociation = akFlowPuCsSoftDropZ05B156PFbTagger.PatJetFlavourAssociation
# akFlowPuCsSoftDropZ05B156PFPatJetFlavourId = cms.Sequence(akFlowPuCsSoftDropZ05B156PFPatJetPartons*akFlowPuCsSoftDropZ05B156PFPatJetFlavourAssociation)

akFlowPuCsSoftDropZ05B156PFJetBtaggingIP = cms.Sequence(
    akFlowPuCsSoftDropZ05B156PFImpactParameterTagInfos *
    akFlowPuCsSoftDropZ05B156PFTrackCountingHighEffBJetTags +
    akFlowPuCsSoftDropZ05B156PFTrackCountingHighPurBJetTags +
    akFlowPuCsSoftDropZ05B156PFJetProbabilityBJetTags +
    akFlowPuCsSoftDropZ05B156PFJetBProbabilityBJetTags
    )

akFlowPuCsSoftDropZ05B156PFJetBtaggingSV = cms.Sequence(
    akFlowPuCsSoftDropZ05B156PFImpactParameterTagInfos *
    akFlowPuCsSoftDropZ05B156PFSecondaryVertexTagInfos *
    akFlowPuCsSoftDropZ05B156PFSimpleSecondaryVertexHighEffBJetTags +
    akFlowPuCsSoftDropZ05B156PFSimpleSecondaryVertexHighPurBJetTags +
    akFlowPuCsSoftDropZ05B156PFCombinedSecondaryVertexBJetTags +
    akFlowPuCsSoftDropZ05B156PFCombinedSecondaryVertexV2BJetTags
    )

akFlowPuCsSoftDropZ05B156PFJetBtaggingNegSV = cms.Sequence(
    akFlowPuCsSoftDropZ05B156PFImpactParameterTagInfos *
    akFlowPuCsSoftDropZ05B156PFSecondaryVertexNegativeTagInfos *
    akFlowPuCsSoftDropZ05B156PFNegativeSimpleSecondaryVertexHighEffBJetTags +
    akFlowPuCsSoftDropZ05B156PFNegativeSimpleSecondaryVertexHighPurBJetTags +
    akFlowPuCsSoftDropZ05B156PFNegativeCombinedSecondaryVertexBJetTags +
    akFlowPuCsSoftDropZ05B156PFPositiveCombinedSecondaryVertexBJetTags +
    akFlowPuCsSoftDropZ05B156PFNegativeCombinedSecondaryVertexV2BJetTags +
    akFlowPuCsSoftDropZ05B156PFPositiveCombinedSecondaryVertexV2BJetTags
    )

akFlowPuCsSoftDropZ05B156PFJetBtaggingMu = cms.Sequence(
    akFlowPuCsSoftDropZ05B156PFSoftPFMuonsTagInfos *
    akFlowPuCsSoftDropZ05B156PFSoftPFMuonBJetTags +
    akFlowPuCsSoftDropZ05B156PFSoftPFMuonByIP3dBJetTags +
    akFlowPuCsSoftDropZ05B156PFSoftPFMuonByPtBJetTags +
    akFlowPuCsSoftDropZ05B156PFNegativeSoftPFMuonByPtBJetTags +
    akFlowPuCsSoftDropZ05B156PFPositiveSoftPFMuonByPtBJetTags
    )

akFlowPuCsSoftDropZ05B156PFJetBtagging = cms.Sequence(
    akFlowPuCsSoftDropZ05B156PFJetBtaggingIP
    * akFlowPuCsSoftDropZ05B156PFJetBtaggingSV
    # * akFlowPuCsSoftDropZ05B156PFJetBtaggingNegSV
    # * akFlowPuCsSoftDropZ05B156PFJetBtaggingMu
    )

akFlowPuCsSoftDropZ05B156PFpatJetsWithBtagging = patJets.clone(
    jetSource = cms.InputTag("akFlowPuCsSoftDropZ05B156PFJets"),
    genJetMatch            = cms.InputTag("akFlowPuCsSoftDropZ05B156PFmatch"),
    genPartonMatch         = cms.InputTag("akFlowPuCsSoftDropZ05B156PFparton"),
    jetCorrFactorsSource   = cms.VInputTag(cms.InputTag("akFlowPuCsSoftDropZ05B156PFcorr")),
    JetPartonMapSource     = cms.InputTag("akFlowPuCsSoftDropZ05B156PFPatJetFlavourAssociationLegacy"),
    JetFlavourInfoSource   = cms.InputTag("akFlowPuCsSoftDropZ05B156PFPatJetFlavourAssociation"),
    trackAssociationSource = cms.InputTag("akFlowPuCsSoftDropZ05B156PFJetTracksAssociatorAtVertex"),
    useLegacyJetMCFlavour  = True,
    discriminatorSources   = cms.VInputTag(
        cms.InputTag("akFlowPuCsSoftDropZ05B156PFSimpleSecondaryVertexHighEffBJetTags"),
        cms.InputTag("akFlowPuCsSoftDropZ05B156PFSimpleSecondaryVertexHighPurBJetTags"),
        cms.InputTag("akFlowPuCsSoftDropZ05B156PFCombinedSecondaryVertexBJetTags"),
        cms.InputTag("akFlowPuCsSoftDropZ05B156PFCombinedSecondaryVertexV2BJetTags"),
        cms.InputTag("akFlowPuCsSoftDropZ05B156PFJetBProbabilityBJetTags"),
        cms.InputTag("akFlowPuCsSoftDropZ05B156PFJetProbabilityBJetTags"),
        # cms.InputTag("akFlowPuCsSoftDropZ05B156PFSoftPFMuonByPtBJetTags"),
        # cms.InputTag("akFlowPuCsSoftDropZ05B156PFSoftPFMuonByIP3dBJetTags"),
        cms.InputTag("akFlowPuCsSoftDropZ05B156PFTrackCountingHighEffBJetTags"),
        cms.InputTag("akFlowPuCsSoftDropZ05B156PFTrackCountingHighPurBJetTags"),
        ),
    tagInfoSources = cms.VInputTag(cms.InputTag("akFlowPuCsSoftDropZ05B156PFImpactParameterTagInfos"),cms.InputTag("akFlowPuCsSoftDropZ05B156PFSecondaryVertexTagInfos")),
    jetIDMap = cms.InputTag("akFlowPuCsSoftDropZ05B156PFJetID"),
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

akFlowPuCsSoftDropZ05B156PFNjettiness = Njettiness.clone(
    src = cms.InputTag("akFlowPuCsSoftDropZ05B156PFJets"),
    R0  = cms.double(0.6)
    )

akFlowPuCsSoftDropZ05B156PFpatJetsWithBtagging.userData.userFloats.src += [
    'akFlowPuCsSoftDropZ05B156PFNjettiness:tau1',
    'akFlowPuCsSoftDropZ05B156PFNjettiness:tau2',
    'akFlowPuCsSoftDropZ05B156PFNjettiness:tau3']

akFlowPuCsSoftDropZ05B156PFJetAnalyzer = inclusiveJetAnalyzer.clone(
    jetTag = cms.InputTag("akFlowPuCsSoftDropZ05B156PFpatJetsWithBtagging"),
    genjetTag = 'ak6GenJets',
    rParam = 0.6,
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
    bTagJetName = cms.untracked.string("akFlowPuCsSoftDropZ05B156PF"),
    jetName = cms.untracked.string("akFlowPuCsSoftDropZ05B156PF"),
    genPtMin = cms.untracked.double(5),
    hltTrgResults = cms.untracked.string('TriggerResults::'+'HISIGNAL'),
    doTower = cms.untracked.bool(False),
    doSubJets = cms.untracked.bool(True),
    doGenSubJets = cms.untracked.bool(False),
    subjetGenTag = cms.untracked.InputTag("akSoftDropZ05B156GenJets"),
    doGenTaus = cms.untracked.bool(False),
    genTau1 = cms.InputTag("akSoftDropZ05B156GenNjettiness","tau1"),
    genTau2 = cms.InputTag("akSoftDropZ05B156GenNjettiness","tau2"),
    genTau3 = cms.InputTag("akSoftDropZ05B156GenNjettiness","tau3"),
    doGenSym = cms.untracked.bool(False),
    genSym = cms.InputTag("akSoftDropZ05B156GenJets","sym"),
    genDroppedBranches = cms.InputTag("akSoftDropZ05B156GenJets","droppedBranches")
    )

akFlowPuCsSoftDropZ05B156PFJetSequence_mc = cms.Sequence(
    # akFlowPuCsSoftDropZ05B156PFclean
    # *
    akFlowPuCsSoftDropZ05B156PFmatch
    # *
    # akFlowPuCsSoftDropZ05B156PFmatchGroomed
    *
    akFlowPuCsSoftDropZ05B156PFparton
    *
    akFlowPuCsSoftDropZ05B156PFcorr
    # *
    # akFlowPuCsSoftDropZ05B156PFJetID
    *
    akFlowPuCsSoftDropZ05B156PFPatJetFlavourIdLegacy
    # *
    # akFlowPuCsSoftDropZ05B156PFPatJetFlavourId # Use legacy algo till PU implemented
    *
    akFlowPuCsSoftDropZ05B156PFJetTracksAssociatorAtVertex
    *
    akFlowPuCsSoftDropZ05B156PFJetBtagging
    *
    # No constituents for calo jets in pp. Must be removed for pp calo jets but
    # I'm not sure how to do this transparently (Marta)
    akFlowPuCsSoftDropZ05B156PFNjettiness
    *
    akFlowPuCsSoftDropZ05B156PFpatJetsWithBtagging
    *
    akFlowPuCsSoftDropZ05B156PFJetAnalyzer
    )

akFlowPuCsSoftDropZ05B156PFJetSequence_data = cms.Sequence(
    akFlowPuCsSoftDropZ05B156PFcorr
    *
    # akFlowPuCsSoftDropZ05B156PFJetID
    # *
    akFlowPuCsSoftDropZ05B156PFJetTracksAssociatorAtVertex
    *
    akFlowPuCsSoftDropZ05B156PFJetBtagging
    *
    akFlowPuCsSoftDropZ05B156PFNjettiness
    *
    akFlowPuCsSoftDropZ05B156PFpatJetsWithBtagging
    *
    akFlowPuCsSoftDropZ05B156PFJetAnalyzer
    )

akFlowPuCsSoftDropZ05B156PFJetSequence_mb = cms.Sequence(
    akFlowPuCsSoftDropZ05B156PFJetSequence_mc)
akFlowPuCsSoftDropZ05B156PFJetSequence_jec = cms.Sequence(
    akFlowPuCsSoftDropZ05B156PFJetSequence_mc)

akFlowPuCsSoftDropZ05B156PFJetSequence = cms.Sequence(
    akFlowPuCsSoftDropZ05B156PFJetSequence_data)
akFlowPuCsSoftDropZ05B156PFpatJetsWithBtagging.userData.userFloats.src += ['akFlowPuCsSoftDropZ05B156PFJets:sym']
akFlowPuCsSoftDropZ05B156PFpatJetsWithBtagging.userData.userInts.src += ['akFlowPuCsSoftDropZ05B156PFJets:droppedBranches']
