import FWCore.ParameterSet.Config as cms

from PhysicsTools.PatAlgos.mcMatchLayer0.jetMatch_cfi import patJetGenJetMatch, patJetPartonMatch
from PhysicsTools.PatAlgos.recoLayer0.jetCorrFactors_cfi import patJetCorrFactors
from PhysicsTools.PatAlgos.producersLayer1.jetProducer_cfi import patJets

from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *

from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akCsSoftDropZ05B151PFmatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akCsSoftDropZ05B151PFJets"),
    matched = cms.InputTag("ak1GenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.1
    )

akCsSoftDropZ05B151PFmatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDropZ05B151GenJets"),
    matched = cms.InputTag("ak1GenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.1
    )

akCsSoftDropZ05B151PFparton = patJetPartonMatch.clone(
    src = cms.InputTag("akCsSoftDropZ05B151PFJets"),
    matched = cms.InputTag("genParticles"))

akCsSoftDropZ05B151PFcorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
    levels   = cms.vstring('L2Relative'),
    src = cms.InputTag("akCsSoftDropZ05B151PFJets"),
    payload = "AK1PF"
    )

akCsSoftDropZ05B151PFJetID = cms.EDProducer(
    'JetIDProducer',
    JetIDParams,
    src = cms.InputTag('akCsSoftDropZ05B151CaloJets'))

# akCsSoftDropZ05B151PFclean = heavyIonCleanedGenJets.clone(
#     src = cms.InputTag('ak1GenJets'))

akCsSoftDropZ05B151PFbTagger = bTaggers(
    "akCsSoftDropZ05B151PF",
    0.1)

# create objects locally since they dont load properly otherwise
akCsSoftDropZ05B151PFPatJetFlavourAssociationLegacy = akCsSoftDropZ05B151PFbTagger.PatJetFlavourAssociationLegacy
akCsSoftDropZ05B151PFPatJetPartons = akCsSoftDropZ05B151PFbTagger.PatJetPartons
akCsSoftDropZ05B151PFJetTracksAssociatorAtVertex = akCsSoftDropZ05B151PFbTagger.JetTracksAssociatorAtVertex
akCsSoftDropZ05B151PFJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akCsSoftDropZ05B151PFSimpleSecondaryVertexHighEffBJetTags = akCsSoftDropZ05B151PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akCsSoftDropZ05B151PFSimpleSecondaryVertexHighPurBJetTags = akCsSoftDropZ05B151PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akCsSoftDropZ05B151PFCombinedSecondaryVertexBJetTags = akCsSoftDropZ05B151PFbTagger.CombinedSecondaryVertexBJetTags
akCsSoftDropZ05B151PFCombinedSecondaryVertexV2BJetTags = akCsSoftDropZ05B151PFbTagger.CombinedSecondaryVertexV2BJetTags
akCsSoftDropZ05B151PFJetBProbabilityBJetTags = akCsSoftDropZ05B151PFbTagger.JetBProbabilityBJetTags
akCsSoftDropZ05B151PFSoftPFMuonByPtBJetTags = akCsSoftDropZ05B151PFbTagger.SoftPFMuonByPtBJetTags
akCsSoftDropZ05B151PFSoftPFMuonByIP3dBJetTags = akCsSoftDropZ05B151PFbTagger.SoftPFMuonByIP3dBJetTags
akCsSoftDropZ05B151PFTrackCountingHighEffBJetTags = akCsSoftDropZ05B151PFbTagger.TrackCountingHighEffBJetTags
akCsSoftDropZ05B151PFTrackCountingHighPurBJetTags = akCsSoftDropZ05B151PFbTagger.TrackCountingHighPurBJetTags
akCsSoftDropZ05B151PFPatJetPartonAssociationLegacy = akCsSoftDropZ05B151PFbTagger.PatJetPartonAssociationLegacy
akCsSoftDropZ05B151PFPatJetPartonAssociationLegacy.partons = "myPartons"

akCsSoftDropZ05B151PFImpactParameterTagInfos = akCsSoftDropZ05B151PFbTagger.ImpactParameterTagInfos
akCsSoftDropZ05B151PFImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akCsSoftDropZ05B151PFJetProbabilityBJetTags = akCsSoftDropZ05B151PFbTagger.JetProbabilityBJetTags

