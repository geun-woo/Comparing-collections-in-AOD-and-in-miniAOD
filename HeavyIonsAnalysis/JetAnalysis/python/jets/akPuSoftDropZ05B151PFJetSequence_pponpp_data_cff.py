import FWCore.ParameterSet.Config as cms

from PhysicsTools.PatAlgos.mcMatchLayer0.jetMatch_cfi import patJetGenJetMatch, patJetPartonMatch
from PhysicsTools.PatAlgos.recoLayer0.jetCorrFactors_cfi import patJetCorrFactors
from PhysicsTools.PatAlgos.producersLayer1.jetProducer_cfi import patJets

from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *

from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akPuSoftDropZ05B151PFmatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akPuSoftDropZ05B151PFJets"),
    matched = cms.InputTag("ak1GenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.1
    )

akPuSoftDropZ05B151PFmatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDropZ05B151GenJets"),
    matched = cms.InputTag("ak1GenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.1
    )

akPuSoftDropZ05B151PFparton = patJetPartonMatch.clone(
    src = cms.InputTag("akPuSoftDropZ05B151PFJets"),
    matched = cms.InputTag("genParticles"))

akPuSoftDropZ05B151PFcorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
    levels   = cms.vstring('L2Relative','L2L3Residual'),
    src = cms.InputTag("akPuSoftDropZ05B151PFJets"),
    payload = "AK1PF"
    )

akPuSoftDropZ05B151PFJetID = cms.EDProducer(
    'JetIDProducer',
    JetIDParams,
    src = cms.InputTag('akPuSoftDropZ05B151CaloJets'))

# akPuSoftDropZ05B151PFclean = heavyIonCleanedGenJets.clone(
#     src = cms.InputTag('ak1GenJets'))

akPuSoftDropZ05B151PFbTagger = bTaggers(
    "akPuSoftDropZ05B151PF",
    0.1)

# create objects locally since they dont load properly otherwise
akPuSoftDropZ05B151PFPatJetFlavourAssociationLegacy = akPuSoftDropZ05B151PFbTagger.PatJetFlavourAssociationLegacy
akPuSoftDropZ05B151PFPatJetPartons = akPuSoftDropZ05B151PFbTagger.PatJetPartons
akPuSoftDropZ05B151PFJetTracksAssociatorAtVertex = akPuSoftDropZ05B151PFbTagger.JetTracksAssociatorAtVertex
akPuSoftDropZ05B151PFJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akPuSoftDropZ05B151PFSimpleSecondaryVertexHighEffBJetTags = akPuSoftDropZ05B151PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akPuSoftDropZ05B151PFSimpleSecondaryVertexHighPurBJetTags = akPuSoftDropZ05B151PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akPuSoftDropZ05B151PFCombinedSecondaryVertexBJetTags = akPuSoftDropZ05B151PFbTagger.CombinedSecondaryVertexBJetTags
akPuSoftDropZ05B151PFCombinedSecondaryVertexV2BJetTags = akPuSoftDropZ05B151PFbTagger.CombinedSecondaryVertexV2BJetTags
akPuSoftDropZ05B151PFJetBProbabilityBJetTags = akPuSoftDropZ05B151PFbTagger.JetBProbabilityBJetTags
akPuSoftDropZ05B151PFSoftPFMuonByPtBJetTags = akPuSoftDropZ05B151PFbTagger.SoftPFMuonByPtBJetTags
akPuSoftDropZ05B151PFSoftPFMuonByIP3dBJetTags = akPuSoftDropZ05B151PFbTagger.SoftPFMuonByIP3dBJetTags
akPuSoftDropZ05B151PFTrackCountingHighEffBJetTags = akPuSoftDropZ05B151PFbTagger.TrackCountingHighEffBJetTags
akPuSoftDropZ05B151PFTrackCountingHighPurBJetTags = akPuSoftDropZ05B151PFbTagger.TrackCountingHighPurBJetTags
akPuSoftDropZ05B151PFPatJetPartonAssociationLegacy = akPuSoftDropZ05B151PFbTagger.PatJetPartonAssociationLegacy
akPuSoftDropZ05B151PFPatJetPartonAssociationLegacy.partons = "myPartons"

akPuSoftDropZ05B151PFImpactParameterTagInfos = akPuSoftDropZ05B151PFbTagger.ImpactParameterTagInfos
akPuSoftDropZ05B151PFImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akPuSoftDropZ05B151PFJetProbabilityBJetTags = akPuSoftDropZ05B151PFbTagger.JetProbabilityBJetTags

