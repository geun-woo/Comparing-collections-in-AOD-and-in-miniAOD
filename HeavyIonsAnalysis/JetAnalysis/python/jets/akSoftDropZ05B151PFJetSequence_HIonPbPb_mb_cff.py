import FWCore.ParameterSet.Config as cms

from PhysicsTools.PatAlgos.mcMatchLayer0.jetMatch_cfi import patJetGenJetMatch, patJetPartonMatch
from PhysicsTools.PatAlgos.recoLayer0.jetCorrFactors_cfi import patJetCorrFactors
from PhysicsTools.PatAlgos.producersLayer1.jetProducer_cfi import patJets

from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *

from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akSoftDropZ05B151PFmatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDropZ05B151PFJets"),
    matched = cms.InputTag("ak1HiCleanedGenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.1
    )

akSoftDropZ05B151PFmatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDropZ05B151HiGenJets"),
    matched = cms.InputTag("ak1HiCleanedGenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.1
    )

akSoftDropZ05B151PFparton = patJetPartonMatch.clone(
    src = cms.InputTag("akSoftDropZ05B151PFJets"),
    matched = cms.InputTag("cleanedPartons"))

akSoftDropZ05B151PFcorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
    levels   = cms.vstring('L2Relative'),
    src = cms.InputTag("akSoftDropZ05B151PFJets"),
    payload = "AK1PF"
    )

akSoftDropZ05B151PFJetID = cms.EDProducer(
    'JetIDProducer',
    JetIDParams,
    src = cms.InputTag('akSoftDropZ05B151CaloJets'))

# akSoftDropZ05B151PFclean = heavyIonCleanedGenJets.clone(
#     src = cms.InputTag('ak1HiCleanedGenJets'))

akSoftDropZ05B151PFbTagger = bTaggers(
    "akSoftDropZ05B151PF",
    0.1)

# create objects locally since they dont load properly otherwise
akSoftDropZ05B151PFPatJetPartons = akSoftDropZ05B151PFbTagger.PatJetPartons
akSoftDropZ05B151PFJetTracksAssociatorAtVertex = akSoftDropZ05B151PFbTagger.JetTracksAssociatorAtVertex
akSoftDropZ05B151PFJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akSoftDropZ05B151PFSimpleSecondaryVertexHighEffBJetTags = akSoftDropZ05B151PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akSoftDropZ05B151PFSimpleSecondaryVertexHighPurBJetTags = akSoftDropZ05B151PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akSoftDropZ05B151PFCombinedSecondaryVertexBJetTags = akSoftDropZ05B151PFbTagger.CombinedSecondaryVertexBJetTags
akSoftDropZ05B151PFCombinedSecondaryVertexV2BJetTags = akSoftDropZ05B151PFbTagger.CombinedSecondaryVertexV2BJetTags
akSoftDropZ05B151PFJetBProbabilityBJetTags = akSoftDropZ05B151PFbTagger.JetBProbabilityBJetTags
akSoftDropZ05B151PFSoftPFMuonByPtBJetTags = akSoftDropZ05B151PFbTagger.SoftPFMuonByPtBJetTags
akSoftDropZ05B151PFSoftPFMuonByIP3dBJetTags = akSoftDropZ05B151PFbTagger.SoftPFMuonByIP3dBJetTags
akSoftDropZ05B151PFTrackCountingHighEffBJetTags = akSoftDropZ05B151PFbTagger.TrackCountingHighEffBJetTags
akSoftDropZ05B151PFTrackCountingHighPurBJetTags = akSoftDropZ05B151PFbTagger.TrackCountingHighPurBJetTags

akSoftDropZ05B151PFImpactParameterTagInfos = akSoftDropZ05B151PFbTagger.ImpactParameterTagInfos
akSoftDropZ05B151PFImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akSoftDropZ05B151PFJetProbabilityBJetTags = akSoftDropZ05B151PFbTagger.JetProbabilityBJetTags

