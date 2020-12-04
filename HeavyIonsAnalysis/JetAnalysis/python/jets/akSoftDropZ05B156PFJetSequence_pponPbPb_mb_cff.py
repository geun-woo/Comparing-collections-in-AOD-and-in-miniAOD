import FWCore.ParameterSet.Config as cms

from PhysicsTools.PatAlgos.mcMatchLayer0.jetMatch_cfi import patJetGenJetMatch, patJetPartonMatch
from PhysicsTools.PatAlgos.recoLayer0.jetCorrFactors_cfi import patJetCorrFactors
from PhysicsTools.PatAlgos.producersLayer1.jetProducer_cfi import patJets

from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *

from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akSoftDropZ05B156PFmatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDropZ05B156PFJets"),
    matched = cms.InputTag("ak6HiCleanedGenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.6
    )

akSoftDropZ05B156PFmatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDropZ05B156HiGenJets"),
    matched = cms.InputTag("ak6HiCleanedGenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.6
    )

akSoftDropZ05B156PFparton = patJetPartonMatch.clone(
    src = cms.InputTag("akSoftDropZ05B156PFJets"),
    matched = cms.InputTag("cleanedPartons"))

akSoftDropZ05B156PFcorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
    levels   = cms.vstring('L2Relative'),
    src = cms.InputTag("akSoftDropZ05B156PFJets"),
    payload = "AK6PF"
    )

akSoftDropZ05B156PFJetID = cms.EDProducer(
    'JetIDProducer',
    JetIDParams,
    src = cms.InputTag('akSoftDropZ05B156CaloJets'))

# akSoftDropZ05B156PFclean = heavyIonCleanedGenJets.clone(
#     src = cms.InputTag('ak6HiCleanedGenJets'))

akSoftDropZ05B156PFbTagger = bTaggers(
    "akSoftDropZ05B156PF",
    0.6)

# create objects locally since they dont load properly otherwise
akSoftDropZ05B156PFPatJetPartons = akSoftDropZ05B156PFbTagger.PatJetPartons
akSoftDropZ05B156PFJetTracksAssociatorAtVertex = akSoftDropZ05B156PFbTagger.JetTracksAssociatorAtVertex
akSoftDropZ05B156PFJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akSoftDropZ05B156PFSimpleSecondaryVertexHighEffBJetTags = akSoftDropZ05B156PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akSoftDropZ05B156PFSimpleSecondaryVertexHighPurBJetTags = akSoftDropZ05B156PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akSoftDropZ05B156PFCombinedSecondaryVertexBJetTags = akSoftDropZ05B156PFbTagger.CombinedSecondaryVertexBJetTags
akSoftDropZ05B156PFCombinedSecondaryVertexV2BJetTags = akSoftDropZ05B156PFbTagger.CombinedSecondaryVertexV2BJetTags
akSoftDropZ05B156PFJetBProbabilityBJetTags = akSoftDropZ05B156PFbTagger.JetBProbabilityBJetTags
akSoftDropZ05B156PFSoftPFMuonByPtBJetTags = akSoftDropZ05B156PFbTagger.SoftPFMuonByPtBJetTags
akSoftDropZ05B156PFSoftPFMuonByIP3dBJetTags = akSoftDropZ05B156PFbTagger.SoftPFMuonByIP3dBJetTags
akSoftDropZ05B156PFTrackCountingHighEffBJetTags = akSoftDropZ05B156PFbTagger.TrackCountingHighEffBJetTags
akSoftDropZ05B156PFTrackCountingHighPurBJetTags = akSoftDropZ05B156PFbTagger.TrackCountingHighPurBJetTags

akSoftDropZ05B156PFImpactParameterTagInfos = akSoftDropZ05B156PFbTagger.ImpactParameterTagInfos
akSoftDropZ05B156PFImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akSoftDropZ05B156PFJetProbabilityBJetTags = akSoftDropZ05B156PFbTagger.JetProbabilityBJetTags