akCsSoftDropZ05B151PFSecondaryVertexTagInfos = akCsSoftDropZ05B151PFbTagger.SecondaryVertexTagInfos
akCsSoftDropZ05B151PFSimpleSecondaryVertexHighEffBJetTags = akCsSoftDropZ05B151PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akCsSoftDropZ05B151PFSimpleSecondaryVertexHighPurBJetTags = akCsSoftDropZ05B151PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akCsSoftDropZ05B151PFCombinedSecondaryVertexBJetTags = akCsSoftDropZ05B151PFbTagger.CombinedSecondaryVertexBJetTags
akCsSoftDropZ05B151PFCombinedSecondaryVertexV2BJetTags = akCsSoftDropZ05B151PFbTagger.CombinedSecondaryVertexV2BJetTags

akCsSoftDropZ05B151PFSecondaryVertexNegativeTagInfos = akCsSoftDropZ05B151PFbTagger.SecondaryVertexNegativeTagInfos
akCsSoftDropZ05B151PFNegativeSimpleSecondaryVertexHighEffBJetTags = akCsSoftDropZ05B151PFbTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akCsSoftDropZ05B151PFNegativeSimpleSecondaryVertexHighPurBJetTags = akCsSoftDropZ05B151PFbTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akCsSoftDropZ05B151PFNegativeCombinedSecondaryVertexBJetTags = akCsSoftDropZ05B151PFbTagger.NegativeCombinedSecondaryVertexBJetTags
akCsSoftDropZ05B151PFPositiveCombinedSecondaryVertexBJetTags = akCsSoftDropZ05B151PFbTagger.PositiveCombinedSecondaryVertexBJetTags
akCsSoftDropZ05B151PFNegativeCombinedSecondaryVertexV2BJetTags = akCsSoftDropZ05B151PFbTagger.NegativeCombinedSecondaryVertexV2BJetTags
akCsSoftDropZ05B151PFPositiveCombinedSecondaryVertexV2BJetTags = akCsSoftDropZ05B151PFbTagger.PositiveCombinedSecondaryVertexV2BJetTags

akCsSoftDropZ05B151PFSoftPFMuonsTagInfos = akCsSoftDropZ05B151PFbTagger.SoftPFMuonsTagInfos
akCsSoftDropZ05B151PFSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akCsSoftDropZ05B151PFSoftPFMuonBJetTags = akCsSoftDropZ05B151PFbTagger.SoftPFMuonBJetTags
akCsSoftDropZ05B151PFSoftPFMuonByIP3dBJetTags = akCsSoftDropZ05B151PFbTagger.SoftPFMuonByIP3dBJetTags
akCsSoftDropZ05B151PFSoftPFMuonByPtBJetTags = akCsSoftDropZ05B151PFbTagger.SoftPFMuonByPtBJetTags
akCsSoftDropZ05B151PFNegativeSoftPFMuonByPtBJetTags = akCsSoftDropZ05B151PFbTagger.NegativeSoftPFMuonByPtBJetTags
akCsSoftDropZ05B151PFPositiveSoftPFMuonByPtBJetTags = akCsSoftDropZ05B151PFbTagger.PositiveSoftPFMuonByPtBJetTags
akCsSoftDropZ05B151PFPatJetFlavourIdLegacy = cms.Sequence(akCsSoftDropZ05B151PFPatJetPartonAssociationLegacy*akCsSoftDropZ05B151PFPatJetFlavourAssociationLegacy)
# Not working with our PU sub, but keep it here for reference
# akCsSoftDropZ05B151PFPatJetFlavourAssociation = akCsSoftDropZ05B151PFbTagger.PatJetFlavourAssociation
# akCsSoftDropZ05B151PFPatJetFlavourId = cms.Sequence(akCsSoftDropZ05B151PFPatJetPartons*akCsSoftDropZ05B151PFPatJetFlavourAssociation)

akCsSoftDropZ05B151PFJetBtaggingIP = cms.Sequence(
    akCsSoftDropZ05B151PFImpactParameterTagInfos *
    akCsSoftDropZ05B151PFTrackCountingHighEffBJetTags +
    akCsSoftDropZ05B151PFTrackCountingHighPurBJetTags +
    akCsSoftDropZ05B151PFJetProbabilityBJetTags +
    akCsSoftDropZ05B151PFJetBProbabilityBJetTags
    )

akCsSoftDropZ05B151PFJetBtaggingSV = cms.Sequence(
    akCsSoftDropZ05B151PFImpactParameterTagInfos *
    akCsSoftDropZ05B151PFSecondaryVertexTagInfos *
    akCsSoftDropZ05B151PFSimpleSecondaryVertexHighEffBJetTags +
    akCsSoftDropZ05B151PFSimpleSecondaryVertexHighPurBJetTags +
    akCsSoftDropZ05B151PFCombinedSecondaryVertexBJetTags +
    akCsSoftDropZ05B151PFCombinedSecondaryVertexV2BJetTags
    )

