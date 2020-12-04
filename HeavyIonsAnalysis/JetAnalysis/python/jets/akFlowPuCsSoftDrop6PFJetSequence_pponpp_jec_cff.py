import FWCore.ParameterSet.Config as cms

from PhysicsTools.PatAlgos.mcMatchLayer0.jetMatch_cfi import patJetGenJetMatch, patJetPartonMatch
from PhysicsTools.PatAlgos.recoLayer0.jetCorrFactors_cfi import patJetCorrFactors
from PhysicsTools.PatAlgos.producersLayer1.jetProducer_cfi import patJets

from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *

from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akFlowPuCsSoftDrop6PFmatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akFlowPuCsSoftDrop6PFJets"),
    matched = cms.InputTag("ak6GenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.6
    )

akFlowPuCsSoftDrop6PFmatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDrop6GenJets"),
    matched = cms.InputTag("ak6GenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.6
    )

akFlowPuCsSoftDrop6PFparton = patJetPartonMatch.clone(
    src = cms.InputTag("akFlowPuCsSoftDrop6PFJets"),
    matched = cms.InputTag("genParticles"))

akFlowPuCsSoftDrop6PFcorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
    levels   = cms.vstring('L2Relative'),
    src = cms.InputTag("akFlowPuCsSoftDrop6PFJets"),
    payload = "AK6PF"
    )

akFlowPuCsSoftDrop6PFJetID = cms.EDProducer(
    'JetIDProducer',
    JetIDParams,
    src = cms.InputTag('akFlowPuCsSoftDrop6CaloJets'))

# akFlowPuCsSoftDrop6PFclean = heavyIonCleanedGenJets.clone(
#     src = cms.InputTag('ak6GenJets'))

akFlowPuCsSoftDrop6PFbTagger = bTaggers(
    "akFlowPuCsSoftDrop6PF",
    0.6)

# create objects locally since they dont load properly otherwise
akFlowPuCsSoftDrop6PFPatJetFlavourAssociationLegacy = akFlowPuCsSoftDrop6PFbTagger.PatJetFlavourAssociationLegacy
akFlowPuCsSoftDrop6PFPatJetPartons = akFlowPuCsSoftDrop6PFbTagger.PatJetPartons
akFlowPuCsSoftDrop6PFJetTracksAssociatorAtVertex = akFlowPuCsSoftDrop6PFbTagger.JetTracksAssociatorAtVertex
akFlowPuCsSoftDrop6PFJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akFlowPuCsSoftDrop6PFSimpleSecondaryVertexHighEffBJetTags = akFlowPuCsSoftDrop6PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akFlowPuCsSoftDrop6PFSimpleSecondaryVertexHighPurBJetTags = akFlowPuCsSoftDrop6PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akFlowPuCsSoftDrop6PFCombinedSecondaryVertexBJetTags = akFlowPuCsSoftDrop6PFbTagger.CombinedSecondaryVertexBJetTags
akFlowPuCsSoftDrop6PFCombinedSecondaryVertexV2BJetTags = akFlowPuCsSoftDrop6PFbTagger.CombinedSecondaryVertexV2BJetTags
akFlowPuCsSoftDrop6PFJetBProbabilityBJetTags = akFlowPuCsSoftDrop6PFbTagger.JetBProbabilityBJetTags
akFlowPuCsSoftDrop6PFSoftPFMuonByPtBJetTags = akFlowPuCsSoftDrop6PFbTagger.SoftPFMuonByPtBJetTags
akFlowPuCsSoftDrop6PFSoftPFMuonByIP3dBJetTags = akFlowPuCsSoftDrop6PFbTagger.SoftPFMuonByIP3dBJetTags
akFlowPuCsSoftDrop6PFTrackCountingHighEffBJetTags = akFlowPuCsSoftDrop6PFbTagger.TrackCountingHighEffBJetTags
akFlowPuCsSoftDrop6PFTrackCountingHighPurBJetTags = akFlowPuCsSoftDrop6PFbTagger.TrackCountingHighPurBJetTags
akFlowPuCsSoftDrop6PFPatJetPartonAssociationLegacy = akFlowPuCsSoftDrop6PFbTagger.PatJetPartonAssociationLegacy
akFlowPuCsSoftDrop6PFPatJetPartonAssociationLegacy.partons = "myPartons"

akFlowPuCsSoftDrop6PFImpactParameterTagInfos = akFlowPuCsSoftDrop6PFbTagger.ImpactParameterTagInfos
akFlowPuCsSoftDrop6PFImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akFlowPuCsSoftDrop6PFJetProbabilityBJetTags = akFlowPuCsSoftDrop6PFbTagger.JetProbabilityBJetTags

