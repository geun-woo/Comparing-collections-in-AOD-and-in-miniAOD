import FWCore.ParameterSet.Config as cms

from PhysicsTools.PatAlgos.mcMatchLayer0.jetMatch_cfi import patJetGenJetMatch, patJetPartonMatch
from PhysicsTools.PatAlgos.recoLayer0.jetCorrFactors_cfi import patJetCorrFactors
from PhysicsTools.PatAlgos.producersLayer1.jetProducer_cfi import patJets

from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *

from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akFlowPuCsSoftDrop4PFmatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akFlowPuCsSoftDrop4PFJets"),
    matched = cms.InputTag("ak4GenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.4
    )

akFlowPuCsSoftDrop4PFmatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDrop4GenJets"),
    matched = cms.InputTag("ak4GenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.4
    )

akFlowPuCsSoftDrop4PFparton = patJetPartonMatch.clone(
    src = cms.InputTag("akFlowPuCsSoftDrop4PFJets"),
    matched = cms.InputTag("genParticles"))

akFlowPuCsSoftDrop4PFcorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
    levels   = cms.vstring('L2Relative'),
    src = cms.InputTag("akFlowPuCsSoftDrop4PFJets"),
    payload = "AK4PF"
    )

akFlowPuCsSoftDrop4PFJetID = cms.EDProducer(
    'JetIDProducer',
    JetIDParams,
    src = cms.InputTag('akFlowPuCsSoftDrop4CaloJets'))

# akFlowPuCsSoftDrop4PFclean = heavyIonCleanedGenJets.clone(
#     src = cms.InputTag('ak4GenJets'))

akFlowPuCsSoftDrop4PFbTagger = bTaggers(
    "akFlowPuCsSoftDrop4PF",
    0.4)

# create objects locally since they dont load properly otherwise
akFlowPuCsSoftDrop4PFPatJetFlavourAssociationLegacy = akFlowPuCsSoftDrop4PFbTagger.PatJetFlavourAssociationLegacy
akFlowPuCsSoftDrop4PFPatJetPartons = akFlowPuCsSoftDrop4PFbTagger.PatJetPartons
akFlowPuCsSoftDrop4PFJetTracksAssociatorAtVertex = akFlowPuCsSoftDrop4PFbTagger.JetTracksAssociatorAtVertex
akFlowPuCsSoftDrop4PFJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akFlowPuCsSoftDrop4PFSimpleSecondaryVertexHighEffBJetTags = akFlowPuCsSoftDrop4PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akFlowPuCsSoftDrop4PFSimpleSecondaryVertexHighPurBJetTags = akFlowPuCsSoftDrop4PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akFlowPuCsSoftDrop4PFCombinedSecondaryVertexBJetTags = akFlowPuCsSoftDrop4PFbTagger.CombinedSecondaryVertexBJetTags
akFlowPuCsSoftDrop4PFCombinedSecondaryVertexV2BJetTags = akFlowPuCsSoftDrop4PFbTagger.CombinedSecondaryVertexV2BJetTags
akFlowPuCsSoftDrop4PFJetBProbabilityBJetTags = akFlowPuCsSoftDrop4PFbTagger.JetBProbabilityBJetTags
akFlowPuCsSoftDrop4PFSoftPFMuonByPtBJetTags = akFlowPuCsSoftDrop4PFbTagger.SoftPFMuonByPtBJetTags
akFlowPuCsSoftDrop4PFSoftPFMuonByIP3dBJetTags = akFlowPuCsSoftDrop4PFbTagger.SoftPFMuonByIP3dBJetTags
akFlowPuCsSoftDrop4PFTrackCountingHighEffBJetTags = akFlowPuCsSoftDrop4PFbTagger.TrackCountingHighEffBJetTags
akFlowPuCsSoftDrop4PFTrackCountingHighPurBJetTags = akFlowPuCsSoftDrop4PFbTagger.TrackCountingHighPurBJetTags
akFlowPuCsSoftDrop4PFPatJetPartonAssociationLegacy = akFlowPuCsSoftDrop4PFbTagger.PatJetPartonAssociationLegacy
akFlowPuCsSoftDrop4PFPatJetPartonAssociationLegacy.partons = "myPartons"

akFlowPuCsSoftDrop4PFImpactParameterTagInfos = akFlowPuCsSoftDrop4PFbTagger.ImpactParameterTagInfos
akFlowPuCsSoftDrop4PFImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akFlowPuCsSoftDrop4PFJetProbabilityBJetTags = akFlowPuCsSoftDrop4PFbTagger.JetProbabilityBJetTags

