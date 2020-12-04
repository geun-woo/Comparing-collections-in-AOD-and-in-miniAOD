import FWCore.ParameterSet.Config as cms

from PhysicsTools.PatAlgos.mcMatchLayer0.jetMatch_cfi import patJetGenJetMatch, patJetPartonMatch
from PhysicsTools.PatAlgos.recoLayer0.jetCorrFactors_cfi import patJetCorrFactors
from PhysicsTools.PatAlgos.producersLayer1.jetProducer_cfi import patJets

from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *

from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akFlowPuCsSoftDrop5PFmatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akFlowPuCsSoftDrop5PFJets"),
    matched = cms.InputTag("ak5HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.5
    )

akFlowPuCsSoftDrop5PFmatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDrop5HiSignalGenJets"),
    matched = cms.InputTag("ak5HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.5
    )

akFlowPuCsSoftDrop5PFparton = patJetPartonMatch.clone(
    src = cms.InputTag("akFlowPuCsSoftDrop5PFJets"),
    matched = cms.InputTag("hiSignalGenParticles"))

akFlowPuCsSoftDrop5PFcorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
    levels   = cms.vstring('L2Relative'),
    src = cms.InputTag("akFlowPuCsSoftDrop5PFJets"),
    payload = "AK5PF"
    )

akFlowPuCsSoftDrop5PFJetID = cms.EDProducer(
    'JetIDProducer',
    JetIDParams,
    src = cms.InputTag('akFlowPuCsSoftDrop5CaloJets'))

# akFlowPuCsSoftDrop5PFclean = heavyIonCleanedGenJets.clone(
#     src = cms.InputTag('ak5HiSignalGenJets'))

akFlowPuCsSoftDrop5PFbTagger = bTaggers(
    "akFlowPuCsSoftDrop5PF",
    0.5)

# create objects locally since they dont load properly otherwise
akFlowPuCsSoftDrop5PFPatJetFlavourAssociationLegacy = akFlowPuCsSoftDrop5PFbTagger.PatJetFlavourAssociationLegacy
akFlowPuCsSoftDrop5PFPatJetPartons = akFlowPuCsSoftDrop5PFbTagger.PatJetPartons
akFlowPuCsSoftDrop5PFJetTracksAssociatorAtVertex = akFlowPuCsSoftDrop5PFbTagger.JetTracksAssociatorAtVertex
akFlowPuCsSoftDrop5PFJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akFlowPuCsSoftDrop5PFSimpleSecondaryVertexHighEffBJetTags = akFlowPuCsSoftDrop5PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akFlowPuCsSoftDrop5PFSimpleSecondaryVertexHighPurBJetTags = akFlowPuCsSoftDrop5PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akFlowPuCsSoftDrop5PFCombinedSecondaryVertexBJetTags = akFlowPuCsSoftDrop5PFbTagger.CombinedSecondaryVertexBJetTags
akFlowPuCsSoftDrop5PFCombinedSecondaryVertexV2BJetTags = akFlowPuCsSoftDrop5PFbTagger.CombinedSecondaryVertexV2BJetTags
akFlowPuCsSoftDrop5PFJetBProbabilityBJetTags = akFlowPuCsSoftDrop5PFbTagger.JetBProbabilityBJetTags
akFlowPuCsSoftDrop5PFSoftPFMuonByPtBJetTags = akFlowPuCsSoftDrop5PFbTagger.SoftPFMuonByPtBJetTags
akFlowPuCsSoftDrop5PFSoftPFMuonByIP3dBJetTags = akFlowPuCsSoftDrop5PFbTagger.SoftPFMuonByIP3dBJetTags
akFlowPuCsSoftDrop5PFTrackCountingHighEffBJetTags = akFlowPuCsSoftDrop5PFbTagger.TrackCountingHighEffBJetTags
akFlowPuCsSoftDrop5PFTrackCountingHighPurBJetTags = akFlowPuCsSoftDrop5PFbTagger.TrackCountingHighPurBJetTags
akFlowPuCsSoftDrop5PFPatJetPartonAssociationLegacy = akFlowPuCsSoftDrop5PFbTagger.PatJetPartonAssociationLegacy
akFlowPuCsSoftDrop5PFPatJetPartonAssociationLegacy.partons = "signalPartons"

akFlowPuCsSoftDrop5PFImpactParameterTagInfos = akFlowPuCsSoftDrop5PFbTagger.ImpactParameterTagInfos
akFlowPuCsSoftDrop5PFImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akFlowPuCsSoftDrop5PFJetProbabilityBJetTags = akFlowPuCsSoftDrop5PFbTagger.JetProbabilityBJetTags