akPuSoftDropZ05B151PFSecondaryVertexTagInfos = akPuSoftDropZ05B151PFbTagger.SecondaryVertexTagInfos
akPuSoftDropZ05B151PFSimpleSecondaryVertexHighEffBJetTags = akPuSoftDropZ05B151PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akPuSoftDropZ05B151PFSimpleSecondaryVertexHighPurBJetTags = akPuSoftDropZ05B151PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akPuSoftDropZ05B151PFCombinedSecondaryVertexBJetTags = akPuSoftDropZ05B151PFbTagger.CombinedSecondaryVertexBJetTags
akPuSoftDropZ05B151PFCombinedSecondaryVertexV2BJetTags = akPuSoftDropZ05B151PFbTagger.CombinedSecondaryVertexV2BJetTags

akPuSoftDropZ05B151PFSecondaryVertexNegativeTagInfos = akPuSoftDropZ05B151PFbTagger.SecondaryVertexNegativeTagInfos
akPuSoftDropZ05B151PFNegativeSimpleSecondaryVertexHighEffBJetTags = akPuSoftDropZ05B151PFbTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akPuSoftDropZ05B151PFNegativeSimpleSecondaryVertexHighPurBJetTags = akPuSoftDropZ05B151PFbTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akPuSoftDropZ05B151PFNegativeCombinedSecondaryVertexBJetTags = akPuSoftDropZ05B151PFbTagger.NegativeCombinedSecondaryVertexBJetTags
akPuSoftDropZ05B151PFPositiveCombinedSecondaryVertexBJetTags = akPuSoftDropZ05B151PFbTagger.PositiveCombinedSecondaryVertexBJetTags
akPuSoftDropZ05B151PFNegativeCombinedSecondaryVertexV2BJetTags = akPuSoftDropZ05B151PFbTagger.NegativeCombinedSecondaryVertexV2BJetTags
akPuSoftDropZ05B151PFPositiveCombinedSecondaryVertexV2BJetTags = akPuSoftDropZ05B151PFbTagger.PositiveCombinedSecondaryVertexV2BJetTags

akPuSoftDropZ05B151PFSoftPFMuonsTagInfos = akPuSoftDropZ05B151PFbTagger.SoftPFMuonsTagInfos
akPuSoftDropZ05B151PFSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akPuSoftDropZ05B151PFSoftPFMuonBJetTags = akPuSoftDropZ05B151PFbTagger.SoftPFMuonBJetTags
akPuSoftDropZ05B151PFSoftPFMuonByIP3dBJetTags = akPuSoftDropZ05B151PFbTagger.SoftPFMuonByIP3dBJetTags
akPuSoftDropZ05B151PFSoftPFMuonByPtBJetTags = akPuSoftDropZ05B151PFbTagger.SoftPFMuonByPtBJetTags
akPuSoftDropZ05B151PFNegativeSoftPFMuonByPtBJetTags = akPuSoftDropZ05B151PFbTagger.NegativeSoftPFMuonByPtBJetTags
akPuSoftDropZ05B151PFPositiveSoftPFMuonByPtBJetTags = akPuSoftDropZ05B151PFbTagger.PositiveSoftPFMuonByPtBJetTags
akPuSoftDropZ05B151PFPatJetFlavourIdLegacy = cms.Sequence(akPuSoftDropZ05B151PFPatJetPartonAssociationLegacy*akPuSoftDropZ05B151PFPatJetFlavourAssociationLegacy)
# Not working with our PU sub, but keep it here for reference
# akPuSoftDropZ05B151PFPatJetFlavourAssociation = akPuSoftDropZ05B151PFbTagger.PatJetFlavourAssociation
# akPuSoftDropZ05B151PFPatJetFlavourId = cms.Sequence(akPuSoftDropZ05B151PFPatJetPartons*akPuSoftDropZ05B151PFPatJetFlavourAssociation)

akPuSoftDropZ05B151PFJetBtaggingIP = cms.Sequence(
    akPuSoftDropZ05B151PFImpactParameterTagInfos *
    akPuSoftDropZ05B151PFTrackCountingHighEffBJetTags +
    akPuSoftDropZ05B151PFTrackCountingHighPurBJetTags +
    akPuSoftDropZ05B151PFJetProbabilityBJetTags +
    akPuSoftDropZ05B151PFJetBProbabilityBJetTags
    )

