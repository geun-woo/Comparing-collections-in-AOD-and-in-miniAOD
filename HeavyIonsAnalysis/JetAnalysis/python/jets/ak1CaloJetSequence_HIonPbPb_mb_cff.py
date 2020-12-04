import FWCore.ParameterSet.Config as cms

from PhysicsTools.PatAlgos.mcMatchLayer0.jetMatch_cfi import patJetGenJetMatch, patJetPartonMatch
from PhysicsTools.PatAlgos.recoLayer0.jetCorrFactors_cfi import patJetCorrFactors
from PhysicsTools.PatAlgos.producersLayer1.jetProducer_cfi import patJets

from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *

from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

ak1Calomatch = patJetGenJetMatch.clone(
    src = cms.InputTag("ak1CaloJets"),
    matched = cms.InputTag("ak1HiCleanedGenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.1
    )

ak1CalomatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("ak1HiGenJets"),
    matched = cms.InputTag("ak1HiCleanedGenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.1
    )

ak1Caloparton = patJetPartonMatch.clone(
    src = cms.InputTag("ak1CaloJets"),
    matched = cms.InputTag("cleanedPartons"))

ak1Calocorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
    levels   = cms.vstring('L2Relative'),
    src = cms.InputTag("ak1CaloJets"),
    payload = "AK4PF"
    )

ak1CaloJetID = cms.EDProducer(
    'JetIDProducer',
    JetIDParams,
    src = cms.InputTag('ak1CaloJets'))

# ak1Caloclean = heavyIonCleanedGenJets.clone(
#     src = cms.InputTag('ak1HiCleanedGenJets'))

ak1CalobTagger = bTaggers(
    "ak1Calo",
    0.1)

# create objects locally since they dont load properly otherwise
ak1CaloPatJetPartons = ak1CalobTagger.PatJetPartons
ak1CaloJetTracksAssociatorAtVertex = ak1CalobTagger.JetTracksAssociatorAtVertex
ak1CaloJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
ak1CaloSimpleSecondaryVertexHighEffBJetTags = ak1CalobTagger.SimpleSecondaryVertexHighEffBJetTags
ak1CaloSimpleSecondaryVertexHighPurBJetTags = ak1CalobTagger.SimpleSecondaryVertexHighPurBJetTags
ak1CaloCombinedSecondaryVertexBJetTags = ak1CalobTagger.CombinedSecondaryVertexBJetTags
ak1CaloCombinedSecondaryVertexV2BJetTags = ak1CalobTagger.CombinedSecondaryVertexV2BJetTags
ak1CaloJetBProbabilityBJetTags = ak1CalobTagger.JetBProbabilityBJetTags
ak1CaloSoftPFMuonByPtBJetTags = ak1CalobTagger.SoftPFMuonByPtBJetTags
ak1CaloSoftPFMuonByIP3dBJetTags = ak1CalobTagger.SoftPFMuonByIP3dBJetTags
ak1CaloTrackCountingHighEffBJetTags = ak1CalobTagger.TrackCountingHighEffBJetTags
ak1CaloTrackCountingHighPurBJetTags = ak1CalobTagger.TrackCountingHighPurBJetTags

ak1CaloImpactParameterTagInfos = ak1CalobTagger.ImpactParameterTagInfos
ak1CaloImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
ak1CaloJetProbabilityBJetTags = ak1CalobTagger.JetProbabilityBJetTags

ak1CaloSecondaryVertexTagInfos = ak1CalobTagger.SecondaryVertexTagInfos
ak1CaloSimpleSecondaryVertexHighEffBJetTags = ak1CalobTagger.SimpleSecondaryVertexHighEffBJetTags
ak1CaloSimpleSecondaryVertexHighPurBJetTags = ak1CalobTagger.SimpleSecondaryVertexHighPurBJetTags
ak1CaloCombinedSecondaryVertexBJetTags = ak1CalobTagger.CombinedSecondaryVertexBJetTags
ak1CaloCombinedSecondaryVertexV2BJetTags = ak1CalobTagger.CombinedSecondaryVertexV2BJetTags

