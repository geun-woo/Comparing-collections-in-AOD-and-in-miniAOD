import FWCore.ParameterSet.Config as cms

from PhysicsTools.PatAlgos.mcMatchLayer0.jetMatch_cfi import patJetGenJetMatch, patJetPartonMatch
from PhysicsTools.PatAlgos.recoLayer0.jetCorrFactors_cfi import patJetCorrFactors
from PhysicsTools.PatAlgos.producersLayer1.jetProducer_cfi import patJets

from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *

from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akCsSoftDropZ05B156PFmatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akCsSoftDropZ05B156PFJets"),
    matched = cms.InputTag("ak6HiCleanedGenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.6
    )

akCsSoftDropZ05B156PFmatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDropZ05B156HiGenJets"),
    matched = cms.InputTag("ak6HiCleanedGenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.6
    )

akCsSoftDropZ05B156PFparton = patJetPartonMatch.clone(
    src = cms.InputTag("akCsSoftDropZ05B156PFJets"),
    matched = cms.InputTag("cleanedPartons"))

akCsSoftDropZ05B156PFcorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
    levels   = cms.vstring('L2Relative'),
    src = cms.InputTag("akCsSoftDropZ05B156PFJets"),
    payload = "AK6PF"
    )

akCsSoftDropZ05B156PFJetID = cms.EDProducer(
    'JetIDProducer',
    JetIDParams,
    src = cms.InputTag('akCsSoftDropZ05B156CaloJets'))

# akCsSoftDropZ05B156PFclean = heavyIonCleanedGenJets.clone(
#     src = cms.InputTag('ak6HiCleanedGenJets'))

akCsSoftDropZ05B156PFbTagger = bTaggers(
    "akCsSoftDropZ05B156PF",
    0.6)

# create objects locally since they dont load properly otherwise
akCsSoftDropZ05B156PFPatJetFlavourAssociationLegacy = akCsSoftDropZ05B156PFbTagger.PatJetFlavourAssociationLegacy
akCsSoftDropZ05B156PFPatJetPartons = akCsSoftDropZ05B156PFbTagger.PatJetPartons
akCsSoftDropZ05B156PFJetTracksAssociatorAtVertex = akCsSoftDropZ05B156PFbTagger.JetTracksAssociatorAtVertex
akCsSoftDropZ05B156PFJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akCsSoftDropZ05B156PFSimpleSecondaryVertexHighEffBJetTags = akCsSoftDropZ05B156PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akCsSoftDropZ05B156PFSimpleSecondaryVertexHighPurBJetTags = akCsSoftDropZ05B156PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akCsSoftDropZ05B156PFCombinedSecondaryVertexBJetTags = akCsSoftDropZ05B156PFbTagger.CombinedSecondaryVertexBJetTags
akCsSoftDropZ05B156PFCombinedSecondaryVertexV2BJetTags = akCsSoftDropZ05B156PFbTagger.CombinedSecondaryVertexV2BJetTags
akCsSoftDropZ05B156PFJetBProbabilityBJetTags = akCsSoftDropZ05B156PFbTagger.JetBProbabilityBJetTags
akCsSoftDropZ05B156PFSoftPFMuonByPtBJetTags = akCsSoftDropZ05B156PFbTagger.SoftPFMuonByPtBJetTags
akCsSoftDropZ05B156PFSoftPFMuonByIP3dBJetTags = akCsSoftDropZ05B156PFbTagger.SoftPFMuonByIP3dBJetTags
akCsSoftDropZ05B156PFTrackCountingHighEffBJetTags = akCsSoftDropZ05B156PFbTagger.TrackCountingHighEffBJetTags
akCsSoftDropZ05B156PFTrackCountingHighPurBJetTags = akCsSoftDropZ05B156PFbTagger.TrackCountingHighPurBJetTags
akCsSoftDropZ05B156PFPatJetPartonAssociationLegacy = akCsSoftDropZ05B156PFbTagger.PatJetPartonAssociationLegacy
akCsSoftDropZ05B156PFPatJetPartonAssociationLegacy.partons = "myPartons"

akCsSoftDropZ05B156PFImpactParameterTagInfos = akCsSoftDropZ05B156PFbTagger.ImpactParameterTagInfos
akCsSoftDropZ05B156PFImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akCsSoftDropZ05B156PFJetProbabilityBJetTags = akCsSoftDropZ05B156PFbTagger.JetProbabilityBJetTags

