import FWCore.ParameterSet.Config as cms

from PhysicsTools.PatAlgos.mcMatchLayer0.jetMatch_cfi import patJetGenJetMatch, patJetPartonMatch
from PhysicsTools.PatAlgos.recoLayer0.jetCorrFactors_cfi import patJetCorrFactors
from PhysicsTools.PatAlgos.producersLayer1.jetProducer_cfi import patJets

from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *

from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akFlowPuCsSoftDrop3PFmatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akFlowPuCsSoftDrop3PFJets"),
    matched = cms.InputTag("ak3HiCleanedGenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.3
    )

akFlowPuCsSoftDrop3PFmatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDrop3HiGenJets"),
    matched = cms.InputTag("ak3HiCleanedGenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.3
    )

akFlowPuCsSoftDrop3PFparton = patJetPartonMatch.clone(
    src = cms.InputTag("akFlowPuCsSoftDrop3PFJets"),
    matched = cms.InputTag("cleanedPartons"))

akFlowPuCsSoftDrop3PFcorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
    levels   = cms.vstring('L2Relative'),
    src = cms.InputTag("akFlowPuCsSoftDrop3PFJets"),
    payload = "AK3PF"
    )

akFlowPuCsSoftDrop3PFJetID = cms.EDProducer(
    'JetIDProducer',
    JetIDParams,
    src = cms.InputTag('akFlowPuCsSoftDrop3CaloJets'))

# akFlowPuCsSoftDrop3PFclean = heavyIonCleanedGenJets.clone(
#     src = cms.InputTag('ak3HiCleanedGenJets'))

akFlowPuCsSoftDrop3PFbTagger = bTaggers(
    "akFlowPuCsSoftDrop3PF",
    0.3)

# create objects locally since they dont load properly otherwise
akFlowPuCsSoftDrop3PFPatJetFlavourAssociationLegacy = akFlowPuCsSoftDrop3PFbTagger.PatJetFlavourAssociationLegacy
akFlowPuCsSoftDrop3PFPatJetPartons = akFlowPuCsSoftDrop3PFbTagger.PatJetPartons
akFlowPuCsSoftDrop3PFJetTracksAssociatorAtVertex = akFlowPuCsSoftDrop3PFbTagger.JetTracksAssociatorAtVertex
akFlowPuCsSoftDrop3PFJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akFlowPuCsSoftDrop3PFSimpleSecondaryVertexHighEffBJetTags = akFlowPuCsSoftDrop3PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akFlowPuCsSoftDrop3PFSimpleSecondaryVertexHighPurBJetTags = akFlowPuCsSoftDrop3PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akFlowPuCsSoftDrop3PFCombinedSecondaryVertexBJetTags = akFlowPuCsSoftDrop3PFbTagger.CombinedSecondaryVertexBJetTags
akFlowPuCsSoftDrop3PFCombinedSecondaryVertexV2BJetTags = akFlowPuCsSoftDrop3PFbTagger.CombinedSecondaryVertexV2BJetTags
akFlowPuCsSoftDrop3PFJetBProbabilityBJetTags = akFlowPuCsSoftDrop3PFbTagger.JetBProbabilityBJetTags
akFlowPuCsSoftDrop3PFSoftPFMuonByPtBJetTags = akFlowPuCsSoftDrop3PFbTagger.SoftPFMuonByPtBJetTags
akFlowPuCsSoftDrop3PFSoftPFMuonByIP3dBJetTags = akFlowPuCsSoftDrop3PFbTagger.SoftPFMuonByIP3dBJetTags
akFlowPuCsSoftDrop3PFTrackCountingHighEffBJetTags = akFlowPuCsSoftDrop3PFbTagger.TrackCountingHighEffBJetTags
akFlowPuCsSoftDrop3PFTrackCountingHighPurBJetTags = akFlowPuCsSoftDrop3PFbTagger.TrackCountingHighPurBJetTags
akFlowPuCsSoftDrop3PFPatJetPartonAssociationLegacy = akFlowPuCsSoftDrop3PFbTagger.PatJetPartonAssociationLegacy
akFlowPuCsSoftDrop3PFPatJetPartonAssociationLegacy.partons = "myPartons"

akFlowPuCsSoftDrop3PFImpactParameterTagInfos = akFlowPuCsSoftDrop3PFbTagger.ImpactParameterTagInfos
akFlowPuCsSoftDrop3PFImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akFlowPuCsSoftDrop3PFJetProbabilityBJetTags = akFlowPuCsSoftDrop3PFbTagger.JetProbabilityBJetTags

