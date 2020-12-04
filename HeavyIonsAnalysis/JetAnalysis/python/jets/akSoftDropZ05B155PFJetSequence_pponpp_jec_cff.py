import FWCore.ParameterSet.Config as cms

from PhysicsTools.PatAlgos.mcMatchLayer0.jetMatch_cfi import patJetGenJetMatch, patJetPartonMatch
from PhysicsTools.PatAlgos.recoLayer0.jetCorrFactors_cfi import patJetCorrFactors
from PhysicsTools.PatAlgos.producersLayer1.jetProducer_cfi import patJets

from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *

from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akSoftDropZ05B155PFmatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDropZ05B155PFJets"),
    matched = cms.InputTag("ak5GenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.5
    )

akSoftDropZ05B155PFmatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDropZ05B155GenJets"),
    matched = cms.InputTag("ak5GenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.5
    )

akSoftDropZ05B155PFparton = patJetPartonMatch.clone(
    src = cms.InputTag("akSoftDropZ05B155PFJets"),
    matched = cms.InputTag("genParticles"))

akSoftDropZ05B155PFcorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
    levels   = cms.vstring('L2Relative'),
    src = cms.InputTag("akSoftDropZ05B155PFJets"),
    payload = "AK5PF"
    )

akSoftDropZ05B155PFJetID = cms.EDProducer(
    'JetIDProducer',
    JetIDParams,
    src = cms.InputTag('akSoftDropZ05B155CaloJets'))

# akSoftDropZ05B155PFclean = heavyIonCleanedGenJets.clone(
#     src = cms.InputTag('ak5GenJets'))

akSoftDropZ05B155PFbTagger = bTaggers(
    "akSoftDropZ05B155PF",
    0.5)

# create objects locally since they dont load properly otherwise
akSoftDropZ05B155PFPatJetPartons = akSoftDropZ05B155PFbTagger.PatJetPartons
akSoftDropZ05B155PFJetTracksAssociatorAtVertex = akSoftDropZ05B155PFbTagger.JetTracksAssociatorAtVertex
akSoftDropZ05B155PFJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akSoftDropZ05B155PFSimpleSecondaryVertexHighEffBJetTags = akSoftDropZ05B155PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akSoftDropZ05B155PFSimpleSecondaryVertexHighPurBJetTags = akSoftDropZ05B155PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akSoftDropZ05B155PFCombinedSecondaryVertexBJetTags = akSoftDropZ05B155PFbTagger.CombinedSecondaryVertexBJetTags
akSoftDropZ05B155PFCombinedSecondaryVertexV2BJetTags = akSoftDropZ05B155PFbTagger.CombinedSecondaryVertexV2BJetTags
akSoftDropZ05B155PFJetBProbabilityBJetTags = akSoftDropZ05B155PFbTagger.JetBProbabilityBJetTags
akSoftDropZ05B155PFSoftPFMuonByPtBJetTags = akSoftDropZ05B155PFbTagger.SoftPFMuonByPtBJetTags
akSoftDropZ05B155PFSoftPFMuonByIP3dBJetTags = akSoftDropZ05B155PFbTagger.SoftPFMuonByIP3dBJetTags
akSoftDropZ05B155PFTrackCountingHighEffBJetTags = akSoftDropZ05B155PFbTagger.TrackCountingHighEffBJetTags
akSoftDropZ05B155PFTrackCountingHighPurBJetTags = akSoftDropZ05B155PFbTagger.TrackCountingHighPurBJetTags

akSoftDropZ05B155PFImpactParameterTagInfos = akSoftDropZ05B155PFbTagger.ImpactParameterTagInfos
akSoftDropZ05B155PFImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akSoftDropZ05B155PFJetProbabilityBJetTags = akSoftDropZ05B155PFbTagger.JetProbabilityBJetTags

