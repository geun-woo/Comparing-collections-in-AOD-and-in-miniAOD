import FWCore.ParameterSet.Config as cms

from PhysicsTools.PatAlgos.mcMatchLayer0.jetMatch_cfi import patJetGenJetMatch, patJetPartonMatch
from PhysicsTools.PatAlgos.recoLayer0.jetCorrFactors_cfi import patJetCorrFactors
from PhysicsTools.PatAlgos.producersLayer1.jetProducer_cfi import patJets

from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *

from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akFlowPuCsSoftDropZ05B155PFmatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akFlowPuCsSoftDropZ05B155PFJets"),
    matched = cms.InputTag("ak5HiCleanedGenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.5
    )

akFlowPuCsSoftDropZ05B155PFmatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDropZ05B155HiGenJets"),
    matched = cms.InputTag("ak5HiCleanedGenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.5
    )

akFlowPuCsSoftDropZ05B155PFparton = patJetPartonMatch.clone(
    src = cms.InputTag("akFlowPuCsSoftDropZ05B155PFJets"),
    matched = cms.InputTag("cleanedPartons"))

akFlowPuCsSoftDropZ05B155PFcorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
    levels   = cms.vstring('L2Relative'),
    src = cms.InputTag("akFlowPuCsSoftDropZ05B155PFJets"),
    payload = "AK5PF"
    )

akFlowPuCsSoftDropZ05B155PFJetID = cms.EDProducer(
    'JetIDProducer',
    JetIDParams,
    src = cms.InputTag('akFlowPuCsSoftDropZ05B155CaloJets'))

# akFlowPuCsSoftDropZ05B155PFclean = heavyIonCleanedGenJets.clone(
#     src = cms.InputTag('ak5HiCleanedGenJets'))

akFlowPuCsSoftDropZ05B155PFbTagger = bTaggers(
    "akFlowPuCsSoftDropZ05B155PF",
    0.5)

# create objects locally since they dont load properly otherwise
akFlowPuCsSoftDropZ05B155PFPatJetFlavourAssociationLegacy = akFlowPuCsSoftDropZ05B155PFbTagger.PatJetFlavourAssociationLegacy
akFlowPuCsSoftDropZ05B155PFPatJetPartons = akFlowPuCsSoftDropZ05B155PFbTagger.PatJetPartons
akFlowPuCsSoftDropZ05B155PFJetTracksAssociatorAtVertex = akFlowPuCsSoftDropZ05B155PFbTagger.JetTracksAssociatorAtVertex
akFlowPuCsSoftDropZ05B155PFJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akFlowPuCsSoftDropZ05B155PFSimpleSecondaryVertexHighEffBJetTags = akFlowPuCsSoftDropZ05B155PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akFlowPuCsSoftDropZ05B155PFSimpleSecondaryVertexHighPurBJetTags = akFlowPuCsSoftDropZ05B155PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akFlowPuCsSoftDropZ05B155PFCombinedSecondaryVertexBJetTags = akFlowPuCsSoftDropZ05B155PFbTagger.CombinedSecondaryVertexBJetTags
akFlowPuCsSoftDropZ05B155PFCombinedSecondaryVertexV2BJetTags = akFlowPuCsSoftDropZ05B155PFbTagger.CombinedSecondaryVertexV2BJetTags
akFlowPuCsSoftDropZ05B155PFJetBProbabilityBJetTags = akFlowPuCsSoftDropZ05B155PFbTagger.JetBProbabilityBJetTags
akFlowPuCsSoftDropZ05B155PFSoftPFMuonByPtBJetTags = akFlowPuCsSoftDropZ05B155PFbTagger.SoftPFMuonByPtBJetTags
akFlowPuCsSoftDropZ05B155PFSoftPFMuonByIP3dBJetTags = akFlowPuCsSoftDropZ05B155PFbTagger.SoftPFMuonByIP3dBJetTags
akFlowPuCsSoftDropZ05B155PFTrackCountingHighEffBJetTags = akFlowPuCsSoftDropZ05B155PFbTagger.TrackCountingHighEffBJetTags
akFlowPuCsSoftDropZ05B155PFTrackCountingHighPurBJetTags = akFlowPuCsSoftDropZ05B155PFbTagger.TrackCountingHighPurBJetTags
akFlowPuCsSoftDropZ05B155PFPatJetPartonAssociationLegacy = akFlowPuCsSoftDropZ05B155PFbTagger.PatJetPartonAssociationLegacy
akFlowPuCsSoftDropZ05B155PFPatJetPartonAssociationLegacy.partons = "myPartons"