akCsSoftDropZ05B156PFSecondaryVertexTagInfos = akCsSoftDropZ05B156PFbTagger.SecondaryVertexTagInfos
akCsSoftDropZ05B156PFSimpleSecondaryVertexHighEffBJetTags = akCsSoftDropZ05B156PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akCsSoftDropZ05B156PFSimpleSecondaryVertexHighPurBJetTags = akCsSoftDropZ05B156PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akCsSoftDropZ05B156PFCombinedSecondaryVertexBJetTags = akCsSoftDropZ05B156PFbTagger.CombinedSecondaryVertexBJetTags
akCsSoftDropZ05B156PFCombinedSecondaryVertexV2BJetTags = akCsSoftDropZ05B156PFbTagger.CombinedSecondaryVertexV2BJetTags

akCsSoftDropZ05B156PFSecondaryVertexNegativeTagInfos = akCsSoftDropZ05B156PFbTagger.SecondaryVertexNegativeTagInfos
akCsSoftDropZ05B156PFNegativeSimpleSecondaryVertexHighEffBJetTags = akCsSoftDropZ05B156PFbTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akCsSoftDropZ05B156PFNegativeSimpleSecondaryVertexHighPurBJetTags = akCsSoftDropZ05B156PFbTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akCsSoftDropZ05B156PFNegativeCombinedSecondaryVertexBJetTags = akCsSoftDropZ05B156PFbTagger.NegativeCombinedSecondaryVertexBJetTags
akCsSoftDropZ05B156PFPositiveCombinedSecondaryVertexBJetTags = akCsSoftDropZ05B156PFbTagger.PositiveCombinedSecondaryVertexBJetTags
akCsSoftDropZ05B156PFNegativeCombinedSecondaryVertexV2BJetTags = akCsSoftDropZ05B156PFbTagger.NegativeCombinedSecondaryVertexV2BJetTags
akCsSoftDropZ05B156PFPositiveCombinedSecondaryVertexV2BJetTags = akCsSoftDropZ05B156PFbTagger.PositiveCombinedSecondaryVertexV2BJetTags

akCsSoftDropZ05B156PFSoftPFMuonsTagInfos = akCsSoftDropZ05B156PFbTagger.SoftPFMuonsTagInfos
akCsSoftDropZ05B156PFSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akCsSoftDropZ05B156PFSoftPFMuonBJetTags = akCsSoftDropZ05B156PFbTagger.SoftPFMuonBJetTags
akCsSoftDropZ05B156PFSoftPFMuonByIP3dBJetTags = akCsSoftDropZ05B156PFbTagger.SoftPFMuonByIP3dBJetTags
akCsSoftDropZ05B156PFSoftPFMuonByPtBJetTags = akCsSoftDropZ05B156PFbTagger.SoftPFMuonByPtBJetTags
akCsSoftDropZ05B156PFNegativeSoftPFMuonByPtBJetTags = akCsSoftDropZ05B156PFbTagger.NegativeSoftPFMuonByPtBJetTags
akCsSoftDropZ05B156PFPositiveSoftPFMuonByPtBJetTags = akCsSoftDropZ05B156PFbTagger.PositiveSoftPFMuonByPtBJetTags
akCsSoftDropZ05B156PFPatJetFlavourIdLegacy = cms.Sequence(akCsSoftDropZ05B156PFPatJetPartonAssociationLegacy*akCsSoftDropZ05B156PFPatJetFlavourAssociationLegacy)
# Not working with our PU sub, but keep it here for reference
# akCsSoftDropZ05B156PFPatJetFlavourAssociation = akCsSoftDropZ05B156PFbTagger.PatJetFlavourAssociation
# akCsSoftDropZ05B156PFPatJetFlavourId = cms.Sequence(akCsSoftDropZ05B156PFPatJetPartons*akCsSoftDropZ05B156PFPatJetFlavourAssociation)

akCsSoftDropZ05B156PFJetBtaggingIP = cms.Sequence(
    akCsSoftDropZ05B156PFImpactParameterTagInfos *
    akCsSoftDropZ05B156PFTrackCountingHighEffBJetTags +
    akCsSoftDropZ05B156PFTrackCountingHighPurBJetTags +
    akCsSoftDropZ05B156PFJetProbabilityBJetTags +
    akCsSoftDropZ05B156PFJetBProbabilityBJetTags
    )