akSoftDropZ05B155PFSecondaryVertexTagInfos = akSoftDropZ05B155PFbTagger.SecondaryVertexTagInfos
akSoftDropZ05B155PFSimpleSecondaryVertexHighEffBJetTags = akSoftDropZ05B155PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akSoftDropZ05B155PFSimpleSecondaryVertexHighPurBJetTags = akSoftDropZ05B155PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akSoftDropZ05B155PFCombinedSecondaryVertexBJetTags = akSoftDropZ05B155PFbTagger.CombinedSecondaryVertexBJetTags
akSoftDropZ05B155PFCombinedSecondaryVertexV2BJetTags = akSoftDropZ05B155PFbTagger.CombinedSecondaryVertexV2BJetTags

akSoftDropZ05B155PFSecondaryVertexNegativeTagInfos = akSoftDropZ05B155PFbTagger.SecondaryVertexNegativeTagInfos
akSoftDropZ05B155PFNegativeSimpleSecondaryVertexHighEffBJetTags = akSoftDropZ05B155PFbTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akSoftDropZ05B155PFNegativeSimpleSecondaryVertexHighPurBJetTags = akSoftDropZ05B155PFbTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akSoftDropZ05B155PFNegativeCombinedSecondaryVertexBJetTags = akSoftDropZ05B155PFbTagger.NegativeCombinedSecondaryVertexBJetTags
akSoftDropZ05B155PFPositiveCombinedSecondaryVertexBJetTags = akSoftDropZ05B155PFbTagger.PositiveCombinedSecondaryVertexBJetTags
akSoftDropZ05B155PFNegativeCombinedSecondaryVertexV2BJetTags = akSoftDropZ05B155PFbTagger.NegativeCombinedSecondaryVertexV2BJetTags
akSoftDropZ05B155PFPositiveCombinedSecondaryVertexV2BJetTags = akSoftDropZ05B155PFbTagger.PositiveCombinedSecondaryVertexV2BJetTags

akSoftDropZ05B155PFSoftPFMuonsTagInfos = akSoftDropZ05B155PFbTagger.SoftPFMuonsTagInfos
akSoftDropZ05B155PFSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akSoftDropZ05B155PFSoftPFMuonBJetTags = akSoftDropZ05B155PFbTagger.SoftPFMuonBJetTags
akSoftDropZ05B155PFSoftPFMuonByIP3dBJetTags = akSoftDropZ05B155PFbTagger.SoftPFMuonByIP3dBJetTags
akSoftDropZ05B155PFSoftPFMuonByPtBJetTags = akSoftDropZ05B155PFbTagger.SoftPFMuonByPtBJetTags
akSoftDropZ05B155PFNegativeSoftPFMuonByPtBJetTags = akSoftDropZ05B155PFbTagger.NegativeSoftPFMuonByPtBJetTags
akSoftDropZ05B155PFPositiveSoftPFMuonByPtBJetTags = akSoftDropZ05B155PFbTagger.PositiveSoftPFMuonByPtBJetTags
akSoftDropZ05B155PFPatJetFlavourAssociation = akSoftDropZ05B155PFbTagger.PatJetFlavourAssociation
akSoftDropZ05B155PFPatJetFlavourId = cms.Sequence(akSoftDropZ05B155PFPatJetPartons*akSoftDropZ05B155PFPatJetFlavourAssociation)

akSoftDropZ05B155PFJetBtaggingIP = cms.Sequence(
    akSoftDropZ05B155PFImpactParameterTagInfos *
    akSoftDropZ05B155PFTrackCountingHighEffBJetTags +
    akSoftDropZ05B155PFTrackCountingHighPurBJetTags +
    akSoftDropZ05B155PFJetProbabilityBJetTags +
    akSoftDropZ05B155PFJetBProbabilityBJetTags
    )

akSoftDropZ05B155PFJetBtaggingSV = cms.Sequence(
    akSoftDropZ05B155PFImpactParameterTagInfos *
    akSoftDropZ05B155PFSecondaryVertexTagInfos *
    akSoftDropZ05B155PFSimpleSecondaryVertexHighEffBJetTags +
    akSoftDropZ05B155PFSimpleSecondaryVertexHighPurBJetTags +
    akSoftDropZ05B155PFCombinedSecondaryVertexBJetTags +
    akSoftDropZ05B155PFCombinedSecondaryVertexV2BJetTags
    )

