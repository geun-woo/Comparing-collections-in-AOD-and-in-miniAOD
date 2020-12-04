import FWCore.ParameterSet.Config as cms

from PhysicsTools.PatAlgos.mcMatchLayer0.jetMatch_cfi import patJetGenJetMatch, patJetPartonMatch
from PhysicsTools.PatAlgos.recoLayer0.jetCorrFactors_cfi import patJetCorrFactors
from PhysicsTools.PatAlgos.producersLayer1.jetProducer_cfi import patJets

from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *

from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akFlowPuCsSoftDrop2PFmatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akFlowPuCsSoftDrop2PFJets"),
    matched = cms.InputTag("ak2HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.2
    )

akFlowPuCsSoftDrop2PFmatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDrop2HiSignalGenJets"),
    matched = cms.InputTag("ak2HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.2
    )

akFlowPuCsSoftDrop2PFparton = patJetPartonMatch.clone(
    src = cms.InputTag("akFlowPuCsSoftDrop2PFJets"),
    matched = cms.InputTag("hiSignalGenParticles"))

akFlowPuCsSoftDrop2PFcorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
    levels   = cms.vstring('L2Relative'),
    src = cms.InputTag("akFlowPuCsSoftDrop2PFJets"),
    payload = "AK2PF"
    )

akFlowPuCsSoftDrop2PFJetID = cms.EDProducer(
    'JetIDProducer',
    JetIDParams,
    src = cms.InputTag('akFlowPuCsSoftDrop2CaloJets'))

# akFlowPuCsSoftDrop2PFclean = heavyIonCleanedGenJets.clone(
#     src = cms.InputTag('ak2HiSignalGenJets'))

akFlowPuCsSoftDrop2PFbTagger = bTaggers(
    "akFlowPuCsSoftDrop2PF",
    0.2)

# create objects locally since they dont load properly otherwise
akFlowPuCsSoftDrop2PFPatJetFlavourAssociationLegacy = akFlowPuCsSoftDrop2PFbTagger.PatJetFlavourAssociationLegacy
akFlowPuCsSoftDrop2PFPatJetPartons = akFlowPuCsSoftDrop2PFbTagger.PatJetPartons
akFlowPuCsSoftDrop2PFJetTracksAssociatorAtVertex = akFlowPuCsSoftDrop2PFbTagger.JetTracksAssociatorAtVertex
akFlowPuCsSoftDrop2PFJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akFlowPuCsSoftDrop2PFSimpleSecondaryVertexHighEffBJetTags = akFlowPuCsSoftDrop2PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akFlowPuCsSoftDrop2PFSimpleSecondaryVertexHighPurBJetTags = akFlowPuCsSoftDrop2PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akFlowPuCsSoftDrop2PFCombinedSecondaryVertexBJetTags = akFlowPuCsSoftDrop2PFbTagger.CombinedSecondaryVertexBJetTags
akFlowPuCsSoftDrop2PFCombinedSecondaryVertexV2BJetTags = akFlowPuCsSoftDrop2PFbTagger.CombinedSecondaryVertexV2BJetTags
akFlowPuCsSoftDrop2PFJetBProbabilityBJetTags = akFlowPuCsSoftDrop2PFbTagger.JetBProbabilityBJetTags
akFlowPuCsSoftDrop2PFSoftPFMuonByPtBJetTags = akFlowPuCsSoftDrop2PFbTagger.SoftPFMuonByPtBJetTags
akFlowPuCsSoftDrop2PFSoftPFMuonByIP3dBJetTags = akFlowPuCsSoftDrop2PFbTagger.SoftPFMuonByIP3dBJetTags
akFlowPuCsSoftDrop2PFTrackCountingHighEffBJetTags = akFlowPuCsSoftDrop2PFbTagger.TrackCountingHighEffBJetTags
akFlowPuCsSoftDrop2PFTrackCountingHighPurBJetTags = akFlowPuCsSoftDrop2PFbTagger.TrackCountingHighPurBJetTags
akFlowPuCsSoftDrop2PFPatJetPartonAssociationLegacy = akFlowPuCsSoftDrop2PFbTagger.PatJetPartonAssociationLegacy
akFlowPuCsSoftDrop2PFPatJetPartonAssociationLegacy.partons = "signalPartons"

akFlowPuCsSoftDrop2PFImpactParameterTagInfos = akFlowPuCsSoftDrop2PFbTagger.ImpactParameterTagInfos
akFlowPuCsSoftDrop2PFImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akFlowPuCsSoftDrop2PFJetProbabilityBJetTags = akFlowPuCsSoftDrop2PFbTagger.JetProbabilityBJetTags