akSoftDropZ05B151PFSecondaryVertexTagInfos = akSoftDropZ05B151PFbTagger.SecondaryVertexTagInfos
akSoftDropZ05B151PFSimpleSecondaryVertexHighEffBJetTags = akSoftDropZ05B151PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akSoftDropZ05B151PFSimpleSecondaryVertexHighPurBJetTags = akSoftDropZ05B151PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akSoftDropZ05B151PFCombinedSecondaryVertexBJetTags = akSoftDropZ05B151PFbTagger.CombinedSecondaryVertexBJetTags
akSoftDropZ05B151PFCombinedSecondaryVertexV2BJetTags = akSoftDropZ05B151PFbTagger.CombinedSecondaryVertexV2BJetTags

akSoftDropZ05B151PFSecondaryVertexNegativeTagInfos = akSoftDropZ05B151PFbTagger.SecondaryVertexNegativeTagInfos
akSoftDropZ05B151PFNegativeSimpleSecondaryVertexHighEffBJetTags = akSoftDropZ05B151PFbTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akSoftDropZ05B151PFNegativeSimpleSecondaryVertexHighPurBJetTags = akSoftDropZ05B151PFbTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akSoftDropZ05B151PFNegativeCombinedSecondaryVertexBJetTags = akSoftDropZ05B151PFbTagger.NegativeCombinedSecondaryVertexBJetTags
akSoftDropZ05B151PFPositiveCombinedSecondaryVertexBJetTags = akSoftDropZ05B151PFbTagger.PositiveCombinedSecondaryVertexBJetTags
akSoftDropZ05B151PFNegativeCombinedSecondaryVertexV2BJetTags = akSoftDropZ05B151PFbTagger.NegativeCombinedSecondaryVertexV2BJetTags
akSoftDropZ05B151PFPositiveCombinedSecondaryVertexV2BJetTags = akSoftDropZ05B151PFbTagger.PositiveCombinedSecondaryVertexV2BJetTags

akSoftDropZ05B151PFSoftPFMuonsTagInfos = akSoftDropZ05B151PFbTagger.SoftPFMuonsTagInfos
akSoftDropZ05B151PFSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akSoftDropZ05B151PFSoftPFMuonBJetTags = akSoftDropZ05B151PFbTagger.SoftPFMuonBJetTags
akSoftDropZ05B151PFSoftPFMuonByIP3dBJetTags = akSoftDropZ05B151PFbTagger.SoftPFMuonByIP3dBJetTags
akSoftDropZ05B151PFSoftPFMuonByPtBJetTags = akSoftDropZ05B151PFbTagger.SoftPFMuonByPtBJetTags
akSoftDropZ05B151PFNegativeSoftPFMuonByPtBJetTags = akSoftDropZ05B151PFbTagger.NegativeSoftPFMuonByPtBJetTags
akSoftDropZ05B151PFPositiveSoftPFMuonByPtBJetTags = akSoftDropZ05B151PFbTagger.PositiveSoftPFMuonByPtBJetTags
akSoftDropZ05B151PFPatJetFlavourAssociation = akSoftDropZ05B151PFbTagger.PatJetFlavourAssociation
akSoftDropZ05B151PFPatJetFlavourId = cms.Sequence(akSoftDropZ05B151PFPatJetPartons*akSoftDropZ05B151PFPatJetFlavourAssociation)

akSoftDropZ05B151PFJetBtaggingIP = cms.Sequence(
    akSoftDropZ05B151PFImpactParameterTagInfos *
    akSoftDropZ05B151PFTrackCountingHighEffBJetTags +
    akSoftDropZ05B151PFTrackCountingHighPurBJetTags +
    akSoftDropZ05B151PFJetProbabilityBJetTags +
    akSoftDropZ05B151PFJetBProbabilityBJetTags
    )

akSoftDropZ05B151PFJetBtaggingSV = cms.Sequence(
    akSoftDropZ05B151PFImpactParameterTagInfos *
    akSoftDropZ05B151PFSecondaryVertexTagInfos *
    akSoftDropZ05B151PFSimpleSecondaryVertexHighEffBJetTags +
    akSoftDropZ05B151PFSimpleSecondaryVertexHighPurBJetTags +
    akSoftDropZ05B151PFCombinedSecondaryVertexBJetTags +
    akSoftDropZ05B151PFCombinedSecondaryVertexV2BJetTags
    )

