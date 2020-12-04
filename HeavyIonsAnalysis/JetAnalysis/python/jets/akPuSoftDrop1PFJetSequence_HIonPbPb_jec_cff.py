import FWCore.ParameterSet.Config as cms

from PhysicsTools.PatAlgos.mcMatchLayer0.jetMatch_cfi import patJetGenJetMatch, patJetPartonMatch
from PhysicsTools.PatAlgos.recoLayer0.jetCorrFactors_cfi import patJetCorrFactors
from PhysicsTools.PatAlgos.producersLayer1.jetProducer_cfi import patJets

from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *

from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akPuSoftDrop1PFmatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akPuSoftDrop1PFJets"),
    matched = cms.InputTag("ak1HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.1
    )

akPuSoftDrop1PFmatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDrop1HiSignalGenJets"),
    matched = cms.InputTag("ak1HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.1
    )

akPuSoftDrop1PFparton = patJetPartonMatch.clone(
    src = cms.InputTag("akPuSoftDrop1PFJets"),
    matched = cms.InputTag("hiSignalGenParticles"))

akPuSoftDrop1PFcorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
    levels   = cms.vstring('L2Relative'),
    src = cms.InputTag("akPuSoftDrop1PFJets"),
    payload = "AKPu1PF_offline"
    )

akPuSoftDrop1PFJetID = cms.EDProducer(
    'JetIDProducer',
    JetIDParams,
    src = cms.InputTag('akPuSoftDrop1CaloJets'))

# akPuSoftDrop1PFclean = heavyIonCleanedGenJets.clone(
#     src = cms.InputTag('ak1HiSignalGenJets'))

akPuSoftDrop1PFbTagger = bTaggers(
    "akPuSoftDrop1PF",
    0.1)

# create objects locally since they dont load properly otherwise
akPuSoftDrop1PFPatJetFlavourAssociationLegacy = akPuSoftDrop1PFbTagger.PatJetFlavourAssociationLegacy
akPuSoftDrop1PFPatJetPartons = akPuSoftDrop1PFbTagger.PatJetPartons
akPuSoftDrop1PFJetTracksAssociatorAtVertex = akPuSoftDrop1PFbTagger.JetTracksAssociatorAtVertex
akPuSoftDrop1PFJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akPuSoftDrop1PFSimpleSecondaryVertexHighEffBJetTags = akPuSoftDrop1PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akPuSoftDrop1PFSimpleSecondaryVertexHighPurBJetTags = akPuSoftDrop1PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akPuSoftDrop1PFCombinedSecondaryVertexBJetTags = akPuSoftDrop1PFbTagger.CombinedSecondaryVertexBJetTags
akPuSoftDrop1PFCombinedSecondaryVertexV2BJetTags = akPuSoftDrop1PFbTagger.CombinedSecondaryVertexV2BJetTags
akPuSoftDrop1PFJetBProbabilityBJetTags = akPuSoftDrop1PFbTagger.JetBProbabilityBJetTags
akPuSoftDrop1PFSoftPFMuonByPtBJetTags = akPuSoftDrop1PFbTagger.SoftPFMuonByPtBJetTags
akPuSoftDrop1PFSoftPFMuonByIP3dBJetTags = akPuSoftDrop1PFbTagger.SoftPFMuonByIP3dBJetTags
akPuSoftDrop1PFTrackCountingHighEffBJetTags = akPuSoftDrop1PFbTagger.TrackCountingHighEffBJetTags
akPuSoftDrop1PFTrackCountingHighPurBJetTags = akPuSoftDrop1PFbTagger.TrackCountingHighPurBJetTags
akPuSoftDrop1PFPatJetPartonAssociationLegacy = akPuSoftDrop1PFbTagger.PatJetPartonAssociationLegacy
akPuSoftDrop1PFPatJetPartonAssociationLegacy.partons = "signalPartons"

akPuSoftDrop1PFImpactParameterTagInfos = akPuSoftDrop1PFbTagger.ImpactParameterTagInfos
akPuSoftDrop1PFImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akPuSoftDrop1PFJetProbabilityBJetTags = akPuSoftDrop1PFbTagger.JetProbabilityBJetTags