akSoftDropZ05B156PFSecondaryVertexTagInfos = akSoftDropZ05B156PFbTagger.SecondaryVertexTagInfos
akSoftDropZ05B156PFSimpleSecondaryVertexHighEffBJetTags = akSoftDropZ05B156PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akSoftDropZ05B156PFSimpleSecondaryVertexHighPurBJetTags = akSoftDropZ05B156PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akSoftDropZ05B156PFCombinedSecondaryVertexBJetTags = akSoftDropZ05B156PFbTagger.CombinedSecondaryVertexBJetTags
akSoftDropZ05B156PFCombinedSecondaryVertexV2BJetTags = akSoftDropZ05B156PFbTagger.CombinedSecondaryVertexV2BJetTags

akSoftDropZ05B156PFSecondaryVertexNegativeTagInfos = akSoftDropZ05B156PFbTagger.SecondaryVertexNegativeTagInfos
akSoftDropZ05B156PFNegativeSimpleSecondaryVertexHighEffBJetTags = akSoftDropZ05B156PFbTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akSoftDropZ05B156PFNegativeSimpleSecondaryVertexHighPurBJetTags = akSoftDropZ05B156PFbTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akSoftDropZ05B156PFNegativeCombinedSecondaryVertexBJetTags = akSoftDropZ05B156PFbTagger.NegativeCombinedSecondaryVertexBJetTags
akSoftDropZ05B156PFPositiveCombinedSecondaryVertexBJetTags = akSoftDropZ05B156PFbTagger.PositiveCombinedSecondaryVertexBJetTags
akSoftDropZ05B156PFNegativeCombinedSecondaryVertexV2BJetTags = akSoftDropZ05B156PFbTagger.NegativeCombinedSecondaryVertexV2BJetTags
akSoftDropZ05B156PFPositiveCombinedSecondaryVertexV2BJetTags = akSoftDropZ05B156PFbTagger.PositiveCombinedSecondaryVertexV2BJetTags

akSoftDropZ05B156PFSoftPFMuonsTagInfos = akSoftDropZ05B156PFbTagger.SoftPFMuonsTagInfos
akSoftDropZ05B156PFSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akSoftDropZ05B156PFSoftPFMuonBJetTags = akSoftDropZ05B156PFbTagger.SoftPFMuonBJetTags
akSoftDropZ05B156PFSoftPFMuonByIP3dBJetTags = akSoftDropZ05B156PFbTagger.SoftPFMuonByIP3dBJetTags
akSoftDropZ05B156PFSoftPFMuonByPtBJetTags = akSoftDropZ05B156PFbTagger.SoftPFMuonByPtBJetTags
akSoftDropZ05B156PFNegativeSoftPFMuonByPtBJetTags = akSoftDropZ05B156PFbTagger.NegativeSoftPFMuonByPtBJetTags
akSoftDropZ05B156PFPositiveSoftPFMuonByPtBJetTags = akSoftDropZ05B156PFbTagger.PositiveSoftPFMuonByPtBJetTags
akSoftDropZ05B156PFPatJetFlavourAssociation = akSoftDropZ05B156PFbTagger.PatJetFlavourAssociation
akSoftDropZ05B156PFPatJetFlavourId = cms.Sequence(akSoftDropZ05B156PFPatJetPartons*akSoftDropZ05B156PFPatJetFlavourAssociation)

akSoftDropZ05B156PFJetBtaggingIP = cms.Sequence(
    akSoftDropZ05B156PFImpactParameterTagInfos *
    akSoftDropZ05B156PFTrackCountingHighEffBJetTags +
    akSoftDropZ05B156PFTrackCountingHighPurBJetTags +
    akSoftDropZ05B156PFJetProbabilityBJetTags +
    akSoftDropZ05B156PFJetBProbabilityBJetTags
    )

akSoftDropZ05B156PFJetBtaggingSV = cms.Sequence(
    akSoftDropZ05B156PFImpactParameterTagInfos *
    akSoftDropZ05B156PFSecondaryVertexTagInfos *
    akSoftDropZ05B156PFSimpleSecondaryVertexHighEffBJetTags +
    akSoftDropZ05B156PFSimpleSecondaryVertexHighPurBJetTags +
    akSoftDropZ05B156PFCombinedSecondaryVertexBJetTags +
    akSoftDropZ05B156PFCombinedSecondaryVertexV2BJetTags
    )

