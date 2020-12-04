import FWCore.ParameterSet.Config as cms

from PhysicsTools.PatAlgos.mcMatchLayer0.jetMatch_cfi import patJetGenJetMatch, patJetPartonMatch
from PhysicsTools.PatAlgos.recoLayer0.jetCorrFactors_cfi import patJetCorrFactors
from PhysicsTools.PatAlgos.producersLayer1.jetProducer_cfi import patJets

from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *

from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akSoftDropZ05B154PFmatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDropZ05B154PFJets"),
    matched = cms.InputTag("ak4HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.4
    )

akSoftDropZ05B154PFmatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDropZ05B154HiSignalGenJets"),
    matched = cms.InputTag("ak4HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.4
    )

akSoftDropZ05B154PFparton = patJetPartonMatch.clone(
    src = cms.InputTag("akSoftDropZ05B154PFJets"),
    matched = cms.InputTag("hiSignalGenParticles"))

akSoftDropZ05B154PFcorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
    levels   = cms.vstring('L2Relative'),
    src = cms.InputTag("akSoftDropZ05B154PFJets"),
    payload = "AK4PF"
    )

akSoftDropZ05B154PFJetID = cms.EDProducer(
    'JetIDProducer',
    JetIDParams,
    src = cms.InputTag('akSoftDropZ05B154CaloJets'))

# akSoftDropZ05B154PFclean = heavyIonCleanedGenJets.clone(
#     src = cms.InputTag('ak4HiSignalGenJets'))

akSoftDropZ05B154PFbTagger = bTaggers(
    "akSoftDropZ05B154PF",
    0.4)

# create objects locally since they dont load properly otherwise
akSoftDropZ05B154PFPatJetPartons = akSoftDropZ05B154PFbTagger.PatJetPartons
akSoftDropZ05B154PFJetTracksAssociatorAtVertex = akSoftDropZ05B154PFbTagger.JetTracksAssociatorAtVertex
akSoftDropZ05B154PFJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akSoftDropZ05B154PFSimpleSecondaryVertexHighEffBJetTags = akSoftDropZ05B154PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akSoftDropZ05B154PFSimpleSecondaryVertexHighPurBJetTags = akSoftDropZ05B154PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akSoftDropZ05B154PFCombinedSecondaryVertexBJetTags = akSoftDropZ05B154PFbTagger.CombinedSecondaryVertexBJetTags
akSoftDropZ05B154PFCombinedSecondaryVertexV2BJetTags = akSoftDropZ05B154PFbTagger.CombinedSecondaryVertexV2BJetTags
akSoftDropZ05B154PFJetBProbabilityBJetTags = akSoftDropZ05B154PFbTagger.JetBProbabilityBJetTags
akSoftDropZ05B154PFSoftPFMuonByPtBJetTags = akSoftDropZ05B154PFbTagger.SoftPFMuonByPtBJetTags
akSoftDropZ05B154PFSoftPFMuonByIP3dBJetTags = akSoftDropZ05B154PFbTagger.SoftPFMuonByIP3dBJetTags
akSoftDropZ05B154PFTrackCountingHighEffBJetTags = akSoftDropZ05B154PFbTagger.TrackCountingHighEffBJetTags
akSoftDropZ05B154PFTrackCountingHighPurBJetTags = akSoftDropZ05B154PFbTagger.TrackCountingHighPurBJetTags

akSoftDropZ05B154PFImpactParameterTagInfos = akSoftDropZ05B154PFbTagger.ImpactParameterTagInfos
akSoftDropZ05B154PFImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akSoftDropZ05B154PFJetProbabilityBJetTags = akSoftDropZ05B154PFbTagger.JetProbabilityBJetTags

akSoftDropZ05B154PFSecondaryVertexTagInfos = akSoftDropZ05B154PFbTagger.SecondaryVertexTagInfos
akSoftDropZ05B154PFSimpleSecondaryVertexHighEffBJetTags = akSoftDropZ05B154PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akSoftDropZ05B154PFSimpleSecondaryVertexHighPurBJetTags = akSoftDropZ05B154PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akSoftDropZ05B154PFCombinedSecondaryVertexBJetTags = akSoftDropZ05B154PFbTagger.CombinedSecondaryVertexBJetTags
akSoftDropZ05B154PFCombinedSecondaryVertexV2BJetTags = akSoftDropZ05B154PFbTagger.CombinedSecondaryVertexV2BJetTags