akFlowPuCsSoftDrop4PFSecondaryVertexTagInfos = akFlowPuCsSoftDrop4PFbTagger.SecondaryVertexTagInfos
akFlowPuCsSoftDrop4PFSimpleSecondaryVertexHighEffBJetTags = akFlowPuCsSoftDrop4PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akFlowPuCsSoftDrop4PFSimpleSecondaryVertexHighPurBJetTags = akFlowPuCsSoftDrop4PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akFlowPuCsSoftDrop4PFCombinedSecondaryVertexBJetTags = akFlowPuCsSoftDrop4PFbTagger.CombinedSecondaryVertexBJetTags
akFlowPuCsSoftDrop4PFCombinedSecondaryVertexV2BJetTags = akFlowPuCsSoftDrop4PFbTagger.CombinedSecondaryVertexV2BJetTags

akFlowPuCsSoftDrop4PFSecondaryVertexNegativeTagInfos = akFlowPuCsSoftDrop4PFbTagger.SecondaryVertexNegativeTagInfos
akFlowPuCsSoftDrop4PFNegativeSimpleSecondaryVertexHighEffBJetTags = akFlowPuCsSoftDrop4PFbTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akFlowPuCsSoftDrop4PFNegativeSimpleSecondaryVertexHighPurBJetTags = akFlowPuCsSoftDrop4PFbTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akFlowPuCsSoftDrop4PFNegativeCombinedSecondaryVertexBJetTags = akFlowPuCsSoftDrop4PFbTagger.NegativeCombinedSecondaryVertexBJetTags
akFlowPuCsSoftDrop4PFPositiveCombinedSecondaryVertexBJetTags = akFlowPuCsSoftDrop4PFbTagger.PositiveCombinedSecondaryVertexBJetTags
akFlowPuCsSoftDrop4PFNegativeCombinedSecondaryVertexV2BJetTags = akFlowPuCsSoftDrop4PFbTagger.NegativeCombinedSecondaryVertexV2BJetTags
akFlowPuCsSoftDrop4PFPositiveCombinedSecondaryVertexV2BJetTags = akFlowPuCsSoftDrop4PFbTagger.PositiveCombinedSecondaryVertexV2BJetTags

akFlowPuCsSoftDrop4PFSoftPFMuonsTagInfos = akFlowPuCsSoftDrop4PFbTagger.SoftPFMuonsTagInfos
akFlowPuCsSoftDrop4PFSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akFlowPuCsSoftDrop4PFSoftPFMuonBJetTags = akFlowPuCsSoftDrop4PFbTagger.SoftPFMuonBJetTags
akFlowPuCsSoftDrop4PFSoftPFMuonByIP3dBJetTags = akFlowPuCsSoftDrop4PFbTagger.SoftPFMuonByIP3dBJetTags
akFlowPuCsSoftDrop4PFSoftPFMuonByPtBJetTags = akFlowPuCsSoftDrop4PFbTagger.SoftPFMuonByPtBJetTags
akFlowPuCsSoftDrop4PFNegativeSoftPFMuonByPtBJetTags = akFlowPuCsSoftDrop4PFbTagger.NegativeSoftPFMuonByPtBJetTags
akFlowPuCsSoftDrop4PFPositiveSoftPFMuonByPtBJetTags = akFlowPuCsSoftDrop4PFbTagger.PositiveSoftPFMuonByPtBJetTags
akFlowPuCsSoftDrop4PFPatJetFlavourIdLegacy = cms.Sequence(akFlowPuCsSoftDrop4PFPatJetPartonAssociationLegacy*akFlowPuCsSoftDrop4PFPatJetFlavourAssociationLegacy)
# Not working with our PU sub, but keep it here for reference
# akFlowPuCsSoftDrop4PFPatJetFlavourAssociation = akFlowPuCsSoftDrop4PFbTagger.PatJetFlavourAssociation
# akFlowPuCsSoftDrop4PFPatJetFlavourId = cms.Sequence(akFlowPuCsSoftDrop4PFPatJetPartons*akFlowPuCsSoftDrop4PFPatJetFlavourAssociation)

akFlowPuCsSoftDrop4PFJetBtaggingIP = cms.Sequence(
    akFlowPuCsSoftDrop4PFImpactParameterTagInfos *
    akFlowPuCsSoftDrop4PFTrackCountingHighEffBJetTags +
    akFlowPuCsSoftDrop4PFTrackCountingHighPurBJetTags +
    akFlowPuCsSoftDrop4PFJetProbabilityBJetTags +
    akFlowPuCsSoftDrop4PFJetBProbabilityBJetTags
    )

akFlowPuCsSoftDrop4PFJetBtaggingSV = cms.Sequence(
    akFlowPuCsSoftDrop4PFImpactParameterTagInfos *
    akFlowPuCsSoftDrop4PFSecondaryVertexTagInfos *
    akFlowPuCsSoftDrop4PFSimpleSecondaryVertexHighEffBJetTags +
    akFlowPuCsSoftDrop4PFSimpleSecondaryVertexHighPurBJetTags +
    akFlowPuCsSoftDrop4PFCombinedSecondaryVertexBJetTags +
    akFlowPuCsSoftDrop4PFCombinedSecondaryVertexV2BJetTags
    )

