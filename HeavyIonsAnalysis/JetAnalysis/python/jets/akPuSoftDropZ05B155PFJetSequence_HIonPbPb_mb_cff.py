import FWCore.ParameterSet.Config as cms

from PhysicsTools.PatAlgos.mcMatchLayer0.jetMatch_cfi import patJetGenJetMatch, patJetPartonMatch
from PhysicsTools.PatAlgos.recoLayer0.jetCorrFactors_cfi import patJetCorrFactors
from PhysicsTools.PatAlgos.producersLayer1.jetProducer_cfi import patJets

from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *

from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akPuSoftDropZ05B155PFmatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akPuSoftDropZ05B155PFJets"),
    matched = cms.InputTag("ak5HiCleanedGenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.5
    )

akPuSoftDropZ05B155PFmatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDropZ05B155HiGenJets"),
    matched = cms.InputTag("ak5HiCleanedGenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.5
    )

akPuSoftDropZ05B155PFparton = patJetPartonMatch.clone(
    src = cms.InputTag("akPuSoftDropZ05B155PFJets"),
    matched = cms.InputTag("cleanedPartons"))

akPuSoftDropZ05B155PFcorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
    levels   = cms.vstring('L2Relative'),
    src = cms.InputTag("akPuSoftDropZ05B155PFJets"),
    payload = "AKPu5PF_offline"
    )

akPuSoftDropZ05B155PFJetID = cms.EDProducer(
    'JetIDProducer',
    JetIDParams,
    src = cms.InputTag('akPuSoftDropZ05B155CaloJets'))

# akPuSoftDropZ05B155PFclean = heavyIonCleanedGenJets.clone(
#     src = cms.InputTag('ak5HiCleanedGenJets'))

akPuSoftDropZ05B155PFbTagger = bTaggers(
    "akPuSoftDropZ05B155PF",
    0.5)

# create objects locally since they dont load properly otherwise
akPuSoftDropZ05B155PFPatJetFlavourAssociationLegacy = akPuSoftDropZ05B155PFbTagger.PatJetFlavourAssociationLegacy
akPuSoftDropZ05B155PFPatJetPartons = akPuSoftDropZ05B155PFbTagger.PatJetPartons
akPuSoftDropZ05B155PFJetTracksAssociatorAtVertex = akPuSoftDropZ05B155PFbTagger.JetTracksAssociatorAtVertex
akPuSoftDropZ05B155PFJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akPuSoftDropZ05B155PFSimpleSecondaryVertexHighEffBJetTags = akPuSoftDropZ05B155PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akPuSoftDropZ05B155PFSimpleSecondaryVertexHighPurBJetTags = akPuSoftDropZ05B155PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akPuSoftDropZ05B155PFCombinedSecondaryVertexBJetTags = akPuSoftDropZ05B155PFbTagger.CombinedSecondaryVertexBJetTags
akPuSoftDropZ05B155PFCombinedSecondaryVertexV2BJetTags = akPuSoftDropZ05B155PFbTagger.CombinedSecondaryVertexV2BJetTags
akPuSoftDropZ05B155PFJetBProbabilityBJetTags = akPuSoftDropZ05B155PFbTagger.JetBProbabilityBJetTags
akPuSoftDropZ05B155PFSoftPFMuonByPtBJetTags = akPuSoftDropZ05B155PFbTagger.SoftPFMuonByPtBJetTags
akPuSoftDropZ05B155PFSoftPFMuonByIP3dBJetTags = akPuSoftDropZ05B155PFbTagger.SoftPFMuonByIP3dBJetTags
akPuSoftDropZ05B155PFTrackCountingHighEffBJetTags = akPuSoftDropZ05B155PFbTagger.TrackCountingHighEffBJetTags
akPuSoftDropZ05B155PFTrackCountingHighPurBJetTags = akPuSoftDropZ05B155PFbTagger.TrackCountingHighPurBJetTags
akPuSoftDropZ05B155PFPatJetPartonAssociationLegacy = akPuSoftDropZ05B155PFbTagger.PatJetPartonAssociationLegacy
akPuSoftDropZ05B155PFPatJetPartonAssociationLegacy.partons = "myPartons"

akPuSoftDropZ05B155PFImpactParameterTagInfos = akPuSoftDropZ05B155PFbTagger.ImpactParameterTagInfos
akPuSoftDropZ05B155PFImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akPuSoftDropZ05B155PFJetProbabilityBJetTags = akPuSoftDropZ05B155PFbTagger.JetProbabilityBJetTags