akFlowPuCsSoftDrop5PFSecondaryVertexTagInfos = akFlowPuCsSoftDrop5PFbTagger.SecondaryVertexTagInfos
akFlowPuCsSoftDrop5PFSimpleSecondaryVertexHighEffBJetTags = akFlowPuCsSoftDrop5PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akFlowPuCsSoftDrop5PFSimpleSecondaryVertexHighPurBJetTags = akFlowPuCsSoftDrop5PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akFlowPuCsSoftDrop5PFCombinedSecondaryVertexBJetTags = akFlowPuCsSoftDrop5PFbTagger.CombinedSecondaryVertexBJetTags
akFlowPuCsSoftDrop5PFCombinedSecondaryVertexV2BJetTags = akFlowPuCsSoftDrop5PFbTagger.CombinedSecondaryVertexV2BJetTags

akFlowPuCsSoftDrop5PFSecondaryVertexNegativeTagInfos = akFlowPuCsSoftDrop5PFbTagger.SecondaryVertexNegativeTagInfos
akFlowPuCsSoftDrop5PFNegativeSimpleSecondaryVertexHighEffBJetTags = akFlowPuCsSoftDrop5PFbTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akFlowPuCsSoftDrop5PFNegativeSimpleSecondaryVertexHighPurBJetTags = akFlowPuCsSoftDrop5PFbTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akFlowPuCsSoftDrop5PFNegativeCombinedSecondaryVertexBJetTags = akFlowPuCsSoftDrop5PFbTagger.NegativeCombinedSecondaryVertexBJetTags
akFlowPuCsSoftDrop5PFPositiveCombinedSecondaryVertexBJetTags = akFlowPuCsSoftDrop5PFbTagger.PositiveCombinedSecondaryVertexBJetTags
akFlowPuCsSoftDrop5PFNegativeCombinedSecondaryVertexV2BJetTags = akFlowPuCsSoftDrop5PFbTagger.NegativeCombinedSecondaryVertexV2BJetTags
akFlowPuCsSoftDrop5PFPositiveCombinedSecondaryVertexV2BJetTags = akFlowPuCsSoftDrop5PFbTagger.PositiveCombinedSecondaryVertexV2BJetTags

akFlowPuCsSoftDrop5PFSoftPFMuonsTagInfos = akFlowPuCsSoftDrop5PFbTagger.SoftPFMuonsTagInfos
akFlowPuCsSoftDrop5PFSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akFlowPuCsSoftDrop5PFSoftPFMuonBJetTags = akFlowPuCsSoftDrop5PFbTagger.SoftPFMuonBJetTags
akFlowPuCsSoftDrop5PFSoftPFMuonByIP3dBJetTags = akFlowPuCsSoftDrop5PFbTagger.SoftPFMuonByIP3dBJetTags
akFlowPuCsSoftDrop5PFSoftPFMuonByPtBJetTags = akFlowPuCsSoftDrop5PFbTagger.SoftPFMuonByPtBJetTags
akFlowPuCsSoftDrop5PFNegativeSoftPFMuonByPtBJetTags = akFlowPuCsSoftDrop5PFbTagger.NegativeSoftPFMuonByPtBJetTags
akFlowPuCsSoftDrop5PFPositiveSoftPFMuonByPtBJetTags = akFlowPuCsSoftDrop5PFbTagger.PositiveSoftPFMuonByPtBJetTags
akFlowPuCsSoftDrop5PFPatJetFlavourIdLegacy = cms.Sequence(akFlowPuCsSoftDrop5PFPatJetPartonAssociationLegacy*akFlowPuCsSoftDrop5PFPatJetFlavourAssociationLegacy)
# Not working with our PU sub, but keep it here for reference
# akFlowPuCsSoftDrop5PFPatJetFlavourAssociation = akFlowPuCsSoftDrop5PFbTagger.PatJetFlavourAssociation
# akFlowPuCsSoftDrop5PFPatJetFlavourId = cms.Sequence(akFlowPuCsSoftDrop5PFPatJetPartons*akFlowPuCsSoftDrop5PFPatJetFlavourAssociation)

akFlowPuCsSoftDrop5PFJetBtaggingIP = cms.Sequence(
    akFlowPuCsSoftDrop5PFImpactParameterTagInfos *
    akFlowPuCsSoftDrop5PFTrackCountingHighEffBJetTags +
    akFlowPuCsSoftDrop5PFTrackCountingHighPurBJetTags +
    akFlowPuCsSoftDrop5PFJetProbabilityBJetTags +
    akFlowPuCsSoftDrop5PFJetBProbabilityBJetTags
    )

akFlowPuCsSoftDrop5PFJetBtaggingSV = cms.Sequence(
    akFlowPuCsSoftDrop5PFImpactParameterTagInfos *
    akFlowPuCsSoftDrop5PFSecondaryVertexTagInfos *
    akFlowPuCsSoftDrop5PFSimpleSecondaryVertexHighEffBJetTags +
    akFlowPuCsSoftDrop5PFSimpleSecondaryVertexHighPurBJetTags +
    akFlowPuCsSoftDrop5PFCombinedSecondaryVertexBJetTags +
    akFlowPuCsSoftDrop5PFCombinedSecondaryVertexV2BJetTags
    )

