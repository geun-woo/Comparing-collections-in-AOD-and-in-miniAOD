import FWCore.ParameterSet.Config as cms

from PhysicsTools.PatAlgos.mcMatchLayer0.jetMatch_cfi import patJetGenJetMatch, patJetPartonMatch
from PhysicsTools.PatAlgos.recoLayer0.jetCorrFactors_cfi import patJetCorrFactors
from PhysicsTools.PatAlgos.producersLayer1.jetProducer_cfi import patJets

from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *

from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akFlowPuCsSoftDropZ05B151PFmatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akFlowPuCsSoftDropZ05B151PFJets"),
    matched = cms.InputTag("ak1HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.1
    )

akFlowPuCsSoftDropZ05B151PFmatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDropZ05B151HiSignalGenJets"),
    matched = cms.InputTag("ak1HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.1
    )

akFlowPuCsSoftDropZ05B151PFparton = patJetPartonMatch.clone(
    src = cms.InputTag("akFlowPuCsSoftDropZ05B151PFJets"),
    matched = cms.InputTag("hiSignalGenParticles"))

akFlowPuCsSoftDropZ05B151PFcorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
    levels   = cms.vstring('L2Relative'),
    src = cms.InputTag("akFlowPuCsSoftDropZ05B151PFJets"),
    payload = "AK1PF"
    )

akFlowPuCsSoftDropZ05B151PFJetID = cms.EDProducer(
    'JetIDProducer',
    JetIDParams,
    src = cms.InputTag('akFlowPuCsSoftDropZ05B151CaloJets'))

# akFlowPuCsSoftDropZ05B151PFclean = heavyIonCleanedGenJets.clone(
#     src = cms.InputTag('ak1HiSignalGenJets'))

akFlowPuCsSoftDropZ05B151PFbTagger = bTaggers(
    "akFlowPuCsSoftDropZ05B151PF",
    0.1)

# create objects locally since they dont load properly otherwise
akFlowPuCsSoftDropZ05B151PFPatJetFlavourAssociationLegacy = akFlowPuCsSoftDropZ05B151PFbTagger.PatJetFlavourAssociationLegacy
akFlowPuCsSoftDropZ05B151PFPatJetPartons = akFlowPuCsSoftDropZ05B151PFbTagger.PatJetPartons
akFlowPuCsSoftDropZ05B151PFJetTracksAssociatorAtVertex = akFlowPuCsSoftDropZ05B151PFbTagger.JetTracksAssociatorAtVertex
akFlowPuCsSoftDropZ05B151PFJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akFlowPuCsSoftDropZ05B151PFSimpleSecondaryVertexHighEffBJetTags = akFlowPuCsSoftDropZ05B151PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akFlowPuCsSoftDropZ05B151PFSimpleSecondaryVertexHighPurBJetTags = akFlowPuCsSoftDropZ05B151PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akFlowPuCsSoftDropZ05B151PFCombinedSecondaryVertexBJetTags = akFlowPuCsSoftDropZ05B151PFbTagger.CombinedSecondaryVertexBJetTags
akFlowPuCsSoftDropZ05B151PFCombinedSecondaryVertexV2BJetTags = akFlowPuCsSoftDropZ05B151PFbTagger.CombinedSecondaryVertexV2BJetTags
akFlowPuCsSoftDropZ05B151PFJetBProbabilityBJetTags = akFlowPuCsSoftDropZ05B151PFbTagger.JetBProbabilityBJetTags
akFlowPuCsSoftDropZ05B151PFSoftPFMuonByPtBJetTags = akFlowPuCsSoftDropZ05B151PFbTagger.SoftPFMuonByPtBJetTags
akFlowPuCsSoftDropZ05B151PFSoftPFMuonByIP3dBJetTags = akFlowPuCsSoftDropZ05B151PFbTagger.SoftPFMuonByIP3dBJetTags
akFlowPuCsSoftDropZ05B151PFTrackCountingHighEffBJetTags = akFlowPuCsSoftDropZ05B151PFbTagger.TrackCountingHighEffBJetTags
akFlowPuCsSoftDropZ05B151PFTrackCountingHighPurBJetTags = akFlowPuCsSoftDropZ05B151PFbTagger.TrackCountingHighPurBJetTags
akFlowPuCsSoftDropZ05B151PFPatJetPartonAssociationLegacy = akFlowPuCsSoftDropZ05B151PFbTagger.PatJetPartonAssociationLegacy
akFlowPuCsSoftDropZ05B151PFPatJetPartonAssociationLegacy.partons = "signalPartons"