akFlowPuCsSoftDrop2PFSecondaryVertexTagInfos = akFlowPuCsSoftDrop2PFbTagger.SecondaryVertexTagInfos
akFlowPuCsSoftDrop2PFSimpleSecondaryVertexHighEffBJetTags = akFlowPuCsSoftDrop2PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akFlowPuCsSoftDrop2PFSimpleSecondaryVertexHighPurBJetTags = akFlowPuCsSoftDrop2PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akFlowPuCsSoftDrop2PFCombinedSecondaryVertexBJetTags = akFlowPuCsSoftDrop2PFbTagger.CombinedSecondaryVertexBJetTags
akFlowPuCsSoftDrop2PFCombinedSecondaryVertexV2BJetTags = akFlowPuCsSoftDrop2PFbTagger.CombinedSecondaryVertexV2BJetTags

akFlowPuCsSoftDrop2PFSecondaryVertexNegativeTagInfos = akFlowPuCsSoftDrop2PFbTagger.SecondaryVertexNegativeTagInfos
akFlowPuCsSoftDrop2PFNegativeSimpleSecondaryVertexHighEffBJetTags = akFlowPuCsSoftDrop2PFbTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akFlowPuCsSoftDrop2PFNegativeSimpleSecondaryVertexHighPurBJetTags = akFlowPuCsSoftDrop2PFbTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akFlowPuCsSoftDrop2PFNegativeCombinedSecondaryVertexBJetTags = akFlowPuCsSoftDrop2PFbTagger.NegativeCombinedSecondaryVertexBJetTags
akFlowPuCsSoftDrop2PFPositiveCombinedSecondaryVertexBJetTags = akFlowPuCsSoftDrop2PFbTagger.PositiveCombinedSecondaryVertexBJetTags
akFlowPuCsSoftDrop2PFNegativeCombinedSecondaryVertexV2BJetTags = akFlowPuCsSoftDrop2PFbTagger.NegativeCombinedSecondaryVertexV2BJetTags
akFlowPuCsSoftDrop2PFPositiveCombinedSecondaryVertexV2BJetTags = akFlowPuCsSoftDrop2PFbTagger.PositiveCombinedSecondaryVertexV2BJetTags

akFlowPuCsSoftDrop2PFSoftPFMuonsTagInfos = akFlowPuCsSoftDrop2PFbTagger.SoftPFMuonsTagInfos
akFlowPuCsSoftDrop2PFSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akFlowPuCsSoftDrop2PFSoftPFMuonBJetTags = akFlowPuCsSoftDrop2PFbTagger.SoftPFMuonBJetTags
akFlowPuCsSoftDrop2PFSoftPFMuonByIP3dBJetTags = akFlowPuCsSoftDrop2PFbTagger.SoftPFMuonByIP3dBJetTags
akFlowPuCsSoftDrop2PFSoftPFMuonByPtBJetTags = akFlowPuCsSoftDrop2PFbTagger.SoftPFMuonByPtBJetTags
akFlowPuCsSoftDrop2PFNegativeSoftPFMuonByPtBJetTags = akFlowPuCsSoftDrop2PFbTagger.NegativeSoftPFMuonByPtBJetTags
akFlowPuCsSoftDrop2PFPositiveSoftPFMuonByPtBJetTags = akFlowPuCsSoftDrop2PFbTagger.PositiveSoftPFMuonByPtBJetTags
akFlowPuCsSoftDrop2PFPatJetFlavourIdLegacy = cms.Sequence(akFlowPuCsSoftDrop2PFPatJetPartonAssociationLegacy*akFlowPuCsSoftDrop2PFPatJetFlavourAssociationLegacy)
# Not working with our PU sub, but keep it here for reference
# akFlowPuCsSoftDrop2PFPatJetFlavourAssociation = akFlowPuCsSoftDrop2PFbTagger.PatJetFlavourAssociation
# akFlowPuCsSoftDrop2PFPatJetFlavourId = cms.Sequence(akFlowPuCsSoftDrop2PFPatJetPartons*akFlowPuCsSoftDrop2PFPatJetFlavourAssociation)

akFlowPuCsSoftDrop2PFJetBtaggingIP = cms.Sequence(
    akFlowPuCsSoftDrop2PFImpactParameterTagInfos *
    akFlowPuCsSoftDrop2PFTrackCountingHighEffBJetTags +
    akFlowPuCsSoftDrop2PFTrackCountingHighPurBJetTags +
    akFlowPuCsSoftDrop2PFJetProbabilityBJetTags +
    akFlowPuCsSoftDrop2PFJetBProbabilityBJetTags
    )

akFlowPuCsSoftDrop2PFJetBtaggingSV = cms.Sequence(
    akFlowPuCsSoftDrop2PFImpactParameterTagInfos *
    akFlowPuCsSoftDrop2PFSecondaryVertexTagInfos *
    akFlowPuCsSoftDrop2PFSimpleSecondaryVertexHighEffBJetTags +
    akFlowPuCsSoftDrop2PFSimpleSecondaryVertexHighPurBJetTags +
    akFlowPuCsSoftDrop2PFCombinedSecondaryVertexBJetTags +
    akFlowPuCsSoftDrop2PFCombinedSecondaryVertexV2BJetTags
    )