akFlowPuCsSoftDropZ05B155PFImpactParameterTagInfos = akFlowPuCsSoftDropZ05B155PFbTagger.ImpactParameterTagInfos
akFlowPuCsSoftDropZ05B155PFImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akFlowPuCsSoftDropZ05B155PFJetProbabilityBJetTags = akFlowPuCsSoftDropZ05B155PFbTagger.JetProbabilityBJetTags

akFlowPuCsSoftDropZ05B155PFSecondaryVertexTagInfos = akFlowPuCsSoftDropZ05B155PFbTagger.SecondaryVertexTagInfos
akFlowPuCsSoftDropZ05B155PFSimpleSecondaryVertexHighEffBJetTags = akFlowPuCsSoftDropZ05B155PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akFlowPuCsSoftDropZ05B155PFSimpleSecondaryVertexHighPurBJetTags = akFlowPuCsSoftDropZ05B155PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akFlowPuCsSoftDropZ05B155PFCombinedSecondaryVertexBJetTags = akFlowPuCsSoftDropZ05B155PFbTagger.CombinedSecondaryVertexBJetTags
akFlowPuCsSoftDropZ05B155PFCombinedSecondaryVertexV2BJetTags = akFlowPuCsSoftDropZ05B155PFbTagger.CombinedSecondaryVertexV2BJetTags

akFlowPuCsSoftDropZ05B155PFSecondaryVertexNegativeTagInfos = akFlowPuCsSoftDropZ05B155PFbTagger.SecondaryVertexNegativeTagInfos
akFlowPuCsSoftDropZ05B155PFNegativeSimpleSecondaryVertexHighEffBJetTags = akFlowPuCsSoftDropZ05B155PFbTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akFlowPuCsSoftDropZ05B155PFNegativeSimpleSecondaryVertexHighPurBJetTags = akFlowPuCsSoftDropZ05B155PFbTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akFlowPuCsSoftDropZ05B155PFNegativeCombinedSecondaryVertexBJetTags = akFlowPuCsSoftDropZ05B155PFbTagger.NegativeCombinedSecondaryVertexBJetTags
akFlowPuCsSoftDropZ05B155PFPositiveCombinedSecondaryVertexBJetTags = akFlowPuCsSoftDropZ05B155PFbTagger.PositiveCombinedSecondaryVertexBJetTags
akFlowPuCsSoftDropZ05B155PFNegativeCombinedSecondaryVertexV2BJetTags = akFlowPuCsSoftDropZ05B155PFbTagger.NegativeCombinedSecondaryVertexV2BJetTags
akFlowPuCsSoftDropZ05B155PFPositiveCombinedSecondaryVertexV2BJetTags = akFlowPuCsSoftDropZ05B155PFbTagger.PositiveCombinedSecondaryVertexV2BJetTags