akPuSoftDrop1PFSecondaryVertexTagInfos = akPuSoftDrop1PFbTagger.SecondaryVertexTagInfos
akPuSoftDrop1PFSimpleSecondaryVertexHighEffBJetTags = akPuSoftDrop1PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akPuSoftDrop1PFSimpleSecondaryVertexHighPurBJetTags = akPuSoftDrop1PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akPuSoftDrop1PFCombinedSecondaryVertexBJetTags = akPuSoftDrop1PFbTagger.CombinedSecondaryVertexBJetTags
akPuSoftDrop1PFCombinedSecondaryVertexV2BJetTags = akPuSoftDrop1PFbTagger.CombinedSecondaryVertexV2BJetTags

akPuSoftDrop1PFSecondaryVertexNegativeTagInfos = akPuSoftDrop1PFbTagger.SecondaryVertexNegativeTagInfos
akPuSoftDrop1PFNegativeSimpleSecondaryVertexHighEffBJetTags = akPuSoftDrop1PFbTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akPuSoftDrop1PFNegativeSimpleSecondaryVertexHighPurBJetTags = akPuSoftDrop1PFbTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akPuSoftDrop1PFNegativeCombinedSecondaryVertexBJetTags = akPuSoftDrop1PFbTagger.NegativeCombinedSecondaryVertexBJetTags
akPuSoftDrop1PFPositiveCombinedSecondaryVertexBJetTags = akPuSoftDrop1PFbTagger.PositiveCombinedSecondaryVertexBJetTags
akPuSoftDrop1PFNegativeCombinedSecondaryVertexV2BJetTags = akPuSoftDrop1PFbTagger.NegativeCombinedSecondaryVertexV2BJetTags
akPuSoftDrop1PFPositiveCombinedSecondaryVertexV2BJetTags = akPuSoftDrop1PFbTagger.PositiveCombinedSecondaryVertexV2BJetTags

akPuSoftDrop1PFSoftPFMuonsTagInfos = akPuSoftDrop1PFbTagger.SoftPFMuonsTagInfos
akPuSoftDrop1PFSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akPuSoftDrop1PFSoftPFMuonBJetTags = akPuSoftDrop1PFbTagger.SoftPFMuonBJetTags
akPuSoftDrop1PFSoftPFMuonByIP3dBJetTags = akPuSoftDrop1PFbTagger.SoftPFMuonByIP3dBJetTags
akPuSoftDrop1PFSoftPFMuonByPtBJetTags = akPuSoftDrop1PFbTagger.SoftPFMuonByPtBJetTags
akPuSoftDrop1PFNegativeSoftPFMuonByPtBJetTags = akPuSoftDrop1PFbTagger.NegativeSoftPFMuonByPtBJetTags
akPuSoftDrop1PFPositiveSoftPFMuonByPtBJetTags = akPuSoftDrop1PFbTagger.PositiveSoftPFMuonByPtBJetTags
akPuSoftDrop1PFPatJetFlavourIdLegacy = cms.Sequence(akPuSoftDrop1PFPatJetPartonAssociationLegacy*akPuSoftDrop1PFPatJetFlavourAssociationLegacy)
# Not working with our PU sub, but keep it here for reference
# akPuSoftDrop1PFPatJetFlavourAssociation = akPuSoftDrop1PFbTagger.PatJetFlavourAssociation
# akPuSoftDrop1PFPatJetFlavourId = cms.Sequence(akPuSoftDrop1PFPatJetPartons*akPuSoftDrop1PFPatJetFlavourAssociation)

akPuSoftDrop1PFJetBtaggingIP = cms.Sequence(
    akPuSoftDrop1PFImpactParameterTagInfos *
    akPuSoftDrop1PFTrackCountingHighEffBJetTags +
    akPuSoftDrop1PFTrackCountingHighPurBJetTags +
    akPuSoftDrop1PFJetProbabilityBJetTags +
    akPuSoftDrop1PFJetBProbabilityBJetTags
    )