akFlowPuCsSoftDropZ05B151PFImpactParameterTagInfos = akFlowPuCsSoftDropZ05B151PFbTagger.ImpactParameterTagInfos
akFlowPuCsSoftDropZ05B151PFImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akFlowPuCsSoftDropZ05B151PFJetProbabilityBJetTags = akFlowPuCsSoftDropZ05B151PFbTagger.JetProbabilityBJetTags

akFlowPuCsSoftDropZ05B151PFSecondaryVertexTagInfos = akFlowPuCsSoftDropZ05B151PFbTagger.SecondaryVertexTagInfos
akFlowPuCsSoftDropZ05B151PFSimpleSecondaryVertexHighEffBJetTags = akFlowPuCsSoftDropZ05B151PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akFlowPuCsSoftDropZ05B151PFSimpleSecondaryVertexHighPurBJetTags = akFlowPuCsSoftDropZ05B151PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akFlowPuCsSoftDropZ05B151PFCombinedSecondaryVertexBJetTags = akFlowPuCsSoftDropZ05B151PFbTagger.CombinedSecondaryVertexBJetTags
akFlowPuCsSoftDropZ05B151PFCombinedSecondaryVertexV2BJetTags = akFlowPuCsSoftDropZ05B151PFbTagger.CombinedSecondaryVertexV2BJetTags

akFlowPuCsSoftDropZ05B151PFSecondaryVertexNegativeTagInfos = akFlowPuCsSoftDropZ05B151PFbTagger.SecondaryVertexNegativeTagInfos
akFlowPuCsSoftDropZ05B151PFNegativeSimpleSecondaryVertexHighEffBJetTags = akFlowPuCsSoftDropZ05B151PFbTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akFlowPuCsSoftDropZ05B151PFNegativeSimpleSecondaryVertexHighPurBJetTags = akFlowPuCsSoftDropZ05B151PFbTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akFlowPuCsSoftDropZ05B151PFNegativeCombinedSecondaryVertexBJetTags = akFlowPuCsSoftDropZ05B151PFbTagger.NegativeCombinedSecondaryVertexBJetTags
akFlowPuCsSoftDropZ05B151PFPositiveCombinedSecondaryVertexBJetTags = akFlowPuCsSoftDropZ05B151PFbTagger.PositiveCombinedSecondaryVertexBJetTags
akFlowPuCsSoftDropZ05B151PFNegativeCombinedSecondaryVertexV2BJetTags = akFlowPuCsSoftDropZ05B151PFbTagger.NegativeCombinedSecondaryVertexV2BJetTags
akFlowPuCsSoftDropZ05B151PFPositiveCombinedSecondaryVertexV2BJetTags = akFlowPuCsSoftDropZ05B151PFbTagger.PositiveCombinedSecondaryVertexV2BJetTags