akPuSoftDropZ05B151PFJetBtaggingSV = cms.Sequence(
    akPuSoftDropZ05B151PFImpactParameterTagInfos *
    akPuSoftDropZ05B151PFSecondaryVertexTagInfos *
    akPuSoftDropZ05B151PFSimpleSecondaryVertexHighEffBJetTags +
    akPuSoftDropZ05B151PFSimpleSecondaryVertexHighPurBJetTags +
    akPuSoftDropZ05B151PFCombinedSecondaryVertexBJetTags +
    akPuSoftDropZ05B151PFCombinedSecondaryVertexV2BJetTags
    )

akPuSoftDropZ05B151PFJetBtaggingNegSV = cms.Sequence(
    akPuSoftDropZ05B151PFImpactParameterTagInfos *
    akPuSoftDropZ05B151PFSecondaryVertexNegativeTagInfos *
    akPuSoftDropZ05B151PFNegativeSimpleSecondaryVertexHighEffBJetTags +
    akPuSoftDropZ05B151PFNegativeSimpleSecondaryVertexHighPurBJetTags +
    akPuSoftDropZ05B151PFNegativeCombinedSecondaryVertexBJetTags +
    akPuSoftDropZ05B151PFPositiveCombinedSecondaryVertexBJetTags +
    akPuSoftDropZ05B151PFNegativeCombinedSecondaryVertexV2BJetTags +
    akPuSoftDropZ05B151PFPositiveCombinedSecondaryVertexV2BJetTags
    )

akPuSoftDropZ05B151PFJetBtaggingMu = cms.Sequence(
    akPuSoftDropZ05B151PFSoftPFMuonsTagInfos *
    akPuSoftDropZ05B151PFSoftPFMuonBJetTags +
    akPuSoftDropZ05B151PFSoftPFMuonByIP3dBJetTags +
    akPuSoftDropZ05B151PFSoftPFMuonByPtBJetTags +
    akPuSoftDropZ05B151PFNegativeSoftPFMuonByPtBJetTags +
    akPuSoftDropZ05B151PFPositiveSoftPFMuonByPtBJetTags
    )

akPuSoftDropZ05B151PFJetBtagging = cms.Sequence(
    akPuSoftDropZ05B151PFJetBtaggingIP
    * akPuSoftDropZ05B151PFJetBtaggingSV
    # * akPuSoftDropZ05B151PFJetBtaggingNegSV
    # * akPuSoftDropZ05B151PFJetBtaggingMu
    )