akPuSoftDropZ05B155PFSecondaryVertexTagInfos = akPuSoftDropZ05B155PFbTagger.SecondaryVertexTagInfos
akPuSoftDropZ05B155PFSimpleSecondaryVertexHighEffBJetTags = akPuSoftDropZ05B155PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akPuSoftDropZ05B155PFSimpleSecondaryVertexHighPurBJetTags = akPuSoftDropZ05B155PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akPuSoftDropZ05B155PFCombinedSecondaryVertexBJetTags = akPuSoftDropZ05B155PFbTagger.CombinedSecondaryVertexBJetTags
akPuSoftDropZ05B155PFCombinedSecondaryVertexV2BJetTags = akPuSoftDropZ05B155PFbTagger.CombinedSecondaryVertexV2BJetTags

akPuSoftDropZ05B155PFSecondaryVertexNegativeTagInfos = akPuSoftDropZ05B155PFbTagger.SecondaryVertexNegativeTagInfos
akPuSoftDropZ05B155PFNegativeSimpleSecondaryVertexHighEffBJetTags = akPuSoftDropZ05B155PFbTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akPuSoftDropZ05B155PFNegativeSimpleSecondaryVertexHighPurBJetTags = akPuSoftDropZ05B155PFbTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akPuSoftDropZ05B155PFNegativeCombinedSecondaryVertexBJetTags = akPuSoftDropZ05B155PFbTagger.NegativeCombinedSecondaryVertexBJetTags
akPuSoftDropZ05B155PFPositiveCombinedSecondaryVertexBJetTags = akPuSoftDropZ05B155PFbTagger.PositiveCombinedSecondaryVertexBJetTags
akPuSoftDropZ05B155PFNegativeCombinedSecondaryVertexV2BJetTags = akPuSoftDropZ05B155PFbTagger.NegativeCombinedSecondaryVertexV2BJetTags
akPuSoftDropZ05B155PFPositiveCombinedSecondaryVertexV2BJetTags = akPuSoftDropZ05B155PFbTagger.PositiveCombinedSecondaryVertexV2BJetTags

akPuSoftDropZ05B155PFSoftPFMuonsTagInfos = akPuSoftDropZ05B155PFbTagger.SoftPFMuonsTagInfos
akPuSoftDropZ05B155PFSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akPuSoftDropZ05B155PFSoftPFMuonBJetTags = akPuSoftDropZ05B155PFbTagger.SoftPFMuonBJetTags
akPuSoftDropZ05B155PFSoftPFMuonByIP3dBJetTags = akPuSoftDropZ05B155PFbTagger.SoftPFMuonByIP3dBJetTags
akPuSoftDropZ05B155PFSoftPFMuonByPtBJetTags = akPuSoftDropZ05B155PFbTagger.SoftPFMuonByPtBJetTags
akPuSoftDropZ05B155PFNegativeSoftPFMuonByPtBJetTags = akPuSoftDropZ05B155PFbTagger.NegativeSoftPFMuonByPtBJetTags
akPuSoftDropZ05B155PFPositiveSoftPFMuonByPtBJetTags = akPuSoftDropZ05B155PFbTagger.PositiveSoftPFMuonByPtBJetTags
akPuSoftDropZ05B155PFPatJetFlavourIdLegacy = cms.Sequence(akPuSoftDropZ05B155PFPatJetPartonAssociationLegacy*akPuSoftDropZ05B155PFPatJetFlavourAssociationLegacy)
# Not working with our PU sub, but keep it here for reference
# akPuSoftDropZ05B155PFPatJetFlavourAssociation = akPuSoftDropZ05B155PFbTagger.PatJetFlavourAssociation
# akPuSoftDropZ05B155PFPatJetFlavourId = cms.Sequence(akPuSoftDropZ05B155PFPatJetPartons*akPuSoftDropZ05B155PFPatJetFlavourAssociation)

akPuSoftDropZ05B155PFJetBtaggingIP = cms.Sequence(
    akPuSoftDropZ05B155PFImpactParameterTagInfos *
    akPuSoftDropZ05B155PFTrackCountingHighEffBJetTags +
    akPuSoftDropZ05B155PFTrackCountingHighPurBJetTags +
    akPuSoftDropZ05B155PFJetProbabilityBJetTags +
    akPuSoftDropZ05B155PFJetBProbabilityBJetTags
    )

