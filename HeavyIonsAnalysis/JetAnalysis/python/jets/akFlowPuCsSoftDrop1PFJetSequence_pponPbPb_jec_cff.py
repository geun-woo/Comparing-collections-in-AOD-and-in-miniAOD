import FWCore.ParameterSet.Config as cms

from PhysicsTools.PatAlgos.mcMatchLayer0.jetMatch_cfi import patJetGenJetMatch, patJetPartonMatch
from PhysicsTools.PatAlgos.recoLayer0.jetCorrFactors_cfi import patJetCorrFactors
from PhysicsTools.PatAlgos.producersLayer1.jetProducer_cfi import patJets

from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *

from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akFlowPuCsSoftDrop1PFmatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akFlowPuCsSoftDrop1PFJets"),
    matched = cms.InputTag("ak1HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.1
    )

akFlowPuCsSoftDrop1PFmatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDrop1HiSignalGenJets"),
    matched = cms.InputTag("ak1HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.1
    )

akFlowPuCsSoftDrop1PFparton = patJetPartonMatch.clone(
    src = cms.InputTag("akFlowPuCsSoftDrop1PFJets"),
    matched = cms.InputTag("hiSignalGenParticles"))

akFlowPuCsSoftDrop1PFcorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
    levels   = cms.vstring('L2Relative'),
    src = cms.InputTag("akFlowPuCsSoftDrop1PFJets"),
    payload = "AK1PF"
    )

akFlowPuCsSoftDrop1PFJetID = cms.EDProducer(
    'JetIDProducer',
    JetIDParams,
    src = cms.InputTag('akFlowPuCsSoftDrop1CaloJets'))

# akFlowPuCsSoftDrop1PFclean = heavyIonCleanedGenJets.clone(
#     src = cms.InputTag('ak1HiSignalGenJets'))

akFlowPuCsSoftDrop1PFbTagger = bTaggers(
    "akFlowPuCsSoftDrop1PF",
    0.1)

# create objects locally since they dont load properly otherwise
akFlowPuCsSoftDrop1PFPatJetFlavourAssociationLegacy = akFlowPuCsSoftDrop1PFbTagger.PatJetFlavourAssociationLegacy
akFlowPuCsSoftDrop1PFPatJetPartons = akFlowPuCsSoftDrop1PFbTagger.PatJetPartons
akFlowPuCsSoftDrop1PFJetTracksAssociatorAtVertex = akFlowPuCsSoftDrop1PFbTagger.JetTracksAssociatorAtVertex
akFlowPuCsSoftDrop1PFJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akFlowPuCsSoftDrop1PFSimpleSecondaryVertexHighEffBJetTags = akFlowPuCsSoftDrop1PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akFlowPuCsSoftDrop1PFSimpleSecondaryVertexHighPurBJetTags = akFlowPuCsSoftDrop1PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akFlowPuCsSoftDrop1PFCombinedSecondaryVertexBJetTags = akFlowPuCsSoftDrop1PFbTagger.CombinedSecondaryVertexBJetTags
akFlowPuCsSoftDrop1PFCombinedSecondaryVertexV2BJetTags = akFlowPuCsSoftDrop1PFbTagger.CombinedSecondaryVertexV2BJetTags
akFlowPuCsSoftDrop1PFJetBProbabilityBJetTags = akFlowPuCsSoftDrop1PFbTagger.JetBProbabilityBJetTags
akFlowPuCsSoftDrop1PFSoftPFMuonByPtBJetTags = akFlowPuCsSoftDrop1PFbTagger.SoftPFMuonByPtBJetTags
akFlowPuCsSoftDrop1PFSoftPFMuonByIP3dBJetTags = akFlowPuCsSoftDrop1PFbTagger.SoftPFMuonByIP3dBJetTags
akFlowPuCsSoftDrop1PFTrackCountingHighEffBJetTags = akFlowPuCsSoftDrop1PFbTagger.TrackCountingHighEffBJetTags
akFlowPuCsSoftDrop1PFTrackCountingHighPurBJetTags = akFlowPuCsSoftDrop1PFbTagger.TrackCountingHighPurBJetTags
akFlowPuCsSoftDrop1PFPatJetPartonAssociationLegacy = akFlowPuCsSoftDrop1PFbTagger.PatJetPartonAssociationLegacy
akFlowPuCsSoftDrop1PFPatJetPartonAssociationLegacy.partons = "signalPartons"

