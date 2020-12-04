import FWCore.ParameterSet.Config as cms

from PhysicsTools.PatAlgos.mcMatchLayer0.jetMatch_cfi import patJetGenJetMatch, patJetPartonMatch
from PhysicsTools.PatAlgos.recoLayer0.jetCorrFactors_cfi import patJetCorrFactors
from PhysicsTools.PatAlgos.producersLayer1.jetProducer_cfi import patJets

from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *

from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akCsSoftDropZ05B155PFmatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akCsSoftDropZ05B155PFJets"),
    matched = cms.InputTag("ak5HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.5
    )

akCsSoftDropZ05B155PFmatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDropZ05B155HiSignalGenJets"),
    matched = cms.InputTag("ak5HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.5
    )

akCsSoftDropZ05B155PFparton = patJetPartonMatch.clone(
    src = cms.InputTag("akCsSoftDropZ05B155PFJets"),
    matched = cms.InputTag("hiSignalGenParticles"))

akCsSoftDropZ05B155PFcorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
    levels   = cms.vstring('L2Relative'),
    src = cms.InputTag("akCsSoftDropZ05B155PFJets"),
    payload = "AK5PF"
    )

akCsSoftDropZ05B155PFJetID = cms.EDProducer(
    'JetIDProducer',
    JetIDParams,
    src = cms.InputTag('akCsSoftDropZ05B155CaloJets'))

# akCsSoftDropZ05B155PFclean = heavyIonCleanedGenJets.clone(
#     src = cms.InputTag('ak5HiSignalGenJets'))

akCsSoftDropZ05B155PFbTagger = bTaggers(
    "akCsSoftDropZ05B155PF",
    0.5)

# create objects locally since they dont load properly otherwise
akCsSoftDropZ05B155PFPatJetFlavourAssociationLegacy = akCsSoftDropZ05B155PFbTagger.PatJetFlavourAssociationLegacy
akCsSoftDropZ05B155PFPatJetPartons = akCsSoftDropZ05B155PFbTagger.PatJetPartons
akCsSoftDropZ05B155PFJetTracksAssociatorAtVertex = akCsSoftDropZ05B155PFbTagger.JetTracksAssociatorAtVertex
akCsSoftDropZ05B155PFJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akCsSoftDropZ05B155PFSimpleSecondaryVertexHighEffBJetTags = akCsSoftDropZ05B155PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akCsSoftDropZ05B155PFSimpleSecondaryVertexHighPurBJetTags = akCsSoftDropZ05B155PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akCsSoftDropZ05B155PFCombinedSecondaryVertexBJetTags = akCsSoftDropZ05B155PFbTagger.CombinedSecondaryVertexBJetTags
akCsSoftDropZ05B155PFCombinedSecondaryVertexV2BJetTags = akCsSoftDropZ05B155PFbTagger.CombinedSecondaryVertexV2BJetTags
akCsSoftDropZ05B155PFJetBProbabilityBJetTags = akCsSoftDropZ05B155PFbTagger.JetBProbabilityBJetTags
akCsSoftDropZ05B155PFSoftPFMuonByPtBJetTags = akCsSoftDropZ05B155PFbTagger.SoftPFMuonByPtBJetTags
akCsSoftDropZ05B155PFSoftPFMuonByIP3dBJetTags = akCsSoftDropZ05B155PFbTagger.SoftPFMuonByIP3dBJetTags
akCsSoftDropZ05B155PFTrackCountingHighEffBJetTags = akCsSoftDropZ05B155PFbTagger.TrackCountingHighEffBJetTags
akCsSoftDropZ05B155PFTrackCountingHighPurBJetTags = akCsSoftDropZ05B155PFbTagger.TrackCountingHighPurBJetTags
akCsSoftDropZ05B155PFPatJetPartonAssociationLegacy = akCsSoftDropZ05B155PFbTagger.PatJetPartonAssociationLegacy
akCsSoftDropZ05B155PFPatJetPartonAssociationLegacy.partons = "signalPartons"

akCsSoftDropZ05B155PFImpactParameterTagInfos = akCsSoftDropZ05B155PFbTagger.ImpactParameterTagInfos
akCsSoftDropZ05B155PFImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akCsSoftDropZ05B155PFJetProbabilityBJetTags = akCsSoftDropZ05B155PFbTagger.JetProbabilityBJetTags