akSoftDropZ05B151PFJetBtaggingNegSV = cms.Sequence(
    akSoftDropZ05B151PFImpactParameterTagInfos *
    akSoftDropZ05B151PFSecondaryVertexNegativeTagInfos *
    akSoftDropZ05B151PFNegativeSimpleSecondaryVertexHighEffBJetTags +
    akSoftDropZ05B151PFNegativeSimpleSecondaryVertexHighPurBJetTags +
    akSoftDropZ05B151PFNegativeCombinedSecondaryVertexBJetTags +
    akSoftDropZ05B151PFPositiveCombinedSecondaryVertexBJetTags +
    akSoftDropZ05B151PFNegativeCombinedSecondaryVertexV2BJetTags +
    akSoftDropZ05B151PFPositiveCombinedSecondaryVertexV2BJetTags
    )

akSoftDropZ05B151PFJetBtaggingMu = cms.Sequence(
    akSoftDropZ05B151PFSoftPFMuonsTagInfos *
    akSoftDropZ05B151PFSoftPFMuonBJetTags +
    akSoftDropZ05B151PFSoftPFMuonByIP3dBJetTags +
    akSoftDropZ05B151PFSoftPFMuonByPtBJetTags +
    akSoftDropZ05B151PFNegativeSoftPFMuonByPtBJetTags +
    akSoftDropZ05B151PFPositiveSoftPFMuonByPtBJetTags
    )

akSoftDropZ05B151PFJetBtagging = cms.Sequence(
    akSoftDropZ05B151PFJetBtaggingIP
    * akSoftDropZ05B151PFJetBtaggingSV
    # * akSoftDropZ05B151PFJetBtaggingNegSV
    # * akSoftDropZ05B151PFJetBtaggingMu
    )