akFlowPuCsSoftDrop1PFImpactParameterTagInfos = akFlowPuCsSoftDrop1PFbTagger.ImpactParameterTagInfos
akFlowPuCsSoftDrop1PFImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akFlowPuCsSoftDrop1PFJetProbabilityBJetTags = akFlowPuCsSoftDrop1PFbTagger.JetProbabilityBJetTags

akFlowPuCsSoftDrop1PFSecondaryVertexTagInfos = akFlowPuCsSoftDrop1PFbTagger.SecondaryVertexTagInfos
akFlowPuCsSoftDrop1PFSimpleSecondaryVertexHighEffBJetTags = akFlowPuCsSoftDrop1PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akFlowPuCsSoftDrop1PFSimpleSecondaryVertexHighPurBJetTags = akFlowPuCsSoftDrop1PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akFlowPuCsSoftDrop1PFCombinedSecondaryVertexBJetTags = akFlowPuCsSoftDrop1PFbTagger.CombinedSecondaryVertexBJetTags
akFlowPuCsSoftDrop1PFCombinedSecondaryVertexV2BJetTags = akFlowPuCsSoftDrop1PFbTagger.CombinedSecondaryVertexV2BJetTags

akFlowPuCsSoftDrop1PFSecondaryVertexNegativeTagInfos = akFlowPuCsSoftDrop1PFbTagger.SecondaryVertexNegativeTagInfos
akFlowPuCsSoftDrop1PFNegativeSimpleSecondaryVertexHighEffBJetTags = akFlowPuCsSoftDrop1PFbTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akFlowPuCsSoftDrop1PFNegativeSimpleSecondaryVertexHighPurBJetTags = akFlowPuCsSoftDrop1PFbTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akFlowPuCsSoftDrop1PFNegativeCombinedSecondaryVertexBJetTags = akFlowPuCsSoftDrop1PFbTagger.NegativeCombinedSecondaryVertexBJetTags
akFlowPuCsSoftDrop1PFPositiveCombinedSecondaryVertexBJetTags = akFlowPuCsSoftDrop1PFbTagger.PositiveCombinedSecondaryVertexBJetTags
akFlowPuCsSoftDrop1PFNegativeCombinedSecondaryVertexV2BJetTags = akFlowPuCsSoftDrop1PFbTagger.NegativeCombinedSecondaryVertexV2BJetTags
akFlowPuCsSoftDrop1PFPositiveCombinedSecondaryVertexV2BJetTags = akFlowPuCsSoftDrop1PFbTagger.PositiveCombinedSecondaryVertexV2BJetTags