akFlowPuCsSoftDropZ05B151PFSoftPFMuonsTagInfos = akFlowPuCsSoftDropZ05B151PFbTagger.SoftPFMuonsTagInfos
akFlowPuCsSoftDropZ05B151PFSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akFlowPuCsSoftDropZ05B151PFSoftPFMuonBJetTags = akFlowPuCsSoftDropZ05B151PFbTagger.SoftPFMuonBJetTags
akFlowPuCsSoftDropZ05B151PFSoftPFMuonByIP3dBJetTags = akFlowPuCsSoftDropZ05B151PFbTagger.SoftPFMuonByIP3dBJetTags
akFlowPuCsSoftDropZ05B151PFSoftPFMuonByPtBJetTags = akFlowPuCsSoftDropZ05B151PFbTagger.SoftPFMuonByPtBJetTags
akFlowPuCsSoftDropZ05B151PFNegativeSoftPFMuonByPtBJetTags = akFlowPuCsSoftDropZ05B151PFbTagger.NegativeSoftPFMuonByPtBJetTags
akFlowPuCsSoftDropZ05B151PFPositiveSoftPFMuonByPtBJetTags = akFlowPuCsSoftDropZ05B151PFbTagger.PositiveSoftPFMuonByPtBJetTags
akFlowPuCsSoftDropZ05B151PFPatJetFlavourIdLegacy = cms.Sequence(akFlowPuCsSoftDropZ05B151PFPatJetPartonAssociationLegacy*akFlowPuCsSoftDropZ05B151PFPatJetFlavourAssociationLegacy)
# Not working with our PU sub, but keep it here for reference
# akFlowPuCsSoftDropZ05B151PFPatJetFlavourAssociation = akFlowPuCsSoftDropZ05B151PFbTagger.PatJetFlavourAssociation
# akFlowPuCsSoftDropZ05B151PFPatJetFlavourId = cms.Sequence(akFlowPuCsSoftDropZ05B151PFPatJetPartons*akFlowPuCsSoftDropZ05B151PFPatJetFlavourAssociation)

akFlowPuCsSoftDropZ05B151PFJetBtaggingIP = cms.Sequence(
    akFlowPuCsSoftDropZ05B151PFImpactParameterTagInfos *
    akFlowPuCsSoftDropZ05B151PFTrackCountingHighEffBJetTags +
    akFlowPuCsSoftDropZ05B151PFTrackCountingHighPurBJetTags +
    akFlowPuCsSoftDropZ05B151PFJetProbabilityBJetTags +
    akFlowPuCsSoftDropZ05B151PFJetBProbabilityBJetTags
    )

akFlowPuCsSoftDropZ05B151PFJetBtaggingSV = cms.Sequence(
    akFlowPuCsSoftDropZ05B151PFImpactParameterTagInfos *
    akFlowPuCsSoftDropZ05B151PFSecondaryVertexTagInfos *
    akFlowPuCsSoftDropZ05B151PFSimpleSecondaryVertexHighEffBJetTags +
    akFlowPuCsSoftDropZ05B151PFSimpleSecondaryVertexHighPurBJetTags +
    akFlowPuCsSoftDropZ05B151PFCombinedSecondaryVertexBJetTags +
    akFlowPuCsSoftDropZ05B151PFCombinedSecondaryVertexV2BJetTags
    )

akFlowPuCsSoftDropZ05B151PFJetBtaggingNegSV = cms.Sequence(
    akFlowPuCsSoftDropZ05B151PFImpactParameterTagInfos *
    akFlowPuCsSoftDropZ05B151PFSecondaryVertexNegativeTagInfos *
    akFlowPuCsSoftDropZ05B151PFNegativeSimpleSecondaryVertexHighEffBJetTags +
    akFlowPuCsSoftDropZ05B151PFNegativeSimpleSecondaryVertexHighPurBJetTags +
    akFlowPuCsSoftDropZ05B151PFNegativeCombinedSecondaryVertexBJetTags +
    akFlowPuCsSoftDropZ05B151PFPositiveCombinedSecondaryVertexBJetTags +
    akFlowPuCsSoftDropZ05B151PFNegativeCombinedSecondaryVertexV2BJetTags +
    akFlowPuCsSoftDropZ05B151PFPositiveCombinedSecondaryVertexV2BJetTags
    )

akFlowPuCsSoftDropZ05B151PFJetBtaggingMu = cms.Sequence(
    akFlowPuCsSoftDropZ05B151PFSoftPFMuonsTagInfos *
    akFlowPuCsSoftDropZ05B151PFSoftPFMuonBJetTags +
    akFlowPuCsSoftDropZ05B151PFSoftPFMuonByIP3dBJetTags +
    akFlowPuCsSoftDropZ05B151PFSoftPFMuonByPtBJetTags +
    akFlowPuCsSoftDropZ05B151PFNegativeSoftPFMuonByPtBJetTags +
    akFlowPuCsSoftDropZ05B151PFPositiveSoftPFMuonByPtBJetTags
    )