akFlowPuCsSoftDrop6PFSecondaryVertexTagInfos = akFlowPuCsSoftDrop6PFbTagger.SecondaryVertexTagInfos
akFlowPuCsSoftDrop6PFSimpleSecondaryVertexHighEffBJetTags = akFlowPuCsSoftDrop6PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akFlowPuCsSoftDrop6PFSimpleSecondaryVertexHighPurBJetTags = akFlowPuCsSoftDrop6PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akFlowPuCsSoftDrop6PFCombinedSecondaryVertexBJetTags = akFlowPuCsSoftDrop6PFbTagger.CombinedSecondaryVertexBJetTags
akFlowPuCsSoftDrop6PFCombinedSecondaryVertexV2BJetTags = akFlowPuCsSoftDrop6PFbTagger.CombinedSecondaryVertexV2BJetTags

akFlowPuCsSoftDrop6PFSecondaryVertexNegativeTagInfos = akFlowPuCsSoftDrop6PFbTagger.SecondaryVertexNegativeTagInfos
akFlowPuCsSoftDrop6PFNegativeSimpleSecondaryVertexHighEffBJetTags = akFlowPuCsSoftDrop6PFbTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akFlowPuCsSoftDrop6PFNegativeSimpleSecondaryVertexHighPurBJetTags = akFlowPuCsSoftDrop6PFbTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akFlowPuCsSoftDrop6PFNegativeCombinedSecondaryVertexBJetTags = akFlowPuCsSoftDrop6PFbTagger.NegativeCombinedSecondaryVertexBJetTags
akFlowPuCsSoftDrop6PFPositiveCombinedSecondaryVertexBJetTags = akFlowPuCsSoftDrop6PFbTagger.PositiveCombinedSecondaryVertexBJetTags
akFlowPuCsSoftDrop6PFNegativeCombinedSecondaryVertexV2BJetTags = akFlowPuCsSoftDrop6PFbTagger.NegativeCombinedSecondaryVertexV2BJetTags
akFlowPuCsSoftDrop6PFPositiveCombinedSecondaryVertexV2BJetTags = akFlowPuCsSoftDrop6PFbTagger.PositiveCombinedSecondaryVertexV2BJetTags

akFlowPuCsSoftDrop6PFSoftPFMuonsTagInfos = akFlowPuCsSoftDrop6PFbTagger.SoftPFMuonsTagInfos
akFlowPuCsSoftDrop6PFSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akFlowPuCsSoftDrop6PFSoftPFMuonBJetTags = akFlowPuCsSoftDrop6PFbTagger.SoftPFMuonBJetTags
akFlowPuCsSoftDrop6PFSoftPFMuonByIP3dBJetTags = akFlowPuCsSoftDrop6PFbTagger.SoftPFMuonByIP3dBJetTags
akFlowPuCsSoftDrop6PFSoftPFMuonByPtBJetTags = akFlowPuCsSoftDrop6PFbTagger.SoftPFMuonByPtBJetTags
akFlowPuCsSoftDrop6PFNegativeSoftPFMuonByPtBJetTags = akFlowPuCsSoftDrop6PFbTagger.NegativeSoftPFMuonByPtBJetTags
akFlowPuCsSoftDrop6PFPositiveSoftPFMuonByPtBJetTags = akFlowPuCsSoftDrop6PFbTagger.PositiveSoftPFMuonByPtBJetTags
akFlowPuCsSoftDrop6PFPatJetFlavourIdLegacy = cms.Sequence(akFlowPuCsSoftDrop6PFPatJetPartonAssociationLegacy*akFlowPuCsSoftDrop6PFPatJetFlavourAssociationLegacy)
# Not working with our PU sub, but keep it here for reference
# akFlowPuCsSoftDrop6PFPatJetFlavourAssociation = akFlowPuCsSoftDrop6PFbTagger.PatJetFlavourAssociation
# akFlowPuCsSoftDrop6PFPatJetFlavourId = cms.Sequence(akFlowPuCsSoftDrop6PFPatJetPartons*akFlowPuCsSoftDrop6PFPatJetFlavourAssociation)

akFlowPuCsSoftDrop6PFJetBtaggingIP = cms.Sequence(
    akFlowPuCsSoftDrop6PFImpactParameterTagInfos *
    akFlowPuCsSoftDrop6PFTrackCountingHighEffBJetTags +
    akFlowPuCsSoftDrop6PFTrackCountingHighPurBJetTags +
    akFlowPuCsSoftDrop6PFJetProbabilityBJetTags +
    akFlowPuCsSoftDrop6PFJetBProbabilityBJetTags
    )