akFlowPuCsSoftDrop4PFJetBtaggingNegSV = cms.Sequence(
    akFlowPuCsSoftDrop4PFImpactParameterTagInfos *
    akFlowPuCsSoftDrop4PFSecondaryVertexNegativeTagInfos *
    akFlowPuCsSoftDrop4PFNegativeSimpleSecondaryVertexHighEffBJetTags +
    akFlowPuCsSoftDrop4PFNegativeSimpleSecondaryVertexHighPurBJetTags +
    akFlowPuCsSoftDrop4PFNegativeCombinedSecondaryVertexBJetTags +
    akFlowPuCsSoftDrop4PFPositiveCombinedSecondaryVertexBJetTags +
    akFlowPuCsSoftDrop4PFNegativeCombinedSecondaryVertexV2BJetTags +
    akFlowPuCsSoftDrop4PFPositiveCombinedSecondaryVertexV2BJetTags
    )

akFlowPuCsSoftDrop4PFJetBtaggingMu = cms.Sequence(
    akFlowPuCsSoftDrop4PFSoftPFMuonsTagInfos *
    akFlowPuCsSoftDrop4PFSoftPFMuonBJetTags +
    akFlowPuCsSoftDrop4PFSoftPFMuonByIP3dBJetTags +
    akFlowPuCsSoftDrop4PFSoftPFMuonByPtBJetTags +
    akFlowPuCsSoftDrop4PFNegativeSoftPFMuonByPtBJetTags +
    akFlowPuCsSoftDrop4PFPositiveSoftPFMuonByPtBJetTags
    )

akFlowPuCsSoftDrop4PFJetBtagging = cms.Sequence(
    akFlowPuCsSoftDrop4PFJetBtaggingIP
    * akFlowPuCsSoftDrop4PFJetBtaggingSV
    # * akFlowPuCsSoftDrop4PFJetBtaggingNegSV
    # * akFlowPuCsSoftDrop4PFJetBtaggingMu
    )