akSoftDropZ05B151PFpatJetsWithBtagging = patJets.clone(
    jetSource = cms.InputTag("akSoftDropZ05B151PFJets"),
    genJetMatch            = cms.InputTag("akSoftDropZ05B151PFmatch"),
    genPartonMatch         = cms.InputTag("akSoftDropZ05B151PFparton"),
    jetCorrFactorsSource   = cms.VInputTag(cms.InputTag("akSoftDropZ05B151PFcorr")),
    JetPartonMapSource     = cms.InputTag("akSoftDropZ05B151PFPatJetFlavourAssociation"),
    JetFlavourInfoSource   = cms.InputTag("akSoftDropZ05B151PFPatJetFlavourAssociation"),
    trackAssociationSource = cms.InputTag("akSoftDropZ05B151PFJetTracksAssociatorAtVertex"),
    useLegacyJetMCFlavour  = False,
    discriminatorSources   = cms.VInputTag(
        cms.InputTag("akSoftDropZ05B151PFSimpleSecondaryVertexHighEffBJetTags"),
        cms.InputTag("akSoftDropZ05B151PFSimpleSecondaryVertexHighPurBJetTags"),
        cms.InputTag("akSoftDropZ05B151PFCombinedSecondaryVertexBJetTags"),
        cms.InputTag("akSoftDropZ05B151PFCombinedSecondaryVertexV2BJetTags"),
        cms.InputTag("akSoftDropZ05B151PFJetBProbabilityBJetTags"),
        cms.InputTag("akSoftDropZ05B151PFJetProbabilityBJetTags"),
        # cms.InputTag("akSoftDropZ05B151PFSoftPFMuonByPtBJetTags"),
        # cms.InputTag("akSoftDropZ05B151PFSoftPFMuonByIP3dBJetTags"),
        cms.InputTag("akSoftDropZ05B151PFTrackCountingHighEffBJetTags"),
        cms.InputTag("akSoftDropZ05B151PFTrackCountingHighPurBJetTags"),
        ),
    tagInfoSources = cms.VInputTag(cms.InputTag("akSoftDropZ05B151PFImpactParameterTagInfos"),cms.InputTag("akSoftDropZ05B151PFSecondaryVertexTagInfos")),
    jetIDMap = cms.InputTag("akSoftDropZ05B151PFJetID"),
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

akSoftDropZ05B151PFNjettiness = Njettiness.clone(
    src = cms.InputTag("akSoftDropZ05B151PFJets"),
    R0  = cms.double(0.1)
    )

akSoftDropZ05B151PFpatJetsWithBtagging.userData.userFloats.src += [
    'akSoftDropZ05B151PFNjettiness:tau1',
    'akSoftDropZ05B151PFNjettiness:tau2',
    'akSoftDropZ05B151PFNjettiness:tau3']

akSoftDropZ05B151PFJetAnalyzer = inclusiveJetAnalyzer.clone(
    jetTag = cms.InputTag("akSoftDropZ05B151PFpatJetsWithBtagging"),
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
    bTagJetName = cms.untracked.string("akSoftDropZ05B151PF"),
    jetName = cms.untracked.string("akSoftDropZ05B151PF"),
    genPtMin = cms.untracked.double(5),
    doTower = cms.untracked.bool(True),
    doSubJets = cms.untracked.bool(True),
    doGenSubJets = cms.untracked.bool(False),
    subjetGenTag = cms.untracked.InputTag("akSoftDropZ05B151GenJets"),
    doGenTaus = cms.untracked.bool(False),
    genTau1 = cms.InputTag("akSoftDropZ05B151HiGenNjettiness","tau1"),
    genTau2 = cms.InputTag("akSoftDropZ05B151HiGenNjettiness","tau2"),
    genTau3 = cms.InputTag("akSoftDropZ05B151HiGenNjettiness","tau3"),
    doGenSym = cms.untracked.bool(False),
    genSym = cms.InputTag("akSoftDropZ05B151GenJets","sym"),
    genDroppedBranches = cms.InputTag("akSoftDropZ05B151GenJets","droppedBranches")
    )

akSoftDropZ05B151PFJetSequence_mc = cms.Sequence(
    # akSoftDropZ05B151PFclean
    # *
    akSoftDropZ05B151PFmatch
    # *
    # akSoftDropZ05B151PFmatchGroomed
    *
    akSoftDropZ05B151PFparton
    *
    akSoftDropZ05B151PFcorr
    # *
    # akSoftDropZ05B151PFJetID
    *
     akSoftDropZ05B151PFPatJetFlavourId 
    *
    akSoftDropZ05B151PFJetTracksAssociatorAtVertex
    *
    akSoftDropZ05B151PFJetBtagging
    *
    # No constituents for calo jets in pp. Must be removed for pp calo jets but
    # I'm not sure how to do this transparently (Marta)
    akSoftDropZ05B151PFNjettiness
    *
    akSoftDropZ05B151PFpatJetsWithBtagging
    *
    akSoftDropZ05B151PFJetAnalyzer
    )

akSoftDropZ05B151PFJetSequence_data = cms.Sequence(
    akSoftDropZ05B151PFcorr
    *
    # akSoftDropZ05B151PFJetID
    # *
    akSoftDropZ05B151PFJetTracksAssociatorAtVertex
    *
    akSoftDropZ05B151PFJetBtagging
    *
    akSoftDropZ05B151PFNjettiness
    *
    akSoftDropZ05B151PFpatJetsWithBtagging
    *
    akSoftDropZ05B151PFJetAnalyzer
    )

akSoftDropZ05B151PFJetSequence_mb = cms.Sequence(
    akSoftDropZ05B151PFJetSequence_mc)
akSoftDropZ05B151PFJetSequence_jec = cms.Sequence(
    akSoftDropZ05B151PFJetSequence_mc)

akSoftDropZ05B151PFJetSequence = cms.Sequence(
    akSoftDropZ05B151PFJetSequence_mb)
akSoftDropZ05B151PFpatJetsWithBtagging.userData.userFloats.src += ['akSoftDropZ05B151PFJets:sym']
akSoftDropZ05B151PFpatJetsWithBtagging.userData.userInts.src += ['akSoftDropZ05B151PFJets:droppedBranches']