akPuSoftDrop1PFJetBtaggingSV = cms.Sequence(
    akPuSoftDrop1PFImpactParameterTagInfos *
    akPuSoftDrop1PFSecondaryVertexTagInfos *
    akPuSoftDrop1PFSimpleSecondaryVertexHighEffBJetTags +
    akPuSoftDrop1PFSimpleSecondaryVertexHighPurBJetTags +
    akPuSoftDrop1PFCombinedSecondaryVertexBJetTags +
    akPuSoftDrop1PFCombinedSecondaryVertexV2BJetTags
    )

akPuSoftDrop1PFJetBtaggingNegSV = cms.Sequence(
    akPuSoftDrop1PFImpactParameterTagInfos *
    akPuSoftDrop1PFSecondaryVertexNegativeTagInfos *
    akPuSoftDrop1PFNegativeSimpleSecondaryVertexHighEffBJetTags +
    akPuSoftDrop1PFNegativeSimpleSecondaryVertexHighPurBJetTags +
    akPuSoftDrop1PFNegativeCombinedSecondaryVertexBJetTags +
    akPuSoftDrop1PFPositiveCombinedSecondaryVertexBJetTags +
    akPuSoftDrop1PFNegativeCombinedSecondaryVertexV2BJetTags +
    akPuSoftDrop1PFPositiveCombinedSecondaryVertexV2BJetTags
    )

akPuSoftDrop1PFJetBtaggingMu = cms.Sequence(
    akPuSoftDrop1PFSoftPFMuonsTagInfos *
    akPuSoftDrop1PFSoftPFMuonBJetTags +
    akPuSoftDrop1PFSoftPFMuonByIP3dBJetTags +
    akPuSoftDrop1PFSoftPFMuonByPtBJetTags +
    akPuSoftDrop1PFNegativeSoftPFMuonByPtBJetTags +
    akPuSoftDrop1PFPositiveSoftPFMuonByPtBJetTags
    )

akPuSoftDrop1PFJetBtagging = cms.Sequence(
    akPuSoftDrop1PFJetBtaggingIP
    * akPuSoftDrop1PFJetBtaggingSV
    # * akPuSoftDrop1PFJetBtaggingNegSV
    # * akPuSoftDrop1PFJetBtaggingMu
    )