akFlowPuCsSoftDrop4PFpatJetsWithBtagging = patJets.clone(
    jetSource = cms.InputTag("akFlowPuCsSoftDrop4PFJets"),
    genJetMatch            = cms.InputTag("akFlowPuCsSoftDrop4PFmatch"),
    genPartonMatch         = cms.InputTag("akFlowPuCsSoftDrop4PFparton"),
    jetCorrFactorsSource   = cms.VInputTag(cms.InputTag("akFlowPuCsSoftDrop4PFcorr")),
    JetPartonMapSource     = cms.InputTag("akFlowPuCsSoftDrop4PFPatJetFlavourAssociationLegacy"),
    JetFlavourInfoSource   = cms.InputTag("akFlowPuCsSoftDrop4PFPatJetFlavourAssociation"),
    trackAssociationSource = cms.InputTag("akFlowPuCsSoftDrop4PFJetTracksAssociatorAtVertex"),
    useLegacyJetMCFlavour  = True,
    discriminatorSources   = cms.VInputTag(
        cms.InputTag("akFlowPuCsSoftDrop4PFSimpleSecondaryVertexHighEffBJetTags"),
        cms.InputTag("akFlowPuCsSoftDrop4PFSimpleSecondaryVertexHighPurBJetTags"),
        cms.InputTag("akFlowPuCsSoftDrop4PFCombinedSecondaryVertexBJetTags"),
        cms.InputTag("akFlowPuCsSoftDrop4PFCombinedSecondaryVertexV2BJetTags"),
        cms.InputTag("akFlowPuCsSoftDrop4PFJetBProbabilityBJetTags"),
        cms.InputTag("akFlowPuCsSoftDrop4PFJetProbabilityBJetTags"),
        # cms.InputTag("akFlowPuCsSoftDrop4PFSoftPFMuonByPtBJetTags"),
        # cms.InputTag("akFlowPuCsSoftDrop4PFSoftPFMuonByIP3dBJetTags"),
        cms.InputTag("akFlowPuCsSoftDrop4PFTrackCountingHighEffBJetTags"),
        cms.InputTag("akFlowPuCsSoftDrop4PFTrackCountingHighPurBJetTags"),
        ),
    tagInfoSources = cms.VInputTag(cms.InputTag("akFlowPuCsSoftDrop4PFImpactParameterTagInfos"),cms.InputTag("akFlowPuCsSoftDrop4PFSecondaryVertexTagInfos")),
    jetIDMap = cms.InputTag("akFlowPuCsSoftDrop4PFJetID"),
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

akFlowPuCsSoftDrop4PFNjettiness = Njettiness.clone(
    src = cms.InputTag("akFlowPuCsSoftDrop4PFJets"),
    R0  = cms.double(0.4)
    )

akFlowPuCsSoftDrop4PFpatJetsWithBtagging.userData.userFloats.src += [
    'akFlowPuCsSoftDrop4PFNjettiness:tau1',
    'akFlowPuCsSoftDrop4PFNjettiness:tau2',
    'akFlowPuCsSoftDrop4PFNjettiness:tau3']

akFlowPuCsSoftDrop4PFJetAnalyzer = inclusiveJetAnalyzer.clone(
    jetTag = cms.InputTag("akFlowPuCsSoftDrop4PFpatJetsWithBtagging"),
    genjetTag = 'ak4GenJets',
    rParam = 0.4,
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
    bTagJetName = cms.untracked.string("akFlowPuCsSoftDrop4PF"),
    jetName = cms.untracked.string("akFlowPuCsSoftDrop4PF"),
    genPtMin = cms.untracked.double(5),
    hltTrgResults = cms.untracked.string('TriggerResults::'+'HISIGNAL'),
    doTower = cms.untracked.bool(False),
    doSubJets = cms.untracked.bool(True),
    doGenSubJets = cms.untracked.bool(True),
    subjetGenTag = cms.untracked.InputTag("akSoftDrop4GenJets"),
    doGenTaus = cms.untracked.bool(False),
    genTau1 = cms.InputTag("akSoftDrop4GenNjettiness","tau1"),
    genTau2 = cms.InputTag("akSoftDrop4GenNjettiness","tau2"),
    genTau3 = cms.InputTag("akSoftDrop4GenNjettiness","tau3"),
    doGenSym = cms.untracked.bool(True),
    genSym = cms.InputTag("akSoftDrop4GenJets","sym"),
    genDroppedBranches = cms.InputTag("akSoftDrop4GenJets","droppedBranches")
    )

akFlowPuCsSoftDrop4PFJetSequence_mc = cms.Sequence(
    # akFlowPuCsSoftDrop4PFclean
    # *
    akFlowPuCsSoftDrop4PFmatch
    # *
    # akFlowPuCsSoftDrop4PFmatchGroomed
    *
    akFlowPuCsSoftDrop4PFparton
    *
    akFlowPuCsSoftDrop4PFcorr
    # *
    # akFlowPuCsSoftDrop4PFJetID
    *
    akFlowPuCsSoftDrop4PFPatJetFlavourIdLegacy
    # *
    # akFlowPuCsSoftDrop4PFPatJetFlavourId # Use legacy algo till PU implemented
    *
    akFlowPuCsSoftDrop4PFJetTracksAssociatorAtVertex
    *
    akFlowPuCsSoftDrop4PFJetBtagging
    *
    # No constituents for calo jets in pp. Must be removed for pp calo jets but
    # I'm not sure how to do this transparently (Marta)
    akFlowPuCsSoftDrop4PFNjettiness
    *
    akFlowPuCsSoftDrop4PFpatJetsWithBtagging
    *
    akFlowPuCsSoftDrop4PFJetAnalyzer
    )

akFlowPuCsSoftDrop4PFJetSequence_data = cms.Sequence(
    akFlowPuCsSoftDrop4PFcorr
    *
    # akFlowPuCsSoftDrop4PFJetID
    # *
    akFlowPuCsSoftDrop4PFJetTracksAssociatorAtVertex
    *
    akFlowPuCsSoftDrop4PFJetBtagging
    *
    akFlowPuCsSoftDrop4PFNjettiness
    *
    akFlowPuCsSoftDrop4PFpatJetsWithBtagging
    *
    akFlowPuCsSoftDrop4PFJetAnalyzer
    )

akFlowPuCsSoftDrop4PFJetSequence_mb = cms.Sequence(
    akFlowPuCsSoftDrop4PFJetSequence_mc)
akFlowPuCsSoftDrop4PFJetSequence_jec = cms.Sequence(
    akFlowPuCsSoftDrop4PFJetSequence_mc)

akFlowPuCsSoftDrop4PFJetSequence = cms.Sequence(
    akFlowPuCsSoftDrop4PFJetSequence_mc)
akFlowPuCsSoftDrop4PFpatJetsWithBtagging.userData.userFloats.src += ['akFlowPuCsSoftDrop4PFJets:sym']
akFlowPuCsSoftDrop4PFpatJetsWithBtagging.userData.userInts.src += ['akFlowPuCsSoftDrop4PFJets:droppedBranches']


akFlowPuCsSoftDrop4PFJetAnalyzer.matchJets = cms.untracked.bool(True)
akFlowPuCsSoftDrop4PFJetAnalyzer.matchTag = cms.untracked.InputTag("ak4PFpatJetsWithBtagging")