akFlowPuCsSoftDrop3PFSecondaryVertexTagInfos = akFlowPuCsSoftDrop3PFbTagger.SecondaryVertexTagInfos
akFlowPuCsSoftDrop3PFSimpleSecondaryVertexHighEffBJetTags = akFlowPuCsSoftDrop3PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akFlowPuCsSoftDrop3PFSimpleSecondaryVertexHighPurBJetTags = akFlowPuCsSoftDrop3PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akFlowPuCsSoftDrop3PFCombinedSecondaryVertexBJetTags = akFlowPuCsSoftDrop3PFbTagger.CombinedSecondaryVertexBJetTags
akFlowPuCsSoftDrop3PFCombinedSecondaryVertexV2BJetTags = akFlowPuCsSoftDrop3PFbTagger.CombinedSecondaryVertexV2BJetTags

akFlowPuCsSoftDrop3PFSecondaryVertexNegativeTagInfos = akFlowPuCsSoftDrop3PFbTagger.SecondaryVertexNegativeTagInfos
akFlowPuCsSoftDrop3PFNegativeSimpleSecondaryVertexHighEffBJetTags = akFlowPuCsSoftDrop3PFbTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akFlowPuCsSoftDrop3PFNegativeSimpleSecondaryVertexHighPurBJetTags = akFlowPuCsSoftDrop3PFbTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akFlowPuCsSoftDrop3PFNegativeCombinedSecondaryVertexBJetTags = akFlowPuCsSoftDrop3PFbTagger.NegativeCombinedSecondaryVertexBJetTags
akFlowPuCsSoftDrop3PFPositiveCombinedSecondaryVertexBJetTags = akFlowPuCsSoftDrop3PFbTagger.PositiveCombinedSecondaryVertexBJetTags
akFlowPuCsSoftDrop3PFNegativeCombinedSecondaryVertexV2BJetTags = akFlowPuCsSoftDrop3PFbTagger.NegativeCombinedSecondaryVertexV2BJetTags
akFlowPuCsSoftDrop3PFPositiveCombinedSecondaryVertexV2BJetTags = akFlowPuCsSoftDrop3PFbTagger.PositiveCombinedSecondaryVertexV2BJetTags

akFlowPuCsSoftDrop3PFSoftPFMuonsTagInfos = akFlowPuCsSoftDrop3PFbTagger.SoftPFMuonsTagInfos
akFlowPuCsSoftDrop3PFSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akFlowPuCsSoftDrop3PFSoftPFMuonBJetTags = akFlowPuCsSoftDrop3PFbTagger.SoftPFMuonBJetTags
akFlowPuCsSoftDrop3PFSoftPFMuonByIP3dBJetTags = akFlowPuCsSoftDrop3PFbTagger.SoftPFMuonByIP3dBJetTags
akFlowPuCsSoftDrop3PFSoftPFMuonByPtBJetTags = akFlowPuCsSoftDrop3PFbTagger.SoftPFMuonByPtBJetTags
akFlowPuCsSoftDrop3PFNegativeSoftPFMuonByPtBJetTags = akFlowPuCsSoftDrop3PFbTagger.NegativeSoftPFMuonByPtBJetTags
akFlowPuCsSoftDrop3PFPositiveSoftPFMuonByPtBJetTags = akFlowPuCsSoftDrop3PFbTagger.PositiveSoftPFMuonByPtBJetTags
akFlowPuCsSoftDrop3PFPatJetFlavourIdLegacy = cms.Sequence(akFlowPuCsSoftDrop3PFPatJetPartonAssociationLegacy*akFlowPuCsSoftDrop3PFPatJetFlavourAssociationLegacy)
# Not working with our PU sub, but keep it here for reference
# akFlowPuCsSoftDrop3PFPatJetFlavourAssociation = akFlowPuCsSoftDrop3PFbTagger.PatJetFlavourAssociation
# akFlowPuCsSoftDrop3PFPatJetFlavourId = cms.Sequence(akFlowPuCsSoftDrop3PFPatJetPartons*akFlowPuCsSoftDrop3PFPatJetFlavourAssociation)

akFlowPuCsSoftDrop3PFJetBtaggingIP = cms.Sequence(
    akFlowPuCsSoftDrop3PFImpactParameterTagInfos *
    akFlowPuCsSoftDrop3PFTrackCountingHighEffBJetTags +
    akFlowPuCsSoftDrop3PFTrackCountingHighPurBJetTags +
    akFlowPuCsSoftDrop3PFJetProbabilityBJetTags +
    akFlowPuCsSoftDrop3PFJetBProbabilityBJetTags
    )