akFlowPuCsSoftDrop1PFSoftPFMuonsTagInfos = akFlowPuCsSoftDrop1PFbTagger.SoftPFMuonsTagInfos
akFlowPuCsSoftDrop1PFSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akFlowPuCsSoftDrop1PFSoftPFMuonBJetTags = akFlowPuCsSoftDrop1PFbTagger.SoftPFMuonBJetTags
akFlowPuCsSoftDrop1PFSoftPFMuonByIP3dBJetTags = akFlowPuCsSoftDrop1PFbTagger.SoftPFMuonByIP3dBJetTags
akFlowPuCsSoftDrop1PFSoftPFMuonByPtBJetTags = akFlowPuCsSoftDrop1PFbTagger.SoftPFMuonByPtBJetTags
akFlowPuCsSoftDrop1PFNegativeSoftPFMuonByPtBJetTags = akFlowPuCsSoftDrop1PFbTagger.NegativeSoftPFMuonByPtBJetTags
akFlowPuCsSoftDrop1PFPositiveSoftPFMuonByPtBJetTags = akFlowPuCsSoftDrop1PFbTagger.PositiveSoftPFMuonByPtBJetTags
akFlowPuCsSoftDrop1PFPatJetFlavourIdLegacy = cms.Sequence(akFlowPuCsSoftDrop1PFPatJetPartonAssociationLegacy*akFlowPuCsSoftDrop1PFPatJetFlavourAssociationLegacy)
# Not working with our PU sub, but keep it here for reference
# akFlowPuCsSoftDrop1PFPatJetFlavourAssociation = akFlowPuCsSoftDrop1PFbTagger.PatJetFlavourAssociation
# akFlowPuCsSoftDrop1PFPatJetFlavourId = cms.Sequence(akFlowPuCsSoftDrop1PFPatJetPartons*akFlowPuCsSoftDrop1PFPatJetFlavourAssociation)

akFlowPuCsSoftDrop1PFJetBtaggingIP = cms.Sequence(
    akFlowPuCsSoftDrop1PFImpactParameterTagInfos *
    akFlowPuCsSoftDrop1PFTrackCountingHighEffBJetTags +
    akFlowPuCsSoftDrop1PFTrackCountingHighPurBJetTags +
    akFlowPuCsSoftDrop1PFJetProbabilityBJetTags +
    akFlowPuCsSoftDrop1PFJetBProbabilityBJetTags
    )

akFlowPuCsSoftDrop1PFJetBtaggingSV = cms.Sequence(
    akFlowPuCsSoftDrop1PFImpactParameterTagInfos *
    akFlowPuCsSoftDrop1PFSecondaryVertexTagInfos *
    akFlowPuCsSoftDrop1PFSimpleSecondaryVertexHighEffBJetTags +
    akFlowPuCsSoftDrop1PFSimpleSecondaryVertexHighPurBJetTags +
    akFlowPuCsSoftDrop1PFCombinedSecondaryVertexBJetTags +
    akFlowPuCsSoftDrop1PFCombinedSecondaryVertexV2BJetTags
    )

akFlowPuCsSoftDrop1PFJetBtaggingNegSV = cms.Sequence(
    akFlowPuCsSoftDrop1PFImpactParameterTagInfos *
    akFlowPuCsSoftDrop1PFSecondaryVertexNegativeTagInfos *
    akFlowPuCsSoftDrop1PFNegativeSimpleSecondaryVertexHighEffBJetTags +
    akFlowPuCsSoftDrop1PFNegativeSimpleSecondaryVertexHighPurBJetTags +
    akFlowPuCsSoftDrop1PFNegativeCombinedSecondaryVertexBJetTags +
    akFlowPuCsSoftDrop1PFPositiveCombinedSecondaryVertexBJetTags +
    akFlowPuCsSoftDrop1PFNegativeCombinedSecondaryVertexV2BJetTags +
    akFlowPuCsSoftDrop1PFPositiveCombinedSecondaryVertexV2BJetTags
    )

akFlowPuCsSoftDrop1PFJetBtaggingMu = cms.Sequence(
    akFlowPuCsSoftDrop1PFSoftPFMuonsTagInfos *
    akFlowPuCsSoftDrop1PFSoftPFMuonBJetTags +
    akFlowPuCsSoftDrop1PFSoftPFMuonByIP3dBJetTags +
    akFlowPuCsSoftDrop1PFSoftPFMuonByPtBJetTags +
    akFlowPuCsSoftDrop1PFNegativeSoftPFMuonByPtBJetTags +
    akFlowPuCsSoftDrop1PFPositiveSoftPFMuonByPtBJetTags
    )