akFlowPuCsSoftDrop5PFJetBtaggingNegSV = cms.Sequence(
    akFlowPuCsSoftDrop5PFImpactParameterTagInfos *
    akFlowPuCsSoftDrop5PFSecondaryVertexNegativeTagInfos *
    akFlowPuCsSoftDrop5PFNegativeSimpleSecondaryVertexHighEffBJetTags +
    akFlowPuCsSoftDrop5PFNegativeSimpleSecondaryVertexHighPurBJetTags +
    akFlowPuCsSoftDrop5PFNegativeCombinedSecondaryVertexBJetTags +
    akFlowPuCsSoftDrop5PFPositiveCombinedSecondaryVertexBJetTags +
    akFlowPuCsSoftDrop5PFNegativeCombinedSecondaryVertexV2BJetTags +
    akFlowPuCsSoftDrop5PFPositiveCombinedSecondaryVertexV2BJetTags
    )

akFlowPuCsSoftDrop5PFJetBtaggingMu = cms.Sequence(
    akFlowPuCsSoftDrop5PFSoftPFMuonsTagInfos *
    akFlowPuCsSoftDrop5PFSoftPFMuonBJetTags +
    akFlowPuCsSoftDrop5PFSoftPFMuonByIP3dBJetTags +
    akFlowPuCsSoftDrop5PFSoftPFMuonByPtBJetTags +
    akFlowPuCsSoftDrop5PFNegativeSoftPFMuonByPtBJetTags +
    akFlowPuCsSoftDrop5PFPositiveSoftPFMuonByPtBJetTags
    )

akFlowPuCsSoftDrop5PFJetBtagging = cms.Sequence(
    akFlowPuCsSoftDrop5PFJetBtaggingIP
    * akFlowPuCsSoftDrop5PFJetBtaggingSV
    # * akFlowPuCsSoftDrop5PFJetBtaggingNegSV
    # * akFlowPuCsSoftDrop5PFJetBtaggingMu
    )