akFlowPuCsSoftDrop3PFJetBtaggingSV = cms.Sequence(
    akFlowPuCsSoftDrop3PFImpactParameterTagInfos *
    akFlowPuCsSoftDrop3PFSecondaryVertexTagInfos *
    akFlowPuCsSoftDrop3PFSimpleSecondaryVertexHighEffBJetTags +
    akFlowPuCsSoftDrop3PFSimpleSecondaryVertexHighPurBJetTags +
    akFlowPuCsSoftDrop3PFCombinedSecondaryVertexBJetTags +
    akFlowPuCsSoftDrop3PFCombinedSecondaryVertexV2BJetTags
    )

akFlowPuCsSoftDrop3PFJetBtaggingNegSV = cms.Sequence(
    akFlowPuCsSoftDrop3PFImpactParameterTagInfos *
    akFlowPuCsSoftDrop3PFSecondaryVertexNegativeTagInfos *
    akFlowPuCsSoftDrop3PFNegativeSimpleSecondaryVertexHighEffBJetTags +
    akFlowPuCsSoftDrop3PFNegativeSimpleSecondaryVertexHighPurBJetTags +
    akFlowPuCsSoftDrop3PFNegativeCombinedSecondaryVertexBJetTags +
    akFlowPuCsSoftDrop3PFPositiveCombinedSecondaryVertexBJetTags +
    akFlowPuCsSoftDrop3PFNegativeCombinedSecondaryVertexV2BJetTags +
    akFlowPuCsSoftDrop3PFPositiveCombinedSecondaryVertexV2BJetTags
    )

akFlowPuCsSoftDrop3PFJetBtaggingMu = cms.Sequence(
    akFlowPuCsSoftDrop3PFSoftPFMuonsTagInfos *
    akFlowPuCsSoftDrop3PFSoftPFMuonBJetTags +
    akFlowPuCsSoftDrop3PFSoftPFMuonByIP3dBJetTags +
    akFlowPuCsSoftDrop3PFSoftPFMuonByPtBJetTags +
    akFlowPuCsSoftDrop3PFNegativeSoftPFMuonByPtBJetTags +
    akFlowPuCsSoftDrop3PFPositiveSoftPFMuonByPtBJetTags
    )

akFlowPuCsSoftDrop3PFJetBtagging = cms.Sequence(
    akFlowPuCsSoftDrop3PFJetBtaggingIP
    * akFlowPuCsSoftDrop3PFJetBtaggingSV
    # * akFlowPuCsSoftDrop3PFJetBtaggingNegSV
    # * akFlowPuCsSoftDrop3PFJetBtaggingMu
    )

