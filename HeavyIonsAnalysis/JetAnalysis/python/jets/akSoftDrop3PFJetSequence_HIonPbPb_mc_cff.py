import FWCore.ParameterSet.Config as cms

from PhysicsTools.PatAlgos.mcMatchLayer0.jetMatch_cfi import patJetGenJetMatch, patJetPartonMatch
from PhysicsTools.PatAlgos.recoLayer0.jetCorrFactors_cfi import patJetCorrFactors
from PhysicsTools.PatAlgos.producersLayer1.jetProducer_cfi import patJets

from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *

from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akSoftDrop3PFmatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDrop3PFJets"),
    matched = cms.InputTag("ak3HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.3
    )

akSoftDrop3PFmatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDrop3HiSignalGenJets"),
    matched = cms.InputTag("ak3HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.3
    )

akSoftDrop3PFparton = patJetPartonMatch.clone(
    src = cms.InputTag("akSoftDrop3PFJets"),
    matched = cms.InputTag("hiSignalGenParticles"))

akSoftDrop3PFcorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
    levels   = cms.vstring('L2Relative'),
    src = cms.InputTag("akSoftDrop3PFJets"),
    payload = "AK3PF"
    )

akSoftDrop3PFJetID = cms.EDProducer(
    'JetIDProducer',
    JetIDParams,
    src = cms.InputTag('akSoftDrop3CaloJets'))

# akSoftDrop3PFclean = heavyIonCleanedGenJets.clone(
#     src = cms.InputTag('ak3HiSignalGenJets'))

akSoftDrop3PFbTagger = bTaggers(
    "akSoftDrop3PF",
    0.3)

# create objects locally since they dont load properly otherwise
akSoftDrop3PFPatJetPartons = akSoftDrop3PFbTagger.PatJetPartons
akSoftDrop3PFJetTracksAssociatorAtVertex = akSoftDrop3PFbTagger.JetTracksAssociatorAtVertex
akSoftDrop3PFJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akSoftDrop3PFSimpleSecondaryVertexHighEffBJetTags = akSoftDrop3PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akSoftDrop3PFSimpleSecondaryVertexHighPurBJetTags = akSoftDrop3PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akSoftDrop3PFCombinedSecondaryVertexBJetTags = akSoftDrop3PFbTagger.CombinedSecondaryVertexBJetTags
akSoftDrop3PFCombinedSecondaryVertexV2BJetTags = akSoftDrop3PFbTagger.CombinedSecondaryVertexV2BJetTags
akSoftDrop3PFJetBProbabilityBJetTags = akSoftDrop3PFbTagger.JetBProbabilityBJetTags
akSoftDrop3PFSoftPFMuonByPtBJetTags = akSoftDrop3PFbTagger.SoftPFMuonByPtBJetTags
akSoftDrop3PFSoftPFMuonByIP3dBJetTags = akSoftDrop3PFbTagger.SoftPFMuonByIP3dBJetTags
akSoftDrop3PFTrackCountingHighEffBJetTags = akSoftDrop3PFbTagger.TrackCountingHighEffBJetTags
akSoftDrop3PFTrackCountingHighPurBJetTags = akSoftDrop3PFbTagger.TrackCountingHighPurBJetTags

akSoftDrop3PFImpactParameterTagInfos = akSoftDrop3PFbTagger.ImpactParameterTagInfos
akSoftDrop3PFImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akSoftDrop3PFJetProbabilityBJetTags = akSoftDrop3PFbTagger.JetProbabilityBJetTags

akSoftDrop3PFSecondaryVertexTagInfos = akSoftDrop3PFbTagger.SecondaryVertexTagInfos
akSoftDrop3PFSimpleSecondaryVertexHighEffBJetTags = akSoftDrop3PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akSoftDrop3PFSimpleSecondaryVertexHighPurBJetTags = akSoftDrop3PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akSoftDrop3PFCombinedSecondaryVertexBJetTags = akSoftDrop3PFbTagger.CombinedSecondaryVertexBJetTags
akSoftDrop3PFCombinedSecondaryVertexV2BJetTags = akSoftDrop3PFbTagger.CombinedSecondaryVertexV2BJetTags

akSoftDrop3PFSecondaryVertexNegativeTagInfos = akSoftDrop3PFbTagger.SecondaryVertexNegativeTagInfos
akSoftDrop3PFNegativeSimpleSecondaryVertexHighEffBJetTags = akSoftDrop3PFbTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akSoftDrop3PFNegativeSimpleSecondaryVertexHighPurBJetTags = akSoftDrop3PFbTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akSoftDrop3PFNegativeCombinedSecondaryVertexBJetTags = akSoftDrop3PFbTagger.NegativeCombinedSecondaryVertexBJetTags
akSoftDrop3PFPositiveCombinedSecondaryVertexBJetTags = akSoftDrop3PFbTagger.PositiveCombinedSecondaryVertexBJetTags
akSoftDrop3PFNegativeCombinedSecondaryVertexV2BJetTags = akSoftDrop3PFbTagger.NegativeCombinedSecondaryVertexV2BJetTags
akSoftDrop3PFPositiveCombinedSecondaryVertexV2BJetTags = akSoftDrop3PFbTagger.PositiveCombinedSecondaryVertexV2BJetTags