akSoftDropZ05B156PFJetBtaggingNegSV = cms.Sequence(
    akSoftDropZ05B156PFImpactParameterTagInfos *
    akSoftDropZ05B156PFSecondaryVertexNegativeTagInfos *
    akSoftDropZ05B156PFNegativeSimpleSecondaryVertexHighEffBJetTags +
    akSoftDropZ05B156PFNegativeSimpleSecondaryVertexHighPurBJetTags +
    akSoftDropZ05B156PFNegativeCombinedSecondaryVertexBJetTags +
    akSoftDropZ05B156PFPositiveCombinedSecondaryVertexBJetTags +
    akSoftDropZ05B156PFNegativeCombinedSecondaryVertexV2BJetTags +
    akSoftDropZ05B156PFPositiveCombinedSecondaryVertexV2BJetTags
    )

akSoftDropZ05B156PFJetBtaggingMu = cms.Sequence(
    akSoftDropZ05B156PFSoftPFMuonsTagInfos *
    akSoftDropZ05B156PFSoftPFMuonBJetTags +
    akSoftDropZ05B156PFSoftPFMuonByIP3dBJetTags +
    akSoftDropZ05B156PFSoftPFMuonByPtBJetTags +
    akSoftDropZ05B156PFNegativeSoftPFMuonByPtBJetTags +
    akSoftDropZ05B156PFPositiveSoftPFMuonByPtBJetTags
    )

akSoftDropZ05B156PFJetBtagging = cms.Sequence(
    akSoftDropZ05B156PFJetBtaggingIP
    * akSoftDropZ05B156PFJetBtaggingSV
    # * akSoftDropZ05B156PFJetBtaggingNegSV
    # * akSoftDropZ05B156PFJetBtaggingMu
    )