akCsSoftDropZ05B155PFSecondaryVertexTagInfos = akCsSoftDropZ05B155PFbTagger.SecondaryVertexTagInfos
akCsSoftDropZ05B155PFSimpleSecondaryVertexHighEffBJetTags = akCsSoftDropZ05B155PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akCsSoftDropZ05B155PFSimpleSecondaryVertexHighPurBJetTags = akCsSoftDropZ05B155PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akCsSoftDropZ05B155PFCombinedSecondaryVertexBJetTags = akCsSoftDropZ05B155PFbTagger.CombinedSecondaryVertexBJetTags
akCsSoftDropZ05B155PFCombinedSecondaryVertexV2BJetTags = akCsSoftDropZ05B155PFbTagger.CombinedSecondaryVertexV2BJetTags

akCsSoftDropZ05B155PFSecondaryVertexNegativeTagInfos = akCsSoftDropZ05B155PFbTagger.SecondaryVertexNegativeTagInfos
akCsSoftDropZ05B155PFNegativeSimpleSecondaryVertexHighEffBJetTags = akCsSoftDropZ05B155PFbTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akCsSoftDropZ05B155PFNegativeSimpleSecondaryVertexHighPurBJetTags = akCsSoftDropZ05B155PFbTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akCsSoftDropZ05B155PFNegativeCombinedSecondaryVertexBJetTags = akCsSoftDropZ05B155PFbTagger.NegativeCombinedSecondaryVertexBJetTags
akCsSoftDropZ05B155PFPositiveCombinedSecondaryVertexBJetTags = akCsSoftDropZ05B155PFbTagger.PositiveCombinedSecondaryVertexBJetTags
akCsSoftDropZ05B155PFNegativeCombinedSecondaryVertexV2BJetTags = akCsSoftDropZ05B155PFbTagger.NegativeCombinedSecondaryVertexV2BJetTags
akCsSoftDropZ05B155PFPositiveCombinedSecondaryVertexV2BJetTags = akCsSoftDropZ05B155PFbTagger.PositiveCombinedSecondaryVertexV2BJetTags

akCsSoftDropZ05B155PFSoftPFMuonsTagInfos = akCsSoftDropZ05B155PFbTagger.SoftPFMuonsTagInfos
akCsSoftDropZ05B155PFSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akCsSoftDropZ05B155PFSoftPFMuonBJetTags = akCsSoftDropZ05B155PFbTagger.SoftPFMuonBJetTags
akCsSoftDropZ05B155PFSoftPFMuonByIP3dBJetTags = akCsSoftDropZ05B155PFbTagger.SoftPFMuonByIP3dBJetTags
akCsSoftDropZ05B155PFSoftPFMuonByPtBJetTags = akCsSoftDropZ05B155PFbTagger.SoftPFMuonByPtBJetTags
akCsSoftDropZ05B155PFNegativeSoftPFMuonByPtBJetTags = akCsSoftDropZ05B155PFbTagger.NegativeSoftPFMuonByPtBJetTags
akCsSoftDropZ05B155PFPositiveSoftPFMuonByPtBJetTags = akCsSoftDropZ05B155PFbTagger.PositiveSoftPFMuonByPtBJetTags
akCsSoftDropZ05B155PFPatJetFlavourIdLegacy = cms.Sequence(akCsSoftDropZ05B155PFPatJetPartonAssociationLegacy*akCsSoftDropZ05B155PFPatJetFlavourAssociationLegacy)
# Not working with our PU sub, but keep it here for reference
# akCsSoftDropZ05B155PFPatJetFlavourAssociation = akCsSoftDropZ05B155PFbTagger.PatJetFlavourAssociation
# akCsSoftDropZ05B155PFPatJetFlavourId = cms.Sequence(akCsSoftDropZ05B155PFPatJetPartons*akCsSoftDropZ05B155PFPatJetFlavourAssociation)

akCsSoftDropZ05B155PFJetBtaggingIP = cms.Sequence(
    akCsSoftDropZ05B155PFImpactParameterTagInfos *
    akCsSoftDropZ05B155PFTrackCountingHighEffBJetTags +
    akCsSoftDropZ05B155PFTrackCountingHighPurBJetTags +
    akCsSoftDropZ05B155PFJetProbabilityBJetTags +
    akCsSoftDropZ05B155PFJetBProbabilityBJetTags
    )

akCsSoftDropZ05B155PFJetBtaggingSV = cms.Sequence(
    akCsSoftDropZ05B155PFImpactParameterTagInfos *
    akCsSoftDropZ05B155PFSecondaryVertexTagInfos *
    akCsSoftDropZ05B155PFSimpleSecondaryVertexHighEffBJetTags +
    akCsSoftDropZ05B155PFSimpleSecondaryVertexHighPurBJetTags +
    akCsSoftDropZ05B155PFCombinedSecondaryVertexBJetTags +
    akCsSoftDropZ05B155PFCombinedSecondaryVertexV2BJetTags
    )