akFlowPuCsSoftDropZ05B155PFSoftPFMuonsTagInfos = akFlowPuCsSoftDropZ05B155PFbTagger.SoftPFMuonsTagInfos
akFlowPuCsSoftDropZ05B155PFSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akFlowPuCsSoftDropZ05B155PFSoftPFMuonBJetTags = akFlowPuCsSoftDropZ05B155PFbTagger.SoftPFMuonBJetTags
akFlowPuCsSoftDropZ05B155PFSoftPFMuonByIP3dBJetTags = akFlowPuCsSoftDropZ05B155PFbTagger.SoftPFMuonByIP3dBJetTags
akFlowPuCsSoftDropZ05B155PFSoftPFMuonByPtBJetTags = akFlowPuCsSoftDropZ05B155PFbTagger.SoftPFMuonByPtBJetTags
akFlowPuCsSoftDropZ05B155PFNegativeSoftPFMuonByPtBJetTags = akFlowPuCsSoftDropZ05B155PFbTagger.NegativeSoftPFMuonByPtBJetTags
akFlowPuCsSoftDropZ05B155PFPositiveSoftPFMuonByPtBJetTags = akFlowPuCsSoftDropZ05B155PFbTagger.PositiveSoftPFMuonByPtBJetTags
akFlowPuCsSoftDropZ05B155PFPatJetFlavourIdLegacy = cms.Sequence(akFlowPuCsSoftDropZ05B155PFPatJetPartonAssociationLegacy*akFlowPuCsSoftDropZ05B155PFPatJetFlavourAssociationLegacy)
# Not working with our PU sub, but keep it here for reference
# akFlowPuCsSoftDropZ05B155PFPatJetFlavourAssociation = akFlowPuCsSoftDropZ05B155PFbTagger.PatJetFlavourAssociation
# akFlowPuCsSoftDropZ05B155PFPatJetFlavourId = cms.Sequence(akFlowPuCsSoftDropZ05B155PFPatJetPartons*akFlowPuCsSoftDropZ05B155PFPatJetFlavourAssociation)

akFlowPuCsSoftDropZ05B155PFJetBtaggingIP = cms.Sequence(
    akFlowPuCsSoftDropZ05B155PFImpactParameterTagInfos *
    akFlowPuCsSoftDropZ05B155PFTrackCountingHighEffBJetTags +
    akFlowPuCsSoftDropZ05B155PFTrackCountingHighPurBJetTags +
    akFlowPuCsSoftDropZ05B155PFJetProbabilityBJetTags +
    akFlowPuCsSoftDropZ05B155PFJetBProbabilityBJetTags
    )

akFlowPuCsSoftDropZ05B155PFJetBtaggingSV = cms.Sequence(
    akFlowPuCsSoftDropZ05B155PFImpactParameterTagInfos *
    akFlowPuCsSoftDropZ05B155PFSecondaryVertexTagInfos *
    akFlowPuCsSoftDropZ05B155PFSimpleSecondaryVertexHighEffBJetTags +
    akFlowPuCsSoftDropZ05B155PFSimpleSecondaryVertexHighPurBJetTags +
    akFlowPuCsSoftDropZ05B155PFCombinedSecondaryVertexBJetTags +
    akFlowPuCsSoftDropZ05B155PFCombinedSecondaryVertexV2BJetTags
    )

akFlowPuCsSoftDropZ05B155PFJetBtaggingNegSV = cms.Sequence(
    akFlowPuCsSoftDropZ05B155PFImpactParameterTagInfos *
    akFlowPuCsSoftDropZ05B155PFSecondaryVertexNegativeTagInfos *
    akFlowPuCsSoftDropZ05B155PFNegativeSimpleSecondaryVertexHighEffBJetTags +
    akFlowPuCsSoftDropZ05B155PFNegativeSimpleSecondaryVertexHighPurBJetTags +
    akFlowPuCsSoftDropZ05B155PFNegativeCombinedSecondaryVertexBJetTags +
    akFlowPuCsSoftDropZ05B155PFPositiveCombinedSecondaryVertexBJetTags +
    akFlowPuCsSoftDropZ05B155PFNegativeCombinedSecondaryVertexV2BJetTags +
    akFlowPuCsSoftDropZ05B155PFPositiveCombinedSecondaryVertexV2BJetTags
    )