akFlowPuCsSoftDrop3PFpatJetsWithBtagging = patJets.clone(
    jetSource = cms.InputTag("akFlowPuCsSoftDrop3PFJets"),
    genJetMatch            = cms.InputTag("akFlowPuCsSoftDrop3PFmatch"),
    genPartonMatch         = cms.InputTag("akFlowPuCsSoftDrop3PFparton"),
    jetCorrFactorsSource   = cms.VInputTag(cms.InputTag("akFlowPuCsSoftDrop3PFcorr")),
    JetPartonMapSource     = cms.InputTag("akFlowPuCsSoftDrop3PFPatJetFlavourAssociationLegacy"),
    JetFlavourInfoSource   = cms.InputTag("akFlowPuCsSoftDrop3PFPatJetFlavourAssociation"),
    trackAssociationSource = cms.InputTag("akFlowPuCsSoftDrop3PFJetTracksAssociatorAtVertex"),
    useLegacyJetMCFlavour  = True,
    discriminatorSources   = cms.VInputTag(
        cms.InputTag("akFlowPuCsSoftDrop3PFSimpleSecondaryVertexHighEffBJetTags"),
        cms.InputTag("akFlowPuCsSoftDrop3PFSimpleSecondaryVertexHighPurBJetTags"),
        cms.InputTag("akFlowPuCsSoftDrop3PFCombinedSecondaryVertexBJetTags"),
        cms.InputTag("akFlowPuCsSoftDrop3PFCombinedSecondaryVertexV2BJetTags"),
        cms.InputTag("akFlowPuCsSoftDrop3PFJetBProbabilityBJetTags"),
        cms.InputTag("akFlowPuCsSoftDrop3PFJetProbabilityBJetTags"),
        # cms.InputTag("akFlowPuCsSoftDrop3PFSoftPFMuonByPtBJetTags"),
        # cms.InputTag("akFlowPuCsSoftDrop3PFSoftPFMuonByIP3dBJetTags"),
        cms.InputTag("akFlowPuCsSoftDrop3PFTrackCountingHighEffBJetTags"),
        cms.InputTag("akFlowPuCsSoftDrop3PFTrackCountingHighPurBJetTags"),
        ),
    tagInfoSources = cms.VInputTag(cms.InputTag("akFlowPuCsSoftDrop3PFImpactParameterTagInfos"),cms.InputTag("akFlowPuCsSoftDrop3PFSecondaryVertexTagInfos")),
    jetIDMap = cms.InputTag("akFlowPuCsSoftDrop3PFJetID"),
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

akFlowPuCsSoftDrop3PFNjettiness = Njettiness.clone(
    src = cms.InputTag("akFlowPuCsSoftDrop3PFJets"),
    R0  = cms.double(0.3)
    )

akFlowPuCsSoftDrop3PFpatJetsWithBtagging.userData.userFloats.src += [
    'akFlowPuCsSoftDrop3PFNjettiness:tau1',
    'akFlowPuCsSoftDrop3PFNjettiness:tau2',
    'akFlowPuCsSoftDrop3PFNjettiness:tau3']

akFlowPuCsSoftDrop3PFJetAnalyzer = inclusiveJetAnalyzer.clone(
    jetTag = cms.InputTag("akFlowPuCsSoftDrop3PFpatJetsWithBtagging"),
    genjetTag = 'ak3HiGenJets',
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
    bTagJetName = cms.untracked.string("akFlowPuCsSoftDrop3PF"),
    jetName = cms.untracked.string("akFlowPuCsSoftDrop3PF"),
    genPtMin = cms.untracked.double(5),
    hltTrgResults = cms.untracked.string('TriggerResults::'+'HISIGNAL'),
    doTower = cms.untracked.bool(True),
    doSubJets = cms.untracked.bool(True),
    doGenSubJets = cms.untracked.bool(False),
    subjetGenTag = cms.untracked.InputTag("akSoftDrop3GenJets"),
    doGenTaus = cms.untracked.bool(False),
    genTau1 = cms.InputTag("akSoftDrop3HiGenNjettiness","tau1"),
    genTau2 = cms.InputTag("akSoftDrop3HiGenNjettiness","tau2"),
    genTau3 = cms.InputTag("akSoftDrop3HiGenNjettiness","tau3"),
    doGenSym = cms.untracked.bool(False),
    genSym = cms.InputTag("akSoftDrop3GenJets","sym"),
    genDroppedBranches = cms.InputTag("akSoftDrop3GenJets","droppedBranches")
    )

akFlowPuCsSoftDrop3PFJetSequence_mc = cms.Sequence(
    # akFlowPuCsSoftDrop3PFclean
    # *
    akFlowPuCsSoftDrop3PFmatch
    # *
    # akFlowPuCsSoftDrop3PFmatchGroomed
    *
    akFlowPuCsSoftDrop3PFparton
    *
    akFlowPuCsSoftDrop3PFcorr
    # *
    # akFlowPuCsSoftDrop3PFJetID
    *
    akFlowPuCsSoftDrop3PFPatJetFlavourIdLegacy
    # *
    # akFlowPuCsSoftDrop3PFPatJetFlavourId # Use legacy algo till PU implemented
    *
    akFlowPuCsSoftDrop3PFJetTracksAssociatorAtVertex
    *
    akFlowPuCsSoftDrop3PFJetBtagging
    *
    # No constituents for calo jets in pp. Must be removed for pp calo jets but
    # I'm not sure how to do this transparently (Marta)
    akFlowPuCsSoftDrop3PFNjettiness
    *
    akFlowPuCsSoftDrop3PFpatJetsWithBtagging
    *
    akFlowPuCsSoftDrop3PFJetAnalyzer
    )

akFlowPuCsSoftDrop3PFJetSequence_data = cms.Sequence(
    akFlowPuCsSoftDrop3PFcorr
    *
    # akFlowPuCsSoftDrop3PFJetID
    # *
    akFlowPuCsSoftDrop3PFJetTracksAssociatorAtVertex
    *
    akFlowPuCsSoftDrop3PFJetBtagging
    *
    akFlowPuCsSoftDrop3PFNjettiness
    *
    akFlowPuCsSoftDrop3PFpatJetsWithBtagging
    *
    akFlowPuCsSoftDrop3PFJetAnalyzer
    )

akFlowPuCsSoftDrop3PFJetSequence_mb = cms.Sequence(
    akFlowPuCsSoftDrop3PFJetSequence_mc)
akFlowPuCsSoftDrop3PFJetSequence_jec = cms.Sequence(
    akFlowPuCsSoftDrop3PFJetSequence_mc)

akFlowPuCsSoftDrop3PFJetSequence = cms.Sequence(
    akFlowPuCsSoftDrop3PFJetSequence_mb)
akFlowPuCsSoftDrop3PFpatJetsWithBtagging.userData.userFloats.src += ['akFlowPuCsSoftDrop3PFJets:sym']
akFlowPuCsSoftDrop3PFpatJetsWithBtagging.userData.userInts.src += ['akFlowPuCsSoftDrop3PFJets:droppedBranches']