ak1CaloSecondaryVertexNegativeTagInfos = ak1CalobTagger.SecondaryVertexNegativeTagInfos
ak1CaloNegativeSimpleSecondaryVertexHighEffBJetTags = ak1CalobTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
ak1CaloNegativeSimpleSecondaryVertexHighPurBJetTags = ak1CalobTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
ak1CaloNegativeCombinedSecondaryVertexBJetTags = ak1CalobTagger.NegativeCombinedSecondaryVertexBJetTags
ak1CaloPositiveCombinedSecondaryVertexBJetTags = ak1CalobTagger.PositiveCombinedSecondaryVertexBJetTags
ak1CaloNegativeCombinedSecondaryVertexV2BJetTags = ak1CalobTagger.NegativeCombinedSecondaryVertexV2BJetTags
ak1CaloPositiveCombinedSecondaryVertexV2BJetTags = ak1CalobTagger.PositiveCombinedSecondaryVertexV2BJetTags

ak1CaloSoftPFMuonsTagInfos = ak1CalobTagger.SoftPFMuonsTagInfos
ak1CaloSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
ak1CaloSoftPFMuonBJetTags = ak1CalobTagger.SoftPFMuonBJetTags
ak1CaloSoftPFMuonByIP3dBJetTags = ak1CalobTagger.SoftPFMuonByIP3dBJetTags
ak1CaloSoftPFMuonByPtBJetTags = ak1CalobTagger.SoftPFMuonByPtBJetTags
ak1CaloNegativeSoftPFMuonByPtBJetTags = ak1CalobTagger.NegativeSoftPFMuonByPtBJetTags
ak1CaloPositiveSoftPFMuonByPtBJetTags = ak1CalobTagger.PositiveSoftPFMuonByPtBJetTags
ak1CaloPatJetFlavourAssociation = ak1CalobTagger.PatJetFlavourAssociation
ak1CaloPatJetFlavourId = cms.Sequence(ak1CaloPatJetPartons*ak1CaloPatJetFlavourAssociation)

ak1CaloJetBtaggingIP = cms.Sequence(
    ak1CaloImpactParameterTagInfos *
    ak1CaloTrackCountingHighEffBJetTags +
    ak1CaloTrackCountingHighPurBJetTags +
    ak1CaloJetProbabilityBJetTags +
    ak1CaloJetBProbabilityBJetTags
    )

ak1CaloJetBtaggingSV = cms.Sequence(
    ak1CaloImpactParameterTagInfos *
    ak1CaloSecondaryVertexTagInfos *
    ak1CaloSimpleSecondaryVertexHighEffBJetTags +
    ak1CaloSimpleSecondaryVertexHighPurBJetTags +
    ak1CaloCombinedSecondaryVertexBJetTags +
    ak1CaloCombinedSecondaryVertexV2BJetTags
    )

ak1CaloJetBtaggingNegSV = cms.Sequence(
    ak1CaloImpactParameterTagInfos *
    ak1CaloSecondaryVertexNegativeTagInfos *
    ak1CaloNegativeSimpleSecondaryVertexHighEffBJetTags +
    ak1CaloNegativeSimpleSecondaryVertexHighPurBJetTags +
    ak1CaloNegativeCombinedSecondaryVertexBJetTags +
    ak1CaloPositiveCombinedSecondaryVertexBJetTags +
    ak1CaloNegativeCombinedSecondaryVertexV2BJetTags +
    ak1CaloPositiveCombinedSecondaryVertexV2BJetTags
    )

ak1CaloJetBtaggingMu = cms.Sequence(
    ak1CaloSoftPFMuonsTagInfos *
    ak1CaloSoftPFMuonBJetTags +
    ak1CaloSoftPFMuonByIP3dBJetTags +
    ak1CaloSoftPFMuonByPtBJetTags +
    ak1CaloNegativeSoftPFMuonByPtBJetTags +
    ak1CaloPositiveSoftPFMuonByPtBJetTags
    )

ak1CaloJetBtagging = cms.Sequence(
    ak1CaloJetBtaggingIP
    * ak1CaloJetBtaggingSV
    # * ak1CaloJetBtaggingNegSV
    # * ak1CaloJetBtaggingMu
    )