akFlowPuCsSoftDropZ05B151PFJetBtagging = cms.Sequence(
    akFlowPuCsSoftDropZ05B151PFJetBtaggingIP
    * akFlowPuCsSoftDropZ05B151PFJetBtaggingSV
    # * akFlowPuCsSoftDropZ05B151PFJetBtaggingNegSV
    # * akFlowPuCsSoftDropZ05B151PFJetBtaggingMu
    )

akFlowPuCsSoftDropZ05B151PFpatJetsWithBtagging = patJets.clone(
    jetSource = cms.InputTag("akFlowPuCsSoftDropZ05B151PFJets"),
    genJetMatch            = cms.InputTag("akFlowPuCsSoftDropZ05B151PFmatch"),
    genPartonMatch         = cms.InputTag("akFlowPuCsSoftDropZ05B151PFparton"),
    jetCorrFactorsSource   = cms.VInputTag(cms.InputTag("akFlowPuCsSoftDropZ05B151PFcorr")),
    JetPartonMapSource     = cms.InputTag("akFlowPuCsSoftDropZ05B151PFPatJetFlavourAssociationLegacy"),
    JetFlavourInfoSource   = cms.InputTag("akFlowPuCsSoftDropZ05B151PFPatJetFlavourAssociation"),
    trackAssociationSource = cms.InputTag("akFlowPuCsSoftDropZ05B151PFJetTracksAssociatorAtVertex"),
    useLegacyJetMCFlavour  = True,
    discriminatorSources   = cms.VInputTag(
        cms.InputTag("akFlowPuCsSoftDropZ05B151PFSimpleSecondaryVertexHighEffBJetTags"),
        cms.InputTag("akFlowPuCsSoftDropZ05B151PFSimpleSecondaryVertexHighPurBJetTags"),
        cms.InputTag("akFlowPuCsSoftDropZ05B151PFCombinedSecondaryVertexBJetTags"),
        cms.InputTag("akFlowPuCsSoftDropZ05B151PFCombinedSecondaryVertexV2BJetTags"),
        cms.InputTag("akFlowPuCsSoftDropZ05B151PFJetBProbabilityBJetTags"),
        cms.InputTag("akFlowPuCsSoftDropZ05B151PFJetProbabilityBJetTags"),
        # cms.InputTag("akFlowPuCsSoftDropZ05B151PFSoftPFMuonByPtBJetTags"),
        # cms.InputTag("akFlowPuCsSoftDropZ05B151PFSoftPFMuonByIP3dBJetTags"),
        cms.InputTag("akFlowPuCsSoftDropZ05B151PFTrackCountingHighEffBJetTags"),
        cms.InputTag("akFlowPuCsSoftDropZ05B151PFTrackCountingHighPurBJetTags"),
        ),
    tagInfoSources = cms.VInputTag(cms.InputTag("akFlowPuCsSoftDropZ05B151PFImpactParameterTagInfos"),cms.InputTag("akFlowPuCsSoftDropZ05B151PFSecondaryVertexTagInfos")),
    jetIDMap = cms.InputTag("akFlowPuCsSoftDropZ05B151PFJetID"),
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

akFlowPuCsSoftDropZ05B151PFNjettiness = Njettiness.clone(
    src = cms.InputTag("akFlowPuCsSoftDropZ05B151PFJets"),
    R0  = cms.double(0.1)
    )

akFlowPuCsSoftDropZ05B151PFpatJetsWithBtagging.userData.userFloats.src += [
    'akFlowPuCsSoftDropZ05B151PFNjettiness:tau1',
    'akFlowPuCsSoftDropZ05B151PFNjettiness:tau2',
    'akFlowPuCsSoftDropZ05B151PFNjettiness:tau3']

akFlowPuCsSoftDropZ05B151PFJetAnalyzer = inclusiveJetAnalyzer.clone(
    jetTag = cms.InputTag("akFlowPuCsSoftDropZ05B151PFpatJetsWithBtagging"),
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
    bTagJetName = cms.untracked.string("akFlowPuCsSoftDropZ05B151PF"),
    jetName = cms.untracked.string("akFlowPuCsSoftDropZ05B151PF"),
    genPtMin = cms.untracked.double(5),
    hltTrgResults = cms.untracked.string('TriggerResults::'+'HISIGNAL'),
    doTower = cms.untracked.bool(False),
    doSubJets = cms.untracked.bool(True),
    doGenSubJets = cms.untracked.bool(False),
    subjetGenTag = cms.untracked.InputTag("akSoftDropZ05B151GenJets"),
    doGenTaus = cms.untracked.bool(False),
    genTau1 = cms.InputTag("akSoftDropZ05B151HiGenNjettiness","tau1"),
    genTau2 = cms.InputTag("akSoftDropZ05B151HiGenNjettiness","tau2"),
    genTau3 = cms.InputTag("akSoftDropZ05B151HiGenNjettiness","tau3"),
    doGenSym = cms.untracked.bool(False),
    genSym = cms.InputTag("akSoftDropZ05B151GenJets","sym"),
    genDroppedBranches = cms.InputTag("akSoftDropZ05B151GenJets","droppedBranches")
    )

akFlowPuCsSoftDropZ05B151PFJetSequence_mc = cms.Sequence(
    # akFlowPuCsSoftDropZ05B151PFclean
    # *
    akFlowPuCsSoftDropZ05B151PFmatch
    # *
    # akFlowPuCsSoftDropZ05B151PFmatchGroomed
    *
    akFlowPuCsSoftDropZ05B151PFparton
    *
    akFlowPuCsSoftDropZ05B151PFcorr
    # *
    # akFlowPuCsSoftDropZ05B151PFJetID
    *
    akFlowPuCsSoftDropZ05B151PFPatJetFlavourIdLegacy
    # *
    # akFlowPuCsSoftDropZ05B151PFPatJetFlavourId # Use legacy algo till PU implemented
    *
    akFlowPuCsSoftDropZ05B151PFJetTracksAssociatorAtVertex
    *
    akFlowPuCsSoftDropZ05B151PFJetBtagging
    *
    # No constituents for calo jets in pp. Must be removed for pp calo jets but
    # I'm not sure how to do this transparently (Marta)
    akFlowPuCsSoftDropZ05B151PFNjettiness
    *
    akFlowPuCsSoftDropZ05B151PFpatJetsWithBtagging
    *
    akFlowPuCsSoftDropZ05B151PFJetAnalyzer
    )

akFlowPuCsSoftDropZ05B151PFJetSequence_data = cms.Sequence(
    akFlowPuCsSoftDropZ05B151PFcorr
    *
    # akFlowPuCsSoftDropZ05B151PFJetID
    # *
    akFlowPuCsSoftDropZ05B151PFJetTracksAssociatorAtVertex
    *
    akFlowPuCsSoftDropZ05B151PFJetBtagging
    *
    akFlowPuCsSoftDropZ05B151PFNjettiness
    *
    akFlowPuCsSoftDropZ05B151PFpatJetsWithBtagging
    *
    akFlowPuCsSoftDropZ05B151PFJetAnalyzer
    )

akFlowPuCsSoftDropZ05B151PFJetSequence_mb = cms.Sequence(
    akFlowPuCsSoftDropZ05B151PFJetSequence_mc)
akFlowPuCsSoftDropZ05B151PFJetSequence_jec = cms.Sequence(
    akFlowPuCsSoftDropZ05B151PFJetSequence_mc)

akFlowPuCsSoftDropZ05B151PFJetSequence = cms.Sequence(
    akFlowPuCsSoftDropZ05B151PFJetSequence_jec)
akFlowPuCsSoftDropZ05B151PFJetAnalyzer.genPtMin = cms.untracked.double(1)
akFlowPuCsSoftDropZ05B151PFJetAnalyzer.jetPtMin = cms.double(1)
akFlowPuCsSoftDropZ05B151PFpatJetsWithBtagging.userData.userFloats.src += ['akFlowPuCsSoftDropZ05B151PFJets:sym']
akFlowPuCsSoftDropZ05B151PFpatJetsWithBtagging.userData.userInts.src += ['akFlowPuCsSoftDropZ05B151PFJets:droppedBranches']