akFlowPuCsSoftDropZ05B155PFJetBtaggingMu = cms.Sequence(
    akFlowPuCsSoftDropZ05B155PFSoftPFMuonsTagInfos *
    akFlowPuCsSoftDropZ05B155PFSoftPFMuonBJetTags +
    akFlowPuCsSoftDropZ05B155PFSoftPFMuonByIP3dBJetTags +
    akFlowPuCsSoftDropZ05B155PFSoftPFMuonByPtBJetTags +
    akFlowPuCsSoftDropZ05B155PFNegativeSoftPFMuonByPtBJetTags +
    akFlowPuCsSoftDropZ05B155PFPositiveSoftPFMuonByPtBJetTags
    )

akFlowPuCsSoftDropZ05B155PFJetBtagging = cms.Sequence(
    akFlowPuCsSoftDropZ05B155PFJetBtaggingIP
    * akFlowPuCsSoftDropZ05B155PFJetBtaggingSV
    # * akFlowPuCsSoftDropZ05B155PFJetBtaggingNegSV
    # * akFlowPuCsSoftDropZ05B155PFJetBtaggingMu
    )

akFlowPuCsSoftDropZ05B155PFpatJetsWithBtagging = patJets.clone(
    jetSource = cms.InputTag("akFlowPuCsSoftDropZ05B155PFJets"),
    genJetMatch            = cms.InputTag("akFlowPuCsSoftDropZ05B155PFmatch"),
    genPartonMatch         = cms.InputTag("akFlowPuCsSoftDropZ05B155PFparton"),
    jetCorrFactorsSource   = cms.VInputTag(cms.InputTag("akFlowPuCsSoftDropZ05B155PFcorr")),
    JetPartonMapSource     = cms.InputTag("akFlowPuCsSoftDropZ05B155PFPatJetFlavourAssociationLegacy"),
    JetFlavourInfoSource   = cms.InputTag("akFlowPuCsSoftDropZ05B155PFPatJetFlavourAssociation"),
    trackAssociationSource = cms.InputTag("akFlowPuCsSoftDropZ05B155PFJetTracksAssociatorAtVertex"),
    useLegacyJetMCFlavour  = True,
    discriminatorSources   = cms.VInputTag(
        cms.InputTag("akFlowPuCsSoftDropZ05B155PFSimpleSecondaryVertexHighEffBJetTags"),
        cms.InputTag("akFlowPuCsSoftDropZ05B155PFSimpleSecondaryVertexHighPurBJetTags"),
        cms.InputTag("akFlowPuCsSoftDropZ05B155PFCombinedSecondaryVertexBJetTags"),
        cms.InputTag("akFlowPuCsSoftDropZ05B155PFCombinedSecondaryVertexV2BJetTags"),
        cms.InputTag("akFlowPuCsSoftDropZ05B155PFJetBProbabilityBJetTags"),
        cms.InputTag("akFlowPuCsSoftDropZ05B155PFJetProbabilityBJetTags"),
        # cms.InputTag("akFlowPuCsSoftDropZ05B155PFSoftPFMuonByPtBJetTags"),
        # cms.InputTag("akFlowPuCsSoftDropZ05B155PFSoftPFMuonByIP3dBJetTags"),
        cms.InputTag("akFlowPuCsSoftDropZ05B155PFTrackCountingHighEffBJetTags"),
        cms.InputTag("akFlowPuCsSoftDropZ05B155PFTrackCountingHighPurBJetTags"),
        ),
    tagInfoSources = cms.VInputTag(cms.InputTag("akFlowPuCsSoftDropZ05B155PFImpactParameterTagInfos"),cms.InputTag("akFlowPuCsSoftDropZ05B155PFSecondaryVertexTagInfos")),
    jetIDMap = cms.InputTag("akFlowPuCsSoftDropZ05B155PFJetID"),
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

akFlowPuCsSoftDropZ05B155PFNjettiness = Njettiness.clone(
    src = cms.InputTag("akFlowPuCsSoftDropZ05B155PFJets"),
    R0  = cms.double(0.5)
    )

akFlowPuCsSoftDropZ05B155PFpatJetsWithBtagging.userData.userFloats.src += [
    'akFlowPuCsSoftDropZ05B155PFNjettiness:tau1',
    'akFlowPuCsSoftDropZ05B155PFNjettiness:tau2',
    'akFlowPuCsSoftDropZ05B155PFNjettiness:tau3']

akFlowPuCsSoftDropZ05B155PFJetAnalyzer = inclusiveJetAnalyzer.clone(
    jetTag = cms.InputTag("akFlowPuCsSoftDropZ05B155PFpatJetsWithBtagging"),
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
    bTagJetName = cms.untracked.string("akFlowPuCsSoftDropZ05B155PF"),
    jetName = cms.untracked.string("akFlowPuCsSoftDropZ05B155PF"),
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

akFlowPuCsSoftDropZ05B155PFJetSequence_mc = cms.Sequence(
    # akFlowPuCsSoftDropZ05B155PFclean
    # *
    akFlowPuCsSoftDropZ05B155PFmatch
    # *
    # akFlowPuCsSoftDropZ05B155PFmatchGroomed
    *
    akFlowPuCsSoftDropZ05B155PFparton
    *
    akFlowPuCsSoftDropZ05B155PFcorr
    # *
    # akFlowPuCsSoftDropZ05B155PFJetID
    *
    akFlowPuCsSoftDropZ05B155PFPatJetFlavourIdLegacy
    # *
    # akFlowPuCsSoftDropZ05B155PFPatJetFlavourId # Use legacy algo till PU implemented
    *
    akFlowPuCsSoftDropZ05B155PFJetTracksAssociatorAtVertex
    *
    akFlowPuCsSoftDropZ05B155PFJetBtagging
    *
    # No constituents for calo jets in pp. Must be removed for pp calo jets but
    # I'm not sure how to do this transparently (Marta)
    akFlowPuCsSoftDropZ05B155PFNjettiness
    *
    akFlowPuCsSoftDropZ05B155PFpatJetsWithBtagging
    *
    akFlowPuCsSoftDropZ05B155PFJetAnalyzer
    )

akFlowPuCsSoftDropZ05B155PFJetSequence_data = cms.Sequence(
    akFlowPuCsSoftDropZ05B155PFcorr
    *
    # akFlowPuCsSoftDropZ05B155PFJetID
    # *
    akFlowPuCsSoftDropZ05B155PFJetTracksAssociatorAtVertex
    *
    akFlowPuCsSoftDropZ05B155PFJetBtagging
    *
    akFlowPuCsSoftDropZ05B155PFNjettiness
    *
    akFlowPuCsSoftDropZ05B155PFpatJetsWithBtagging
    *
    akFlowPuCsSoftDropZ05B155PFJetAnalyzer
    )

akFlowPuCsSoftDropZ05B155PFJetSequence_mb = cms.Sequence(
    akFlowPuCsSoftDropZ05B155PFJetSequence_mc)
akFlowPuCsSoftDropZ05B155PFJetSequence_jec = cms.Sequence(
    akFlowPuCsSoftDropZ05B155PFJetSequence_mc)

akFlowPuCsSoftDropZ05B155PFJetSequence = cms.Sequence(
    akFlowPuCsSoftDropZ05B155PFJetSequence_mb)
akFlowPuCsSoftDropZ05B155PFpatJetsWithBtagging.userData.userFloats.src += ['akFlowPuCsSoftDropZ05B155PFJets:sym']
akFlowPuCsSoftDropZ05B155PFpatJetsWithBtagging.userData.userInts.src += ['akFlowPuCsSoftDropZ05B155PFJets:droppedBranches']