akPuSoftDropZ05B155PFJetBtaggingSV = cms.Sequence(
    akPuSoftDropZ05B155PFImpactParameterTagInfos *
    akPuSoftDropZ05B155PFSecondaryVertexTagInfos *
    akPuSoftDropZ05B155PFSimpleSecondaryVertexHighEffBJetTags +
    akPuSoftDropZ05B155PFSimpleSecondaryVertexHighPurBJetTags +
    akPuSoftDropZ05B155PFCombinedSecondaryVertexBJetTags +
    akPuSoftDropZ05B155PFCombinedSecondaryVertexV2BJetTags
    )

akPuSoftDropZ05B155PFJetBtaggingNegSV = cms.Sequence(
    akPuSoftDropZ05B155PFImpactParameterTagInfos *
    akPuSoftDropZ05B155PFSecondaryVertexNegativeTagInfos *
    akPuSoftDropZ05B155PFNegativeSimpleSecondaryVertexHighEffBJetTags +
    akPuSoftDropZ05B155PFNegativeSimpleSecondaryVertexHighPurBJetTags +
    akPuSoftDropZ05B155PFNegativeCombinedSecondaryVertexBJetTags +
    akPuSoftDropZ05B155PFPositiveCombinedSecondaryVertexBJetTags +
    akPuSoftDropZ05B155PFNegativeCombinedSecondaryVertexV2BJetTags +
    akPuSoftDropZ05B155PFPositiveCombinedSecondaryVertexV2BJetTags
    )

akPuSoftDropZ05B155PFJetBtaggingMu = cms.Sequence(
    akPuSoftDropZ05B155PFSoftPFMuonsTagInfos *
    akPuSoftDropZ05B155PFSoftPFMuonBJetTags +
    akPuSoftDropZ05B155PFSoftPFMuonByIP3dBJetTags +
    akPuSoftDropZ05B155PFSoftPFMuonByPtBJetTags +
    akPuSoftDropZ05B155PFNegativeSoftPFMuonByPtBJetTags +
    akPuSoftDropZ05B155PFPositiveSoftPFMuonByPtBJetTags
    )

akPuSoftDropZ05B155PFJetBtagging = cms.Sequence(
    akPuSoftDropZ05B155PFJetBtaggingIP
    * akPuSoftDropZ05B155PFJetBtaggingSV
    # * akPuSoftDropZ05B155PFJetBtaggingNegSV
    # * akPuSoftDropZ05B155PFJetBtaggingMu
    )