akSoftDropZ05B155PFJetBtaggingNegSV = cms.Sequence(
    akSoftDropZ05B155PFImpactParameterTagInfos *
    akSoftDropZ05B155PFSecondaryVertexNegativeTagInfos *
    akSoftDropZ05B155PFNegativeSimpleSecondaryVertexHighEffBJetTags +
    akSoftDropZ05B155PFNegativeSimpleSecondaryVertexHighPurBJetTags +
    akSoftDropZ05B155PFNegativeCombinedSecondaryVertexBJetTags +
    akSoftDropZ05B155PFPositiveCombinedSecondaryVertexBJetTags +
    akSoftDropZ05B155PFNegativeCombinedSecondaryVertexV2BJetTags +
    akSoftDropZ05B155PFPositiveCombinedSecondaryVertexV2BJetTags
    )

akSoftDropZ05B155PFJetBtaggingMu = cms.Sequence(
    akSoftDropZ05B155PFSoftPFMuonsTagInfos *
    akSoftDropZ05B155PFSoftPFMuonBJetTags +
    akSoftDropZ05B155PFSoftPFMuonByIP3dBJetTags +
    akSoftDropZ05B155PFSoftPFMuonByPtBJetTags +
    akSoftDropZ05B155PFNegativeSoftPFMuonByPtBJetTags +
    akSoftDropZ05B155PFPositiveSoftPFMuonByPtBJetTags
    )

akSoftDropZ05B155PFJetBtagging = cms.Sequence(
    akSoftDropZ05B155PFJetBtaggingIP
    * akSoftDropZ05B155PFJetBtaggingSV
    # * akSoftDropZ05B155PFJetBtaggingNegSV
    # * akSoftDropZ05B155PFJetBtaggingMu
    )