ak1CalopatJetsWithBtagging = patJets.clone(
    jetSource = cms.InputTag("ak1CaloJets"),
    genJetMatch            = cms.InputTag("ak1Calomatch"),
    genPartonMatch         = cms.InputTag("ak1Caloparton"),
    jetCorrFactorsSource   = cms.VInputTag(cms.InputTag("ak1Calocorr")),
    JetPartonMapSource     = cms.InputTag("ak1CaloPatJetFlavourAssociation"),
    JetFlavourInfoSource   = cms.InputTag("ak1CaloPatJetFlavourAssociation"),
    trackAssociationSource = cms.InputTag("ak1CaloJetTracksAssociatorAtVertex"),
    useLegacyJetMCFlavour  = False,
    discriminatorSources   = cms.VInputTag(
        cms.InputTag("ak1CaloSimpleSecondaryVertexHighEffBJetTags"),
        cms.InputTag("ak1CaloSimpleSecondaryVertexHighPurBJetTags"),
        cms.InputTag("ak1CaloCombinedSecondaryVertexBJetTags"),
        cms.InputTag("ak1CaloCombinedSecondaryVertexV2BJetTags"),
        cms.InputTag("ak1CaloJetBProbabilityBJetTags"),
        cms.InputTag("ak1CaloJetProbabilityBJetTags"),
        # cms.InputTag("ak1CaloSoftPFMuonByPtBJetTags"),
        # cms.InputTag("ak1CaloSoftPFMuonByIP3dBJetTags"),
        cms.InputTag("ak1CaloTrackCountingHighEffBJetTags"),
        cms.InputTag("ak1CaloTrackCountingHighPurBJetTags"),
        ),
    tagInfoSources = cms.VInputTag(cms.InputTag("ak1CaloImpactParameterTagInfos"),cms.InputTag("ak1CaloSecondaryVertexTagInfos")),
    jetIDMap = cms.InputTag("ak1CaloJetID"),
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

ak1CaloNjettiness = Njettiness.clone(
    src = cms.InputTag("ak1CaloJets"),
    R0  = cms.double(0.1)
    )

ak1CalopatJetsWithBtagging.userData.userFloats.src += [
    'ak1CaloNjettiness:tau1',
    'ak1CaloNjettiness:tau2',
    'ak1CaloNjettiness:tau3']

ak1CaloJetAnalyzer = inclusiveJetAnalyzer.clone(
    jetTag = cms.InputTag("ak1CalopatJetsWithBtagging"),
    genjetTag = 'ak1HiGenJets',
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
    bTagJetName = cms.untracked.string("ak1Calo"),
    jetName = cms.untracked.string("ak1Calo"),
    genPtMin = cms.untracked.double(5),
    doTower = cms.untracked.bool(True),
    doSubJets = cms.untracked.bool(False),
    doGenSubJets = cms.untracked.bool(False),
    subjetGenTag = cms.untracked.InputTag("ak1GenJets"),
    doGenTaus = cms.untracked.bool(False),
    genTau1 = cms.InputTag("ak1HiGenNjettiness","tau1"),
    genTau2 = cms.InputTag("ak1HiGenNjettiness","tau2"),
    genTau3 = cms.InputTag("ak1HiGenNjettiness","tau3"),
    doGenSym = cms.untracked.bool(False),
    genSym = cms.InputTag("ak1GenJets","sym"),
    genDroppedBranches = cms.InputTag("ak1GenJets","droppedBranches")
    )

ak1CaloJetSequence_mc = cms.Sequence(
    # ak1Caloclean
    # *
    ak1Calomatch
    # *
    # ak1CalomatchGroomed
    *
    ak1Caloparton
    *
    ak1Calocorr
    # *
    # ak1CaloJetID
    *
     ak1CaloPatJetFlavourId 
    *
    ak1CaloJetTracksAssociatorAtVertex
    *
    ak1CaloJetBtagging
    *
    # No constituents for calo jets in pp. Must be removed for pp calo jets but
    # I'm not sure how to do this transparently (Marta)
    ak1CaloNjettiness
    *
    ak1CalopatJetsWithBtagging
    *
    ak1CaloJetAnalyzer
    )

ak1CaloJetSequence_data = cms.Sequence(
    ak1Calocorr
    *
    # ak1CaloJetID
    # *
    ak1CaloJetTracksAssociatorAtVertex
    *
    ak1CaloJetBtagging
    *
    ak1CaloNjettiness
    *
    ak1CalopatJetsWithBtagging
    *
    ak1CaloJetAnalyzer
    )

ak1CaloJetSequence_mb = cms.Sequence(
    ak1CaloJetSequence_mc)
ak1CaloJetSequence_jec = cms.Sequence(
    ak1CaloJetSequence_mc)

ak1CaloJetSequence = cms.Sequence(
    ak1CaloJetSequence_mb)