akFlowPuCsSoftDrop6PFJetBtaggingSV = cms.Sequence(
    akFlowPuCsSoftDrop6PFImpactParameterTagInfos *
    akFlowPuCsSoftDrop6PFSecondaryVertexTagInfos *
    akFlowPuCsSoftDrop6PFSimpleSecondaryVertexHighEffBJetTags +
    akFlowPuCsSoftDrop6PFSimpleSecondaryVertexHighPurBJetTags +
    akFlowPuCsSoftDrop6PFCombinedSecondaryVertexBJetTags +
    akFlowPuCsSoftDrop6PFCombinedSecondaryVertexV2BJetTags
    )

akFlowPuCsSoftDrop6PFJetBtaggingNegSV = cms.Sequence(
    akFlowPuCsSoftDrop6PFImpactParameterTagInfos *
    akFlowPuCsSoftDrop6PFSecondaryVertexNegativeTagInfos *
    akFlowPuCsSoftDrop6PFNegativeSimpleSecondaryVertexHighEffBJetTags +
    akFlowPuCsSoftDrop6PFNegativeSimpleSecondaryVertexHighPurBJetTags +
    akFlowPuCsSoftDrop6PFNegativeCombinedSecondaryVertexBJetTags +
    akFlowPuCsSoftDrop6PFPositiveCombinedSecondaryVertexBJetTags +
    akFlowPuCsSoftDrop6PFNegativeCombinedSecondaryVertexV2BJetTags +
    akFlowPuCsSoftDrop6PFPositiveCombinedSecondaryVertexV2BJetTags
    )

akFlowPuCsSoftDrop6PFJetBtaggingMu = cms.Sequence(
    akFlowPuCsSoftDrop6PFSoftPFMuonsTagInfos *
    akFlowPuCsSoftDrop6PFSoftPFMuonBJetTags +
    akFlowPuCsSoftDrop6PFSoftPFMuonByIP3dBJetTags +
    akFlowPuCsSoftDrop6PFSoftPFMuonByPtBJetTags +
    akFlowPuCsSoftDrop6PFNegativeSoftPFMuonByPtBJetTags +
    akFlowPuCsSoftDrop6PFPositiveSoftPFMuonByPtBJetTags
    )

akFlowPuCsSoftDrop6PFJetBtagging = cms.Sequence(
    akFlowPuCsSoftDrop6PFJetBtaggingIP
    * akFlowPuCsSoftDrop6PFJetBtaggingSV
    # * akFlowPuCsSoftDrop6PFJetBtaggingNegSV
    # * akFlowPuCsSoftDrop6PFJetBtaggingMu
    )