akSoftDropZ05B154PFSecondaryVertexNegativeTagInfos = akSoftDropZ05B154PFbTagger.SecondaryVertexNegativeTagInfos
akSoftDropZ05B154PFNegativeSimpleSecondaryVertexHighEffBJetTags = akSoftDropZ05B154PFbTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akSoftDropZ05B154PFNegativeSimpleSecondaryVertexHighPurBJetTags = akSoftDropZ05B154PFbTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akSoftDropZ05B154PFNegativeCombinedSecondaryVertexBJetTags = akSoftDropZ05B154PFbTagger.NegativeCombinedSecondaryVertexBJetTags
akSoftDropZ05B154PFPositiveCombinedSecondaryVertexBJetTags = akSoftDropZ05B154PFbTagger.PositiveCombinedSecondaryVertexBJetTags
akSoftDropZ05B154PFNegativeCombinedSecondaryVertexV2BJetTags = akSoftDropZ05B154PFbTagger.NegativeCombinedSecondaryVertexV2BJetTags
akSoftDropZ05B154PFPositiveCombinedSecondaryVertexV2BJetTags = akSoftDropZ05B154PFbTagger.PositiveCombinedSecondaryVertexV2BJetTags

akSoftDropZ05B154PFSoftPFMuonsTagInfos = akSoftDropZ05B154PFbTagger.SoftPFMuonsTagInfos
akSoftDropZ05B154PFSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akSoftDropZ05B154PFSoftPFMuonBJetTags = akSoftDropZ05B154PFbTagger.SoftPFMuonBJetTags
akSoftDropZ05B154PFSoftPFMuonByIP3dBJetTags = akSoftDropZ05B154PFbTagger.SoftPFMuonByIP3dBJetTags
akSoftDropZ05B154PFSoftPFMuonByPtBJetTags = akSoftDropZ05B154PFbTagger.SoftPFMuonByPtBJetTags
akSoftDropZ05B154PFNegativeSoftPFMuonByPtBJetTags = akSoftDropZ05B154PFbTagger.NegativeSoftPFMuonByPtBJetTags
akSoftDropZ05B154PFPositiveSoftPFMuonByPtBJetTags = akSoftDropZ05B154PFbTagger.PositiveSoftPFMuonByPtBJetTags
akSoftDropZ05B154PFPatJetFlavourAssociation = akSoftDropZ05B154PFbTagger.PatJetFlavourAssociation
akSoftDropZ05B154PFPatJetFlavourId = cms.Sequence(akSoftDropZ05B154PFPatJetPartons*akSoftDropZ05B154PFPatJetFlavourAssociation)

akSoftDropZ05B154PFJetBtaggingIP = cms.Sequence(
    akSoftDropZ05B154PFImpactParameterTagInfos *
    akSoftDropZ05B154PFTrackCountingHighEffBJetTags +
    akSoftDropZ05B154PFTrackCountingHighPurBJetTags +
    akSoftDropZ05B154PFJetProbabilityBJetTags +
    akSoftDropZ05B154PFJetBProbabilityBJetTags
    )

akSoftDropZ05B154PFJetBtaggingSV = cms.Sequence(
    akSoftDropZ05B154PFImpactParameterTagInfos *
    akSoftDropZ05B154PFSecondaryVertexTagInfos *
    akSoftDropZ05B154PFSimpleSecondaryVertexHighEffBJetTags +
    akSoftDropZ05B154PFSimpleSecondaryVertexHighPurBJetTags +
    akSoftDropZ05B154PFCombinedSecondaryVertexBJetTags +
    akSoftDropZ05B154PFCombinedSecondaryVertexV2BJetTags
    )