akSoftDrop3PFSoftPFMuonsTagInfos = akSoftDrop3PFbTagger.SoftPFMuonsTagInfos
akSoftDrop3PFSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akSoftDrop3PFSoftPFMuonBJetTags = akSoftDrop3PFbTagger.SoftPFMuonBJetTags
akSoftDrop3PFSoftPFMuonByIP3dBJetTags = akSoftDrop3PFbTagger.SoftPFMuonByIP3dBJetTags
akSoftDrop3PFSoftPFMuonByPtBJetTags = akSoftDrop3PFbTagger.SoftPFMuonByPtBJetTags
akSoftDrop3PFNegativeSoftPFMuonByPtBJetTags = akSoftDrop3PFbTagger.NegativeSoftPFMuonByPtBJetTags
akSoftDrop3PFPositiveSoftPFMuonByPtBJetTags = akSoftDrop3PFbTagger.PositiveSoftPFMuonByPtBJetTags
akSoftDrop3PFPatJetFlavourAssociation = akSoftDrop3PFbTagger.PatJetFlavourAssociation
akSoftDrop3PFPatJetFlavourId = cms.Sequence(akSoftDrop3PFPatJetPartons*akSoftDrop3PFPatJetFlavourAssociation)

akSoftDrop3PFJetBtaggingIP = cms.Sequence(
    akSoftDrop3PFImpactParameterTagInfos *
    akSoftDrop3PFTrackCountingHighEffBJetTags +
    akSoftDrop3PFTrackCountingHighPurBJetTags +
    akSoftDrop3PFJetProbabilityBJetTags +
    akSoftDrop3PFJetBProbabilityBJetTags
    )

akSoftDrop3PFJetBtaggingSV = cms.Sequence(
    akSoftDrop3PFImpactParameterTagInfos *
    akSoftDrop3PFSecondaryVertexTagInfos *
    akSoftDrop3PFSimpleSecondaryVertexHighEffBJetTags +
    akSoftDrop3PFSimpleSecondaryVertexHighPurBJetTags +
    akSoftDrop3PFCombinedSecondaryVertexBJetTags +
    akSoftDrop3PFCombinedSecondaryVertexV2BJetTags
    )

akSoftDrop3PFJetBtaggingNegSV = cms.Sequence(
    akSoftDrop3PFImpactParameterTagInfos *
    akSoftDrop3PFSecondaryVertexNegativeTagInfos *
    akSoftDrop3PFNegativeSimpleSecondaryVertexHighEffBJetTags +
    akSoftDrop3PFNegativeSimpleSecondaryVertexHighPurBJetTags +
    akSoftDrop3PFNegativeCombinedSecondaryVertexBJetTags +
    akSoftDrop3PFPositiveCombinedSecondaryVertexBJetTags +
    akSoftDrop3PFNegativeCombinedSecondaryVertexV2BJetTags +
    akSoftDrop3PFPositiveCombinedSecondaryVertexV2BJetTags
    )

akSoftDrop3PFJetBtaggingMu = cms.Sequence(
    akSoftDrop3PFSoftPFMuonsTagInfos *
    akSoftDrop3PFSoftPFMuonBJetTags +
    akSoftDrop3PFSoftPFMuonByIP3dBJetTags +
    akSoftDrop3PFSoftPFMuonByPtBJetTags +
    akSoftDrop3PFNegativeSoftPFMuonByPtBJetTags +
    akSoftDrop3PFPositiveSoftPFMuonByPtBJetTags
    )

akSoftDrop3PFJetBtagging = cms.Sequence(
    akSoftDrop3PFJetBtaggingIP
    * akSoftDrop3PFJetBtaggingSV
    # * akSoftDrop3PFJetBtaggingNegSV
    # * akSoftDrop3PFJetBtaggingMu
    )