akCsSoftDropZ05B156PFJetBtaggingSV = cms.Sequence(
    akCsSoftDropZ05B156PFImpactParameterTagInfos *
    akCsSoftDropZ05B156PFSecondaryVertexTagInfos *
    akCsSoftDropZ05B156PFSimpleSecondaryVertexHighEffBJetTags +
    akCsSoftDropZ05B156PFSimpleSecondaryVertexHighPurBJetTags +
    akCsSoftDropZ05B156PFCombinedSecondaryVertexBJetTags +
    akCsSoftDropZ05B156PFCombinedSecondaryVertexV2BJetTags
    )

akCsSoftDropZ05B156PFJetBtaggingNegSV = cms.Sequence(
    akCsSoftDropZ05B156PFImpactParameterTagInfos *
    akCsSoftDropZ05B156PFSecondaryVertexNegativeTagInfos *
    akCsSoftDropZ05B156PFNegativeSimpleSecondaryVertexHighEffBJetTags +
    akCsSoftDropZ05B156PFNegativeSimpleSecondaryVertexHighPurBJetTags +
    akCsSoftDropZ05B156PFNegativeCombinedSecondaryVertexBJetTags +
    akCsSoftDropZ05B156PFPositiveCombinedSecondaryVertexBJetTags +
    akCsSoftDropZ05B156PFNegativeCombinedSecondaryVertexV2BJetTags +
    akCsSoftDropZ05B156PFPositiveCombinedSecondaryVertexV2BJetTags
    )

akCsSoftDropZ05B156PFJetBtaggingMu = cms.Sequence(
    akCsSoftDropZ05B156PFSoftPFMuonsTagInfos *
    akCsSoftDropZ05B156PFSoftPFMuonBJetTags +
    akCsSoftDropZ05B156PFSoftPFMuonByIP3dBJetTags +
    akCsSoftDropZ05B156PFSoftPFMuonByPtBJetTags +
    akCsSoftDropZ05B156PFNegativeSoftPFMuonByPtBJetTags +
    akCsSoftDropZ05B156PFPositiveSoftPFMuonByPtBJetTags
    )

akCsSoftDropZ05B156PFJetBtagging = cms.Sequence(
    akCsSoftDropZ05B156PFJetBtaggingIP
    * akCsSoftDropZ05B156PFJetBtaggingSV
    # * akCsSoftDropZ05B156PFJetBtaggingNegSV
    # * akCsSoftDropZ05B156PFJetBtaggingMu
    )