akCsSoftDropZ05B155PFJetBtaggingNegSV = cms.Sequence(
    akCsSoftDropZ05B155PFImpactParameterTagInfos *
    akCsSoftDropZ05B155PFSecondaryVertexNegativeTagInfos *
    akCsSoftDropZ05B155PFNegativeSimpleSecondaryVertexHighEffBJetTags +
    akCsSoftDropZ05B155PFNegativeSimpleSecondaryVertexHighPurBJetTags +
    akCsSoftDropZ05B155PFNegativeCombinedSecondaryVertexBJetTags +
    akCsSoftDropZ05B155PFPositiveCombinedSecondaryVertexBJetTags +
    akCsSoftDropZ05B155PFNegativeCombinedSecondaryVertexV2BJetTags +
    akCsSoftDropZ05B155PFPositiveCombinedSecondaryVertexV2BJetTags
    )

akCsSoftDropZ05B155PFJetBtaggingMu = cms.Sequence(
    akCsSoftDropZ05B155PFSoftPFMuonsTagInfos *
    akCsSoftDropZ05B155PFSoftPFMuonBJetTags +
    akCsSoftDropZ05B155PFSoftPFMuonByIP3dBJetTags +
    akCsSoftDropZ05B155PFSoftPFMuonByPtBJetTags +
    akCsSoftDropZ05B155PFNegativeSoftPFMuonByPtBJetTags +
    akCsSoftDropZ05B155PFPositiveSoftPFMuonByPtBJetTags
    )

akCsSoftDropZ05B155PFJetBtagging = cms.Sequence(
    akCsSoftDropZ05B155PFJetBtaggingIP
    * akCsSoftDropZ05B155PFJetBtaggingSV
    # * akCsSoftDropZ05B155PFJetBtaggingNegSV
    # * akCsSoftDropZ05B155PFJetBtaggingMu
    )