akPuSoftDrop1PFpatJetsWithBtagging = patJets.clone(
    jetSource = cms.InputTag("akPuSoftDrop1PFJets"),
    genJetMatch            = cms.InputTag("akPuSoftDrop1PFmatch"),
    genPartonMatch         = cms.InputTag("akPuSoftDrop1PFparton"),
    jetCorrFactorsSource   = cms.VInputTag(cms.InputTag("akPuSoftDrop1PFcorr")),
    JetPartonMapSource     = cms.InputTag("akPuSoftDrop1PFPatJetFlavourAssociationLegacy"),
    JetFlavourInfoSource   = cms.InputTag("akPuSoftDrop1PFPatJetFlavourAssociation"),
    trackAssociationSource = cms.InputTag("akPuSoftDrop1PFJetTracksAssociatorAtVertex"),
    useLegacyJetMCFlavour  = True,
    discriminatorSources   = cms.VInputTag(
        cms.InputTag("akPuSoftDrop1PFSimpleSecondaryVertexHighEffBJetTags"),
        cms.InputTag("akPuSoftDrop1PFSimpleSecondaryVertexHighPurBJetTags"),
        cms.InputTag("akPuSoftDrop1PFCombinedSecondaryVertexBJetTags"),
        cms.InputTag("akPuSoftDrop1PFCombinedSecondaryVertexV2BJetTags"),
        cms.InputTag("akPuSoftDrop1PFJetBProbabilityBJetTags"),
        cms.InputTag("akPuSoftDrop1PFJetProbabilityBJetTags"),
        # cms.InputTag("akPuSoftDrop1PFSoftPFMuonByPtBJetTags"),
        # cms.InputTag("akPuSoftDrop1PFSoftPFMuonByIP3dBJetTags"),
        cms.InputTag("akPuSoftDrop1PFTrackCountingHighEffBJetTags"),
        cms.InputTag("akPuSoftDrop1PFTrackCountingHighPurBJetTags"),
        ),
    tagInfoSources = cms.VInputTag(cms.InputTag("akPuSoftDrop1PFImpactParameterTagInfos"),cms.InputTag("akPuSoftDrop1PFSecondaryVertexTagInfos")),
    jetIDMap = cms.InputTag("akPuSoftDrop1PFJetID"),
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

akPuSoftDrop1PFNjettiness = Njettiness.clone(
    src = cms.InputTag("akPuSoftDrop1PFJets"),
    R0  = cms.double(0.1)
    )

akPuSoftDrop1PFpatJetsWithBtagging.userData.userFloats.src += [
    'akPuSoftDrop1PFNjettiness:tau1',
    'akPuSoftDrop1PFNjettiness:tau2',
    'akPuSoftDrop1PFNjettiness:tau3']

akPuSoftDrop1PFJetAnalyzer = inclusiveJetAnalyzer.clone(
    jetTag = cms.InputTag("akPuSoftDrop1PFpatJetsWithBtagging"),
    genjetTag = 'ak1HiSignalGenJets',
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
    bTagJetName = cms.untracked.string("akPuSoftDrop1PF"),
    jetName = cms.untracked.string("akPuSoftDrop1PF"),
    genPtMin = cms.untracked.double(5),
    hltTrgResults = cms.untracked.string('TriggerResults::'+'HISIGNAL'),
    doTower = cms.untracked.bool(True),
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

akPuSoftDrop1PFJetSequence_mc = cms.Sequence(
    # akPuSoftDrop1PFclean
    # *
    akPuSoftDrop1PFmatch
    # *
    # akPuSoftDrop1PFmatchGroomed
    *
    akPuSoftDrop1PFparton
    *
    akPuSoftDrop1PFcorr
    # *
    # akPuSoftDrop1PFJetID
    *
    akPuSoftDrop1PFPatJetFlavourIdLegacy
    # *
    # akPuSoftDrop1PFPatJetFlavourId # Use legacy algo till PU implemented
    *
    akPuSoftDrop1PFJetTracksAssociatorAtVertex
    *
    akPuSoftDrop1PFJetBtagging
    *
    # No constituents for calo jets in pp. Must be removed for pp calo jets but
    # I'm not sure how to do this transparently (Marta)
    akPuSoftDrop1PFNjettiness
    *
    akPuSoftDrop1PFpatJetsWithBtagging
    *
    akPuSoftDrop1PFJetAnalyzer
    )

akPuSoftDrop1PFJetSequence_data = cms.Sequence(
    akPuSoftDrop1PFcorr
    *
    # akPuSoftDrop1PFJetID
    # *
    akPuSoftDrop1PFJetTracksAssociatorAtVertex
    *
    akPuSoftDrop1PFJetBtagging
    *
    akPuSoftDrop1PFNjettiness
    *
    akPuSoftDrop1PFpatJetsWithBtagging
    *
    akPuSoftDrop1PFJetAnalyzer
    )

akPuSoftDrop1PFJetSequence_mb = cms.Sequence(
    akPuSoftDrop1PFJetSequence_mc)
akPuSoftDrop1PFJetSequence_jec = cms.Sequence(
    akPuSoftDrop1PFJetSequence_mc)

akPuSoftDrop1PFJetSequence = cms.Sequence(
    akPuSoftDrop1PFJetSequence_jec)
akPuSoftDrop1PFJetAnalyzer.genPtMin = cms.untracked.double(1)
akPuSoftDrop1PFJetAnalyzer.jetPtMin = cms.double(1)
akPuSoftDrop1PFpatJetsWithBtagging.userData.userFloats.src += ['akPuSoftDrop1PFJets:sym']
akPuSoftDrop1PFpatJetsWithBtagging.userData.userInts.src += ['akPuSoftDrop1PFJets:droppedBranches']