akCsSoftDropZ05B151PFJetBtaggingNegSV = cms.Sequence(
    akCsSoftDropZ05B151PFImpactParameterTagInfos *
    akCsSoftDropZ05B151PFSecondaryVertexNegativeTagInfos *
    akCsSoftDropZ05B151PFNegativeSimpleSecondaryVertexHighEffBJetTags +
    akCsSoftDropZ05B151PFNegativeSimpleSecondaryVertexHighPurBJetTags +
    akCsSoftDropZ05B151PFNegativeCombinedSecondaryVertexBJetTags +
    akCsSoftDropZ05B151PFPositiveCombinedSecondaryVertexBJetTags +
    akCsSoftDropZ05B151PFNegativeCombinedSecondaryVertexV2BJetTags +
    akCsSoftDropZ05B151PFPositiveCombinedSecondaryVertexV2BJetTags
    )

akCsSoftDropZ05B151PFJetBtaggingMu = cms.Sequence(
    akCsSoftDropZ05B151PFSoftPFMuonsTagInfos *
    akCsSoftDropZ05B151PFSoftPFMuonBJetTags +
    akCsSoftDropZ05B151PFSoftPFMuonByIP3dBJetTags +
    akCsSoftDropZ05B151PFSoftPFMuonByPtBJetTags +
    akCsSoftDropZ05B151PFNegativeSoftPFMuonByPtBJetTags +
    akCsSoftDropZ05B151PFPositiveSoftPFMuonByPtBJetTags
    )

akCsSoftDropZ05B151PFJetBtagging = cms.Sequence(
    akCsSoftDropZ05B151PFJetBtaggingIP
    * akCsSoftDropZ05B151PFJetBtaggingSV
    # * akCsSoftDropZ05B151PFJetBtaggingNegSV
    # * akCsSoftDropZ05B151PFJetBtaggingMu
    )