akCsSoftDropZ05B156PFpatJetsWithBtagging = patJets.clone(
    jetSource = cms.InputTag("akCsSoftDropZ05B156PFJets"),
    genJetMatch            = cms.InputTag("akCsSoftDropZ05B156PFmatch"),
    genPartonMatch         = cms.InputTag("akCsSoftDropZ05B156PFparton"),
    jetCorrFactorsSource   = cms.VInputTag(cms.InputTag("akCsSoftDropZ05B156PFcorr")),
    JetPartonMapSource     = cms.InputTag("akCsSoftDropZ05B156PFPatJetFlavourAssociationLegacy"),
    JetFlavourInfoSource   = cms.InputTag("akCsSoftDropZ05B156PFPatJetFlavourAssociation"),
    trackAssociationSource = cms.InputTag("akCsSoftDropZ05B156PFJetTracksAssociatorAtVertex"),
    useLegacyJetMCFlavour  = True,
    discriminatorSources   = cms.VInputTag(
        cms.InputTag("akCsSoftDropZ05B156PFSimpleSecondaryVertexHighEffBJetTags"),
        cms.InputTag("akCsSoftDropZ05B156PFSimpleSecondaryVertexHighPurBJetTags"),
        cms.InputTag("akCsSoftDropZ05B156PFCombinedSecondaryVertexBJetTags"),
        cms.InputTag("akCsSoftDropZ05B156PFCombinedSecondaryVertexV2BJetTags"),
        cms.InputTag("akCsSoftDropZ05B156PFJetBProbabilityBJetTags"),
        cms.InputTag("akCsSoftDropZ05B156PFJetProbabilityBJetTags"),
        # cms.InputTag("akCsSoftDropZ05B156PFSoftPFMuonByPtBJetTags"),
        # cms.InputTag("akCsSoftDropZ05B156PFSoftPFMuonByIP3dBJetTags"),
        cms.InputTag("akCsSoftDropZ05B156PFTrackCountingHighEffBJetTags"),
        cms.InputTag("akCsSoftDropZ05B156PFTrackCountingHighPurBJetTags"),
        ),
    tagInfoSources = cms.VInputTag(cms.InputTag("akCsSoftDropZ05B156PFImpactParameterTagInfos"),cms.InputTag("akCsSoftDropZ05B156PFSecondaryVertexTagInfos")),
    jetIDMap = cms.InputTag("akCsSoftDropZ05B156PFJetID"),
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

akCsSoftDropZ05B156PFNjettiness = Njettiness.clone(
    src = cms.InputTag("akCsSoftDropZ05B156PFJets"),
    R0  = cms.double(0.6)
    )

akCsSoftDropZ05B156PFpatJetsWithBtagging.userData.userFloats.src += [
    'akCsSoftDropZ05B156PFNjettiness:tau1',
    'akCsSoftDropZ05B156PFNjettiness:tau2',
    'akCsSoftDropZ05B156PFNjettiness:tau3']

akCsSoftDropZ05B156PFJetAnalyzer = inclusiveJetAnalyzer.clone(
    jetTag = cms.InputTag("akCsSoftDropZ05B156PFpatJetsWithBtagging"),
    genjetTag = 'ak6HiGenJets',
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
    bTagJetName = cms.untracked.string("akCsSoftDropZ05B156PF"),
    jetName = cms.untracked.string("akCsSoftDropZ05B156PF"),
    genPtMin = cms.untracked.double(5),
    hltTrgResults = cms.untracked.string('TriggerResults::'+'HISIGNAL'),
    doTower = cms.untracked.bool(False),
    doSubJets = cms.untracked.bool(True),
    doGenSubJets = cms.untracked.bool(False),
    subjetGenTag = cms.untracked.InputTag("akSoftDropZ05B156GenJets"),
    doGenTaus = cms.untracked.bool(False),
    genTau1 = cms.InputTag("akSoftDropZ05B156HiGenNjettiness","tau1"),
    genTau2 = cms.InputTag("akSoftDropZ05B156HiGenNjettiness","tau2"),
    genTau3 = cms.InputTag("akSoftDropZ05B156HiGenNjettiness","tau3"),
    doGenSym = cms.untracked.bool(False),
    genSym = cms.InputTag("akSoftDropZ05B156GenJets","sym"),
    genDroppedBranches = cms.InputTag("akSoftDropZ05B156GenJets","droppedBranches")
    )

akCsSoftDropZ05B156PFJetSequence_mc = cms.Sequence(
    # akCsSoftDropZ05B156PFclean
    # *
    akCsSoftDropZ05B156PFmatch
    # *
    # akCsSoftDropZ05B156PFmatchGroomed
    *
    akCsSoftDropZ05B156PFparton
    *
    akCsSoftDropZ05B156PFcorr
    # *
    # akCsSoftDropZ05B156PFJetID
    *
    akCsSoftDropZ05B156PFPatJetFlavourIdLegacy
    # *
    # akCsSoftDropZ05B156PFPatJetFlavourId # Use legacy algo till PU implemented
    *
    akCsSoftDropZ05B156PFJetTracksAssociatorAtVertex
    *
    akCsSoftDropZ05B156PFJetBtagging
    *
    # No constituents for calo jets in pp. Must be removed for pp calo jets but
    # I'm not sure how to do this transparently (Marta)
    akCsSoftDropZ05B156PFNjettiness
    *
    akCsSoftDropZ05B156PFpatJetsWithBtagging
    *
    akCsSoftDropZ05B156PFJetAnalyzer
    )

akCsSoftDropZ05B156PFJetSequence_data = cms.Sequence(
    akCsSoftDropZ05B156PFcorr
    *
    # akCsSoftDropZ05B156PFJetID
    # *
    akCsSoftDropZ05B156PFJetTracksAssociatorAtVertex
    *
    akCsSoftDropZ05B156PFJetBtagging
    *
    akCsSoftDropZ05B156PFNjettiness
    *
    akCsSoftDropZ05B156PFpatJetsWithBtagging
    *
    akCsSoftDropZ05B156PFJetAnalyzer
    )

akCsSoftDropZ05B156PFJetSequence_mb = cms.Sequence(
    akCsSoftDropZ05B156PFJetSequence_mc)
akCsSoftDropZ05B156PFJetSequence_jec = cms.Sequence(
    akCsSoftDropZ05B156PFJetSequence_mc)

akCsSoftDropZ05B156PFJetSequence = cms.Sequence(
    akCsSoftDropZ05B156PFJetSequence_mb)
akCsSoftDropZ05B156PFpatJetsWithBtagging.userData.userFloats.src += ['akCsSoftDropZ05B156PFJets:sym']
akCsSoftDropZ05B156PFpatJetsWithBtagging.userData.userInts.src += ['akCsSoftDropZ05B156PFJets:droppedBranches']