akSoftDropZ05B155PFpatJetsWithBtagging = patJets.clone(
    jetSource = cms.InputTag("akSoftDropZ05B155PFJets"),
    genJetMatch            = cms.InputTag("akSoftDropZ05B155PFmatch"),
    genPartonMatch         = cms.InputTag("akSoftDropZ05B155PFparton"),
    jetCorrFactorsSource   = cms.VInputTag(cms.InputTag("akSoftDropZ05B155PFcorr")),
    JetPartonMapSource     = cms.InputTag("akSoftDropZ05B155PFPatJetFlavourAssociation"),
    JetFlavourInfoSource   = cms.InputTag("akSoftDropZ05B155PFPatJetFlavourAssociation"),
    trackAssociationSource = cms.InputTag("akSoftDropZ05B155PFJetTracksAssociatorAtVertex"),
    useLegacyJetMCFlavour  = False,
    discriminatorSources   = cms.VInputTag(
        cms.InputTag("akSoftDropZ05B155PFSimpleSecondaryVertexHighEffBJetTags"),
        cms.InputTag("akSoftDropZ05B155PFSimpleSecondaryVertexHighPurBJetTags"),
        cms.InputTag("akSoftDropZ05B155PFCombinedSecondaryVertexBJetTags"),
        cms.InputTag("akSoftDropZ05B155PFCombinedSecondaryVertexV2BJetTags"),
        cms.InputTag("akSoftDropZ05B155PFJetBProbabilityBJetTags"),
        cms.InputTag("akSoftDropZ05B155PFJetProbabilityBJetTags"),
        # cms.InputTag("akSoftDropZ05B155PFSoftPFMuonByPtBJetTags"),
        # cms.InputTag("akSoftDropZ05B155PFSoftPFMuonByIP3dBJetTags"),
        cms.InputTag("akSoftDropZ05B155PFTrackCountingHighEffBJetTags"),
        cms.InputTag("akSoftDropZ05B155PFTrackCountingHighPurBJetTags"),
        ),
    tagInfoSources = cms.VInputTag(cms.InputTag("akSoftDropZ05B155PFImpactParameterTagInfos"),cms.InputTag("akSoftDropZ05B155PFSecondaryVertexTagInfos")),
    jetIDMap = cms.InputTag("akSoftDropZ05B155PFJetID"),
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

akSoftDropZ05B155PFNjettiness = Njettiness.clone(
    src = cms.InputTag("akSoftDropZ05B155PFJets"),
    R0  = cms.double(0.5)
    )

akSoftDropZ05B155PFpatJetsWithBtagging.userData.userFloats.src += [
    'akSoftDropZ05B155PFNjettiness:tau1',
    'akSoftDropZ05B155PFNjettiness:tau2',
    'akSoftDropZ05B155PFNjettiness:tau3']

akSoftDropZ05B155PFJetAnalyzer = inclusiveJetAnalyzer.clone(
    jetTag = cms.InputTag("akSoftDropZ05B155PFpatJetsWithBtagging"),
    genjetTag = 'ak5GenJets',
    rParam = 0.5,
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
    bTagJetName = cms.untracked.string("akSoftDropZ05B155PF"),
    jetName = cms.untracked.string("akSoftDropZ05B155PF"),
    genPtMin = cms.untracked.double(5),
    doTower = cms.untracked.bool(False),
    doSubJets = cms.untracked.bool(True),
    doGenSubJets = cms.untracked.bool(False),
    subjetGenTag = cms.untracked.InputTag("akSoftDropZ05B155GenJets"),
    doGenTaus = cms.untracked.bool(False),
    genTau1 = cms.InputTag("akSoftDropZ05B155GenNjettiness","tau1"),
    genTau2 = cms.InputTag("akSoftDropZ05B155GenNjettiness","tau2"),
    genTau3 = cms.InputTag("akSoftDropZ05B155GenNjettiness","tau3"),
    doGenSym = cms.untracked.bool(False),
    genSym = cms.InputTag("akSoftDropZ05B155GenJets","sym"),
    genDroppedBranches = cms.InputTag("akSoftDropZ05B155GenJets","droppedBranches")
    )

akSoftDropZ05B155PFJetSequence_mc = cms.Sequence(
    # akSoftDropZ05B155PFclean
    # *
    akSoftDropZ05B155PFmatch
    # *
    # akSoftDropZ05B155PFmatchGroomed
    *
    akSoftDropZ05B155PFparton
    *
    akSoftDropZ05B155PFcorr
    # *
    # akSoftDropZ05B155PFJetID
    *
     akSoftDropZ05B155PFPatJetFlavourId 
    *
    akSoftDropZ05B155PFJetTracksAssociatorAtVertex
    *
    akSoftDropZ05B155PFJetBtagging
    *
    # No constituents for calo jets in pp. Must be removed for pp calo jets but
    # I'm not sure how to do this transparently (Marta)
    akSoftDropZ05B155PFNjettiness
    *
    akSoftDropZ05B155PFpatJetsWithBtagging
    *
    akSoftDropZ05B155PFJetAnalyzer
    )

akSoftDropZ05B155PFJetSequence_data = cms.Sequence(
    akSoftDropZ05B155PFcorr
    *
    # akSoftDropZ05B155PFJetID
    # *
    akSoftDropZ05B155PFJetTracksAssociatorAtVertex
    *
    akSoftDropZ05B155PFJetBtagging
    *
    akSoftDropZ05B155PFNjettiness
    *
    akSoftDropZ05B155PFpatJetsWithBtagging
    *
    akSoftDropZ05B155PFJetAnalyzer
    )

akSoftDropZ05B155PFJetSequence_mb = cms.Sequence(
    akSoftDropZ05B155PFJetSequence_mc)
akSoftDropZ05B155PFJetSequence_jec = cms.Sequence(
    akSoftDropZ05B155PFJetSequence_mc)

akSoftDropZ05B155PFJetSequence = cms.Sequence(
    akSoftDropZ05B155PFJetSequence_jec)
akSoftDropZ05B155PFJetAnalyzer.genPtMin = cms.untracked.double(1)
akSoftDropZ05B155PFJetAnalyzer.jetPtMin = cms.double(1)
akSoftDropZ05B155PFpatJetsWithBtagging.userData.userFloats.src += ['akSoftDropZ05B155PFJets:sym']
akSoftDropZ05B155PFpatJetsWithBtagging.userData.userInts.src += ['akSoftDropZ05B155PFJets:droppedBranches']