akCsSoftDropZ05B151PFpatJetsWithBtagging = patJets.clone(
    jetSource = cms.InputTag("akCsSoftDropZ05B151PFJets"),
    genJetMatch            = cms.InputTag("akCsSoftDropZ05B151PFmatch"),
    genPartonMatch         = cms.InputTag("akCsSoftDropZ05B151PFparton"),
    jetCorrFactorsSource   = cms.VInputTag(cms.InputTag("akCsSoftDropZ05B151PFcorr")),
    JetPartonMapSource     = cms.InputTag("akCsSoftDropZ05B151PFPatJetFlavourAssociationLegacy"),
    JetFlavourInfoSource   = cms.InputTag("akCsSoftDropZ05B151PFPatJetFlavourAssociation"),
    trackAssociationSource = cms.InputTag("akCsSoftDropZ05B151PFJetTracksAssociatorAtVertex"),
    useLegacyJetMCFlavour  = True,
    discriminatorSources   = cms.VInputTag(
        cms.InputTag("akCsSoftDropZ05B151PFSimpleSecondaryVertexHighEffBJetTags"),
        cms.InputTag("akCsSoftDropZ05B151PFSimpleSecondaryVertexHighPurBJetTags"),
        cms.InputTag("akCsSoftDropZ05B151PFCombinedSecondaryVertexBJetTags"),
        cms.InputTag("akCsSoftDropZ05B151PFCombinedSecondaryVertexV2BJetTags"),
        cms.InputTag("akCsSoftDropZ05B151PFJetBProbabilityBJetTags"),
        cms.InputTag("akCsSoftDropZ05B151PFJetProbabilityBJetTags"),
        # cms.InputTag("akCsSoftDropZ05B151PFSoftPFMuonByPtBJetTags"),
        # cms.InputTag("akCsSoftDropZ05B151PFSoftPFMuonByIP3dBJetTags"),
        cms.InputTag("akCsSoftDropZ05B151PFTrackCountingHighEffBJetTags"),
        cms.InputTag("akCsSoftDropZ05B151PFTrackCountingHighPurBJetTags"),
        ),
    tagInfoSources = cms.VInputTag(cms.InputTag("akCsSoftDropZ05B151PFImpactParameterTagInfos"),cms.InputTag("akCsSoftDropZ05B151PFSecondaryVertexTagInfos")),
    jetIDMap = cms.InputTag("akCsSoftDropZ05B151PFJetID"),
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

akCsSoftDropZ05B151PFNjettiness = Njettiness.clone(
    src = cms.InputTag("akCsSoftDropZ05B151PFJets"),
    R0  = cms.double(0.1)
    )

akCsSoftDropZ05B151PFpatJetsWithBtagging.userData.userFloats.src += [
    'akCsSoftDropZ05B151PFNjettiness:tau1',
    'akCsSoftDropZ05B151PFNjettiness:tau2',
    'akCsSoftDropZ05B151PFNjettiness:tau3']

akCsSoftDropZ05B151PFJetAnalyzer = inclusiveJetAnalyzer.clone(
    jetTag = cms.InputTag("akCsSoftDropZ05B151PFpatJetsWithBtagging"),
    genjetTag = 'ak1GenJets',
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
    bTagJetName = cms.untracked.string("akCsSoftDropZ05B151PF"),
    jetName = cms.untracked.string("akCsSoftDropZ05B151PF"),
    genPtMin = cms.untracked.double(5),
    hltTrgResults = cms.untracked.string('TriggerResults::'+'HISIGNAL'),
    doTower = cms.untracked.bool(False),
    doSubJets = cms.untracked.bool(True),
    doGenSubJets = cms.untracked.bool(True),
    subjetGenTag = cms.untracked.InputTag("akSoftDropZ05B151GenJets"),
    doGenTaus = cms.untracked.bool(False),
    genTau1 = cms.InputTag("akSoftDropZ05B151GenNjettiness","tau1"),
    genTau2 = cms.InputTag("akSoftDropZ05B151GenNjettiness","tau2"),
    genTau3 = cms.InputTag("akSoftDropZ05B151GenNjettiness","tau3"),
    doGenSym = cms.untracked.bool(True),
    genSym = cms.InputTag("akSoftDropZ05B151GenJets","sym"),
    genDroppedBranches = cms.InputTag("akSoftDropZ05B151GenJets","droppedBranches")
    )

akCsSoftDropZ05B151PFJetSequence_mc = cms.Sequence(
    # akCsSoftDropZ05B151PFclean
    # *
    akCsSoftDropZ05B151PFmatch
    # *
    # akCsSoftDropZ05B151PFmatchGroomed
    *
    akCsSoftDropZ05B151PFparton
    *
    akCsSoftDropZ05B151PFcorr
    # *
    # akCsSoftDropZ05B151PFJetID
    *
    akCsSoftDropZ05B151PFPatJetFlavourIdLegacy
    # *
    # akCsSoftDropZ05B151PFPatJetFlavourId # Use legacy algo till PU implemented
    *
    akCsSoftDropZ05B151PFJetTracksAssociatorAtVertex
    *
    akCsSoftDropZ05B151PFJetBtagging
    *
    # No constituents for calo jets in pp. Must be removed for pp calo jets but
    # I'm not sure how to do this transparently (Marta)
    akCsSoftDropZ05B151PFNjettiness
    *
    akCsSoftDropZ05B151PFpatJetsWithBtagging
    *
    akCsSoftDropZ05B151PFJetAnalyzer
    )

akCsSoftDropZ05B151PFJetSequence_data = cms.Sequence(
    akCsSoftDropZ05B151PFcorr
    *
    # akCsSoftDropZ05B151PFJetID
    # *
    akCsSoftDropZ05B151PFJetTracksAssociatorAtVertex
    *
    akCsSoftDropZ05B151PFJetBtagging
    *
    akCsSoftDropZ05B151PFNjettiness
    *
    akCsSoftDropZ05B151PFpatJetsWithBtagging
    *
    akCsSoftDropZ05B151PFJetAnalyzer
    )

akCsSoftDropZ05B151PFJetSequence_mb = cms.Sequence(
    akCsSoftDropZ05B151PFJetSequence_mc)
akCsSoftDropZ05B151PFJetSequence_jec = cms.Sequence(
    akCsSoftDropZ05B151PFJetSequence_mc)

akCsSoftDropZ05B151PFJetSequence = cms.Sequence(
    akCsSoftDropZ05B151PFJetSequence_mc)
akCsSoftDropZ05B151PFpatJetsWithBtagging.userData.userFloats.src += ['akCsSoftDropZ05B151PFJets:sym']
akCsSoftDropZ05B151PFpatJetsWithBtagging.userData.userInts.src += ['akCsSoftDropZ05B151PFJets:droppedBranches']


akCsSoftDropZ05B151PFJetAnalyzer.matchJets = cms.untracked.bool(True)
akCsSoftDropZ05B151PFJetAnalyzer.matchTag = cms.untracked.InputTag("ak1PFpatJetsWithBtagging")