akFlowPuCsSoftDrop2PFJetBtaggingNegSV = cms.Sequence(
    akFlowPuCsSoftDrop2PFImpactParameterTagInfos *
    akFlowPuCsSoftDrop2PFSecondaryVertexNegativeTagInfos *
    akFlowPuCsSoftDrop2PFNegativeSimpleSecondaryVertexHighEffBJetTags +
    akFlowPuCsSoftDrop2PFNegativeSimpleSecondaryVertexHighPurBJetTags +
    akFlowPuCsSoftDrop2PFNegativeCombinedSecondaryVertexBJetTags +
    akFlowPuCsSoftDrop2PFPositiveCombinedSecondaryVertexBJetTags +
    akFlowPuCsSoftDrop2PFNegativeCombinedSecondaryVertexV2BJetTags +
    akFlowPuCsSoftDrop2PFPositiveCombinedSecondaryVertexV2BJetTags
    )

akFlowPuCsSoftDrop2PFJetBtaggingMu = cms.Sequence(
    akFlowPuCsSoftDrop2PFSoftPFMuonsTagInfos *
    akFlowPuCsSoftDrop2PFSoftPFMuonBJetTags +
    akFlowPuCsSoftDrop2PFSoftPFMuonByIP3dBJetTags +
    akFlowPuCsSoftDrop2PFSoftPFMuonByPtBJetTags +
    akFlowPuCsSoftDrop2PFNegativeSoftPFMuonByPtBJetTags +
    akFlowPuCsSoftDrop2PFPositiveSoftPFMuonByPtBJetTags
    )

akFlowPuCsSoftDrop2PFJetBtagging = cms.Sequence(
    akFlowPuCsSoftDrop2PFJetBtaggingIP
    * akFlowPuCsSoftDrop2PFJetBtaggingSV
    # * akFlowPuCsSoftDrop2PFJetBtaggingNegSV
    # * akFlowPuCsSoftDrop2PFJetBtaggingMu
    )