akCsSoftDropZ05B155PFpatJetsWithBtagging = patJets.clone(
    jetSource = cms.InputTag("akCsSoftDropZ05B155PFJets"),
    genJetMatch            = cms.InputTag("akCsSoftDropZ05B155PFmatch"),
    genPartonMatch         = cms.InputTag("akCsSoftDropZ05B155PFparton"),
    jetCorrFactorsSource   = cms.VInputTag(cms.InputTag("akCsSoftDropZ05B155PFcorr")),
    JetPartonMapSource     = cms.InputTag("akCsSoftDropZ05B155PFPatJetFlavourAssociationLegacy"),
    JetFlavourInfoSource   = cms.InputTag("akCsSoftDropZ05B155PFPatJetFlavourAssociation"),
    trackAssociationSource = cms.InputTag("akCsSoftDropZ05B155PFJetTracksAssociatorAtVertex"),
    useLegacyJetMCFlavour  = True,
    discriminatorSources   = cms.VInputTag(
        cms.InputTag("akCsSoftDropZ05B155PFSimpleSecondaryVertexHighEffBJetTags"),
        cms.InputTag("akCsSoftDropZ05B155PFSimpleSecondaryVertexHighPurBJetTags"),
        cms.InputTag("akCsSoftDropZ05B155PFCombinedSecondaryVertexBJetTags"),
        cms.InputTag("akCsSoftDropZ05B155PFCombinedSecondaryVertexV2BJetTags"),
        cms.InputTag("akCsSoftDropZ05B155PFJetBProbabilityBJetTags"),
        cms.InputTag("akCsSoftDropZ05B155PFJetProbabilityBJetTags"),
        # cms.InputTag("akCsSoftDropZ05B155PFSoftPFMuonByPtBJetTags"),
        # cms.InputTag("akCsSoftDropZ05B155PFSoftPFMuonByIP3dBJetTags"),
        cms.InputTag("akCsSoftDropZ05B155PFTrackCountingHighEffBJetTags"),
        cms.InputTag("akCsSoftDropZ05B155PFTrackCountingHighPurBJetTags"),
        ),
    tagInfoSources = cms.VInputTag(cms.InputTag("akCsSoftDropZ05B155PFImpactParameterTagInfos"),cms.InputTag("akCsSoftDropZ05B155PFSecondaryVertexTagInfos")),
    jetIDMap = cms.InputTag("akCsSoftDropZ05B155PFJetID"),
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

akCsSoftDropZ05B155PFNjettiness = Njettiness.clone(
    src = cms.InputTag("akCsSoftDropZ05B155PFJets"),
    R0  = cms.double(0.5)
    )

akCsSoftDropZ05B155PFpatJetsWithBtagging.userData.userFloats.src += [
    'akCsSoftDropZ05B155PFNjettiness:tau1',
    'akCsSoftDropZ05B155PFNjettiness:tau2',
    'akCsSoftDropZ05B155PFNjettiness:tau3']

akCsSoftDropZ05B155PFJetAnalyzer = inclusiveJetAnalyzer.clone(
    jetTag = cms.InputTag("akCsSoftDropZ05B155PFpatJetsWithBtagging"),
    genjetTag = 'ak5HiSignalGenJets',
    rParam = 0.5,
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
    bTagJetName = cms.untracked.string("akCsSoftDropZ05B155PF"),
    jetName = cms.untracked.string("akCsSoftDropZ05B155PF"),
    genPtMin = cms.untracked.double(5),
    hltTrgResults = cms.untracked.string('TriggerResults::'+'HISIGNAL'),
    doTower = cms.untracked.bool(False),
    doSubJets = cms.untracked.bool(True),
    doGenSubJets = cms.untracked.bool(True),
    subjetGenTag = cms.untracked.InputTag("akSoftDropZ05B155GenJets"),
    doGenTaus = cms.untracked.bool(False),
    genTau1 = cms.InputTag("akSoftDropZ05B155HiGenNjettiness","tau1"),
    genTau2 = cms.InputTag("akSoftDropZ05B155HiGenNjettiness","tau2"),
    genTau3 = cms.InputTag("akSoftDropZ05B155HiGenNjettiness","tau3"),
    doGenSym = cms.untracked.bool(True),
    genSym = cms.InputTag("akSoftDropZ05B155GenJets","sym"),
    genDroppedBranches = cms.InputTag("akSoftDropZ05B155GenJets","droppedBranches")
    )

akCsSoftDropZ05B155PFJetSequence_mc = cms.Sequence(
    # akCsSoftDropZ05B155PFclean
    # *
    akCsSoftDropZ05B155PFmatch
    # *
    # akCsSoftDropZ05B155PFmatchGroomed
    *
    akCsSoftDropZ05B155PFparton
    *
    akCsSoftDropZ05B155PFcorr
    # *
    # akCsSoftDropZ05B155PFJetID
    *
    akCsSoftDropZ05B155PFPatJetFlavourIdLegacy
    # *
    # akCsSoftDropZ05B155PFPatJetFlavourId # Use legacy algo till PU implemented
    *
    akCsSoftDropZ05B155PFJetTracksAssociatorAtVertex
    *
    akCsSoftDropZ05B155PFJetBtagging
    *
    # No constituents for calo jets in pp. Must be removed for pp calo jets but
    # I'm not sure how to do this transparently (Marta)
    akCsSoftDropZ05B155PFNjettiness
    *
    akCsSoftDropZ05B155PFpatJetsWithBtagging
    *
    akCsSoftDropZ05B155PFJetAnalyzer
    )

akCsSoftDropZ05B155PFJetSequence_data = cms.Sequence(
    akCsSoftDropZ05B155PFcorr
    *
    # akCsSoftDropZ05B155PFJetID
    # *
    akCsSoftDropZ05B155PFJetTracksAssociatorAtVertex
    *
    akCsSoftDropZ05B155PFJetBtagging
    *
    akCsSoftDropZ05B155PFNjettiness
    *
    akCsSoftDropZ05B155PFpatJetsWithBtagging
    *
    akCsSoftDropZ05B155PFJetAnalyzer
    )

akCsSoftDropZ05B155PFJetSequence_mb = cms.Sequence(
    akCsSoftDropZ05B155PFJetSequence_mc)
akCsSoftDropZ05B155PFJetSequence_jec = cms.Sequence(
    akCsSoftDropZ05B155PFJetSequence_mc)

akCsSoftDropZ05B155PFJetSequence = cms.Sequence(
    akCsSoftDropZ05B155PFJetSequence_mc)
akCsSoftDropZ05B155PFpatJetsWithBtagging.userData.userFloats.src += ['akCsSoftDropZ05B155PFJets:sym']
akCsSoftDropZ05B155PFpatJetsWithBtagging.userData.userInts.src += ['akCsSoftDropZ05B155PFJets:droppedBranches']


akCsSoftDropZ05B155PFJetAnalyzer.matchJets = cms.untracked.bool(True)
akCsSoftDropZ05B155PFJetAnalyzer.matchTag = cms.untracked.InputTag("ak5PFpatJetsWithBtagging")