akSoftDropZ05B154PFJetBtaggingNegSV = cms.Sequence(
    akSoftDropZ05B154PFImpactParameterTagInfos *
    akSoftDropZ05B154PFSecondaryVertexNegativeTagInfos *
    akSoftDropZ05B154PFNegativeSimpleSecondaryVertexHighEffBJetTags +
    akSoftDropZ05B154PFNegativeSimpleSecondaryVertexHighPurBJetTags +
    akSoftDropZ05B154PFNegativeCombinedSecondaryVertexBJetTags +
    akSoftDropZ05B154PFPositiveCombinedSecondaryVertexBJetTags +
    akSoftDropZ05B154PFNegativeCombinedSecondaryVertexV2BJetTags +
    akSoftDropZ05B154PFPositiveCombinedSecondaryVertexV2BJetTags
    )

akSoftDropZ05B154PFJetBtaggingMu = cms.Sequence(
    akSoftDropZ05B154PFSoftPFMuonsTagInfos *
    akSoftDropZ05B154PFSoftPFMuonBJetTags +
    akSoftDropZ05B154PFSoftPFMuonByIP3dBJetTags +
    akSoftDropZ05B154PFSoftPFMuonByPtBJetTags +
    akSoftDropZ05B154PFNegativeSoftPFMuonByPtBJetTags +
    akSoftDropZ05B154PFPositiveSoftPFMuonByPtBJetTags
    )

akSoftDropZ05B154PFJetBtagging = cms.Sequence(
    akSoftDropZ05B154PFJetBtaggingIP
    * akSoftDropZ05B154PFJetBtaggingSV
    # * akSoftDropZ05B154PFJetBtaggingNegSV
    # * akSoftDropZ05B154PFJetBtaggingMu
    )