akFlowPuCsSoftDrop2PFpatJetsWithBtagging = patJets.clone(
    jetSource = cms.InputTag("akFlowPuCsSoftDrop2PFJets"),
    genJetMatch            = cms.InputTag("akFlowPuCsSoftDrop2PFmatch"),
    genPartonMatch         = cms.InputTag("akFlowPuCsSoftDrop2PFparton"),
    jetCorrFactorsSource   = cms.VInputTag(cms.InputTag("akFlowPuCsSoftDrop2PFcorr")),
    JetPartonMapSource     = cms.InputTag("akFlowPuCsSoftDrop2PFPatJetFlavourAssociationLegacy"),
    JetFlavourInfoSource   = cms.InputTag("akFlowPuCsSoftDrop2PFPatJetFlavourAssociation"),
    trackAssociationSource = cms.InputTag("akFlowPuCsSoftDrop2PFJetTracksAssociatorAtVertex"),
    useLegacyJetMCFlavour  = True,
    discriminatorSources   = cms.VInputTag(
        cms.InputTag("akFlowPuCsSoftDrop2PFSimpleSecondaryVertexHighEffBJetTags"),
        cms.InputTag("akFlowPuCsSoftDrop2PFSimpleSecondaryVertexHighPurBJetTags"),
        cms.InputTag("akFlowPuCsSoftDrop2PFCombinedSecondaryVertexBJetTags"),
        cms.InputTag("akFlowPuCsSoftDrop2PFCombinedSecondaryVertexV2BJetTags"),
        cms.InputTag("akFlowPuCsSoftDrop2PFJetBProbabilityBJetTags"),
        cms.InputTag("akFlowPuCsSoftDrop2PFJetProbabilityBJetTags"),
        # cms.InputTag("akFlowPuCsSoftDrop2PFSoftPFMuonByPtBJetTags"),
        # cms.InputTag("akFlowPuCsSoftDrop2PFSoftPFMuonByIP3dBJetTags"),
        cms.InputTag("akFlowPuCsSoftDrop2PFTrackCountingHighEffBJetTags"),
        cms.InputTag("akFlowPuCsSoftDrop2PFTrackCountingHighPurBJetTags"),
        ),
    tagInfoSources = cms.VInputTag(cms.InputTag("akFlowPuCsSoftDrop2PFImpactParameterTagInfos"),cms.InputTag("akFlowPuCsSoftDrop2PFSecondaryVertexTagInfos")),
    jetIDMap = cms.InputTag("akFlowPuCsSoftDrop2PFJetID"),
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

akFlowPuCsSoftDrop2PFNjettiness = Njettiness.clone(
    src = cms.InputTag("akFlowPuCsSoftDrop2PFJets"),
    R0  = cms.double(0.2)
    )

akFlowPuCsSoftDrop2PFpatJetsWithBtagging.userData.userFloats.src += [
    'akFlowPuCsSoftDrop2PFNjettiness:tau1',
    'akFlowPuCsSoftDrop2PFNjettiness:tau2',
    'akFlowPuCsSoftDrop2PFNjettiness:tau3']

akFlowPuCsSoftDrop2PFJetAnalyzer = inclusiveJetAnalyzer.clone(
    jetTag = cms.InputTag("akFlowPuCsSoftDrop2PFpatJetsWithBtagging"),
    genjetTag = 'ak2HiSignalGenJets',
    rParam = 0.2,
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
    bTagJetName = cms.untracked.string("akFlowPuCsSoftDrop2PF"),
    jetName = cms.untracked.string("akFlowPuCsSoftDrop2PF"),
    genPtMin = cms.untracked.double(5),
    hltTrgResults = cms.untracked.string('TriggerResults::'+'HISIGNAL'),
    doTower = cms.untracked.bool(False),
    doSubJets = cms.untracked.bool(True),
    doGenSubJets = cms.untracked.bool(False),
    subjetGenTag = cms.untracked.InputTag("akSoftDrop2GenJets"),
    doGenTaus = cms.untracked.bool(False),
    genTau1 = cms.InputTag("akSoftDrop2HiGenNjettiness","tau1"),
    genTau2 = cms.InputTag("akSoftDrop2HiGenNjettiness","tau2"),
    genTau3 = cms.InputTag("akSoftDrop2HiGenNjettiness","tau3"),
    doGenSym = cms.untracked.bool(False),
    genSym = cms.InputTag("akSoftDrop2GenJets","sym"),
    genDroppedBranches = cms.InputTag("akSoftDrop2GenJets","droppedBranches")
    )

akFlowPuCsSoftDrop2PFJetSequence_mc = cms.Sequence(
    # akFlowPuCsSoftDrop2PFclean
    # *
    akFlowPuCsSoftDrop2PFmatch
    # *
    # akFlowPuCsSoftDrop2PFmatchGroomed
    *
    akFlowPuCsSoftDrop2PFparton
    *
    akFlowPuCsSoftDrop2PFcorr
    # *
    # akFlowPuCsSoftDrop2PFJetID
    *
    akFlowPuCsSoftDrop2PFPatJetFlavourIdLegacy
    # *
    # akFlowPuCsSoftDrop2PFPatJetFlavourId # Use legacy algo till PU implemented
    *
    akFlowPuCsSoftDrop2PFJetTracksAssociatorAtVertex
    *
    akFlowPuCsSoftDrop2PFJetBtagging
    *
    # No constituents for calo jets in pp. Must be removed for pp calo jets but
    # I'm not sure how to do this transparently (Marta)
    akFlowPuCsSoftDrop2PFNjettiness
    *
    akFlowPuCsSoftDrop2PFpatJetsWithBtagging
    *
    akFlowPuCsSoftDrop2PFJetAnalyzer
    )

akFlowPuCsSoftDrop2PFJetSequence_data = cms.Sequence(
    akFlowPuCsSoftDrop2PFcorr
    *
    # akFlowPuCsSoftDrop2PFJetID
    # *
    akFlowPuCsSoftDrop2PFJetTracksAssociatorAtVertex
    *
    akFlowPuCsSoftDrop2PFJetBtagging
    *
    akFlowPuCsSoftDrop2PFNjettiness
    *
    akFlowPuCsSoftDrop2PFpatJetsWithBtagging
    *
    akFlowPuCsSoftDrop2PFJetAnalyzer
    )

akFlowPuCsSoftDrop2PFJetSequence_mb = cms.Sequence(
    akFlowPuCsSoftDrop2PFJetSequence_mc)
akFlowPuCsSoftDrop2PFJetSequence_jec = cms.Sequence(
    akFlowPuCsSoftDrop2PFJetSequence_mc)

akFlowPuCsSoftDrop2PFJetSequence = cms.Sequence(
    akFlowPuCsSoftDrop2PFJetSequence_jec)
akFlowPuCsSoftDrop2PFJetAnalyzer.genPtMin = cms.untracked.double(1)
akFlowPuCsSoftDrop2PFJetAnalyzer.jetPtMin = cms.double(1)
akFlowPuCsSoftDrop2PFpatJetsWithBtagging.userData.userFloats.src += ['akFlowPuCsSoftDrop2PFJets:sym']
akFlowPuCsSoftDrop2PFpatJetsWithBtagging.userData.userInts.src += ['akFlowPuCsSoftDrop2PFJets:droppedBranches']