akPuSoftDropZ05B151PFpatJetsWithBtagging = patJets.clone(
    jetSource = cms.InputTag("akPuSoftDropZ05B151PFJets"),
    genJetMatch            = cms.InputTag("akPuSoftDropZ05B151PFmatch"),
    genPartonMatch         = cms.InputTag("akPuSoftDropZ05B151PFparton"),
    jetCorrFactorsSource   = cms.VInputTag(cms.InputTag("akPuSoftDropZ05B151PFcorr")),
    JetPartonMapSource     = cms.InputTag("akPuSoftDropZ05B151PFPatJetFlavourAssociationLegacy"),
    JetFlavourInfoSource   = cms.InputTag("akPuSoftDropZ05B151PFPatJetFlavourAssociation"),
    trackAssociationSource = cms.InputTag("akPuSoftDropZ05B151PFJetTracksAssociatorAtVertex"),
    useLegacyJetMCFlavour  = True,
    discriminatorSources   = cms.VInputTag(
        cms.InputTag("akPuSoftDropZ05B151PFSimpleSecondaryVertexHighEffBJetTags"),
        cms.InputTag("akPuSoftDropZ05B151PFSimpleSecondaryVertexHighPurBJetTags"),
        cms.InputTag("akPuSoftDropZ05B151PFCombinedSecondaryVertexBJetTags"),
        cms.InputTag("akPuSoftDropZ05B151PFCombinedSecondaryVertexV2BJetTags"),
        cms.InputTag("akPuSoftDropZ05B151PFJetBProbabilityBJetTags"),
        cms.InputTag("akPuSoftDropZ05B151PFJetProbabilityBJetTags"),
        # cms.InputTag("akPuSoftDropZ05B151PFSoftPFMuonByPtBJetTags"),
        # cms.InputTag("akPuSoftDropZ05B151PFSoftPFMuonByIP3dBJetTags"),
        cms.InputTag("akPuSoftDropZ05B151PFTrackCountingHighEffBJetTags"),
        cms.InputTag("akPuSoftDropZ05B151PFTrackCountingHighPurBJetTags"),
        ),
    tagInfoSources = cms.VInputTag(cms.InputTag("akPuSoftDropZ05B151PFImpactParameterTagInfos"),cms.InputTag("akPuSoftDropZ05B151PFSecondaryVertexTagInfos")),
    jetIDMap = cms.InputTag("akPuSoftDropZ05B151PFJetID"),
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

akPuSoftDropZ05B151PFNjettiness = Njettiness.clone(
    src = cms.InputTag("akPuSoftDropZ05B151PFJets"),
    R0  = cms.double(0.1)
    )

akPuSoftDropZ05B151PFpatJetsWithBtagging.userData.userFloats.src += [
    'akPuSoftDropZ05B151PFNjettiness:tau1',
    'akPuSoftDropZ05B151PFNjettiness:tau2',
    'akPuSoftDropZ05B151PFNjettiness:tau3']

akPuSoftDropZ05B151PFJetAnalyzer = inclusiveJetAnalyzer.clone(
    jetTag = cms.InputTag("akPuSoftDropZ05B151PFpatJetsWithBtagging"),
    genjetTag = 'ak1GenJets',
    rParam = 0.1,
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
    bTagJetName = cms.untracked.string("akPuSoftDropZ05B151PF"),
    jetName = cms.untracked.string("akPuSoftDropZ05B151PF"),
    genPtMin = cms.untracked.double(5),
    hltTrgResults = cms.untracked.string('TriggerResults::'+'HISIGNAL'),
    doTower = cms.untracked.bool(False),
    doSubJets = cms.untracked.bool(True),
    doGenSubJets = cms.untracked.bool(False),
    subjetGenTag = cms.untracked.InputTag("akSoftDropZ05B151GenJets"),
    doGenTaus = cms.untracked.bool(False),
    genTau1 = cms.InputTag("akSoftDropZ05B151GenNjettiness","tau1"),
    genTau2 = cms.InputTag("akSoftDropZ05B151GenNjettiness","tau2"),
    genTau3 = cms.InputTag("akSoftDropZ05B151GenNjettiness","tau3"),
    doGenSym = cms.untracked.bool(False),
    genSym = cms.InputTag("akSoftDropZ05B151GenJets","sym"),
    genDroppedBranches = cms.InputTag("akSoftDropZ05B151GenJets","droppedBranches")
    )

akPuSoftDropZ05B151PFJetSequence_mc = cms.Sequence(
    # akPuSoftDropZ05B151PFclean
    # *
    akPuSoftDropZ05B151PFmatch
    # *
    # akPuSoftDropZ05B151PFmatchGroomed
    *
    akPuSoftDropZ05B151PFparton
    *
    akPuSoftDropZ05B151PFcorr
    # *
    # akPuSoftDropZ05B151PFJetID
    *
    akPuSoftDropZ05B151PFPatJetFlavourIdLegacy
    # *
    # akPuSoftDropZ05B151PFPatJetFlavourId # Use legacy algo till PU implemented
    *
    akPuSoftDropZ05B151PFJetTracksAssociatorAtVertex
    *
    akPuSoftDropZ05B151PFJetBtagging
    *
    # No constituents for calo jets in pp. Must be removed for pp calo jets but
    # I'm not sure how to do this transparently (Marta)
    akPuSoftDropZ05B151PFNjettiness
    *
    akPuSoftDropZ05B151PFpatJetsWithBtagging
    *
    akPuSoftDropZ05B151PFJetAnalyzer
    )

akPuSoftDropZ05B151PFJetSequence_data = cms.Sequence(
    akPuSoftDropZ05B151PFcorr
    *
    # akPuSoftDropZ05B151PFJetID
    # *
    akPuSoftDropZ05B151PFJetTracksAssociatorAtVertex
    *
    akPuSoftDropZ05B151PFJetBtagging
    *
    akPuSoftDropZ05B151PFNjettiness
    *
    akPuSoftDropZ05B151PFpatJetsWithBtagging
    *
    akPuSoftDropZ05B151PFJetAnalyzer
    )

akPuSoftDropZ05B151PFJetSequence_mb = cms.Sequence(
    akPuSoftDropZ05B151PFJetSequence_mc)
akPuSoftDropZ05B151PFJetSequence_jec = cms.Sequence(
    akPuSoftDropZ05B151PFJetSequence_mc)

akPuSoftDropZ05B151PFJetSequence = cms.Sequence(
    akPuSoftDropZ05B151PFJetSequence_data)
akPuSoftDropZ05B151PFpatJetsWithBtagging.userData.userFloats.src += ['akPuSoftDropZ05B151PFJets:sym']
akPuSoftDropZ05B151PFpatJetsWithBtagging.userData.userInts.src += ['akPuSoftDropZ05B151PFJets:droppedBranches']