akSoftDropZ05B154PFpatJetsWithBtagging = patJets.clone(
    jetSource = cms.InputTag("akSoftDropZ05B154PFJets"),
    genJetMatch            = cms.InputTag("akSoftDropZ05B154PFmatch"),
    genPartonMatch         = cms.InputTag("akSoftDropZ05B154PFparton"),
    jetCorrFactorsSource   = cms.VInputTag(cms.InputTag("akSoftDropZ05B154PFcorr")),
    JetPartonMapSource     = cms.InputTag("akSoftDropZ05B154PFPatJetFlavourAssociation"),
    JetFlavourInfoSource   = cms.InputTag("akSoftDropZ05B154PFPatJetFlavourAssociation"),
    trackAssociationSource = cms.InputTag("akSoftDropZ05B154PFJetTracksAssociatorAtVertex"),
    useLegacyJetMCFlavour  = False,
    discriminatorSources   = cms.VInputTag(
        cms.InputTag("akSoftDropZ05B154PFSimpleSecondaryVertexHighEffBJetTags"),
        cms.InputTag("akSoftDropZ05B154PFSimpleSecondaryVertexHighPurBJetTags"),
        cms.InputTag("akSoftDropZ05B154PFCombinedSecondaryVertexBJetTags"),
        cms.InputTag("akSoftDropZ05B154PFCombinedSecondaryVertexV2BJetTags"),
        cms.InputTag("akSoftDropZ05B154PFJetBProbabilityBJetTags"),
        cms.InputTag("akSoftDropZ05B154PFJetProbabilityBJetTags"),
        # cms.InputTag("akSoftDropZ05B154PFSoftPFMuonByPtBJetTags"),
        # cms.InputTag("akSoftDropZ05B154PFSoftPFMuonByIP3dBJetTags"),
        cms.InputTag("akSoftDropZ05B154PFTrackCountingHighEffBJetTags"),
        cms.InputTag("akSoftDropZ05B154PFTrackCountingHighPurBJetTags"),
        ),
    tagInfoSources = cms.VInputTag(cms.InputTag("akSoftDropZ05B154PFImpactParameterTagInfos"),cms.InputTag("akSoftDropZ05B154PFSecondaryVertexTagInfos")),
    jetIDMap = cms.InputTag("akSoftDropZ05B154PFJetID"),
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

akSoftDropZ05B154PFNjettiness = Njettiness.clone(
    src = cms.InputTag("akSoftDropZ05B154PFJets"),
    R0  = cms.double(0.4)
    )

akSoftDropZ05B154PFpatJetsWithBtagging.userData.userFloats.src += [
    'akSoftDropZ05B154PFNjettiness:tau1',
    'akSoftDropZ05B154PFNjettiness:tau2',
    'akSoftDropZ05B154PFNjettiness:tau3']

akSoftDropZ05B154PFJetAnalyzer = inclusiveJetAnalyzer.clone(
    jetTag = cms.InputTag("akSoftDropZ05B154PFpatJetsWithBtagging"),
    genjetTag = 'ak4HiSignalGenJets',
    rParam = 0.4,
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
    bTagJetName = cms.untracked.string("akSoftDropZ05B154PF"),
    jetName = cms.untracked.string("akSoftDropZ05B154PF"),
    genPtMin = cms.untracked.double(5),
    doTower = cms.untracked.bool(True),
    doSubJets = cms.untracked.bool(True),
    doGenSubJets = cms.untracked.bool(False),
    subjetGenTag = cms.untracked.InputTag("akSoftDropZ05B154GenJets"),
    doGenTaus = cms.untracked.bool(False),
    genTau1 = cms.InputTag("akSoftDropZ05B154HiGenNjettiness","tau1"),
    genTau2 = cms.InputTag("akSoftDropZ05B154HiGenNjettiness","tau2"),
    genTau3 = cms.InputTag("akSoftDropZ05B154HiGenNjettiness","tau3"),
    doGenSym = cms.untracked.bool(False),
    genSym = cms.InputTag("akSoftDropZ05B154GenJets","sym"),
    genDroppedBranches = cms.InputTag("akSoftDropZ05B154GenJets","droppedBranches")
    )

akSoftDropZ05B154PFJetSequence_mc = cms.Sequence(
    # akSoftDropZ05B154PFclean
    # *
    akSoftDropZ05B154PFmatch
    # *
    # akSoftDropZ05B154PFmatchGroomed
    *
    akSoftDropZ05B154PFparton
    *
    akSoftDropZ05B154PFcorr
    # *
    # akSoftDropZ05B154PFJetID
    *
     akSoftDropZ05B154PFPatJetFlavourId 
    *
    akSoftDropZ05B154PFJetTracksAssociatorAtVertex
    *
    akSoftDropZ05B154PFJetBtagging
    *
    # No constituents for calo jets in pp. Must be removed for pp calo jets but
    # I'm not sure how to do this transparently (Marta)
    akSoftDropZ05B154PFNjettiness
    *
    akSoftDropZ05B154PFpatJetsWithBtagging
    *
    akSoftDropZ05B154PFJetAnalyzer
    )

akSoftDropZ05B154PFJetSequence_data = cms.Sequence(
    akSoftDropZ05B154PFcorr
    *
    # akSoftDropZ05B154PFJetID
    # *
    akSoftDropZ05B154PFJetTracksAssociatorAtVertex
    *
    akSoftDropZ05B154PFJetBtagging
    *
    akSoftDropZ05B154PFNjettiness
    *
    akSoftDropZ05B154PFpatJetsWithBtagging
    *
    akSoftDropZ05B154PFJetAnalyzer
    )

akSoftDropZ05B154PFJetSequence_mb = cms.Sequence(
    akSoftDropZ05B154PFJetSequence_mc)
akSoftDropZ05B154PFJetSequence_jec = cms.Sequence(
    akSoftDropZ05B154PFJetSequence_mc)

akSoftDropZ05B154PFJetSequence = cms.Sequence(
    akSoftDropZ05B154PFJetSequence_jec)
akSoftDropZ05B154PFJetAnalyzer.genPtMin = cms.untracked.double(1)
akSoftDropZ05B154PFJetAnalyzer.jetPtMin = cms.double(1)
akSoftDropZ05B154PFpatJetsWithBtagging.userData.userFloats.src += ['akSoftDropZ05B154PFJets:sym']
akSoftDropZ05B154PFpatJetsWithBtagging.userData.userInts.src += ['akSoftDropZ05B154PFJets:droppedBranches']