akFlowPuCsSoftDrop6PFpatJetsWithBtagging = patJets.clone(
    jetSource = cms.InputTag("akFlowPuCsSoftDrop6PFJets"),
    genJetMatch            = cms.InputTag("akFlowPuCsSoftDrop6PFmatch"),
    genPartonMatch         = cms.InputTag("akFlowPuCsSoftDrop6PFparton"),
    jetCorrFactorsSource   = cms.VInputTag(cms.InputTag("akFlowPuCsSoftDrop6PFcorr")),
    JetPartonMapSource     = cms.InputTag("akFlowPuCsSoftDrop6PFPatJetFlavourAssociationLegacy"),
    JetFlavourInfoSource   = cms.InputTag("akFlowPuCsSoftDrop6PFPatJetFlavourAssociation"),
    trackAssociationSource = cms.InputTag("akFlowPuCsSoftDrop6PFJetTracksAssociatorAtVertex"),
    useLegacyJetMCFlavour  = True,
    discriminatorSources   = cms.VInputTag(
        cms.InputTag("akFlowPuCsSoftDrop6PFSimpleSecondaryVertexHighEffBJetTags"),
        cms.InputTag("akFlowPuCsSoftDrop6PFSimpleSecondaryVertexHighPurBJetTags"),
        cms.InputTag("akFlowPuCsSoftDrop6PFCombinedSecondaryVertexBJetTags"),
        cms.InputTag("akFlowPuCsSoftDrop6PFCombinedSecondaryVertexV2BJetTags"),
        cms.InputTag("akFlowPuCsSoftDrop6PFJetBProbabilityBJetTags"),
        cms.InputTag("akFlowPuCsSoftDrop6PFJetProbabilityBJetTags"),
        # cms.InputTag("akFlowPuCsSoftDrop6PFSoftPFMuonByPtBJetTags"),
        # cms.InputTag("akFlowPuCsSoftDrop6PFSoftPFMuonByIP3dBJetTags"),
        cms.InputTag("akFlowPuCsSoftDrop6PFTrackCountingHighEffBJetTags"),
        cms.InputTag("akFlowPuCsSoftDrop6PFTrackCountingHighPurBJetTags"),
        ),
    tagInfoSources = cms.VInputTag(cms.InputTag("akFlowPuCsSoftDrop6PFImpactParameterTagInfos"),cms.InputTag("akFlowPuCsSoftDrop6PFSecondaryVertexTagInfos")),
    jetIDMap = cms.InputTag("akFlowPuCsSoftDrop6PFJetID"),
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

akFlowPuCsSoftDrop6PFNjettiness = Njettiness.clone(
    src = cms.InputTag("akFlowPuCsSoftDrop6PFJets"),
    R0  = cms.double(0.6)
    )

akFlowPuCsSoftDrop6PFpatJetsWithBtagging.userData.userFloats.src += [
    'akFlowPuCsSoftDrop6PFNjettiness:tau1',
    'akFlowPuCsSoftDrop6PFNjettiness:tau2',
    'akFlowPuCsSoftDrop6PFNjettiness:tau3']

akFlowPuCsSoftDrop6PFJetAnalyzer = inclusiveJetAnalyzer.clone(
    jetTag = cms.InputTag("akFlowPuCsSoftDrop6PFpatJetsWithBtagging"),
    genjetTag = 'ak6GenJets',
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
    bTagJetName = cms.untracked.string("akFlowPuCsSoftDrop6PF"),
    jetName = cms.untracked.string("akFlowPuCsSoftDrop6PF"),
    genPtMin = cms.untracked.double(5),
    hltTrgResults = cms.untracked.string('TriggerResults::'+'HISIGNAL'),
    doTower = cms.untracked.bool(False),
    doSubJets = cms.untracked.bool(True),
    doGenSubJets = cms.untracked.bool(False),
    subjetGenTag = cms.untracked.InputTag("akSoftDrop6GenJets"),
    doGenTaus = cms.untracked.bool(False),
    genTau1 = cms.InputTag("akSoftDrop6GenNjettiness","tau1"),
    genTau2 = cms.InputTag("akSoftDrop6GenNjettiness","tau2"),
    genTau3 = cms.InputTag("akSoftDrop6GenNjettiness","tau3"),
    doGenSym = cms.untracked.bool(False),
    genSym = cms.InputTag("akSoftDrop6GenJets","sym"),
    genDroppedBranches = cms.InputTag("akSoftDrop6GenJets","droppedBranches")
    )

akFlowPuCsSoftDrop6PFJetSequence_mc = cms.Sequence(
    # akFlowPuCsSoftDrop6PFclean
    # *
    akFlowPuCsSoftDrop6PFmatch
    # *
    # akFlowPuCsSoftDrop6PFmatchGroomed
    *
    akFlowPuCsSoftDrop6PFparton
    *
    akFlowPuCsSoftDrop6PFcorr
    # *
    # akFlowPuCsSoftDrop6PFJetID
    *
    akFlowPuCsSoftDrop6PFPatJetFlavourIdLegacy
    # *
    # akFlowPuCsSoftDrop6PFPatJetFlavourId # Use legacy algo till PU implemented
    *
    akFlowPuCsSoftDrop6PFJetTracksAssociatorAtVertex
    *
    akFlowPuCsSoftDrop6PFJetBtagging
    *
    # No constituents for calo jets in pp. Must be removed for pp calo jets but
    # I'm not sure how to do this transparently (Marta)
    akFlowPuCsSoftDrop6PFNjettiness
    *
    akFlowPuCsSoftDrop6PFpatJetsWithBtagging
    *
    akFlowPuCsSoftDrop6PFJetAnalyzer
    )

akFlowPuCsSoftDrop6PFJetSequence_data = cms.Sequence(
    akFlowPuCsSoftDrop6PFcorr
    *
    # akFlowPuCsSoftDrop6PFJetID
    # *
    akFlowPuCsSoftDrop6PFJetTracksAssociatorAtVertex
    *
    akFlowPuCsSoftDrop6PFJetBtagging
    *
    akFlowPuCsSoftDrop6PFNjettiness
    *
    akFlowPuCsSoftDrop6PFpatJetsWithBtagging
    *
    akFlowPuCsSoftDrop6PFJetAnalyzer
    )

akFlowPuCsSoftDrop6PFJetSequence_mb = cms.Sequence(
    akFlowPuCsSoftDrop6PFJetSequence_mc)
akFlowPuCsSoftDrop6PFJetSequence_jec = cms.Sequence(
    akFlowPuCsSoftDrop6PFJetSequence_mc)

akFlowPuCsSoftDrop6PFJetSequence = cms.Sequence(
    akFlowPuCsSoftDrop6PFJetSequence_jec)
akFlowPuCsSoftDrop6PFJetAnalyzer.genPtMin = cms.untracked.double(1)
akFlowPuCsSoftDrop6PFJetAnalyzer.jetPtMin = cms.double(1)
akFlowPuCsSoftDrop6PFpatJetsWithBtagging.userData.userFloats.src += ['akFlowPuCsSoftDrop6PFJets:sym']
akFlowPuCsSoftDrop6PFpatJetsWithBtagging.userData.userInts.src += ['akFlowPuCsSoftDrop6PFJets:droppedBranches']