akFlowPuCsSoftDrop1PFJetBtagging = cms.Sequence(
    akFlowPuCsSoftDrop1PFJetBtaggingIP
    * akFlowPuCsSoftDrop1PFJetBtaggingSV
    # * akFlowPuCsSoftDrop1PFJetBtaggingNegSV
    # * akFlowPuCsSoftDrop1PFJetBtaggingMu
    )

akFlowPuCsSoftDrop1PFpatJetsWithBtagging = patJets.clone(
    jetSource = cms.InputTag("akFlowPuCsSoftDrop1PFJets"),
    genJetMatch            = cms.InputTag("akFlowPuCsSoftDrop1PFmatch"),
    genPartonMatch         = cms.InputTag("akFlowPuCsSoftDrop1PFparton"),
    jetCorrFactorsSource   = cms.VInputTag(cms.InputTag("akFlowPuCsSoftDrop1PFcorr")),
    JetPartonMapSource     = cms.InputTag("akFlowPuCsSoftDrop1PFPatJetFlavourAssociationLegacy"),
    JetFlavourInfoSource   = cms.InputTag("akFlowPuCsSoftDrop1PFPatJetFlavourAssociation"),
    trackAssociationSource = cms.InputTag("akFlowPuCsSoftDrop1PFJetTracksAssociatorAtVertex"),
    useLegacyJetMCFlavour  = True,
    discriminatorSources   = cms.VInputTag(
        cms.InputTag("akFlowPuCsSoftDrop1PFSimpleSecondaryVertexHighEffBJetTags"),
        cms.InputTag("akFlowPuCsSoftDrop1PFSimpleSecondaryVertexHighPurBJetTags"),
        cms.InputTag("akFlowPuCsSoftDrop1PFCombinedSecondaryVertexBJetTags"),
        cms.InputTag("akFlowPuCsSoftDrop1PFCombinedSecondaryVertexV2BJetTags"),
        cms.InputTag("akFlowPuCsSoftDrop1PFJetBProbabilityBJetTags"),
        cms.InputTag("akFlowPuCsSoftDrop1PFJetProbabilityBJetTags"),
        # cms.InputTag("akFlowPuCsSoftDrop1PFSoftPFMuonByPtBJetTags"),
        # cms.InputTag("akFlowPuCsSoftDrop1PFSoftPFMuonByIP3dBJetTags"),
        cms.InputTag("akFlowPuCsSoftDrop1PFTrackCountingHighEffBJetTags"),
        cms.InputTag("akFlowPuCsSoftDrop1PFTrackCountingHighPurBJetTags"),
        ),
    tagInfoSources = cms.VInputTag(cms.InputTag("akFlowPuCsSoftDrop1PFImpactParameterTagInfos"),cms.InputTag("akFlowPuCsSoftDrop1PFSecondaryVertexTagInfos")),
    jetIDMap = cms.InputTag("akFlowPuCsSoftDrop1PFJetID"),
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

akFlowPuCsSoftDrop1PFNjettiness = Njettiness.clone(
    src = cms.InputTag("akFlowPuCsSoftDrop1PFJets"),
    R0  = cms.double(0.1)
    )

akFlowPuCsSoftDrop1PFpatJetsWithBtagging.userData.userFloats.src += [
    'akFlowPuCsSoftDrop1PFNjettiness:tau1',
    'akFlowPuCsSoftDrop1PFNjettiness:tau2',
    'akFlowPuCsSoftDrop1PFNjettiness:tau3']

akFlowPuCsSoftDrop1PFJetAnalyzer = inclusiveJetAnalyzer.clone(
    jetTag = cms.InputTag("akFlowPuCsSoftDrop1PFpatJetsWithBtagging"),
    genjetTag = 'ak1HiSignalGenJets',
    rParam = 0.1,
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
    bTagJetName = cms.untracked.string("akFlowPuCsSoftDrop1PF"),
    jetName = cms.untracked.string("akFlowPuCsSoftDrop1PF"),
    genPtMin = cms.untracked.double(5),
    hltTrgResults = cms.untracked.string('TriggerResults::'+'HISIGNAL'),
    doTower = cms.untracked.bool(False),
    doSubJets = cms.untracked.bool(True),
    doGenSubJets = cms.untracked.bool(False),
    subjetGenTag = cms.untracked.InputTag("akSoftDrop1GenJets"),
    doGenTaus = cms.untracked.bool(False),
    genTau1 = cms.InputTag("akSoftDrop1HiGenNjettiness","tau1"),
    genTau2 = cms.InputTag("akSoftDrop1HiGenNjettiness","tau2"),
    genTau3 = cms.InputTag("akSoftDrop1HiGenNjettiness","tau3"),
    doGenSym = cms.untracked.bool(False),
    genSym = cms.InputTag("akSoftDrop1GenJets","sym"),
    genDroppedBranches = cms.InputTag("akSoftDrop1GenJets","droppedBranches")
    )

akFlowPuCsSoftDrop1PFJetSequence_mc = cms.Sequence(
    # akFlowPuCsSoftDrop1PFclean
    # *
    akFlowPuCsSoftDrop1PFmatch
    # *
    # akFlowPuCsSoftDrop1PFmatchGroomed
    *
    akFlowPuCsSoftDrop1PFparton
    *
    akFlowPuCsSoftDrop1PFcorr
    # *
    # akFlowPuCsSoftDrop1PFJetID
    *
    akFlowPuCsSoftDrop1PFPatJetFlavourIdLegacy
    # *
    # akFlowPuCsSoftDrop1PFPatJetFlavourId # Use legacy algo till PU implemented
    *
    akFlowPuCsSoftDrop1PFJetTracksAssociatorAtVertex
    *
    akFlowPuCsSoftDrop1PFJetBtagging
    *
    # No constituents for calo jets in pp. Must be removed for pp calo jets but
    # I'm not sure how to do this transparently (Marta)
    akFlowPuCsSoftDrop1PFNjettiness
    *
    akFlowPuCsSoftDrop1PFpatJetsWithBtagging
    *
    akFlowPuCsSoftDrop1PFJetAnalyzer
    )

akFlowPuCsSoftDrop1PFJetSequence_data = cms.Sequence(
    akFlowPuCsSoftDrop1PFcorr
    *
    # akFlowPuCsSoftDrop1PFJetID
    # *
    akFlowPuCsSoftDrop1PFJetTracksAssociatorAtVertex
    *
    akFlowPuCsSoftDrop1PFJetBtagging
    *
    akFlowPuCsSoftDrop1PFNjettiness
    *
    akFlowPuCsSoftDrop1PFpatJetsWithBtagging
    *
    akFlowPuCsSoftDrop1PFJetAnalyzer
    )

akFlowPuCsSoftDrop1PFJetSequence_mb = cms.Sequence(
    akFlowPuCsSoftDrop1PFJetSequence_mc)
akFlowPuCsSoftDrop1PFJetSequence_jec = cms.Sequence(
    akFlowPuCsSoftDrop1PFJetSequence_mc)

akFlowPuCsSoftDrop1PFJetSequence = cms.Sequence(
    akFlowPuCsSoftDrop1PFJetSequence_jec)
akFlowPuCsSoftDrop1PFJetAnalyzer.genPtMin = cms.untracked.double(1)
akFlowPuCsSoftDrop1PFJetAnalyzer.jetPtMin = cms.double(1)
akFlowPuCsSoftDrop1PFpatJetsWithBtagging.userData.userFloats.src += ['akFlowPuCsSoftDrop1PFJets:sym']
akFlowPuCsSoftDrop1PFpatJetsWithBtagging.userData.userInts.src += ['akFlowPuCsSoftDrop1PFJets:droppedBranches']