akSoftDropZ05B156PFpatJetsWithBtagging = patJets.clone(
    jetSource = cms.InputTag("akSoftDropZ05B156PFJets"),
    genJetMatch            = cms.InputTag("akSoftDropZ05B156PFmatch"),
    genPartonMatch         = cms.InputTag("akSoftDropZ05B156PFparton"),
    jetCorrFactorsSource   = cms.VInputTag(cms.InputTag("akSoftDropZ05B156PFcorr")),
    JetPartonMapSource     = cms.InputTag("akSoftDropZ05B156PFPatJetFlavourAssociation"),
    JetFlavourInfoSource   = cms.InputTag("akSoftDropZ05B156PFPatJetFlavourAssociation"),
    trackAssociationSource = cms.InputTag("akSoftDropZ05B156PFJetTracksAssociatorAtVertex"),
    useLegacyJetMCFlavour  = False,
    discriminatorSources   = cms.VInputTag(
        cms.InputTag("akSoftDropZ05B156PFSimpleSecondaryVertexHighEffBJetTags"),
        cms.InputTag("akSoftDropZ05B156PFSimpleSecondaryVertexHighPurBJetTags"),
        cms.InputTag("akSoftDropZ05B156PFCombinedSecondaryVertexBJetTags"),
        cms.InputTag("akSoftDropZ05B156PFCombinedSecondaryVertexV2BJetTags"),
        cms.InputTag("akSoftDropZ05B156PFJetBProbabilityBJetTags"),
        cms.InputTag("akSoftDropZ05B156PFJetProbabilityBJetTags"),
        # cms.InputTag("akSoftDropZ05B156PFSoftPFMuonByPtBJetTags"),
        # cms.InputTag("akSoftDropZ05B156PFSoftPFMuonByIP3dBJetTags"),
        cms.InputTag("akSoftDropZ05B156PFTrackCountingHighEffBJetTags"),
        cms.InputTag("akSoftDropZ05B156PFTrackCountingHighPurBJetTags"),
        ),
    tagInfoSources = cms.VInputTag(cms.InputTag("akSoftDropZ05B156PFImpactParameterTagInfos"),cms.InputTag("akSoftDropZ05B156PFSecondaryVertexTagInfos")),
    jetIDMap = cms.InputTag("akSoftDropZ05B156PFJetID"),
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

akSoftDropZ05B156PFNjettiness = Njettiness.clone(
    src = cms.InputTag("akSoftDropZ05B156PFJets"),
    R0  = cms.double(0.6)
    )

akSoftDropZ05B156PFpatJetsWithBtagging.userData.userFloats.src += [
    'akSoftDropZ05B156PFNjettiness:tau1',
    'akSoftDropZ05B156PFNjettiness:tau2',
    'akSoftDropZ05B156PFNjettiness:tau3']

akSoftDropZ05B156PFJetAnalyzer = inclusiveJetAnalyzer.clone(
    jetTag = cms.InputTag("akSoftDropZ05B156PFpatJetsWithBtagging"),
    genjetTag = 'ak6HiGenJets',
    rParam = 0.6,
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
    bTagJetName = cms.untracked.string("akSoftDropZ05B156PF"),
    jetName = cms.untracked.string("akSoftDropZ05B156PF"),
    genPtMin = cms.untracked.double(5),
    doTower = cms.untracked.bool(False),
    doSubJets = cms.untracked.bool(True),
    doGenSubJets = cms.untracked.bool(False),
    subjetGenTag = cms.untracked.InputTag("akSoftDropZ05B156GenJets"),
    doGenTaus = cms.untracked.bool(False),
    genTau1 = cms.InputTag("akSoftDropZ05B156HiGenNjettiness","tau1"),
    genTau2 = cms.InputTag("akSoftDropZ05B156HiGenNjettiness","tau2"),
    genTau3 = cms.InputTag("akSoftDropZ05B156HiGenNjettiness","tau3"),
    doGenSym = cms.untracked.bool(False),
    genSym = cms.InputTag("akSoftDropZ05B156GenJets","sym"),
    genDroppedBranches = cms.InputTag("akSoftDropZ05B156GenJets","droppedBranches")
    )

akSoftDropZ05B156PFJetSequence_mc = cms.Sequence(
    # akSoftDropZ05B156PFclean
    # *
    akSoftDropZ05B156PFmatch
    # *
    # akSoftDropZ05B156PFmatchGroomed
    *
    akSoftDropZ05B156PFparton
    *
    akSoftDropZ05B156PFcorr
    # *
    # akSoftDropZ05B156PFJetID
    *
     akSoftDropZ05B156PFPatJetFlavourId 
    *
    akSoftDropZ05B156PFJetTracksAssociatorAtVertex
    *
    akSoftDropZ05B156PFJetBtagging
    *
    # No constituents for calo jets in pp. Must be removed for pp calo jets but
    # I'm not sure how to do this transparently (Marta)
    akSoftDropZ05B156PFNjettiness
    *
    akSoftDropZ05B156PFpatJetsWithBtagging
    *
    akSoftDropZ05B156PFJetAnalyzer
    )

akSoftDropZ05B156PFJetSequence_data = cms.Sequence(
    akSoftDropZ05B156PFcorr
    *
    # akSoftDropZ05B156PFJetID
    # *
    akSoftDropZ05B156PFJetTracksAssociatorAtVertex
    *
    akSoftDropZ05B156PFJetBtagging
    *
    akSoftDropZ05B156PFNjettiness
    *
    akSoftDropZ05B156PFpatJetsWithBtagging
    *
    akSoftDropZ05B156PFJetAnalyzer
    )

akSoftDropZ05B156PFJetSequence_mb = cms.Sequence(
    akSoftDropZ05B156PFJetSequence_mc)
akSoftDropZ05B156PFJetSequence_jec = cms.Sequence(
    akSoftDropZ05B156PFJetSequence_mc)

akSoftDropZ05B156PFJetSequence = cms.Sequence(
    akSoftDropZ05B156PFJetSequence_mb)
akSoftDropZ05B156PFpatJetsWithBtagging.userData.userFloats.src += ['akSoftDropZ05B156PFJets:sym']
akSoftDropZ05B156PFpatJetsWithBtagging.userData.userInts.src += ['akSoftDropZ05B156PFJets:droppedBranches']