akFlowPuCsSoftDrop5PFpatJetsWithBtagging = patJets.clone(
    jetSource = cms.InputTag("akFlowPuCsSoftDrop5PFJets"),
    genJetMatch            = cms.InputTag("akFlowPuCsSoftDrop5PFmatch"),
    genPartonMatch         = cms.InputTag("akFlowPuCsSoftDrop5PFparton"),
    jetCorrFactorsSource   = cms.VInputTag(cms.InputTag("akFlowPuCsSoftDrop5PFcorr")),
    JetPartonMapSource     = cms.InputTag("akFlowPuCsSoftDrop5PFPatJetFlavourAssociationLegacy"),
    JetFlavourInfoSource   = cms.InputTag("akFlowPuCsSoftDrop5PFPatJetFlavourAssociation"),
    trackAssociationSource = cms.InputTag("akFlowPuCsSoftDrop5PFJetTracksAssociatorAtVertex"),
    useLegacyJetMCFlavour  = True,
    discriminatorSources   = cms.VInputTag(
        cms.InputTag("akFlowPuCsSoftDrop5PFSimpleSecondaryVertexHighEffBJetTags"),
        cms.InputTag("akFlowPuCsSoftDrop5PFSimpleSecondaryVertexHighPurBJetTags"),
        cms.InputTag("akFlowPuCsSoftDrop5PFCombinedSecondaryVertexBJetTags"),
        cms.InputTag("akFlowPuCsSoftDrop5PFCombinedSecondaryVertexV2BJetTags"),
        cms.InputTag("akFlowPuCsSoftDrop5PFJetBProbabilityBJetTags"),
        cms.InputTag("akFlowPuCsSoftDrop5PFJetProbabilityBJetTags"),
        # cms.InputTag("akFlowPuCsSoftDrop5PFSoftPFMuonByPtBJetTags"),
        # cms.InputTag("akFlowPuCsSoftDrop5PFSoftPFMuonByIP3dBJetTags"),
        cms.InputTag("akFlowPuCsSoftDrop5PFTrackCountingHighEffBJetTags"),
        cms.InputTag("akFlowPuCsSoftDrop5PFTrackCountingHighPurBJetTags"),
        ),
    tagInfoSources = cms.VInputTag(cms.InputTag("akFlowPuCsSoftDrop5PFImpactParameterTagInfos"),cms.InputTag("akFlowPuCsSoftDrop5PFSecondaryVertexTagInfos")),
    jetIDMap = cms.InputTag("akFlowPuCsSoftDrop5PFJetID"),
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

akFlowPuCsSoftDrop5PFNjettiness = Njettiness.clone(
    src = cms.InputTag("akFlowPuCsSoftDrop5PFJets"),
    R0  = cms.double(0.5)
    )

akFlowPuCsSoftDrop5PFpatJetsWithBtagging.userData.userFloats.src += [
    'akFlowPuCsSoftDrop5PFNjettiness:tau1',
    'akFlowPuCsSoftDrop5PFNjettiness:tau2',
    'akFlowPuCsSoftDrop5PFNjettiness:tau3']

akFlowPuCsSoftDrop5PFJetAnalyzer = inclusiveJetAnalyzer.clone(
    jetTag = cms.InputTag("akFlowPuCsSoftDrop5PFpatJetsWithBtagging"),
    genjetTag = 'ak5HiSignalGenJets',
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
    bTagJetName = cms.untracked.string("akFlowPuCsSoftDrop5PF"),
    jetName = cms.untracked.string("akFlowPuCsSoftDrop5PF"),
    genPtMin = cms.untracked.double(5),
    hltTrgResults = cms.untracked.string('TriggerResults::'+'HISIGNAL'),
    doTower = cms.untracked.bool(True),
    doSubJets = cms.untracked.bool(True),
    doGenSubJets = cms.untracked.bool(False),
    subjetGenTag = cms.untracked.InputTag("akSoftDrop5GenJets"),
    doGenTaus = cms.untracked.bool(False),
    genTau1 = cms.InputTag("akSoftDrop5HiGenNjettiness","tau1"),
    genTau2 = cms.InputTag("akSoftDrop5HiGenNjettiness","tau2"),
    genTau3 = cms.InputTag("akSoftDrop5HiGenNjettiness","tau3"),
    doGenSym = cms.untracked.bool(False),
    genSym = cms.InputTag("akSoftDrop5GenJets","sym"),
    genDroppedBranches = cms.InputTag("akSoftDrop5GenJets","droppedBranches")
    )

akFlowPuCsSoftDrop5PFJetSequence_mc = cms.Sequence(
    # akFlowPuCsSoftDrop5PFclean
    # *
    akFlowPuCsSoftDrop5PFmatch
    # *
    # akFlowPuCsSoftDrop5PFmatchGroomed
    *
    akFlowPuCsSoftDrop5PFparton
    *
    akFlowPuCsSoftDrop5PFcorr
    # *
    # akFlowPuCsSoftDrop5PFJetID
    *
    akFlowPuCsSoftDrop5PFPatJetFlavourIdLegacy
    # *
    # akFlowPuCsSoftDrop5PFPatJetFlavourId # Use legacy algo till PU implemented
    *
    akFlowPuCsSoftDrop5PFJetTracksAssociatorAtVertex
    *
    akFlowPuCsSoftDrop5PFJetBtagging
    *
    # No constituents for calo jets in pp. Must be removed for pp calo jets but
    # I'm not sure how to do this transparently (Marta)
    akFlowPuCsSoftDrop5PFNjettiness
    *
    akFlowPuCsSoftDrop5PFpatJetsWithBtagging
    *
    akFlowPuCsSoftDrop5PFJetAnalyzer
    )

akFlowPuCsSoftDrop5PFJetSequence_data = cms.Sequence(
    akFlowPuCsSoftDrop5PFcorr
    *
    # akFlowPuCsSoftDrop5PFJetID
    # *
    akFlowPuCsSoftDrop5PFJetTracksAssociatorAtVertex
    *
    akFlowPuCsSoftDrop5PFJetBtagging
    *
    akFlowPuCsSoftDrop5PFNjettiness
    *
    akFlowPuCsSoftDrop5PFpatJetsWithBtagging
    *
    akFlowPuCsSoftDrop5PFJetAnalyzer
    )

akFlowPuCsSoftDrop5PFJetSequence_mb = cms.Sequence(
    akFlowPuCsSoftDrop5PFJetSequence_mc)
akFlowPuCsSoftDrop5PFJetSequence_jec = cms.Sequence(
    akFlowPuCsSoftDrop5PFJetSequence_mc)

akFlowPuCsSoftDrop5PFJetSequence = cms.Sequence(
    akFlowPuCsSoftDrop5PFJetSequence_jec)
akFlowPuCsSoftDrop5PFJetAnalyzer.genPtMin = cms.untracked.double(1)
akFlowPuCsSoftDrop5PFJetAnalyzer.jetPtMin = cms.double(1)
akFlowPuCsSoftDrop5PFpatJetsWithBtagging.userData.userFloats.src += ['akFlowPuCsSoftDrop5PFJets:sym']
akFlowPuCsSoftDrop5PFpatJetsWithBtagging.userData.userInts.src += ['akFlowPuCsSoftDrop5PFJets:droppedBranches']