akPuSoftDropZ05B155PFpatJetsWithBtagging = patJets.clone(
    jetSource = cms.InputTag("akPuSoftDropZ05B155PFJets"),
    genJetMatch            = cms.InputTag("akPuSoftDropZ05B155PFmatch"),
    genPartonMatch         = cms.InputTag("akPuSoftDropZ05B155PFparton"),
    jetCorrFactorsSource   = cms.VInputTag(cms.InputTag("akPuSoftDropZ05B155PFcorr")),
    JetPartonMapSource     = cms.InputTag("akPuSoftDropZ05B155PFPatJetFlavourAssociationLegacy"),
    JetFlavourInfoSource   = cms.InputTag("akPuSoftDropZ05B155PFPatJetFlavourAssociation"),
    trackAssociationSource = cms.InputTag("akPuSoftDropZ05B155PFJetTracksAssociatorAtVertex"),
    useLegacyJetMCFlavour  = True,
    discriminatorSources   = cms.VInputTag(
        cms.InputTag("akPuSoftDropZ05B155PFSimpleSecondaryVertexHighEffBJetTags"),
        cms.InputTag("akPuSoftDropZ05B155PFSimpleSecondaryVertexHighPurBJetTags"),
        cms.InputTag("akPuSoftDropZ05B155PFCombinedSecondaryVertexBJetTags"),
        cms.InputTag("akPuSoftDropZ05B155PFCombinedSecondaryVertexV2BJetTags"),
        cms.InputTag("akPuSoftDropZ05B155PFJetBProbabilityBJetTags"),
        cms.InputTag("akPuSoftDropZ05B155PFJetProbabilityBJetTags"),
        # cms.InputTag("akPuSoftDropZ05B155PFSoftPFMuonByPtBJetTags"),
        # cms.InputTag("akPuSoftDropZ05B155PFSoftPFMuonByIP3dBJetTags"),
        cms.InputTag("akPuSoftDropZ05B155PFTrackCountingHighEffBJetTags"),
        cms.InputTag("akPuSoftDropZ05B155PFTrackCountingHighPurBJetTags"),
        ),
    tagInfoSources = cms.VInputTag(cms.InputTag("akPuSoftDropZ05B155PFImpactParameterTagInfos"),cms.InputTag("akPuSoftDropZ05B155PFSecondaryVertexTagInfos")),
    jetIDMap = cms.InputTag("akPuSoftDropZ05B155PFJetID"),
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

akPuSoftDropZ05B155PFNjettiness = Njettiness.clone(
    src = cms.InputTag("akPuSoftDropZ05B155PFJets"),
    R0  = cms.double(0.5)
    )

akPuSoftDropZ05B155PFpatJetsWithBtagging.userData.userFloats.src += [
    'akPuSoftDropZ05B155PFNjettiness:tau1',
    'akPuSoftDropZ05B155PFNjettiness:tau2',
    'akPuSoftDropZ05B155PFNjettiness:tau3']

akPuSoftDropZ05B155PFJetAnalyzer = inclusiveJetAnalyzer.clone(
    jetTag = cms.InputTag("akPuSoftDropZ05B155PFpatJetsWithBtagging"),
    genjetTag = 'ak5HiGenJets',
    rParam = 0.5,
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
    bTagJetName = cms.untracked.string("akPuSoftDropZ05B155PF"),
    jetName = cms.untracked.string("akPuSoftDropZ05B155PF"),
    genPtMin = cms.untracked.double(5),
    hltTrgResults = cms.untracked.string('TriggerResults::'+'HISIGNAL'),
    doTower = cms.untracked.bool(True),
    doSubJets = cms.untracked.bool(True),
    doGenSubJets = cms.untracked.bool(False),
    subjetGenTag = cms.untracked.InputTag("akSoftDropZ05B155GenJets"),
    doGenTaus = cms.untracked.bool(False),
    genTau1 = cms.InputTag("akSoftDropZ05B155HiGenNjettiness","tau1"),
    genTau2 = cms.InputTag("akSoftDropZ05B155HiGenNjettiness","tau2"),
    genTau3 = cms.InputTag("akSoftDropZ05B155HiGenNjettiness","tau3"),
    doGenSym = cms.untracked.bool(False),
    genSym = cms.InputTag("akSoftDropZ05B155GenJets","sym"),
    genDroppedBranches = cms.InputTag("akSoftDropZ05B155GenJets","droppedBranches")
    )

akPuSoftDropZ05B155PFJetSequence_mc = cms.Sequence(
    # akPuSoftDropZ05B155PFclean
    # *
    akPuSoftDropZ05B155PFmatch
    # *
    # akPuSoftDropZ05B155PFmatchGroomed
    *
    akPuSoftDropZ05B155PFparton
    *
    akPuSoftDropZ05B155PFcorr
    # *
    # akPuSoftDropZ05B155PFJetID
    *
    akPuSoftDropZ05B155PFPatJetFlavourIdLegacy
    # *
    # akPuSoftDropZ05B155PFPatJetFlavourId # Use legacy algo till PU implemented
    *
    akPuSoftDropZ05B155PFJetTracksAssociatorAtVertex
    *
    akPuSoftDropZ05B155PFJetBtagging
    *
    # No constituents for calo jets in pp. Must be removed for pp calo jets but
    # I'm not sure how to do this transparently (Marta)
    akPuSoftDropZ05B155PFNjettiness
    *
    akPuSoftDropZ05B155PFpatJetsWithBtagging
    *
    akPuSoftDropZ05B155PFJetAnalyzer
    )

akPuSoftDropZ05B155PFJetSequence_data = cms.Sequence(
    akPuSoftDropZ05B155PFcorr
    *
    # akPuSoftDropZ05B155PFJetID
    # *
    akPuSoftDropZ05B155PFJetTracksAssociatorAtVertex
    *
    akPuSoftDropZ05B155PFJetBtagging
    *
    akPuSoftDropZ05B155PFNjettiness
    *
    akPuSoftDropZ05B155PFpatJetsWithBtagging
    *
    akPuSoftDropZ05B155PFJetAnalyzer
    )

akPuSoftDropZ05B155PFJetSequence_mb = cms.Sequence(
    akPuSoftDropZ05B155PFJetSequence_mc)
akPuSoftDropZ05B155PFJetSequence_jec = cms.Sequence(
    akPuSoftDropZ05B155PFJetSequence_mc)

akPuSoftDropZ05B155PFJetSequence = cms.Sequence(
    akPuSoftDropZ05B155PFJetSequence_mb)
akPuSoftDropZ05B155PFpatJetsWithBtagging.userData.userFloats.src += ['akPuSoftDropZ05B155PFJets:sym']
akPuSoftDropZ05B155PFpatJetsWithBtagging.userData.userInts.src += ['akPuSoftDropZ05B155PFJets:droppedBranches']