akSoftDrop3PFpatJetsWithBtagging = patJets.clone(
    jetSource = cms.InputTag("akSoftDrop3PFJets"),
    genJetMatch            = cms.InputTag("akSoftDrop3PFmatch"),
    genPartonMatch         = cms.InputTag("akSoftDrop3PFparton"),
    jetCorrFactorsSource   = cms.VInputTag(cms.InputTag("akSoftDrop3PFcorr")),
    JetPartonMapSource     = cms.InputTag("akSoftDrop3PFPatJetFlavourAssociation"),
    JetFlavourInfoSource   = cms.InputTag("akSoftDrop3PFPatJetFlavourAssociation"),
    trackAssociationSource = cms.InputTag("akSoftDrop3PFJetTracksAssociatorAtVertex"),
    useLegacyJetMCFlavour  = False,
    discriminatorSources   = cms.VInputTag(
        cms.InputTag("akSoftDrop3PFSimpleSecondaryVertexHighEffBJetTags"),
        cms.InputTag("akSoftDrop3PFSimpleSecondaryVertexHighPurBJetTags"),
        cms.InputTag("akSoftDrop3PFCombinedSecondaryVertexBJetTags"),
        cms.InputTag("akSoftDrop3PFCombinedSecondaryVertexV2BJetTags"),
        cms.InputTag("akSoftDrop3PFJetBProbabilityBJetTags"),
        cms.InputTag("akSoftDrop3PFJetProbabilityBJetTags"),
        # cms.InputTag("akSoftDrop3PFSoftPFMuonByPtBJetTags"),
        # cms.InputTag("akSoftDrop3PFSoftPFMuonByIP3dBJetTags"),
        cms.InputTag("akSoftDrop3PFTrackCountingHighEffBJetTags"),
        cms.InputTag("akSoftDrop3PFTrackCountingHighPurBJetTags"),
        ),
    tagInfoSources = cms.VInputTag(cms.InputTag("akSoftDrop3PFImpactParameterTagInfos"),cms.InputTag("akSoftDrop3PFSecondaryVertexTagInfos")),
    jetIDMap = cms.InputTag("akSoftDrop3PFJetID"),
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

akSoftDrop3PFNjettiness = Njettiness.clone(
    src = cms.InputTag("akSoftDrop3PFJets"),
    R0  = cms.double(0.3)
    )

akSoftDrop3PFpatJetsWithBtagging.userData.userFloats.src += [
    'akSoftDrop3PFNjettiness:tau1',
    'akSoftDrop3PFNjettiness:tau2',
    'akSoftDrop3PFNjettiness:tau3']

akSoftDrop3PFJetAnalyzer = inclusiveJetAnalyzer.clone(
    jetTag = cms.InputTag("akSoftDrop3PFpatJetsWithBtagging"),
    genjetTag = 'ak3HiSignalGenJets',
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
    bTagJetName = cms.untracked.string("akSoftDrop3PF"),
    jetName = cms.untracked.string("akSoftDrop3PF"),
    genPtMin = cms.untracked.double(5),
    doTower = cms.untracked.bool(True),
    doSubJets = cms.untracked.bool(True),
    doGenSubJets = cms.untracked.bool(True),
    subjetGenTag = cms.untracked.InputTag("akSoftDrop3GenJets"),
    doGenTaus = cms.untracked.bool(False),
    genTau1 = cms.InputTag("akSoftDrop3HiGenNjettiness","tau1"),
    genTau2 = cms.InputTag("akSoftDrop3HiGenNjettiness","tau2"),
    genTau3 = cms.InputTag("akSoftDrop3HiGenNjettiness","tau3"),
    doGenSym = cms.untracked.bool(True),
    genSym = cms.InputTag("akSoftDrop3GenJets","sym"),
    genDroppedBranches = cms.InputTag("akSoftDrop3GenJets","droppedBranches")
    )

akSoftDrop3PFJetSequence_mc = cms.Sequence(
    # akSoftDrop3PFclean
    # *
    akSoftDrop3PFmatch
    # *
    # akSoftDrop3PFmatchGroomed
    *
    akSoftDrop3PFparton
    *
    akSoftDrop3PFcorr
    # *
    # akSoftDrop3PFJetID
    *
     akSoftDrop3PFPatJetFlavourId 
    *
    akSoftDrop3PFJetTracksAssociatorAtVertex
    *
    akSoftDrop3PFJetBtagging
    *
    # No constituents for calo jets in pp. Must be removed for pp calo jets but
    # I'm not sure how to do this transparently (Marta)
    akSoftDrop3PFNjettiness
    *
    akSoftDrop3PFpatJetsWithBtagging
    *
    akSoftDrop3PFJetAnalyzer
    )

akSoftDrop3PFJetSequence_data = cms.Sequence(
    akSoftDrop3PFcorr
    *
    # akSoftDrop3PFJetID
    # *
    akSoftDrop3PFJetTracksAssociatorAtVertex
    *
    akSoftDrop3PFJetBtagging
    *
    akSoftDrop3PFNjettiness
    *
    akSoftDrop3PFpatJetsWithBtagging
    *
    akSoftDrop3PFJetAnalyzer
    )

akSoftDrop3PFJetSequence_mb = cms.Sequence(
    akSoftDrop3PFJetSequence_mc)
akSoftDrop3PFJetSequence_jec = cms.Sequence(
    akSoftDrop3PFJetSequence_mc)

akSoftDrop3PFJetSequence = cms.Sequence(
    akSoftDrop3PFJetSequence_mc)
akSoftDrop3PFpatJetsWithBtagging.userData.userFloats.src += ['akSoftDrop3PFJets:sym']
akSoftDrop3PFpatJetsWithBtagging.userData.userInts.src += ['akSoftDrop3PFJets:droppedBranches']
